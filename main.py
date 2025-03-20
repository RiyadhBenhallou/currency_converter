import requests

api_key = "fca_live_NSDgsNc6IOqG6CvRVVUJ1v6F0fn4f9euiREdLBmF"
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
currencies = ["USD", "EUR", "CAD", "AUD", "CNY"]


def convert_currency(base_currency):
    try:
        response = requests.get(
            f"{url}&base_currency={base_currency}&currencies={','.join(currencies)}"
        )
        data = response.json().get("data")
        return data
    except Exception:
        return None


while True:
    base = input("Enter the base currency (q/quit): ").upper()
    if base == "Q":
        break
    amount = int(input("Enter the amount: "))
    try:
        data = convert_currency(base)
        if data:
            del data[base]
        for key, value in data.items():
            print(f"{key}: {(value * amount):.2f}")
    except Exception:
        print("Invalid Currency, please try again")
