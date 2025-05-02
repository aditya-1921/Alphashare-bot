from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

# ─── Bot Configuration ─────────────────────────────────────────────────────────
BOT_TOKEN    = os.getenv("BOT_TOKEN",    "7674845797:AAFc9pErEgOsfOO4qF28kzJrGANXlICL-4g")
API_ID       = int(os.getenv("API_ID",       "27294940"))
API_HASH     = os.getenv("API_HASH",     "67dea18182fcb410bd8c4e1a336d8c9e")

# ─── Database Configuration ────────────────────────────────────────────────────
MONGO_URI    = os.getenv("MONGO_URI",    "mongodb+srv://poisondeath1921:N8pGonrmdVx1mzBB@cluster0.3bdouge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "")

# ─── Channel Configuration ─────────────────────────────────────────────────────
DB_CHANNEL_ID        = int(os.getenv("DB_CHANNEL_ID",        "-1002505082306"))
FORCE_SUB_CHANNEL    = int(os.getenv("FORCE_SUB_CHANNEL",    "-1002276280920"))
FORCE_SUB_CHANNEL_2  = int(os.getenv("FORCE_SUB_CHANNEL_2",  "0"))

CHANNEL_LINK   = os.getenv("CHANNEL_LINK",   "")
CHANNEL_LINK_2 = os.getenv("CHANNEL_LINK_2", "")

# ─── Bot Information ──────────────────────────────────────────────────────────
BOT_USERNAME = os.getenv("BOT_USERNAME", "@replica_file_bot")
BOT_NAME     = os.getenv("BOT_NAME",     "Replica file bot")
BOT_VERSION  = "1.6"

# ─── Privacy / Auto-Delete ─────────────────────────────────────────────────────
PRIVACY_MODE      = os.getenv("PRIVACY_MODE", "off").lower() == "on"
AUTO_DELETE_TIME  = int(os.getenv("AUTO_DELETE_TIME", "30"))

# ─── Modiji API Key ───────────────────────────────────────────────────────────
MODIJI_API_KEY = os.getenv("MODIJI_API_KEY")
if not MODIJI_API_KEY:
    print("⚠️ Warning: MODIJI_API_KEY not set in environment variables")

# ─── Support Links ─────────────────────────────────────────────────────────────
DEVELOPER_LINK = os.getenv("DEVELOPER_LINK", "")
SUPPORT_LINK   = os.getenv("SUPPORT_LINK",   "")

# ─── Web-Ping (Koyeb/Render) ──────────────────────────────────────────────────
WEB_SERVER = os.getenv("WEB_SERVER", "True").lower() == "true"
PING_URL   = os.getenv("PING_URL",   "")
PING_TIME  = int(os.getenv("PING_TIME", "0"))

# ─── Admin IDs ─────────────────────────────────────────────────────────────────
# comma-separated list in ENV, e.g. 5478765030,7038050465
ADMIN_IDS: List[int] = [
    int(x.strip())
    for x in os.getenv("ADMIN_IDS", "5478765030,7038050465").split(",")
    if x.strip().isdigit()
]

# ─── File limits & types ──────────────────────────────────────────────────────
MAX_FILE_SIZE = 2_000 * 1024 * 1024  # 2 GB

SUPPORTED_TYPES = [
    "document", "video", "audio", "photo", "voice",
    "video_note", "animation"
]

SUPPORTED_EXTENSIONS = [
    # Documents
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    # Code & data
    "py", "js", "html", "css", "json", "xml", "yaml", "yml", "csv", "md",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2",
    # Media
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov", "webm", "3gp", "m4v", "ogg", "opus",
    # Images
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    # Apps & executables
    "apk", "exe", "msi", "deb", "rpm",
    # Subtitles/logs
    "srt", "sub", "log", "text"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-7z-compressed",
    "video/mp4",
    "audio/mpeg",
    "audio/mp4",
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/vnd.android.package-archive",
    "application/x-executable",
]

# ─── Messages & Buttons ───────────────────────────────────────────────────────
class Messages:
    START_TEXT = """
🎉 Welcome to {bot_name}! 🎉

Hello {user_mention}! I'm your secure file sharing assistant.

🔐 Key Features:
• Secure File Sharing
• Unique Download Links
• Multiple File Types Support
• Real-time Tracking
• Force Subscribe

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
