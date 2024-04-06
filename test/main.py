import requests

url = "http://localhost:8000/download-file/model.h5"
response = requests.get(url)

with open("model/model.h5", "wb") as f:
    f.write(response.content)
