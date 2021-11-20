

async def pause_reaction(ctx):
    lab_file = check_valid_user_reaction(chn, membr)
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
            message = await ctx.send("Çalıştığınız Süre: " + tot_time)
            await message.add_reaction(pauseEmoji)
            await message.add_reaction(stopEmoji)