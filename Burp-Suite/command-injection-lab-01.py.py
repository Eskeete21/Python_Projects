import requests
import sys
import urllib3
#from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def main():
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> <command>" % sys.argv[0])
        print("(+) Example: %s www.example.com whoami" % sys.argv[0])
        sys.exit(-1)

if __name__ == "__main__":
    main()

