
import requests
from datetime import date
url = "https://XYZ.erpnext.com/api/resource/attendance"

headers ={
    "Authorization":"token b8117b2c836c634:***************"
}
data ={
    "employee":"HR-EMP-00001",
    "status":"Present"
}
response =requests.post(url,headers=headers,json=data)
print(response.json())