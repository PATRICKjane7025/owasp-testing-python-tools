import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


url = 'https://stage.virtualcaresystems.org'
sensitive_extensions = ['.env', '.bak', '.sql', '.log', '.git', '.htpasswd', '.config']


def create_session():
    session = requests.Session()
    retry = Retry(
        total=5, 
        backoff_factor=1, 
        status_forcelist=[502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    return session


def check_sensitive_files(url, extensions):
    session = create_session()
    for ext in extensions:
        test_url = f'{url}/{ext}'
        try:
            response = session.get(test_url, verify=False)  
            if response.status_code == 200:
                print(f"Sensitive file found: {test_url}")
            elif response.status_code == 403:
                print(f"Forbidden access to: {test_url}")
            elif response.status_code == 404:
                print(f"File not found: {test_url}")
            else:
                print(f"Unexpected status code {response.status_code} for {test_url}")
        except requests.RequestException as e:
            print(f"Error accessing {test_url}: {e}")


check_sensitive_files(url, sensitive_extensions)
