import requests
from env_setup import Endpoints

class LoginDfile:

    def __init__(self, session: requests.Session):
        self.session = session
        self.jwttoken = None
        # self.headers = {"Authorization": f"Bearer {self.jwttoken}"}


    def login_dfile(self):
        headers = {'Content-Type': 'application/json'}
        params = {
    "device_id": "70c9c4e9ad15088c46561c0310ad14c6750f1518",
  "password": "Qwerty123!",
  "source": "d.file-tax.net",
  "username": "teвцstj@mail.com"
}
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/token", headers=headers, json=params)
        self.jwttoken = response.json()['jwt_token']

    def users_me(self):
        self.login_dfile()
        if self.jwttoken:
            headers = {"Authorization": f"Bearer {self.jwttoken}"}
            response = self.session.get(f"{Endpoints.BASE_URL_DFILE}/users/me", headers=headers)
            expected_email = "teвцstj@mail.com"
            assert response.json()[
                       'email'] == expected_email, f"actual email: {response.json()['email']}, but expected {expected_email}"
            assert response.json()['phone'] == '9840000000', f"actual email: {response.json()['phone']}"
            assert response.json()['funnel'] == 'A0', f"actual email: {response.json()['funnel']}"
            assert response.json()['first_name'] == 'drherh', f"actual email: {response.json()['first_name']}"
            assert response.json()['last_name'] == 'srhrh', f"actual email: {response.json()['last_name']}"