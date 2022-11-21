from dotenv import load_dotenv
from tarkovmarket import *
import discord
import os

load_dotenv()
DISC_TOKEN = os.getenv("DISCORD_TOKEN")
TK_TOKEN = os.getenv("TARKMARK_TOKEN")

market = TarkovMarket(TK_TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    text = message.content

    if text.startswith('!tip help'):
        channel = "Item names must be in channel named \"TarkItemPrice\"\n"
        commands = "Example: !psu"
        await message.channel.send(channel + commands)
        return

    elif message.channel.name == "tarkitemprice":
        if not message.author.bot:
            item = market.get_item_by_name(text.replace("!", ""))
            image = None
            if "Weapon" in item.tags:
                image = item.img_big
            else:
                image = item.img
            name = item.name
            fleaprice = item.price
            trader = item.trader_name
            traderprice = item.trader_price
            tradercur = item.trader_price_currency
            await message.channel.send(f"{image}")
            await message.channel.send(f"```\n{name} \n"
                                       f"  Flea market price : ₽{fleaprice}\n"
                                       f"  Trader price      : {tradercur}{traderprice} from {trader}```\n")
            return

client.run(DISC_TOKEN)
