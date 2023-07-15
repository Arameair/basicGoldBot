import os
import wolframalpha
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_commodity_price(commodity, weight_in_grams=1, karat=None):
    # Get the WolframAlpha App ID from the environment variables
    app_id = os.getenv('WOLFRAM_APP_ID')
    client = wolframalpha.Client(app_id)
    res = client.query(f'{commodity} price')
    price_per_ounce = float(next(res.results).text.replace('$', '').split('/')[0])  # Extract the price from the result

    # Convert weight from grams to troy ounces (1 troy ounce is approximately 31.1035 grams)
    weight_in_ounces = weight_in_grams / 31.1035

    # If the commodity is gold and a karat value is provided, adjust the price for the gold purity
    if commodity == 'gold' and karat is not None:
        price_per_ounce *= karat / 24.0  # 24 karat gold is considered pure gold

    return price_per_ounce * weight_in_ounces

def get_commodity_prices():
    commodity = input("Enter the commodity (gold/silver/platinum): ")
    weight_in_grams = float(input("Enter the weight in grams: "))
    karat = None
    if commodity == 'gold':
        karat = int(input("Enter the karat (if gold): "))
    price = get_commodity_price(commodity, weight_in_grams, karat)
    return f'The price of {weight_in_grams} grams of {commodity} is approximately ${price:.2f}'

print(get_commodity_prices())
