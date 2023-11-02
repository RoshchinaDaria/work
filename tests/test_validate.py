import pytest

email_test_data = [
    ("testwerhui@gmail.com", {'status': True}),
    ("drina@my.waketech.edu", {'status': True}),
    ("test.email+regex@example.com", {'status': True}),
    ("test@gmail.com", {'status': False, 'error': 'email already exists', 'token': None}),
    ("@testexample.com", {'status': False, 'error': 'email has invalid syntax', 'token': None}),
    ("test@", {'status': False, 'error': 'email has invalid syntax', 'token': None}),
    ("test@exa$mple.com", {'status': False, 'error': 'email has invalid syntax', 'token': None}),
    (" test@example.com", {'status': False, 'error': 'email has invalid syntax', 'token': None}),
    ("test@examplecom",
     {'status': False, 'error': 'Incorrect email format, unresolvable email provider, please try again',
      'token': None}),
    ("test@fhfghdfghdfghd.dfghfdgd",
     {'status': False, 'error': 'Incorrect email format, unresolvable email provider, please try again', 'token': None})
]


@pytest.mark.parametrize("input_email,expected_output", email_test_data)
def test_validate_email(validate, input_email, expected_output):
    validate.validate_email(input_email, expected_output)


password_test_data = [
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "Qwerty123!"}, {'status': True}),
    ({
         "password": "F8NCf@fKjZKvnYqAQr9gE^SpCCHk@qVxppKyVu@KDw5RdnNAKBn%2xso%AiyeQ8BK4@m^&6!deuvjrHJD28DeM%WV^8CRerF^!WH5UJgRdPfVwBXUrE5@Q&84BZwpF5k$5Rto3qZ%2hjc5cbLw5p3DeFSiDb5H$d52DUvTejR4diqeq"},
     {'status': True}),
    ({"email": "@inva@2#@lidEmail", "first_name": "213432453246", "last_name": "jhgjg$&*jhkроалп",
      "password": "F8NCf@fKjZKvnYqAQr9gE^Spgf прлаплCCHk@qVxppKyVu@KDw5RdnNAKBn%2аенлдаелxso%AiyeQ8BK4@m^&6!deuvjrHJD28DeM%WV^8CRerF^!WH5UJgRdPfVwBXUrE5@Q&84BZwpF5k$5Rto3qZ%2hjc5cbLw    5p3DeFSiDb5H$d52DUvTejR4diqeq"},
     {'status': True}),
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "Qwerty123"},
     {'status': False, 'error': 'PASSWORD MUST HAVE AT LEAST ONE SPECIAL CHARACTER CHARACTER'}),
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "Qwertyyyyy!"},
     {'status': False, 'error': 'PASSWORD MUST HAVE AT LEAST ONE NUMBER CHARACTER'}),
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "qwerty123!"},
     {'status': False, 'error': 'PASSWORD MUST HAVE AT LEAST ONE UPPERCASE CHARACTER'}),
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "Qw123!"},
     {'status': False, 'error': 'PASSWORD SHOULD BE AT LEAST 8 CHARACTERS LONG'}),
    ({"email": "string", "first_name": "string", "last_name": "string", "password": "QWERTY123!"},
     {'status': False, 'error': 'PASSWORD MUST HAVE AT LEAST ONE LOWERCASE CHARACTER'}),
]


@pytest.mark.parametrize("input_data,expected_output", password_test_data)
def test_validate_password(validate, input_data, expected_output):
    validate.validate_password(input_data, expected_output)


phone_test_data = [
    ({"phone": "9847667"}, 400, {'msg': "Please enter a valid cell phone number"}),
    ({"phone": "0000000000"}, 400, {'msg': "Please enter a valid cell phone number"}),
    ({"phone": "9847384617"}, 200, {})
]


@pytest.mark.parametrize("input_phone,expected_status_code, expected_output", phone_test_data)
def test_validate_phone(validate, input_phone, expected_status_code, expected_output):
    validate.validate_phone(input_phone, expected_status_code, expected_output)
