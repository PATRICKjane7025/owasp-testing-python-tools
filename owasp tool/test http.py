import requests

def test_http_methods(url):
    methods = [
        'GET',
        'POST',
        'PUT',
        'DELETE',
        'HEAD',
        'OPTIONS',
        'PATCH',
        'TRACE',
        'CONNECT'
    ]
    
    for method in methods:
        try:
            # Use requests.request() to handle different HTTP methods
            response = requests.request(method, url, allow_redirects=False, verify=False)
            print(f"Method: {method}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Body (truncated): {response.text[:200]}")  # Truncate for readability
            print("-" * 40)
        except requests.RequestException as e:
            print(f"Method: {method}")
            print(f"Error: {e}")
            print("-" * 40)

def main():
    
    test_url = 'https://azqa.reloology.com'
    test_http_methods(test_url)

if __name__ == "__main__":
    main()
