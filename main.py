import os
import discord
from discord.ext import commands
from discord.ext import tasks
from keep_alive import keep_alive
from scrap import currency
from scrap2 import daily
from discord import Color
from datetime import datetime, timedelta
from check_user import check_valid, check_user

music = discord.Activity(
    type=discord.ActivityType.listening, name="Her Halini Severim")
client = commands.Bot(command_prefix="!",
                      status=discord.Status.online, activity=music)


@client.event
async def on_ready():
    print('{0.user} is ready to go!'.format(client))
    rates.start()
    daily_update.start()
    ch_name.start()

nameFile = 'dolar.txt'

file1 = open(nameFile, "r")
n = float(file1.read())

green = Color.dark_green()
red = Color.red()
prev = [n]
file1.close()


@tasks.loop(seconds=20)
async def rates():
    channel = client.get_channel(901924767513329695)
    channel2 = client.get_channel(902109009329389598)
    # ch_labne = client.get_channel(838136630425944066)

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

        # if(dollar >= 10):
        #  await ch_labne.send(embed=em3)

        await channel2.send(embed=em2)
        await channel.send(embed=em)
        print("Sent!")


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
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

client.add_command(join)


@commands.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.add_command(leave)


lab_lib_ch = [909170792347107358, 901055167825346600, 845613490000494602,
              845613443851485184, 845613337236602942, 525024033381810179]
ir_id = 522835029596831774
guz_id = 522825818225901578
hra_id = 462700306724290563


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
        await ctx.send("İyi çalışmalar!")


client.add_command(start)


@commands.command()
async def pause(ctx):
    lab_file = check_valid(ctx)
    if (lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Mola")):
            await ctx.send("Zaten Moladasınız!")
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
            await ctx.send("Süre duraklatıldı!")
            await ctx.send("Çalıştığınız Süre: " + tot_time)

client.add_command(pause)


@commands.command()
async def cont(ctx):
    lab_file = check_valid(ctx)
    if(lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                if (line.startswith("Mola")):
                    last_line = line
                else:
                    continue
        # print(last_line[-9:])
        f.close()
        FMT = '%H:%M:%S'
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        log_file = open(lab_file, "a")
        log_file.write("Başlangıç " + now + "\n")
        log_file.close()
        await ctx.send("İyi çalışmalar!")
        diff = str(datetime.strptime(
            now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
        await ctx.send("Mola Süresi: " + diff)

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
        f.close()

        f = open(lab_file, "r")
        start = f.readline()
        f.close()
        FMT = '%H:%M:%S'
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        log_file = open(lab_file, "a")
        log_file.write("Bitiş " + now + "\n")
        log_file.close()
        tot_file = check_user(lab_file)
        tot_time = datetime.strptime("00:00:00", FMT)
        with open(tot_file):
            for line in f:
                tot_time += datetime.strptime(line, FMT)

        diff = str(datetime.strptime(
            now[-8:], FMT) - datetime.strptime(start[-9:-1], FMT))
        str_time = datetime.strptime(
            start[-9:-1], FMT) + timedelta(hours=3)
        now_t = datetime.strptime(
            now[-8:], FMT) + timedelta(hours=3)
        await ctx.send("Toplam Çalışma süresi: " + tot_time)
        await ctx.send("Başlangıç: " + str_time.strftime("%H:%M:%S") + ", Bitiş: " + now_t.strftime("%H:%M:%S"))

client.add_command(stop)


@commands.command()
async def time(ctx):
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
            await ctx.send("Çalıştığınız Süre: " + tot_time)
        else:
            await ctx.send("Mola Süreniz: " + tot_time)

client.add_command(time)

my_secret = os.environ['TOKEN']
keep_alive()
client.run(os.getenv('TOKEN'))
