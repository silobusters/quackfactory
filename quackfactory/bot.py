from discord.ext import commands
import discord
import config
import logging
from cogs.utils import context

log = logging.getLogger(__name__)

cog_commands = (
  'cogs.reactions'  
)

class QuackFactory(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix='planty ', intents=config.get_intents())  
    
    # This will have to change to cog_commands instead of a hard coded string
    self.load_extension('cogs.reactions')

  async def on_ready(self):
    log.info(f'Quack logged in: {self.user} (ID: {self.user.id})')

  async def process_commands(self, message):
    ctx = await self.get_context(message, cls=context.QuackContext)
    if ctx.valid:
      await self.invoke(ctx)

  async def on_message(self, message):
    if message.author.bot:
      return

    await self.process_commands(message)
  
  def run(self):
    try:
      super().run(config.TOKEN, reconnect=True)
    finally:
      log.info(f'Quack logged off.')
