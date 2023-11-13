import requests
from env_setup import Endpoints


class Forgot:

    def __init__(self, session: requests.Session):
        self.session = session
        self.headers = {'Content-Type': 'application/json'}

    def forgot_email_dfile(self):
        data = {"email": "dariatestik+1@gmail.com"}
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/forgot_password_intent", headers=self.headers,
                                     json=data)
        assert response.status_code == 200, f"actual status code: {response.status_code}"

    def forgot_email_dfile_bad(self):
        data = {"email": "darey@mail.com"}
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/oauth/forgot_password_intent", headers=self.headers,
                                     json=data)
        assert response.status_code == 400, f"actual status code: {response.status_code}"
        assert response.json() == {
            "msg": "This email does not have an existing account"}, f"actual response body: {response.json()}"

    def forgot_email_satelit(self):
        data = {"email": "dariatestik+33@gmail.com", "source": "stage.irsextension.online"}
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/recover/", headers=self.headers, json=data)
        assert response.status_code == 200, f"actual status code: {response.status_code}"
        assert response.json() == {"status": True}, f"actual response body: {response.json()}"

    def forgot_email_satelit_bad(self):
        data = {"email": "dariagmail.com", "source": "stage.irsextension.online"}
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/recover/", headers=self.headers, json=data)
        assert response.status_code == 200, f"actual status code: {response.status_code}"
        assert response.json() == {"status": False, "error": "This email does not have an existing account",
                                   "token": None}, f"actual response body: {response.json()}"
