import requests
from bs4 import BeautifulSoup, Comment

def review_webpage(url):
   
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Invalid URL. URL should start with http:// or https://")
        return

    try:
       
        response = requests.get(url, verify=False)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')


        comments = soup.findAll(string=lambda text: isinstance(text, Comment))
        if comments:
            print("Comments found:")
            for comment in comments:
                print(f"Comment: {comment}")
        else:
            print("No comments found.")

        meta_tags = soup.find_all('meta')
        if meta_tags:
            print("\nMetadata found:")
            for meta in meta_tags:
                print(f"Meta tag: {meta}")
        else:
            print("No metadata found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# URL of the target webpage
url = 'https://stage.virtualcaresystems.org'
review_webpage(url)
