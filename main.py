import os
import discord
import time
from discord.ext import commands, tasks
from keep_alive import keep_alive
from scrap import currency, daily
from discord import Color
from datetime import datetime, timedelta
from check_user import check_valid, check_user
from timer import pause_reaction, cont_reaction, stop_reaction
from dizipal import findLink

music = discord.Activity(
    type=discord.ActivityType.listening, name="Her Halini Severim")
client = commands.Bot(command_prefix="!",
                      status=discord.Status.online, activity=music )


@client.event
async def on_ready():
  
  print('{0.user} is ready to go!'.format(client))
  #if not rates.is_running():    
    #rates.start()
    #daily_update.start()
    #ch_name.start()
    #check_if_con.start()


nameFile = 'data/dolar.txt'

file1 = open(nameFile, "r")
n = float(file1.read())

green = Color.dark_green()
red = Color.red()
prev = [n]
file1.close()

startEmoji_t = "<:start:911666089115660338>"
startEmojiID_t = 911666089115660338
pauseEmoji_t = "<:pause:911666263988785203>"
pauseEmojiID_t = 911666263988785203
stopEmoji_t = "<:stop:911666095822352474>"
stopEmojiID_t = 911666095822352474

startEmoji = "<:start:911666593623334962>"
startEmojiID = 911666593623334962
pauseEmoji = "<:pause:911666600342589451>"
pauseEmojiID = 911666600342589451
stopEmoji = "<:stop:911666606965391391>"
stopEmojiID = 911666606965391391

lab_lib_ch = [909170792347107358, 901055167825346600, 845613490000494602,
              845613443851485184, 845613337236602942, 525024033381810179]
guz_id = 522825818225901578
hra_id = 462700306724290563
ir_id = 522835029596831774
lab_ids = [ir_id, guz_id, hra_id]

@tasks.loop(seconds=5)
async def rates():
  try:
      channel = client.get_channel(901924767513329695)
      channel2 = client.get_channel(902109009329389598)
      #ch_labne = client.get_channel(838136630425944066)

      dollar = float(str(currency()).replace(",", "."))
      up = '<:greenUp:902101687043514378> '
      down = '<:redDown:902101653845594142> '

      up2 = '<:greenUp:902110266278424606> '
      down2 = '<:redDown:902110295986679860> '

      diff = abs(((dollar - prev[0]) / prev[0])*100)
      if(diff <= 0.025):
          pass
      else:
          if (prev[0] <= dollar):
              pos_ratio = '```diff\nDolar: {} ₺\n+ %{}\n```'.format(
                  dollar, round(diff, 4))
              em = discord.Embed(color=green, title="")
              em.add_field(name=up*6, value=pos_ratio)

              em2 = discord.Embed(color=green, title="")
              em2.add_field(name=up2*6, value=pos_ratio)
          else:
              neg_ratio = '```diff\nDolar: {} ₺\n- %{}\n```'.format(
                  dollar, round(diff, 4))
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
          em4 = discord.Embed(title="Dolar yükseldi. (Son mesaj...)")
          # if(dollar >= 10):
          #  await ch_labne.send(embed=em3)

          await channel2.send(embed=em4)
          await channel.send(embed=em4)
          channel5 = client.get_channel(887041498288365568)
          await channel5.send("geldim geldim...")
          #print("Sent!")
  except:
    print("value error")


@tasks.loop(minutes=5)
async def daily_update():
    channel = client.get_channel(901924767513329695)
    difference = daily()
    await channel.edit(topic="Günlük aralık: " + difference)


@tasks.loop(minutes=6)
async def ch_name():
    channel = client.get_channel(901924767513329695)
    dollar_num = round(float(currency().replace(',', '.')), 2)
    dollar = str(dollar_num).replace('.', '-')
    await channel.edit(name="dolar-{}".format(dollar))


@tasks.loop(seconds=2)
async def check_if_con():
    channel1 = client.get_channel(764085102648098821)
    labne = client.get_guild(764085102648098817)
    text_ch = client.get_channel(909170792347107358)
    hra = await labne.fetch_member(462700306724290563)

    #irm = labne.get_member(522835029596831774)
    #guz = labne.get_member(522825818225901578)
    #members = [hra, irm, guz]
    #print(hra.name)
    #if hra.voice is None:
      #await text_ch.send("no")
    #else:
      #if hra.voice.channel == channel1:
        #await text_ch.send("yea")
        #check_if_con.stop()
    #print(labne.name)
    #if hra in channel.members:
    #    print("yes")
    #else:
    #    print("no")
  
@commands.command(name = "dizipal")
async def link(ctx):
  try:
    msg = await ctx.send("Hemmen arıyorum...")
    await msg.edit(content="█.......ariyorum..........")
    time.sleep(0.6)
    await msg.edit(content="███.ariyorum..........")
    time.sleep(0.6)
    await msg.edit(content="████riyorum..........")
    time.sleep(0.6)
    await msg.edit(content="██████rum...........")
    time.sleep(0.6)
    await msg.edit(content="█████████..........")
    
    nameFile = 'data/dizipal.txt'

    file1 = open(nameFile, "r")
    a = int(file1.read()[15:18])
    file1.close()
    link = findLink(a, a+1)
    if link == "0":
      link=findLink(250,350)
      # print("not found")
    if link == "0":
      link=findLink(100,250)
      await msg.edit(content="███████████...")
    if link == "0":
      link=findLink(350,400)
      await msg.edit(content="███████████...")
    if link == "0":
      # link=findLink(250,300)
      await msg.edit(content="████████████")
      await ctx.send('Yok bulamadım :/ \nŞuradan bak istersen: https://twitter.com/search?q=%23dizipal&f=live')
    else:
      await msg.edit(content="████████████")
      await ctx.send(link)
      await msg.edit(content=":)")
      file1 = open(nameFile, "w")
      file1.write(link)
      file1.close()
      chn1 = client.get_channel(887041498288365568)
      chn2 = client.get_channel(815199496044019714)
      await chn1.edit(topic=link)
      await chn2.edit(topic=link)
      await ctx.message.channel.edit(topic=link)
      return
  except Exception as e: print(e)
    #print("Exception...")
    
client.add_command(link)


deleted_messages = []


@commands.command(name="yardim")
async def guideline(ctx):
  help_message = "Komutlar:\n!help !süpür !dizipal !bombarda !oops !curr !katil !ayril"
  await ctx.send(help_message)
client.add_command(guideline)

@commands.command(name = "oops")
async def send_deleted_msg(ctx):
  if ctx.message.author.id != hra_id and ctx.message.author.id != ir_id:
    await ctx.send("Admin izni gerekiyor! ( hra :) )")
    return
  if deleted_messages:
    try:
      for msg in reversed(deleted_messages):
        msg_content = "**"+msg.author.name+"**" +" at " + "__*"+msg.created_at.strftime("%m/%d/%Y %H:%M:%S")+"*__" + " : " + "*"+msg.content+"*" + "\n"
        await ctx.send(msg_content)
    except Exception as e:
      print(e)
  else:
    print("no deleted messages")
      
client.add_command(send_deleted_msg)


@commands.command(name = "süpür")
async def delete_message(ctx, *args):
  try:
    channel = ctx.message.channel
    global deleted_messages
    if len(args) == 2:
      if args[1] == "dk":
        deleted_messages = await channel.purge(limit=200, check=None, before=None, after=datetime.now()-timedelta(minutes=int(args[0])), around=None, oldest_first=False, bulk=True)
    elif len(args) == 1:    
      deleted_messages = await channel.purge(limit=int(args[0])+1, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
  except ValueError:
    await ctx.send("'!süpür [mesaj sayısı]' veya '!süpür [dakika] dk' şeklinde gir lütfen...")
    return
  except IndexError:
    await ctx.send("Kaç mesaj sileyim???")
    return

  if deleted_messages:
    with open("data/deleted_messages.txt", "a") as deleted_msg:
      for msg in deleted_messages:
        deleted_msg.write(msg.author.name +" - " + 
                         " at " + str(msg.created_at) + ": ")
        deleted_msg.write(msg.content+"\n")

      
client.add_command(delete_message)
  
@commands.command(name="saldır")
async def attack_on_user(ctx, *args):
  try:
    ments = ctx.message.mentions
    url = "https://media.giphy.com/media/9IZKPmNdZ7juU/giphy.gif"
    url2 = "https://media.giphy.com/media/gfl7CKcgs6exW/giphy.gif"
    if ments[0] == ctx.message.author:
      em = discord.Embed(title="Akıl hastanesini arıyorum...")
      em.set_image(url=url2)
    elif ments[0].name == 'hra':
      em = discord.Embed(title="O benim sahibim laan ", description=ctx.message.author.mention)
      em.set_image(url=url)      
    else:
      em = discord.Embed(title="HRRR HAV HAV ", description=ments[0].mention)
      em.set_image(url=url)
    await ctx.send(embed=em)
    #print(ments)
  except:
    print("Exception")

client.add_command(attack_on_user)

@commands.command()
async def curr(ctx):
    dollar = currency()
    send_this = "💲: {} ₺".format(dollar)
    em = discord.Embed(color=green, title=send_this)
    await ctx.send(embed=em)

client.add_command(curr)


@commands.command()
async def say(ctx, *args):
    await ctx.send(" ".join(args))

client.add_command(say)


@commands.command()
async def bombarda(ctx, *args):
    f = discord.File("data/wenamechainsama.mp4")
    await ctx.send(file = f)

client.add_command(bombarda)



@commands.command(name="katil")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

client.add_command(join)


@commands.command(pass_context=True, name="ayril")
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.add_command(leave)




@commands.command()
async def start(ctx):
    lab_file = check_valid(ctx)
    if (lab_file == "wrong"):
        return
    else:
        log_file = open(lab_file, "w")
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        log_file.write("Başlangıç " + now + "\n")
        log_file.close()
        tot_file = check_user(lab_file)
        open(tot_file, 'w').close()
        theMessage = await ctx.send("İyi çalışmalar!")
        await theMessage.add_reaction(pauseEmoji)
        await theMessage.add_reaction(stopEmoji)
        await ctx.message.delete()


client.add_command(start)


@commands.command(name="break")
async def pause(ctx):
    lab_file = check_valid(ctx)
    if (lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Mola")):
            await ctx.send("Zaten Moladasınız!", delete_after = 3.0)
            return
        else:
            last_line = line
            now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            log_file = open(lab_file, "a")
            log_file.write("Mola başlangıç " + now + "\n")
            log_file.close()
            FMT = '%H:%M:%S'
            tot_time = str(datetime.strptime(
                now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
            tot_fi_name = check_user(lab_file)
            tot_file = open(tot_fi_name, "a")
            tot_file.write(tot_time + "\n")
            tot_file.close()
            await ctx.send("Süre duraklatıldı!", delete_after=3.0)
            msg = await ctx.send("Çalıştığınız Süre: " + tot_time)
            await msg.add_reaction(startEmoji)
            await msg.add_reaction(stopEmoji)
            await ctx.message.delete()            

client.add_command(pause)


@commands.command()
async def cont(ctx):
    lab_file = check_valid(ctx)
    if(lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Başlangıç")):
            await ctx.send("Zaten süre devam etmekte!")
            return
        else:

            last_line = line
            FMT = '%H:%M:%S'
            now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            log_file = open(lab_file, "a")
            log_file.write("Başlangıç " + now + "\n")
            log_file.close()
            await ctx.send("İyi çalışmalar!", delete_after=3.0)
            diff = str(datetime.strptime(
                now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
            msg = await ctx.send("Mola Süresi: " + diff)
            await msg.add_reaction(pauseEmoji)
            await msg.add_reaction(stopEmoji)
            await ctx.message.delete()

client.add_command(cont)


@commands.command()
async def stop(ctx):
    lab_file = check_valid(ctx)
    if(lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
            last_line = line
        tot_file = check_user(lab_file)
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        FMT = '%H:%M:%S'
        if last_line.startswith("Başlangıç"):
            tot_time = str(datetime.strptime(
                now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
            tot_fi = open(tot_file, "a")
            tot_fi.write(tot_time + "\n")
            tot_fi.close()
        f = open(lab_file, "r")
        start = f.readline()
        f.close()

        log_file = open(lab_file, "a")
        log_file.write("Bitiş " + now + "\n")
        log_file.close()
        tot_time = datetime.strptime("00:00:00", FMT)
        time_zero = datetime.strptime('00:00:00', FMT)
        with open(tot_file) as f:
            for line in f:
                t2 = datetime.strptime(line[:-1], FMT)
                tot_time = (tot_time - time_zero + t2)

        #diff = str(datetime.strptime(
            #now[-8:], FMT) - datetime.strptime(start[-9:-1], FMT))
        str_time = datetime.strptime(
            start[-9:-1], FMT) + timedelta(hours=3)
        now_t = datetime.strptime(
            now[-8:], FMT) + timedelta(hours=3)
        await ctx.send("Toplam Çalışma süresi: " + str(tot_time.time()))
        await ctx.send("Başlangıç: " + str_time.strftime("%H:%M:%S") + ", Bitiş: " + now_t.strftime("%H:%M:%S"))
        await ctx.message.delete()

client.add_command(stop)


@commands.command(name="time")
async def timer(ctx):
    lab_file = check_valid(ctx)
    if (lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Mola")):
            mola = True
        else:
            mola = False

        last_line = line
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        FMT = '%H:%M:%S'
        tot_time = str(datetime.strptime(
            now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
        if (not mola):
            await ctx.send("Çalıştığınız Süre: " + tot_time, delete_after=8.0)
        else:
            await ctx.send("Mola Süreniz: " + tot_time, delete_after=8.0)
            await ctx.message.delete()

client.add_command(timer)

@client.event
async def on_raw_reaction_add(payload):
  membr = payload.member
  reaction = payload.emoji
  if membr.id in lab_ids:
    guild = client.get_guild(payload.guild_id)
    ch_id = payload.channel_id
    channel = guild.get_channel(ch_id)
    msg = await channel.fetch_message(payload.message_id)
    if reaction.id == pauseEmojiID:
      if await pause_reaction(channel, membr):      
        await msg.clear_reactions()
      #await channel.send("reaction added")
    elif reaction.id == stopEmojiID:
      #await channel.send("reaction added")
      if await stop_reaction(channel, membr):
        await msg.clear_reactions()
    elif reaction.id == startEmojiID:
      if await cont_reaction(channel, membr):
        await msg.clear_reactions()
      #await channel.send("reaction added")      

#labne_lib = 525024033381810176


keep_alive()
client.run(os.getenv('TOKEN'))