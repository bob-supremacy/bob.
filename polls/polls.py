import discord


from redbot.core import Config, checks, commands

class poll(commands.Cog):
    """Commands for Polls"""
    
    def __init__(self, bot):
        self.bot = bot