from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection
from colorama import Fore

def check_https_url(url):
    HTTPS_URL = f'https://{url}'
    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=2)
        connection.request('HEAD', HTTPS_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False


def check_http_url(url):
    HTTP_URL = f'http://{url}'
    try:
        HTTP_URL = urlparse(HTTP_URL)
        connection = HTTPConnection(HTTP_URL.netloc)
        connection.request('HEAD', HTTP_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False


with open('C:/chemin/vers/le/fichier/urls.txt', 'r') as file:
    for BASE_URL in file:
        if check_https_url(BASE_URL):
            print("https://" + BASE_URL, end = "")
        elif check_http_url(BASE_URL):
            print("http://" + BASE_URL, end = "")
        else:
            print(Fore.RED + "MARCHE PAS - " + BASE_URL, end = "")

