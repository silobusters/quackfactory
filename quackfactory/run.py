import discord
import config
import coloredlogs, logging
import contextlib

from logging.handlers import RotatingFileHandler
from discord.ext import commands
from bot import QuackFactory

@contextlib.contextmanager
def set_logging():
  try:
    logging.getLogger('discord').setLevel(logging.INFO)
    logging.getLogger('discord.http').setLevel(logging.WARNING)
    logging.getLogger('discord.state').setLevel(logging.DEBUG)

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
  
    date_format = '%Y-%m-%d %H:%M:%S'
    handler = RotatingFileHandler(filename=config.LOG_FILENAME, encoding='utf-8', mode='a')
    fmt = logging.Formatter('[{asctime}] [{levelname}] {name}: {message}', date_format, style='{')

    handler.setFormatter(fmt)
    log.addHandler(handler)

    yield 
  finally:
    for handler in log.handlers[:]:
      handler.close()
      log.removeHandler(handler)

def start_bot():
  log = logging.getLogger()
  try:
    bot = QuackFactory()
    bot.run()
  except Exception as e:
    log.error(e)

def main():
	with set_logging():
		start_bot()

if __name__ == '__main__':
	main()
