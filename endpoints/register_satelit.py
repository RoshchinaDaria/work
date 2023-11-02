import requests
from support.common import generate_email
from env_setup import Endpoints

class RegisterSatelit:

    def __init__(self, session: requests.Session):
        self.session = session
        self.email_generator = generate_email(5)
        self.token = None
        self.jwttoken = None
        self.headers = {"Authorization": f"Bearer {self.jwttoken}", "Content-Type": "application/json"}

    def _get_token(self):
        headers = {'Content-Type': 'application/json'}
        params = {
            "email": f"dariatestik+{self.email_generator}@gmail.com",
            "device_id": "70c9c4e9ad15088c46561c0310ad14c6750f1518",
            "password": "Qwerty123!",
            "product_focus": "extension",
            "source": "stage.irsextension.online"
        }
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/register", headers=headers, json=params)
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
            assert response.json()['email'] == f"dariatestik+{self.email_generator}@gmail.com", f"actual email: {response.json()['email']}"





