import urllib.request as urlib

def main(url):
    print("Checking conectivity...")

    response = urlib.urlopen(url)
    print(f"Connected to {url} sucessfully")
    print(f"The response code was: {response.getcode()}")


print("Site Conectivity Checker\n")
input_url = input("Input url\n")
main(input_url)