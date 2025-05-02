📢 Join @Thealphabotz for updates!
👨‍💻 Contact @adarsh2626 for support
A Open Source Repo :- github.com/utkarshdubey2008/alphashare

Use /help to see available commands!
"""
    HELP_TEXT = """
📚 Available Commands

👤 User Commands:
• /start – Start the bot
• /help – Show this menu
• /about – Bot details
• /short [url] – Shorten a link (e.g. /short example.com)
• /repo – Show GitHub repo

👑 Admin Commands:
• /upload – Upload a file (reply to a file)
• /stats – View bot stats
• /broadcast – Message all users
• /auto_del – Set auto-delete timer

🗑 Files auto-delete after the set time. Change with /auto_del.
🔗 /batch – Group multiple files into one link.
"""
    ABOUT_TEXT = """
ℹ️ About {bot_name}

Version: {version}
Developer: @seasonal_culture
Framework: Pyrogram

📢 Updates & Support: https://t.me/seasonal_culture

Features:
• Secure File Sharing
• Force Subscribe
• Admin Controls
• Real-time Stats
• Auto File-Type Detection
"""
    FILE_TEXT = """
📁 File Details

Name: {file_name}
Size: {file_size}
Type: {file_type}
Downloads: {downloads}
Uploaded: {upload_time}
By: {uploader}

🔗 Share Link:
{share_link}
"""
class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Help 📚",    "callback_data": "help"},
                {"text": "About ℹ️",   "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢",  "url": CHANNEL_LINK},
                {"text": "Developer 👨‍💻", "url": DEVELOPER_LINK}
            ]
        ]
    def help_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠",     "callback_data": "home"},
                {"text": "About ℹ️",    "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢",  "url": CHANNEL_LINK}
            ]
        ]
    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠",     "callback_data": "home"},
                {"text": "Help 📚",     "callback_data": "help"}
            ],
            [
                {"text": "Channel 📢",  "url": CHANNEL_LINK}
            ]
        ]
    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗",    "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢",  "url": CHANNEL_LINK}
            ]
        ]
class Progress:
    PROGRESS_BAR       = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT      = """
{0} {1}%

⚡️ Speed: {2}/s
💫 Done: {3}
💭 Total: {4}
⏰ Time Left: {5}
"""
