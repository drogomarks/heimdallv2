from flask_wtf import Form
from wtforms import StringField, TextField, IntegerField, SubmitField, SelectField, validators

class GetuserForm(Form):
    customer_id = IntegerField('Customer ID')
    domain = TextField('Domain')
    user = TextField('User')
    mbx_type = SelectField(u'Mailbox Type', choices=[('rs', 'rs'), ('ex', 'ex')])


class GetdomainForm(Form):
    customer_id = IntegerField('Customer ID')
    domain = TextField('Domain')
    mbx_type = SelectField(u'Mailbox Type', choices=[('rs', 'rs'), ('ex', 'ex')])

class GetallForm(Form):
    customer_id = IntegerField('Customer ID')
    domain = TextField('Domain')
    mbx_type = SelectField(u'Mailbox Type', choices=[('rs', 'rs'), ('ex', 'ex')])

class PutuservexForm(Form):
    customer_id = IntegerField('Customer ID')
    domain = TextField('Domain')
    user = TextField('User')
    mbx_type = SelectField(u'Mailbox Type', choices=[('rs', 'rs'), ('ex', 'ex')])
    user_vex_val = SelectField(u'Value', choices=[('true', 'true'), ('false', 'false')])

class PutdomainvexForm(Form):
    customer_id = IntegerField('Customer ID')
    domain = TextField('Domain')
    mbx_type = SelectField(u'Mailbox Type', choices=[('rs', 'rs'), ('ex', 'ex')])
    domain_vex_val = SelectField(u'Value', choices=[('true', 'true'), ('false', 'false')])
