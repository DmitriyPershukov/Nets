
import sys
import requests
import json


try:
    userId = int(sys.argv[1])
    token = sys.argv[2];
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