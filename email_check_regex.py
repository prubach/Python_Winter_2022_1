import re

email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = 'pawel.rubach@.pl'
email4 = '@sgh.pl'

regex = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

def check_email(email):
    match = re.fullmatch(regex, email)

    if match is not None:
        print(f'The email "{match.group()}" is valid')
        return True
    else:
        print(f'The email "{email}"" is not valid')
        return False


for em in [email1, email2, email3, email4]:
    print('--------------------')
    print('{} : {}'.format(em, check_email(em)))
    #print(check_email(em))

