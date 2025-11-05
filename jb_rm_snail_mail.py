email = str(input('Please enter you email\n'))

error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_wrong_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"
error_message_wrong_adress_name = "The adress cannot start with a '.' character!"
error_message_empty_address = "The address cannot be empty"

ok_message = "Valid email address :)"



if email.count('@') == 0:
    print (error_message_no_at)
    exit(1)
    
elif email.count('@') > 1:
    print (error_message_too_many_at)
    exit(1)

else:
    uname_dom = email.split('@')
    uname = uname_dom[0]
    dom = uname_dom[1]

if uname == '':
    print(error_message_no_username)
    exit(1)

elif dom == '':
    print(error_message_no_domain)
    exit(1)

elif email.count('.') < 1:
    print(error_message_no_dot)
    exit(1)

elif dom.count('.') < 1:
    print(error_message_no_dot_in_domain)
    exit(1)

elif dom.startswith('.'):
    print(error_message_wrong_adress_name)
    exit(1)

else:
    sdom = dom.split('.')
    adress_dom = sdom[0]
    toplevel_dom = sdom[1]

if toplevel_dom == '':
    print(error_message_no_tld)
    exit(1)

elif adress_dom == '':
    print(error_message_empty_address)
    exit(1)

elif len(toplevel_dom) < 2:
    print(error_message_short_tld)
    exit(1)

elif uname.startswith('.'):
    print(error_message_invalid_username)
    exit(1)

elif toplevel_dom.startswith('.'):
    print(error_message_wrong_server_name)
    exit(1)

else:
    print(ok_message)

