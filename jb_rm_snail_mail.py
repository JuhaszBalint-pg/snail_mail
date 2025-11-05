email = str(input('Please enter you email\n'))

atfinder= email.find("@")
if atfinder != -1 and atfinder == 1:
    uname_dom = email.split('@')
    uname = uname_dom[0]
    dom = uname_dom[1]
    sdom = dom.split('.')
    adress_dom = sdom[0]
    toplevel_dom = sdom[1]

error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_no_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"
error_message_no_adress_name = "The adress cannot start with a '.' character!"
error_message_empty_address = "The address cannot be empty"

ok_message = "Valid email address :)"



if email.count('@') < 1:
    print (error_message_no_at)
    
elif email.count('@') > 1:
    print (error_message_too_many_at)

elif uname == '':
    print(error_message_no_username)

elif dom == '':
    print(error_message_no_domain)

elif email.count('.') < 1:
    print(error_message_no_dot)

elif dom.count('.') < 1:
    print(error_message_no_dot_in_domain)

elif toplevel_dom == '':
    print(error_message_no_tld)

elif adress_dom == '':
    print(error_message_empty_address)

elif len(toplevel_dom) < 2:
    print(error_message_short_tld)

elif uname.startswith('.'):
    print(error_message_invalid_username)

elif toplevel_dom.startswith('.'):
    print(error_message_no_server_name)

elif adress_dom.startswith('.'):
    print(error_message_no_adress_name)

else:
    print(ok_message)

