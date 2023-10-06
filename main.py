import requests
class сonverter:
   def __init__(self):
       self.rates = {}
   def get_rates(self):
       response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
       data = response.json()
       for item in data:
           self.rates[item['cc']] = item['rate']
   def convert(self,amount,from_currency,to_currency):
       if from_currency != "USD":
           amount = amount / self.rates[from_currency]
       amount = round(amount * self.rates[to_currency], 2)
       return amount
converter = сonverter()
converter.get_rates()
while True:
   try:
       amount = input(input("Enter the amount of currency: "))
       fromcurrency = input(input("Enter the currency code of the amount you entered: "))
       tocurrency = "USD"
       convertedamount = converter.convert(amount,fromcurrency.upper(),tocurrency)
       print("The amount of {} {} is equal to {:.2f} USD".format(amount,fromcurrency.upper(),convertedamount))
       break
   except KeyError:
       print("Invalid currency code entered. Please try again.")
   except ValueError:
       print("Invalid amount entered. Please try again.")