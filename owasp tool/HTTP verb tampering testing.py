import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of HTTP methods to test
http_methods = [
    'OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT',
    'PROPFIND', 'PROPPATCH', 'MKCOL', 'COPY', 'MOVE', 'LOCK', 'UNLOCK'
]

def test_http_methods(url):
    # Ensure the URL has the correct format
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    print(f"Testing HTTP methods for: {url}\n")

    for method in http_methods:
        try:
            # Send the request with the current HTTP method
            response = requests.request(method, url, verify=False)
            
            # Determine if the test was successful or failed
            if response.status_code in [200, 204, 301, 302]:  # Success codes
                result = "SUCCESS"
            elif response.status_code == 405:  # Method Not Allowed
                result = "FAILED (Method Not Allowed)"
            else:
                result = "FAILED (Other Error)"

            # Print the results
            print(f"Method: {method}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Result: {result}\n")
        except requests.exceptions.RequestException as e:
            print(f"Method: {method} encountered an error: {e}\n")

if __name__ == "__main__":
    url = input("Enter the URL to test: ")
    test_http_methods(url)
