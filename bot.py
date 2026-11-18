
import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ZYROX WHITELIST ONLINE: {bot.user}")

@bot.command()
async def whitelist(ctx, *, username):
    embed = discord.Embed(
        title="Minecraft Whitelist Request",
        description=f"Player: **{username}**",
        color=discord.Color.purple()
    )

    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

bot.run(TOKEN)

