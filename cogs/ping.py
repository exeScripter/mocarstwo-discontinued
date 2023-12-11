import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(title="Pong! 🏓", description=f'{round(self.bot.latency * 1000)}ms', color=0x00ff00)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ping(bot))
