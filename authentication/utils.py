from rest_framework.exceptions import ValidationError


def validate_email(name,email):
    domain_list = ['gmail.com','frshrtech.com','yahoo.co.in','frshr.tech']
    user, domain = email.split('@')
    if domain not in domain_list:
        raise ValidationError("Not the allowed domain")
    if name.lower() not in user.lower():
        raise ValidationError("Name not in email")

def check_username(name, username):
    if name.lower() not in username.lower():
        raise ValidationError("username must contain name")
def password_check(passwd):
    SpecialSym =['$', '@', '#', '%','!','^','&','*','&','(','|','}']
    if len(passwd) < 8:
        raise ValidationError('Passwords must be 8 characters long')
		
    if not any(char.isdigit() for char in passwd):
        raise ValidationError('Password should have at least one numeral')
		
    if not any(char.isupper() for char in passwd):
        raise ValidationError('Password should have at least one uppercase letter')
		
    if not any(char.islower() for char in passwd):
        raise ValidationError('Password should have at least one lowercase letter')
		
    if not any(char in SpecialSym for char in passwd):
        raise ValidationError('Password should have at least one of the symbols $@#')