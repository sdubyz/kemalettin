import os
import discord
from discord.ext import commands
from discord.ext import tasks
from keep_alive import keep_alive
from scrap import currency
from scrap2 import daily
from discord import Color
from discord import Spotify
from datetime import datetime

music = discord.Activity(type=discord.ActivityType.listening, name ="Her Halini Severim", start=datetime(2021, 5, 30, 12, 12, 12, 342380))
#music = Spotify(title='Her Halini Severim', artist='Feyyaz Yiğit')
client = commands.Bot(command_prefix="!", status=discord.Status.online, activity=music)

@client.event
async def on_ready():
    print('{0.user} is ready to go!'.format(client))
    rates.start()
    daily_update.start()
    ch_name.start()

nameFile = 'dolar.txt'

file1 = open(nameFile, "r")
n = ''
n = float(file1.read())

green = Color.dark_green()
red = Color.red()
prev = [n]
file1.close()

@tasks.loop(seconds=20)
async def rates():
    channel = client.get_channel(901924767513329695)
    channel2 = client.get_channel(902109009329389598)
    ch_labne = client.get_channel(838136630425944066)

    dollar = float(str(currency()).replace(",","."))
    up = '<:greenUp:902101687043514378> '
    down = '<:redDown:902101653845594142> '

    up2 = '<:greenUp:902110266278424606> '
    down2 = '<:redDown:902110295986679860> '

    diff = abs(((dollar - prev[0]) / prev[0] )*100)
    if(diff <= 0.025):
      pass
    else:
      if (prev[0] <= dollar):
        pos_ratio = '```diff\nDolar: {} ₺\n+ %{}\n```'.format(dollar, round(diff,4))
        em = discord.Embed(color=green, title ="")
        em.add_field(name=up*6, value=pos_ratio)

        em2 = discord.Embed(color=green, title="")
        em2.add_field(name=up2*6 ,value=pos_ratio)
      else:
        neg_ratio = '```diff\nDolar: {} ₺\n- %{}\n```'.format(dollar, round(diff,4))
        em = discord.Embed(color=red, title="")
        em.add_field(name=down*6, value=neg_ratio)

        em2 = discord.Embed(color=red, title="")
        em2.add_field(name=down2*6, value=neg_ratio)

      prev.pop(0)
      prev.append(dollar)
      file1 = open(nameFile, "w")
      file1.write(str(dollar))
      file1.close()
      em3 = discord.Embed(color=red, title="")
      em3.add_field(name="DOLAR 10!!!", value="2023'e hazırız")
      rte_gif = "https://media.giphy.com/media/ELFInaH0V34jNkBdTb/giphy.gif"
      em3.set_image(url=rte_gif)
      
      #if(dollar >= 10):
      #  await ch_labne.send(embed=em3)

      await channel2.send(embed=em2)
      await channel.send(embed=em)
      print("Sent!")


@tasks.loop(minutes=5)
async def daily_update():
  channel = client.get_channel(901924767513329695)
  difference = daily()
  await channel.edit(topic = "Günlük aralık: " + difference)


@tasks.loop(minutes=6)
async def ch_name():
    channel = client.get_channel(901924767513329695)
    dollar_num = round(float(currency().replace(',','.')), 2)
    dollar = str(dollar_num).replace('.','-')
    await channel.edit(name="dolar-{}".format(dollar))

@commands.command()
async def curr(ctx):
    dollar = currency()
    send_this = "💲: {} ₺".format(dollar)
    em = discord.Embed(color = green, title = send_this)
    await ctx.send(embed=em)

client.add_command(curr)

@commands.command()
async def say(ctx, *args):
    await ctx.send(" ".join(args))

client.add_command(say)


@commands.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

client.add_command(join)


@commands.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.add_command(leave)

@commands.command()
async def curr(ctx):
    dollar = currency()
    send_this = "💲: {} ₺".format(dollar)
    em = discord.Embed(color = green, title = send_this)
    await ctx.send(embed=em)

client.add_command(curr)


my_secret = os.environ['TOKEN']
keep_alive()
client.run(os.getenv('TOKEN'))
