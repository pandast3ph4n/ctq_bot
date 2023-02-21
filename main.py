import random
import discord
from discord.ext import commands
from discord import app_commands
from settings import TOKEN
from settings import SERVERID

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Online")

@bot.event
async def on_message(message):
    if message.content == "Hello CTQ-BOT".lower():
        await message.channel.send("Hello fellow human.")
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Welcome To CTQ")

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Goodbye :(")

@bot.command()
async def latency(ctx):
    await ctx.reply(f"**Latency: ** {round(bot.latency * 1000)}ms")

@bot.command(aliases=['8ball', '8'])
async def eightball(ctx, *, question):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt'] # Add more responses
    await ctx.send(f"**Question: ** {question}\n **Answers:** {random.choice(responses)}")

@bot.command()
async def embed(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author
    
    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title="This is my embed", description="Very cool embed", color=discord.Colour.random())
    embed.set_author(name=f'{name}', url="https://www.youtube.com/c/CivoProHD", icon_url="https://cdn-icons-png.flaticon.com/512/455/455691.png")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name='This is 1 field', value='This is a value')
    embed.add_field(name='This is 2 field', value='This is inline true', inline=True)
    embed.add_field(name='This is 3 field', value='This is inline false', inline=False)
    embed.set_footer(text=f'{name} Made this embed')

    await ctx.send(embed=embed)

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=SERVERID))
        self.synced = True
        print("Bot is Online")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="ping", description="Pings the user", guild=discord.Object(id=SERVERID))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong")

@tree.command(name="eightball", description="Gives you a answer", guild=discord.Object(id=SERVERID))
async def self(interaction: discord.Interaction, question:str):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt'] # Add more responses
    await interaction.response.send_message(f"**Question: ** {question}\n **Answer: ** {random.choice(responses)}")

bot.run(TOKEN) 