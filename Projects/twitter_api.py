import os
import webbrowser
from twython import Twython
# Feel free to plug your key and secret in directly
CONSUMER_KEY = os.environ.get("PLLmB0p9Yu4ecNDp2NytjOby8")
CONSUMER_SECRET = os.environ.get("Jdr3kQSr30fUhQ89Np7xa4P7YgkpI4CPIqazqFyE9dC4cJ8Ndt")

# Get a temporary client to retrieve an authentication URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['https://twitter.com/dritonz_']
# Now visit that URL to authorize the application and get a PIN
print(f"go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")
# Now we use that PIN_CODE to get the actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds['247469867-1AZ0jzbqcVeNk9k31nUJ7YAGuQ4gbAyLTHCYMcYn'],
                      temp_creds['lv5wioC7GgOKKPaaEWqhb3HnXuVHHbNr2BEySbsjtlMwv'])
final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN = final_step['247469867-1AZ0jzbqcVeNk9k31nUJ7YAGuQ4gbAyLTHCYMcYn']
ACCESS_TOKEN_SECRET = final_step['lv5wioC7GgOKKPaaEWqhb3HnXuVHHbNr2BEySbsjtlMwv']
# And get a new Twython instance using them.
twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)

# Search for tweets containing the phrase "data science"
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
text = status["text"]
print(f"{user}: {text}\n")