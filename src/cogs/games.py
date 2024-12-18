import discord
import random

from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        dice_roll = random.randint(1, 6)
        response_embed = discord.Embed(
            title="Dice roll 🎲",
            description=f"You rolled a {dice_roll}"
        )
        response_embed.set_footer("Created by weeaboo")
        # try:
        await ctx.send(embed=response_embed)
        # except Exception as e:
        #     print(e)


async def setup(bot):
    await bot.add_cog(Games(bot))
