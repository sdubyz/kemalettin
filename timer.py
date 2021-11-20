from check_user import check_valid, check_user, check_valid_user_reaction
from datetime import datetime, timedelta

startEmoji = "<:start:911666593623334962>"
startEmojiID = 911666593623334962
pauseEmoji = "<:pause:911666600342589451>"
pauseEmojiID = 911666600342589451
stopEmoji = "<:stop:911666606965391391>"
stopEmojiID = 911666606965391391

async def pause_reaction(chn, membr):
    lab_file = check_valid_user_reaction(chn, membr)
    if (lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Mola")):
            await chn.send("Zaten Moladasınız!", delete_after = 3.0)
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
            await chn.send("Süre duraklatıldı!", delete_after=3.0)
            message = await chn.send("Çalıştığınız Süre: " + tot_time)
            await message.add_reaction(startEmoji)
            await message.add_reaction(stopEmoji)

async def cont_reaction(chn, membr):
    lab_file = check_valid_user_reaction(chn, membr)
    if(lab_file == "wrong"):
        return
    else:
        with open(lab_file) as f:
            for line in f:
                pass
        if (line.startswith("Başlangıç")):
            await chn.send("Zaten süre devam etmekte!")
            return
        else:

            last_line = line
            FMT = '%H:%M:%S'
            now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            log_file = open(lab_file, "a")
            log_file.write("Başlangıç " + now + "\n")
            log_file.close()
            await chn.send("İyi çalışmalar!", delete_after=3.0)
            diff = str(datetime.strptime(
                now[-8:], FMT) - datetime.strptime(last_line[-9:-1], FMT))
            message = await chn.send("Mola Süresi: " + diff)
            await message.add_reaction(pauseEmoji)
            await message.add_reaction(stopEmoji)


async def stop_reaction(chn, membr):
    lab_file = check_valid_user_reaction(chn, membr)
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

        diff = str(datetime.strptime(
            now[-8:], FMT) - datetime.strptime(start[-9:-1], FMT))
        str_time = datetime.strptime(
            start[-9:-1], FMT) + timedelta(hours=3)
        now_t = datetime.strptime(
            now[-8:], FMT) + timedelta(hours=3)
        await chn.send("Toplam Çalışma süresi: " + str(tot_time.time()))
        await chn.send("Başlangıç: " + str_time.strftime("%H:%M:%S") + ", Bitiş: " + now_t.strftime("%H:%M:%S"))
