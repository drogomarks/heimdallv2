#!/usr/bin/env python
import base64
import hashlib
import time
import requests
import json


# Get Keys & Set User Agent
usrkey = 'USER_KEY';
scrtkey = 'SECRET_KEY';
usr_agent  = 'USER_AGENT_HERE';

# Get Date/Time: YYYYMMDDHHmmss
tm_stmp = time.strftime("%Y%m%d%H%M%S")
# Hash: <User Key><User Agent><Timestamp><Secret Key>
hash_str = usrkey + usr_agent + tm_stmp + scrtkey
# Get the hash
sha1 = base64.b64encode(hashlib.sha1(hash_str).digest())
# Create API Signature
api_sig = usrkey + ":" + tm_stmp + ":" + sha1

# Base URL/Headers
base_url  = "https://api.emailsrvr.com/v1/customers/"
headers = {"Accept":"application/json", "User-Agent" : "MigFwdTool", "X-Api-Signature" : api_sig}


def user_get(cst_id, domain, mbx_type, user):
    # Set Mailbox Type key for dict
    if mbx_type == 'rs':
        mbx_key = 'rsMailboxes'
    else:
        mbx_key = 'mailboxes'

    url = base_url + cst_id + "/domains/" + domain + "/" + mbx_type +  "/mailboxes/" + user
    request = requests.get(url, headers=headers)
    data = request.json()
    return data

def domain_get(cst_id, domain, mbx_type):
    # Set Mailbox Type key for dict
    if mbx_type == 'rs':
        mbx_key = 'rsMailboxes'
    else:
        mbx_key = 'mailboxes'

    url = base_url + cst_id + "/domains/" + domain
    request = requests.get(url, headers=headers)
    data = request.json()
    return data

def mbx_get(cst_id, domain, mbx_type):
    # Set Mailbox Type key for dict
    if mbx_type == 'rs':
        mbx_key = 'rsMailboxes'
    else:
        mbx_key = 'mailboxes'

    # offset value/url string
    off_val = 0
    off_str = "&offset=%s" % off_val
    # size value/url string
    sz_val= 50
    sz_str = "?size=%s" % sz_val

    url = base_url + cst_id + "/domains/" + domain + "/" + mbx_type +  "/mailboxes" + sz_str + off_str
    request = requests.get(url, headers=headers)
    data = request.json()
    mbx_total = data['total']
    # Empty list for mailboxes
    mailboxes = []
    global mailboxes
    # Offset Val variable to start at 0
    off_val = -50
    # While the offset value is less than the total mbx
    while mbx_total > off_val:
        # Set off value to self + the size value
        off_val += sz_val
        off_str = "&offset=%s" % off_val
        # Construct URL and make call
        url = base_url + cst_id + "/domains/" + domain + "/" + mbx_type +  "/mailboxes" + sz_str + off_str
        request = requests.get(url, headers=headers)
        data = request.json()
        # Add Users to Mailbox list
        for key in data[mbx_key]:
            mbx_usr = key['name']
            mailboxes.append(mbx_usr)
    return mailboxes


def user_vex(cst_id, domain, mbx_type, user, user_vex_val):
    # Set Mailbox Type key for dict
    if mbx_type == 'rs':
        mbx_key = 'rsMailboxes'
    else:
        mbx_key = 'mailboxes'

    payload = {'visibleInExchangeGAL' : user_vex_val }
    url = base_url + cst_id + "/domains/" + domain + "/" + mbx_type +  "/mailboxes/" + user
    request = requests.put(url, headers=headers, data=payload)
    return "User: '%s' visibleInExchangeGAL has been set to %s" % (user, user_vex_val)

def domain_vex(cst_id, domain, mbx_type, domain_vex_val):
    # Set Mailbox Type key for dict
    if mbx_type == 'rs':
        mbx_key = 'rsMailboxes'
    else:
        mbx_key = 'mailboxes'

    payload = {'visibleInExchangeGAL' : domain_vex_val }
    mbx_get(cst_id, domain, mbx_type)
    progress = []
    for user in mailboxes:
        url = base_url + cst_id + "/domains/" + domain + "/" + mbx_type +  "/mailboxes/" + user
        request = requests.put(url, headers=headers, data=payload)
        current_prog = "%s has been updated to %s" % (user, domain_vex_val)
        print current_prog
        progress.append(current_prog)
    return progress
