import pyshorteners
import re

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # ...or localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or IP address
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or IPv6 address
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def short_odkaz(url, service='tinyurl'):
    s = pyshorteners.Shortener()
    if service == 'tinyurl':
        short_link = s.tinyurl.short(url)
    elif service == 'bitly':
        short_link = s.bitly.short(url)
    else:
        raise ValueError("ERROR 505 Unknown service not well recognized.")
    return short_link

def main():
    url = input("Please enter a link for shortening: ")
    if not validate_url(url):
        print("Invalid link. Please try again.")
        return
    
    print("Please select the service you wish to use.")
    print("1. - TinyURL")
    print("2. - Bitly")
    choice = input("Please enter the service number (1 for TinyURL, 2 for Bitly): ")

    if choice == '1':
        service = 'tinyurl'
    elif choice == '2':
        service = 'bitly'
    else:
        print("Invalid choice. Please try again.")
        return

    try:
        short_link = short_odkaz(url, service)
        print(f"Shortened link: {short_link}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
