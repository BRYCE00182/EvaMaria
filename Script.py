class script(object):
    START_TXT = """Yo...Yo... Cinema Bot {} 💖
I'm a Powerful Auto-Filter Bot. You can use me as an auto-filter bot in your groups.

It's easy to use me; just add me to your group as an admin, 
and I will provide movies there seamlessly! 🤓🤪

📢 Join our channels for updates:
- <a href=https://t.me/FireflixMovies>Fireflix Movies</a>
- <a href=https://t.me/FireflixCinema>Fireflix Cinema</a>

⚠️ For more help, check the help button below.

😎 Powered by Fireflix Cinema"""

    HELP_TXT = """
    🙋🏻‍♂️ Hellooo {} 🤓

○ It's not complicated...🤓

○ Search using inline mode:
This method works in any chat. Just type `@FireflixCinemabot`, leave a space, and search for any movie you want.

○ Available Commands:
     
 /start - Check if I'm alive..
 /status - Bot status
 /info - User info 
 /id - User id
 /stats - Database status  
 /broadcast - Broadcast (owner only)

📢 Join our channels:
- <a href=https://t.me/FireflixMovies>Fireflix Movies</a>
- <a href=https://t.me/FireflixCinema>Fireflix Cinema</a>

○ Notice 📙:-

○ Don't spam me...🤒

😎 Powered by Fireflix Cinema"""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: Fireflix Cinema Bot
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝚁𝙴𝙽𝙳𝙴𝚁
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙿𝚁𝙾𝙳𝚄𝙲𝚃𝙸𝙾𝙽 ]"""

    SOURCE_TXT = """<b>NOTE:</b>
- Fireflix Cinema Bot is customized for high-speed file sharing."""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is a feature where users can set automated replies for a particular keyword, and the bot will respond whenever that keyword is found in a message.

<b>NOTE:</b>
1. The bot should have admin privileges.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete all filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both URL and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allow you to send buttons without content, so content is mandatory.
2. Supports buttons with any Telegram media type.
3. Buttons should be properly formatted in markdown.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/FireflixMovies)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure your channel does not contain prohibited or fake files.
3. Forward the last message from your channel here.
I'll add all the files from that channel to my database automatically."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect the bot to your PM for managing filters privately.
- Helps avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> to connect me to your PM.

<b>Commands and Usage:</b>
• /connect - <code>connect a particular chat to your PM</code>
• /disconnect - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are extra features available in the bot.

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info - <code>get information about a user.</code>
• /imdb - <code>get film information from IMDb.</code>
• /search - <code>search for film information.</code>"""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module works only for authorized bot admins.

<b>Commands and Usage:</b>
• /logs - <code>to get recent errors</code>
• /stats - <code>to get status of files in db</code>
• /delete - <code>to delete a specific file from db</code>
• /users - <code>to get list of users and IDs</code>
• /chats - <code>to get list of chats and IDs</code>
• /leave - <code>to leave a chat</code>
• /disable - <code>to disable a chat</code>
• /ban - <code>to ban a user</code>
• /unban - <code>to unban a user</code>
• /channel - <code>to get list of connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
