email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = 'pawel.rubach@.pl'
email4 = '@sgh.pl'

#['pawel.rubach@sgh.waw.pl', 'pawel.rubach@.pl']

def check_email(email):
    #TODO implement real checks
    if not email:
        return False
    if email.find('@')<=0 or email.find('@')!=email.rfind('@'):
        print('@ not found or too many of them')
        return False
    return True




for em in [email1, email2, email3, email4]:
    print('--------------------')
    print('{} : {}'.format(em, check_email(em)))
    #print(check_email(em))




