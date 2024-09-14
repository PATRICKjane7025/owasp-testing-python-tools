import requests
import ssl
import socket
from urllib.parse import urlparse

def check_security_headers(url):
    try:
        
        response = requests.get(url, verify=False)
        headers = response.headers
        
        security_headers = {
            "Strict-Transport-Security": "HSTS (HTTP Strict Transport Security)",
            "Content-Security-Policy": "CSP (Content Security Policy)",
            "X-Frame-Options": "Protects against clickjacking",
            "X-XSS-Protection": "Cross-site scripting protection",
            "X-Content-Type-Options": "Prevents MIME-sniffing",
            "Referrer-Policy": "Controls the information sent in referrer headers"
        }
        
        print(f"\nTesting security headers for {url}\n")
        
        for header, description in security_headers.items():
            if header in headers:
                print(f"{header}: Present - {description}")
            else:
                print(f"{header}: Missing - {description}")
                
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def check_https_configuration(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        if not hostname:
            raise ValueError("Invalid URL, unable to extract hostname.")

       
        context = ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')  

        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"\nSSL Certificate for {hostname}:\n{cert}")

    except (ValueError, Exception) as e:
        print(f"Error with HTTPS configuration for {url}: {e}")

def main():
    
    test_url = 'https://azqa.reloology.com'
    
    check_security_headers(test_url)


    parsed_url = urlparse(test_url)
    if parsed_url.scheme == 'https':
        check_https_configuration(test_url)
    else:
        print(f"URL does not use HTTPS: {test_url}")

if __name__ == "__main__":
    main()
