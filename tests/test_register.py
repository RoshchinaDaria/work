def test_success_register_satelit(register_satelit):
    register_satelit.users_me()


def test_success_register_dfile(register_dfile):
    register_dfile.users_me()


def test_registered_email_dfile(register_dfile):
    register_dfile.registered_email_dfile()


def test_registered_email_satelit(register_satelit):
    register_satelit.registered_email_satelit()
