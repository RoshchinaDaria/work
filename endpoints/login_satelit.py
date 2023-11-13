import allure
import requests
from env_setup import Endpoints


class LoginSatelit:

    def __init__(self, session: requests.Session):
        self.session = session
        self.token = None
        self.jwttoken = None
        self.headers = {"Authorization": f"Bearer {self.jwttoken}", "Content-Type": "application/json"}

    def login_satelit(self):
        headers = {'Content-Type': 'application/json'}
        params = {
            "device_id": "8882c48a32a23d3a2594014a8210b8295f92a4f7",
            "password": "Qwerty123!",
            "source": "stage.irsextension.online",
            "username": "dariatestik+3@gmail.com"
        }
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/login", headers=headers, json=params)
        self.token = response.json()['token']

    def _exchange_token(self):
        if self.token:
            headers = {'Content-Type': 'application/json'}
            body = {"token": f'{self._get_token()}'}
            response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/exchange/token", headers=headers, json=body)
            self.jwttoken = response.json()['jwt_token']

    def users_me(self):
        self._exchange_token()
        if self.jwttoken:
            response = self.session.get(f"{Endpoints.BASE_URL_DFILE}/users/me", headers=self.headers)
            assert response.json()['email'] == "dariatestik+3@gmail.com", f"actual email: {response.json()['email']}"

    def login_satelit_bad(self):
        headers = {'Content-Type': 'application/json'}
        params = {
            "device_id": "8882c48a32a23d3a2594014a8210b8295f92a4f7",
            "password": "Qwerty123!",
            "source": "stage.irsextension.online",
            "username": "darq@gmail.com"
        }
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/login", headers=headers, json=params)
        assert response.status_code == 200, f"actual status code: {response.status_code}"
        assert response.json() == {
            "status": False,
            "error": "Email or Username / Password combination not found.",
            "token": None
        }, f"actual response body: {response.json()}"
