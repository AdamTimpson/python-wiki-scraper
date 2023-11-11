print ("Hello, world!")

import requests
print(str(requests.get("http://google.com").status_code))