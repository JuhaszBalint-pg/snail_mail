email = str(input('Please enter you email'))

if email.count('@') < 1:
    print ("An email address has to contain a '@' character!")
    
if email.count('@') > 1:
    print ("An email address cannot contain more than one '@' characters!")

uname_dom = email.split('@')
uname = uname_dom[0]
dom = uname_dom[1]
if uname == '':
    print("The username before the '@' character cannot be empty!")

if dom == '':
    print("The domain after the '@' character cannot be empty!")

if email.count('.') < 1:
    print("An email address has to contain at least one '.' character!")

if dom.count('.') < 1:
    print("The domain has to contain at least one '.' character!")

sdom = dom.split('.')
adress_dom = sdom[0]
toplevel_dom = sdom[1]

if toplevel_dom == '':
    print("The top-level domain cannot be empty!")

if toplevel_dom.count < 2:
    print("The top-level domain has to be at least two characters long!")

if uname.startswith('.'):
    print("The username cannot start with a '.' character!")

if toplevel_dom.startswith('.'):
    print("The domain cannot start with a '.' character!")

if adress_dom.startswith('.'):
    print("The adress cannot start with a '.' character!")



