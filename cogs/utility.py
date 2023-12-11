from discord.ext import commands
import discord
from discord import Member

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, *, member: Member = None):
        if not member: # if member is none 
            member = ctx.author # set member as the author

        pfp = member.avatar.url # get the avatar url of the member   
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at,
                              title=f"Informacje o użytkowniku - {member}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nazwa:", value=member.display_name)
        embed.add_field(name="Stworzono:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Dołączono:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Role:", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Najwyższa rola:", value=member.top_role.mention)
        embed.set_thumbnail(url=pfp)
        embed.set_footer(text=f"Zapytanie od {ctx.author}", icon_url=pfp)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))