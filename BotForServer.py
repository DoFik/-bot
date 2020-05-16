import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='?')
@client.event
async def on_ready():
    print('Bot on!')
@client.event
async def on_message(mes):
    chal_oc = ''
    if mes.author.bot == False:
        chal = mes.guild.get_channel(710886653073555517)
        chal_oc = mes.guild.get_channel(channel_id = 703548679918714911)
        await chal.send(embed = discord.Embed(description=f"Юзер {mes.author} написал `{mes.content}` в канале {mes.channel}"))
        await client.process_commands(mes)
    while True:
            m = 0
            of = 0
            members = mes.guild.members
            for i in range(len(members)):
                if members[i].status == discord.Status.online:
                    m += 1
                elif members[i].status == discord.Status.idle:
                    m += 1
                elif members[i].status == discord.Status.dnd:
                    m += 1
                elif members[i].status == discord.Status.invisible:
                    m += 1
                else:
                    of += 1
            await asyncio.sleep(10)
            game = discord.Game(f"?help | Людей online - {m}\n Людей offline - {of}")
            await client.change_presence(activity=game)
    while True:
        await asyncio.sleep(600)
        await chal_oc.purge(limit=25)
    
@client.command()
async def пинг(ctx):
    await ctx.send('Понг!')
@client.command()
async def youtube(ctx):
    em = discord.Embed(description = "Ютуб канал Do_Fik'а\n[Do Fik](https://www.youtube.com/channel/UCmYGNJrCHRe-3DKTiVjH4pA)")
    await ctx.send(embed = em)
@client.command()
async def twitch(ctx):
    await ctx.send("Твич канал Do_Fik'а\nhttps://twitch.tv/do_fik")
@client.event
async def on_message_delete(message):    
    aut = message.author
    con = message.content
    chal = message.channel
    em = discord.Embed(description = f'Юзер {aut} удалил сообщение `{con}` в канале {chal}')
    chale = message.guild.get_channel(710886653073555517)
    await chale.send(embed = em)
@client.event
async def on_message_edit(before,after):
    chale = before.guild.get_channel(710886653073555517)
    if before.channel.id != 710886653073555517:
        eme = discord.Embed(description = f"{before.author} изменил сообщение `{before.content}` на `{after.content}`")
        await chale.send(embed = eme)
    else:
        pass
@client.command()
async def ls(ctx,arg : discord.Member = None,*,mese):
    if arg == None:
        mem = ctx.guild.get_member(int(arg))
        await mem.send(mese)
    else:
        await arg.send(mese)
@client.command()
async def cd(ctx,arg : discord.TextChannel):
    await arg.purge()
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
