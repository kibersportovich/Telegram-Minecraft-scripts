import configparser
import os

ini_path = os.path.join('config', 'telegram.INI')
config = configparser.ConfigParser()
config.read(ini_path)

def set_properties():
    if not config.has_section('telegram'):
        config.add_section('telegram')
    telegram_id = int(input("введи telegram_id: "))
    config.set('telegram', 'telegram_id', str(telegram_id))
    telegram_hash = input("введи telegram hash: ")
    config.set('telegram', 'telegram_hash', telegram_hash)
    with open(ini_path, 'w') as configfile:
        config.write(configfile)
    return [telegram_id, telegram_hash]

def init_ini():
    if 'telegram.INI' not in os.listdir('config'):
        with open(ini_path, 'x'):
            pass
        return set_properties()
    try:
        telegram_id = config.getint('telegram', 'telegram_id')
        telegram_hash = config.get('telegram', 'telegram_hash')
    except:
        return set_properties()
    return [telegram_id, telegram_hash]


