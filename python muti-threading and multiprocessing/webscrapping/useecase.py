'''
Real-world example: Multithreading for I/O-bound tasks
Scenario: Web scapping
Web scappin often involves making numerous network requestos to fetch web pages. These tasks are I/O bound because they spend a lot of time
waiting for responses from the server.
Using multithreading can significantly speed up the process by allowing multiple requests to be made concurrently.
This can be especially useful when dealing with websites that have slow response times or when making a large number of requests.
'''

'''
https://registry.terraform.io/providers/hashicorp/aws/latest/docs
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_account
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_base_path_mapping
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://registry.terraform.io/providers/hashicorp/aws/latest/docs',
'https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_account',
'https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_base_path_mapping'
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution.")
