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
            a = r.json()
            self.accessToken = a["access_token"]
            

    def getListResources(self):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/", headers=headers)
        
        if (r.status_code == 200):
            return r.json()
        else:
            raise Exception(r.json()[0].get('message'))

    def getListObjects(self, resource):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/", headers=headers)

        if (r.status_code == 200):
            return r.json()
        else:
            raise Exception(r.json()[0].get('message'))

    def getMetadata(self, resource, theObject):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/", headers=headers)

        if (r.status_code == 200):
            return r.json()
        else:
            raise Exception(r.json()[0].get('message'))

    def createRecord(self, resource, theObject, data):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "Content-Type" : "application/json",
            "X-PrettyPrint" : "1"
        }

        r = requests.post(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/", headers=headers, data=data)

        if (r.status_code == 201):
            return r.json()
        else:
            raise Exception(r.json()[0].get('message'))

    def updateRecord(self, resource, theObject, record, data):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "Content-Type" : "application/json",
            "X-PrettyPrint" : "1"
        }

        r = requests.patch(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers, data=data)

        if (r.status_code == 204 or r.status_code == 201):
            return True
        
        raise Exception(r.json()[0].get('message'))

    def deleteRecord(self, resource, theObject, record):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.delete(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers)

        if (r.status_code == 204):
            return True
        
        raise Exception(r.json()[0].get('message'))

    def queryOnRecord(self, resource, theObject, record, query):

        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }
        if query != "":
            r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}?fields={query}", headers=headers)
        else:
            r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers)

        if (r.status_code == 200):
            return r.json()
        
        raise Exception(r.json()[0].get('message'))

