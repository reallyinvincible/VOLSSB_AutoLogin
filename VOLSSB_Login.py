import requests
username = ""
password = ""

url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://phc.prontonetworks.com/"
load = {'userId': username, 'serviceName': "ProntoAuthentication", 'password': password, 'Submit22': "Login"}
session = requests.Session()
session.get(url)
r = session.post(url, data=load)
