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

        r = requests.post(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/", headers=headers, data=data)

        # print(r.text)

        if (r.status_code == 201):
            return r.content.decode()
        
        raise Exception (r.json()[0]["message"])

    def updateRecord(self, resource, theObject, record, data):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "Content-Type" : "application/json",
            "X-PrettyPrint" : "1"
        }

        r = requests.patch(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers, data=data)

        if (r.status_code == 204):
            return True
        
        raise Exception (r.json()[0]["message"])

    def deleteRecord(self, resource, theObject, record):
        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.delete(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}", headers=headers)

        if (r.status_code == 204):
            return True
        
        raise Exception (r.json()[0]["message"])

    def queryOnRecord(self, resource, theObject, record, query):

        headers = {
            "Authorization" : f"Bearer {self.accessToken}",
            "X-PrettyPrint" : "1"
        }

        r = requests.get(f"https://{self.domain}.salesforce.com/services/data/v52.0/{resource}/{theObject}/{record}?fields={query}", headers=headers)

        if (r.status_code == 200):
            return r.content.decode()
        
        raise Exception (r.json()[0]["message"])

if __name__ == "__main__":

    import requests
    import json

    data = {"grant_type":"password",
            "client_id":"3MVG9ayzKZt5EleHsI9aFMkaUhMYgp8wYbToQQ2e.Qd7zK3UIkfI8kw1cybdjjvRiViuyHRzd_hpsc4X7cJQs",
            "client_secret":"E6F1E861EED2E92DB0DA70131307C738D918BF1AE6962FAB56D8F7BEEF7ED84D",
            "username":"rocketbot@salesforce.desarrollo",
            "password":"Salesf0rce Rocket 2021aTl3VbIRSYMN82lC1qdxaxad2"}

    r = requests.post('https://wodobox--rocketbot.my.salesforce.com/services/oauth2/token', data=data)
    a = eval(r.content.decode())
    # print(a["access_token"])
    # print(r.content.decode())
    # print(r.status_code)
    # print(a["access_token"])

    # r = requests.get('https://wodobox--rocketbot.my.salesforce.com/services/data/')

    # a = eval(r.content.decode())

    # print(a)

    # record = {
    #     "Name" : "Probando record2"
    # }

    # record = json.dumps(record)
    # print(record)

    # headers = {
    #     "Authorization" : f'Bearer {a["access_token"]}',
    #     "Content-Type" : "application/json",
    #     "X-PrettyPrint" : "1"
    # }

    # data = record

    # r = requests.patch('https://wodobox--rocketbot.my.salesforce.com/services/data/v52.0/sobjects/Account/00153000004veFTAAY', headers=headers, data=record)

    # # b = eval(r.content.decode())
    # b = r.content.decode()
    
    # print(b)


    headers = {
        "Authorization" : f'Bearer {a["access_token"]}',
        "X-PrettyPrint" : "1"
    }


    r = requests.get('https://wodobox--rocketbot.my.salesforce.com/services/data/v52.0/sobjects/Account/', headers=headers)

    # b = eval(r.content.decode())
    b = r.content.decode()
    
    print(b)

    # url = "https://wodobox--rocketbot.my.salesforce.com/services/oauth2/token"

    # payload='grant_type=password&client_id=3MVG9ayzKZt5EleHsI9aFMkaUhMYgp8wYbToQQ2e.Qd7zK3UIkfI8kw1cybdjjvRiViuyHRzd_hpsc4X7cJQs&client_secret=E6F1E861EED2E92DB0DA70131307C738D918BF1AE6962FAB56D8F7BEEF7ED84D&username=rocketbot@salesforce.desarrollo&password=Salesf0rce Rocket 2021'
    # headers = {
    #   'Content-Type': 'application/x-www-form-urlencoded',
    #   'Accept': 'application/json',
    #   'Cookie': 'BrowserId=h6vfZybKEeyyQ_0wZGRyRQ'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    # print(response.content.decode())
    # print(response.status_code)

    # # curl https://wodobox--rocketbot.my.salesforce.com/services/oauth2/token -d 'grant_type=password' -d 'client_id=3MVG9ayzKZt5EleHsI9aFMkaUhMYgp8wYbToQQ2e.Qd7zK3UIkfI8kw1cybdjjvRiViuyHRzd_hpsc4X7cJQs' -d 'client_secret=E6F1E861EED2E92DB0DA70131307C738D918BF1AE6962FAB56D8F7BEEF7ED84D' -d 'username=rocketbot@salesforce.desarrollo' -d 'password=Salesf0rce Rocket 2021'


    ###

    # import requests

    # # Consumer Key
    # client_id = '3MVG9ayzKZt5EleHsI9aFMkaUhMYgp8wYbToQQ2e.Qd7zK3UIkfI8kw1cybdjjvRiViuyHRzd_hpsc4X7cJQs'

    # # Consumer Secret
    # client_secret = 'E6F1E861EED2E92DB0DA70131307C738D918BF1AE6962FAB56D8F7BEEF7ED84D'

    # # Callback URL
    # redirect_uri = 'http://localhost:55555/'

    # # sfdc_user = your SFDC username
    # sfdc_user = 'rocketbot@salesforce.desarrollo'

    # # sfdc_pass = your SFDC password
    # sfdc_pass = 'Salesf0rce Rocket 2021'

    # # Visit https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_oauth_endpoints.htm
    # auth_url = 'https://wodobox--rocketbot.my.salesforce.com/services/oauth2/token'

    # # POST request for access token
    # response = requests.post(auth_url, data = {
    #                     'client_id':client_id,
    #                     'client_secret':client_secret,
    #                     'grant_type':'password',
    #                     'username':sfdc_user,
    #                     'password':sfdc_pass
    #                     })

    # print(response.content)
    # print(response.status_code)
