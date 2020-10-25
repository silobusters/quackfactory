from discord.ext import commands
import discord
import logging

log = logging.getLogger(__name__)

class Reactions(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.message_id == 0: # ID of the message that will handle the rubber duck reactions
      if payload.emoji.name == 'rubberduck':
        if payload.event_type == 'REACTION_ADD':
          guild = discord.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
          role = discord.utils.get(guild.roles, name='Rubber Duck')

          if role is not None:
            if not role in payload.member.roles:
              await payload.member.add_roles(role)
              log.debug(f'Added the role to the user {payload.member.name}')
          else:
             log.error(f'Role Rubber Duck does not exist.')

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    if payload.message_id == 0: # ID of the message that will handle the rubber duck reactions
      if payload.emoji.name == 'rubberduck':
        if payload.event_type == 'REACTION_REMOVE':
          guild = discord.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
          member = guild.get_member(payload.user_id)
          role = discord.utils.get(guild.roles, name='Rubber Duck')

          if member is not None:
            await member.remove_roles(role)
            log.debug(f'Removed the role {role.name} from user {member.name}')
          else:
            log.debug(f'User with the ID {payload.user_id} has not been found.') 
  
  @commands.command(name='give')
  async def add_rubber_duck(self, ctx, input_role: str):
    role = discord.utils.get(ctx.guild.roles, name=input_role)
    if role in ctx.author.roles:
      await ctx.add_reaction('\N{CROSS MARK}')
      await ctx.send('You already have the role.')
    else:
      await ctx.add_reaction('\N{WHITE HEAVY CHECK MARK}')
      await ctx.author.add_roles(role)
      await ctx.send('Role has been added')

  @commands.command(name='remove')
  async def remove_role(self, ctx, input_role: str):
    role = discord.utils.get(ctx.guild.roles, name=input_role)

    if not role in ctx.author.roles:
      await ctx.add_reaction('\N{CROSS MARK}')
      await ctx.send('You do not have this role.')
    else:
      await ctx.add_reaction('\N{WHITE HEAVY CHECK MARK}')
      await ctx.author.remove_role(role)
      await ctx.send(f'Role {input_role} has been removed.') 

def setup(bot):
  bot.add_cog(Reactions(bot))
