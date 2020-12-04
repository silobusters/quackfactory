import discord
from discord.ext import commands

class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(member, before, after):

        guild = member.guild
        role =  # Rubber Duck Role
        role_id =  # Rubber Duck Role ID
        everyone = "@everyone" 
        channel_id = 756574459556659323 # Voice chat's channel ID
        message = f"Hey there! {member} needs a rubber duck!" # Message sent to rubberduck.

        if after.channel.id == channel_id:
            await after.channel.set_permissions(discord.utils.get(guild.roles, name=role), connect=True)
            await after.channel.set_permissions(discord.utils.get(guild.roles, name=everyone), connect=False)
            await after.channel.edit(user_limit=2)

            for member in guild.members:
                for role in member.roles:
                    if role.id == role_id:
                        if member.status == discord.Status.online:
                            await member.send(message)

def setup(bot):
    bot.add_cog(Session(bot))
