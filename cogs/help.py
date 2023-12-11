import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="**Pomoc 📚**", description='```!help - przedstawia to okno\n!ping - przedstawia opóźnienie\n - Informacje - \n!userinfo - informacje o danym użytkowniku```', color=0x242124)
        # embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))
