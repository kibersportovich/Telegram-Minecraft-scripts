from telethon import TelegramClient
import random
import sys
from config import configure

list = configure.init_ini()
api_id = list[0]
api_hash = list[1]
client = TelegramClient('telegram', api_id, api_hash)

async def script_manual():
    async with client.conversation("@BotFather") as conv:
        await conv.send_message("/newbot")
        response_text = (await conv.get_response()).raw_text
        if response_text.split(',')[0] != "Alright":
            print(response_text)
            return
        await conv.send_message(input("your bot name: "))
        while True:
            response_text = (await conv.get_response()).raw_text
            if response_text.split('.')[0] == "Good":
                break
            print(response_text, end='\n')
            await conv.send_message(input("your bot name: "))
        mess = "let\'s choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.\n"
        bot = input(mess)
        await conv.send_message(bot)
        while True:
            response_text = (await conv.get_response()).raw_text
            if response_text.split(' ')[0] == "Done!":
                break
            print(response_text, end='\n')
            bot = input(mess)
            await conv.send_message(bot)
        if bot[0] != '@':
            bot = f"@{bot}"
        await conv.send_message("/token")
        await conv.get_response()
        await conv.send_message(bot)
        token = (await conv.get_response()).raw_text
        print(token)
        await conv.send_message("/setprivacy")
        await conv.send_message(bot)
        await conv.send_message("Disable")
        await client.send_message(bot, "hi")
        print(done)

async def script_auto():
    async with client.conversation("@BotFather") as conv:
        await conv.send_message("/newbot")
        response_text = (await conv.get_response()).raw_text
        if response_text.split(',')[0] != "Alright":
            print(response_text)
            return
        await conv.send_message("Tg_mine_bot")
        await conv.get_response()
        bot = random_username()
        await conv.send_message(bot)
        while True:
            response_text = (await conv.get_response()).raw_text
            if response_text.split(' ')[0] == "Done!":
                break
            bot = random_username()
            await conv.send_message(bot)
        await conv.send_message("/token")
        await conv.get_response()
        await conv.send_message(bot)
        token = (await conv.get_response()).raw_text
        print(f"your bot\'s username is {bot}\n\n")
        print(token)
        await conv.send_message("/setprivacy")
        await conv.send_message(bot)
        await conv.send_message("Disable")
        await client.send_message(bot, "hi")
        print(done)


def random_username():
    first_string = "@Tg_mine_"
    second_string = str()
    chars_tuple = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o",
     "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m")
    i = 0
    while i < 6:
        second_string = second_string + chars_tuple[random.randint(0, 35)]
        i = i + 1
    return first_string + second_string + "_bot"

done = '''
  _____   ____  _   _ ______ _ 
 |  __ \ / __ \| \ | |  ____| |
 | |  | | |  | |  \| | |__  | |
 | |  | | |  | | . ` |  __| | |
 | |__| | |__| | |\  | |____|_|
 |_____/ \____/|_| \_|______(_)
       '''


with client as cl:
    if len(sys.argv) == 1:
        cl.loop.run_until_complete(script_auto())
    elif sys.argv[1] == "--manual" or sys.argv[1] == "-m":
        cl.loop.run_until_complete(script_manual())
    else:
        cl.loop.run_until_complete(script_auto())
