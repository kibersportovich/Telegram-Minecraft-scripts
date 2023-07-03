_To simplify Telegram-Minecraft mod configuration, you can use scripts written in python._
___
# Requirements
* **[api id and hash](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id)**
* **Python 3.6+**

# Installation
```cmd
git clone https://github.com/kibersportovich/Telegram-Minecraft-scripts
cd Telegram-Minecraft-scripts
pip3 install -r requirements.txt
```
# Usage
#### Linux/macOS

```cmd
python3 sript_name.py
```
#### Windows 

```cmd
python sript_name.py
```
___
# Scripts

#### get_chat.py
just send a "get_chat" message to telegram chat to find out its id

#### create_bot.py
The script will create and configure the bot and send its token
* if you want to configure the username and name of your bot run the script with the flag -m or --manual
  
  ```cmd
  python create_bot.py -m
  ```


