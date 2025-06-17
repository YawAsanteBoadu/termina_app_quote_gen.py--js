import requests 
import pyperclip

# @function: fetch a random qoute from the API 
def fetch_random_qoute():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return{'qoutes' : data['content'], 'auhtor' : data['author']}
        else:
            print("Error fetching quote. Try again later")
            return None
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        return None