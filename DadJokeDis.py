import requests
import random

# List of dad jokes
jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why did the coffee file a police report? It got mugged!",
    "Why don't oysters give to charity? Because they're shellfish!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why do chicken coops only have two doors? Because if they had four, they'd be a chicken sedan!",
]

# Choose a random joke
joke = random.choice(jokes)

# Discord webhook URL
webhook_url = "Your webhook url"

# Payload for the webhook
payload = {
    "content": joke
}

# Send the webhook
response = requests.post(webhook_url, json=payload)

# Print the response status code
print(response.status_code)
