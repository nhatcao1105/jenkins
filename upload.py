import requests
import json
base_url = 'http://20.239.191.41:8081'
headers = {"X-JFrog-Art-Api":"AKCp8mYoWpeZkQbHVswXzLBCL1ckJ5MRLgCrcDFHSEisPJTHp1sHKDacbZT5XvnuvBCCGrCUr"}
data ={
    "path":"text.text"
}
req = requests.put(url=f'{base_url}/artifactory/generic-local/text.text',headers=headers,json =data)


print("Status Code", req.status_code)
print("JSON Response ", req.json())