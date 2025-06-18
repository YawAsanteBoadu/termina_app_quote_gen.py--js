import requests
import pyperclip

# @function: fetch a random qoute from the API.  
def fetch_random_qoute():
    first_api = "https://api.api-ninjas.com/v1/quotes"
    # second_api = ""https://zenquotes.io/api/quotes/author/abraham-lincoln/"
    try:
        response = requests.get(first_api, verify=False)
        if response.status_code == 200:
            data = response.json()
            return{'qoute' : data['content'], 'auhtor' : data['author']}
        else:
            print("Error fetching quote. Try again!")
            return None
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        return None
    
# @functon: to display the menu. 
def display_menu():
    print(f'\nWelcome to the Quote Generator written in Python')
    print(f'1. Generate a new quote')
    print(f'2. Copy the quote to clipboard')
    print(f'3. Exit')

# main application. 
def run_quote_generator():
    current_quote = None

while True:
    display_menu()
    choice = input(f'Choose an option¦  ')

    if choice == "1":
        current_quote = fetch_random_qoute()
        if current_quote:
            print(f'Quote: {current_quote['quote']}')
            print(f'Author: {current_quote['author']}')
    elif choice == "2":
        if current_quote:
            quote_text = f'{current_quote['quote']} - {current_quote['author']}'
            pyperclip.copy(quote_text)
            print('Your quote has been copied to the clipboard!')
        else:
            print('Generate a quote first📥')
    elif choice == "3":
        print('Thank You for your time. GoodBye👋 🙋‍♂️')
        break
    else:
        print('You need to a proper input‼️')

# run the application:
run_quote_generator()


