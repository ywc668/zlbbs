from wtforms import IntegerField
from wtforms import StringField
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import InputRequired
from wtforms.validators import Length

from apps.forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[
        Email(message='Please input correct email'),
        InputRequired(message='Please input your email')
    ])
    password = StringField(validators=[
        Length(6, 20, message='Password length error')
    ])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[
        Length(6, 20, message='Please input correct current password')
    ])
    newpwd = StringField(validators=[
        Length(6, 20, message='Please input new password of correct length')
    ])
    newpwd2 = StringField(validators=[
        EqualTo("newpwd")
    ])
