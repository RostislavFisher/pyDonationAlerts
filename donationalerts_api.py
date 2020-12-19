import requests

class DonationAlertsApi:


	def __init__(self, client_id, client_secret, redirect_uri, scope="oauth-donation-index"):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri
		self.scope = scope
		self.login_url = f"https://www.donationalerts.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
		self.token_url = f"https://www.donationalerts.com/oauth/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code="
		self.user_api = "https://www.donationalerts.com/api/v1/user/oauth"
		self.donations_api = "https://www.donationalerts.com/api/v1/alerts/donations"

	def login(self):
		return self.login_url

	def getAccessToken(self, code):
		payload = {
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": self.redirect_uri,
			"scope": self.scope
		}

		access_token = requests.post(url = self.token_url, data = payload).json()
		return access_token.get("access_token")

	def getDonations(self, access_token):
		headers = {"Authorization": f"Bearer {access_token}"}
		donate_object = requests.get(url = self.donations_api, headers = headers).json()
		print(donate_object)
		return donate_object.get("data")
