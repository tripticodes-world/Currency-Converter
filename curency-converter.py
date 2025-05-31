class CurrencyConverter:
    def __init__(self, rates, names):
        self.rates = rates
        self.names = names

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            return "Currency not supported."

        usd_amount = amount / self.rates[from_currency]
        converted = usd_amount * self.rates[to_currency]
        return round(converted, 2)

    def get_currency_name(self, code):
        return self.names.get(code, code)

def main():
    # Exchange rates relative to USD
    exchange_rates = {
        "USD": 1.0,
        "INR": 83.0,
        "EUR": 0.92,
        "GBP": 0.78,
        "JPY": 157.3,
        "AUD": 1.51
    }

    # Full names of currencies
    currency_names = {
        "USD": "United States Dollar",
        "INR": "Indian Rupee",
        "EUR": "Euro",
        "GBP": "British Pound Sterling",
        "JPY": "Japanese Yen",
        "AUD": "Australian Dollar"
    }

    converter = CurrencyConverter(exchange_rates, currency_names)

    print("💱 Welcome to the Currency Converter 💱")
    print("\nSupported Currencies:")
    for code, name in currency_names.items():
        print(f"  {code} - {name}")

    try:
        amount = float(input("\nEnter amount: "))
        from_currency = input("From currency code (e.g., USD, INR): ").upper()
        to_currency = input("To currency code (e.g., EUR, JPY): ").upper()

        result = converter.convert(amount, from_currency, to_currency)

        if isinstance(result, str):
            print(result)
        else:
            from_name = converter.get_currency_name(from_currency)
            to_name = converter.get_currency_name(to_currency)
            print(f"\n{amount} {from_currency} ({from_name}) = {result} {to_currency} ({to_name})")

    except ValueError:
        print("Invalid amount entered. Please enter a number.")


if __name__ == "__main__":
    main()
