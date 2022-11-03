email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = 'pawel.rubach@.pl'
email4 = '@sgh.pl'


def check_email(email):
    if email:
        return True
    else:
        return False


for em in [email1, email2, email3, email4]:
    print('{} : {}'.format(em, check_email(em)))
    #print(check_email(em))




