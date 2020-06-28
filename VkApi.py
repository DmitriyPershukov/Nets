
import sys
import requests

if(sys.argv[1] is None or sys.argv[2] is None):
    print("need argument")
userId = int(sys.argv[1]);
token = "b09eafbbd3026b3f2094968fb144c16ffa4a477cc55f33ff06bfa3f5663c0b7b5c57519a9661c9e91130d"

url = f"https://api.vk.com/method/friends.get?user_id={userId}&fields=nickname&access_token={token}&v=5.52";
responce = requests.get(url)
print(responce.content)
