import requests
import json

class SalesforceObj:

    def __init__(self, username, password, client_id, client_secret, token, domain):

            self.username = username
            self.password = password
            self.client_id = client_id
            self.client_secret = client_secret
            self.token = token
            self.domain = domain
            self.accessToken = ""

            data = {"grant_type":"password",
                    "client_id":f"{client_id}",
                    "client_secret":f"{client_secret}",
                    "username":f"{username}",
                    "password":f"{password}{token}"}

            r = requests.post(f"https://{domain}.salesforce.com/services/oauth2/token", data=data)

            a = eval(r.content.decode())

            self.accessToken = a["access_token"]
            

    def getListResources(self):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/", headers=headers)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False

    def getListObjects(self, resource):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/", headers=headers)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False

    def getMetadata(self, resource, theObject):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/", headers=headers)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False

    def createRecord(self, resource, theObject, data):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "Content-Type" : "application/json",
            "X-PrettyPrint" : "1"
        }

        data = json.dumps(data)

        r = requests.post(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/", headers=headers, data=data)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False

    def updateRecord(self, resource, theObject, record, data):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "Content-Type" : "application/json",
            "X-PrettyPrint" : "1"
        }

        data = json.dumps(data)

        r = requests.patch(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers, data=data)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False

    def deleteRecord(self, resource, theObject, record):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.delete(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers)

        if (r.status_code == 200):
            return r.content.decode()
        else:
            return False
