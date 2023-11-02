import requests
from env_setup import Endpoints

class Validate:

    def __init__(self, session: requests.Session):
        self.session = session
        self.headers = {'Content-Type': 'application/json'}

    def validate_email(self, input_email, expected_output):
        data = {"email": input_email}
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/validate/email", headers=self.headers, json=data)
        assert response.status_code == 200, f"actual status code: {response.status_code}"
        assert response.json() == expected_output, f"actual response body: {response.json()}"

    def validate_password(self, input_data, expected_output):
        response = self.session.post(f"{Endpoints.BASE_URL_IRSEXTENSION}/api/validate/password", headers=self.headers, json=input_data)
        assert response.status_code == 200, f"actual status code: {response.status_code}"
        assert response.json() == expected_output, f"actual response body: {response.json()}"

    def validate_phone(self, input_data, expected_status_code, expected_output):
        response = self.session.post(f"{Endpoints.BASE_URL_DFILE}/utils/validate/phone", headers=self.headers, json=input_data)
        assert response.status_code == expected_status_code, f"actual status code: {response.status_code}"
        assert response.json() == expected_output, f"actual response body: {response.json()}"