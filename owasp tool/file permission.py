import os
import requests
from urllib.parse import urlparse

def check_file_permissions(url):
    
    try:
        response = requests.get(url, verify=False)  
        response.raise_for_status()  
        
    
        if response.status_code == 200:
          
            print(f"File found at {url} - Status Code: {response.status_code}")
          
        else:
            print(f"File not found or inaccessible at {url} - Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def check_website_file_permissions(base_url, paths):
    parsed_url = urlparse(base_url)
    for path in paths:
        url = f"{parsed_url.scheme}://{parsed_url.netloc}{path}"
        check_file_permissions(url)


base_url = 'https://stage.virtualcaresystems.org'
file_paths = [
    '/path/to/file1',
    '/path/to/file2',
    '/another/path/to/file'
]

check_website_file_permissions(base_url, file_paths)
