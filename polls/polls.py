import discord


from redbot.core import Config, checks, commands

class Polls(commands.Cog):
    """Commands for Polls"""
    
    def __init__(self, bot):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=423187441546)
        default_guild_settings = {"polls":{},"embed":True}
        self.conf.register_guild(**default_guild_settings)
        self.conf.register_global(polls=[])
        
    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return
    
    
    