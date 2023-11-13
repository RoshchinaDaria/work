import requests
from support.common import generate_email
from env_setup import Endpoints


class RegisterDFile:

    def __init__(self, session: requests.Session):
        self.session = session
        self.email_generator = generate_email(5)
        self.jwttoken = None

    def _get_token(self):
        headers = {'Content-Type': 'application/json'}
        params = {
            "email": f"dariatestik+{self.email_generator}@gmail.com",
            "engine": "string",
            "first_name": "Donald",
            "funnel": "A12",
            "ip_address": "string",
            "last_name": "Trump",
            "password": "Qwerty123!",
            "phone": "4563457624",
            "product_focus": "extension",
            "t_info": {
                "aff_sub_id": "string",
                "affiliate_id": "string",
                "device_id": "70c9c4e9ad15088c46561c0310ad14c6750f1518",
                "lead_id": "string",
                "msclkid": "string",
                "one_signal_app_id": "string",
                "one_signal_user_id": "string",
                "redtrack_click_id": "string",
                "redtrack_domain": "string",
                "search_source": "string",
                "source": "d.file-tax.net",
                "transaction_id": "string"
            },
            "user_agent": "string"
        }
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/register", headers=headers, json=params)
        self.jwttoken = response.json()['jwt_token']

    def users_me(self):
        self._get_token()
        if self.jwttoken:
            headers = {"Authorization": f"Bearer {self.jwttoken}"}
            response = self.session.get(f"{Endpoints.BASE_URL_DFILE}/users/me", headers=headers)
            expected_email = f"dariatestik+{self.email_generator}@gmail.com"
            assert response.json()[
                       'email'] == expected_email, f"actual email: {response.json()['email']}, but expected {expected_email}"
            assert response.json()['phone'] == '4563457624', f"actual email: {response.json()['phone']}"
            assert response.json()['funnel'] == 'A12', f"actual email: {response.json()['funnel']}"
            assert response.json()['first_name'] == 'Donald', f"actual email: {response.json()['first_name']}"
            assert response.json()['last_name'] == 'Trump', f"actual email: {response.json()['last_name']}"

    def registered_email_dfile(self):
        headers = {'Content-Type': 'application/json'}
        params = {
            "email": "dariatestik+456344456@gmail.com",
            "engine": "string",
            "first_name": "Donald",
            "funnel": "A12",
            "ip_address": "string",
            "last_name": "Trump",
            "password": "Qwerty123!",
            "phone": "4563457624",
            "product_focus": "extension",
            "t_info": {
                "aff_sub_id": "string",
                "affiliate_id": "string",
                "device_id": "70c9c4e9ad15088c46561c0310ad14c6750f1518",
                "lead_id": "string",
                "msclkid": "string",
                "one_signal_app_id": "string",
                "one_signal_user_id": "string",
                "redtrack_click_id": "string",
                "redtrack_domain": "string",
                "search_source": "string",
                "source": "d.file-tax.net",
                "transaction_id": "string"
            },
            "user_agent": "string"
        }
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/register", headers=headers, json=params)
        assert response.status_code == 400, f"actual status code: {response.status_code}"
        assert response.json() == {
            "msg": "User with this email or username already exists."
        }, f"actual response body: {response.json()}"
