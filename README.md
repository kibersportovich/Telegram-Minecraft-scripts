_To simplify Telegram-Minecraft mod configuration, you can use scripts written in python._

# Download scripts
```cmd
git clone https://github.com/kibersportovich/Telegram-Minecraft-scripts
```
___
# get_chat.py
just send a "get_chat" message to telegram chat to find out its id

#### Linux/macOS

```cmd
pip3 install -r requirements.txt
python3 get_chat.py
```
#### Windows 

```cmd
pip3 install -r requirements.txt
python get_chat.py
```

# create_bot.py
The script will create and configure the bot and send its token
* if you want to configure the username and name of your bot run the script with the flag -m or --manual
  
  ```cmd
  python create_bot.py -m
  ```

#### Linux/macOS
```cmd
pip3 install -r requirements.txt
python3 create_bot.py
```
#### Windows 

```cmd
pip3 install -r requirements.txt
python create_bot.py
```
