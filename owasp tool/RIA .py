import requests

def check_cross_domain_policy(url):
    try:
        
        response = requests.get(f"{url}/crossdomain.xml", verify=False)
        if response.status_code == 200:
            print(f"Cross-domain policy file found at {url}/crossdomain.xml")
            print("Content:")
            print(response.text)
        else:
            print(f"No cross-domain policy file found at {url}/crossdomain.xml")
    except requests.RequestException as e:
        print(f"Error accessing {url}/crossdomain.xml: {e}")

def main():
    
    test_url = 'https://azqa.reloology.com'
    check_cross_domain_policy(test_url)

if __name__ == "__main__":
    main()
