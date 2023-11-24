import json
import requests
import sys

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif isFloat(sys.argv[1]) == False:
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        jsonResponse = response.json()
        quantity = float(sys.argv[1])
        btcPrice = jsonResponse["bpi"]["USD"]["rate_float"]

        amount = quantity * btcPrice
        print(f"${amount:,.4f}")

    except requests.RequestException:
        pass


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

main()