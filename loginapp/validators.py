import re

from django.forms import ValidationError

REGEX_PASSWORD     = '^(?=.*[A-Za-z])(?=.*[0-9])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

def password_validate(password):
    if not re.match(REGEX_PASSWORD, password):
                raise ValidationError("비밀번호 양식이 맞지 않습니다.")
