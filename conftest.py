import pytest
import requests
from endpoints.register_satelit import RegisterSatelit
from endpoints.register_dfile import RegisterDFile
from endpoints.validate import Validate
from endpoints.login_satelit import LoginSatelit
from endpoints.login_dfile import LoginDfile
@pytest.fixture()
def create_session():
    yield requests.Session()

@pytest.fixture()
def register_satelit(create_session):
    yield RegisterSatelit(session=create_session)

@pytest.fixture()
def register_dfile(create_session):
    yield RegisterDFile(session=create_session)

@pytest.fixture()
def validate(create_session):
    yield Validate(session=create_session)

@pytest.fixture()
def login_satelit(create_session):
    yield LoginSatelit(session=create_session)

@pytest.fixture()
def login_dfile(create_session):
    yield LoginDfile(session=create_session)