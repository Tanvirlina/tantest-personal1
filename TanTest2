import requests

url = "https://open.er-api.com/v6/latest/USD"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Get Bangladeshi Taka rate
    bdt_rate = data["rates"]["BDT"]

    print("Today's Dollar to Taka Exchange Rate")
    print("------------------------------------")
    print(f"1 USD = {bdt_rate:.2f} BDT")

    # Example conversion
    dollars = 100
    taka = dollars * bdt_rate

    print(f"${dollars} = {taka:.2f} BDT")

except requests.exceptions.RequestException as error:
    print("Error getting exchange rate:")
    print(error)

except KeyError:
    print("Could not find BDT exchange rate.")