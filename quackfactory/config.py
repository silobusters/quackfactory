from discord import Intents

def get_intents() -> Intents:
  intents = Intents.default()
  intents.reactions = True
  intents.members = True
  intents.presences = True
  return intents

LOG_FILENAME = 'quack.log'
TOKEN = ''
