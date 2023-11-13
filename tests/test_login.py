def test_success_login_satelit(login_satelit):
    login_satelit.users_me()


def test_success_login_dfile(login_dfile):
    login_dfile.users_me()


def test_login_bad(login_dfile):
    login_dfile.login_dfile_bad()


def test_login_bad(login_satelit):
    login_satelit.login_satelit_bad()
