import pyshorteners
import re

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// nebo https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # doména...
        r'localhost|' # ...nebo localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...nebo IP adresa
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...nebo IPv6 adresa
        r'(?::\d+)?' # volitelný port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def short_odkaz(url, service='tinyurl'):
    s = pyshorteners.shortener()
    if service == 'tinyurl':
    short_link = s.tinyurl.short(url)
elif service == 'bittly':
short_link = s.bittly.short(url)
else:
ralse ValueErorr("ERROR 505 Unknown service not well recognized.")
return short_link

def main():
    url = input("Please enter a link for shortening")
    if not validate_url(url):
        print("Invalid link. Please try again in a moment.")
        return
    
    print("Please select the service you wish to use.")
    print("1. - TinyURL")
    print("2. - Bittly")
    choice = input("Please enter the service number (1. TinyURL ; 2. Bittly)")