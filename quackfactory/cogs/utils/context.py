from discord.ext import commands
import discord
import logging

log = logging.getLogger(__name__)

class QuackContext(commands.Context):
  async def add_reaction(self, emoji):
    try:
      await self.message.add_reaction(emoji)
    except discord.HTTPException as e:
       log.error(e)
