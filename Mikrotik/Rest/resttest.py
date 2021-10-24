import requests
from requests.auth import HTTPBasicAuth



response = requests.get('https://192.168.2.1/rest/interface', auth=HTTPBasicAuth('api','mysecretsauce123'), verify=False)
print(response.json())

