<h1 align="center">
  <b>Fireflix Cinema Bot</b>
</h1>

## Features
- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] File Store

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using @BotFather, and get the Telegram API token.
* `API_ID`: Get this value from my.telegram.org
* `API_HASH`: Get this value from my.telegram.org
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: mongoDB URI. Get this value from mongoDB.
* `DATABASE_NAME`: Name of the database in mongoDB.
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.

### Optional Variables
* `PICS`: Telegraph links of images to show in start message.
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made. Separate multiple IDs by space.
* Check `info.py` for more.

## Deploy To VPS
```bash
git clone [https://github.com/BRYCE00182/EvaMaria](https://github.com/BRYCE00182/EvaMaria)
# Install Packages
pip3 install -U -r requirements.txt
# Edit info.py with variables, then run bot
python3 bot.py
