import json
import random
import click
from difflib import get_close_matches
from scr import wolfram  # Import the wolfram module

def load_intents(file_path: str):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents

def find_best_match(user_input: str, intents: dict) -> dict | None:
    for intent in intents["intents"]:
        matches = get_close_matches(user_input, intent["patterns"], n=1, cutoff=0.6)
        if matches:
            return intent
    return None

def get_response_for_input(user_input: str, intents: dict) -> str:
    best_match = find_best_match(user_input, intents)
    if best_match:
        if best_match["tag"] == "commodities":  # If the intent is commodities
            return wolfram.get_commodity_prices()  # Get the commodity prices
        else:
            return random.choice(best_match["responses"])
    else:
        # If no match is found, return a response from the 'noanswer' intent
        noanswer_intent = next(intent for intent in intents["intents"] if intent["tag"] == "noanswer")
        return random.choice(noanswer_intent["responses"])

@click.command()
@click.argument('user_input', default='Hi')
def chatbot(user_input):
    intents = load_intents('data/intents.json')  # Update the path here
    response = get_response_for_input(user_input, intents)
    print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
