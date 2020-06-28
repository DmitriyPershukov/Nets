
import sys
import requests
import json


try:
    userId = int(sys.argv[1]);
    token = "074477f9e69ea437917912cbf84b0dc22375d592ee28a56d96f07856b3a888d3f5ad45264ea5dfaacecdd"
except:
    print()
    sys.exit(9)

url = f"https://api.vk.com/method/photos.getAlbums?user_id={userId}&fields=nickname&access_token={token}&v=5.52";
responce = requests.get(url)
jsonParsed = json.loads(responce.content)
try:
    for i in jsonParsed['response']["items"]:
        print(f"id{i['id']}")
except:
    print(jsonParsed["error"]["error_msg"])
f :int = 3
