import discord

lab_lib_ch = [909170792347107358, 901055167825346600, 845613490000494602,
              845613443851485184, 845613337236602942, 525024033381810179]
ir_id = 522835029596831774
guz_id = 522825818225901578
hra_id = 462700306724290563


startEmoji = "<:start:911666089115660338>"
startEmojiID = 911666089115660338
pauseEmoji = "<:pause:911666263988785203>"
pauseEmojiID = 911666263988785203
stopEmoji = "<:stop:911666095822352474>"
stopEmojiID = 911666095822352474

def check_valid(ctx):
    if ctx.message.channel.id in lab_lib_ch:
        if ctx.message.author.id == ir_id:
            return "irem.txt"
        elif ctx.message.author.id == guz_id:
            return "guzi.txt"
        elif ctx.message.author.id == hra_id:
            return "hra.txt"
        else:
            return "unknown_user.txt"
    else:
        return "wrong"

def check_valid_user_reaction(chn, usr):
    if chn.id in lab_lib_ch:
        if usr.id == ir_id:
            return "irem.txt"
        elif usr.id == guz_id:
            return "guzi.txt"
        elif usr.id == hra_id:
            return "hra.txt"
        else:
            return "unknown_user.txt"
    else:
        return "wrong"


def check_user(txt_file):
    if txt_file == "irem.txt":
        return "irem_tot.txt"
    elif txt_file == "guzi.txt":
        return "guzi_tot.txt"
    elif txt_file == "hra.txt":
        return "hra_tot.txt"
