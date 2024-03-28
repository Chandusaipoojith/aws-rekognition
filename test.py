import requests

url="https://hq1een3z64.execute-api.us-east-1.amazonaws.com/dev/detection"
with open("cat.jpeg","rb") as image:
    image_data=image.read()

headers={
    "Content-Type":"image/*",
}
response=requests.post(url,headers=headers,data=image_data)
d={}
d[1]=response.json()
print(d)