import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    print("Error")

rate = float(response["bpi"]["USD"]["rate"].replace(",", ""))

amount = bitcoin * rate

print(f"${amount:,.4f}")
