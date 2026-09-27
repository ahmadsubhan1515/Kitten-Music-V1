import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "token": os.getenv("TOKEN"),
        "prefix": os.getenv("PREFIX", "$"),
        "allowed": [], 
        "dashboard_password": os.getenv("DASHBOARD_PASSWORD", "admin"),
        "dashboard_port": int(os.getenv("PORT") or os.getenv("DASHBOARD_PORT") or 5000),
        "dashboard_host": os.getenv("DASHBOARD_HOST", "0.0.0.0"),
        "lavalink_uri": os.getenv("LAVALINK_URI", "http://lavalinkv4.serenetia.com:80"),
        "lavalink_password": os.getenv("LAVALINK_PASSWORD", "https://seretia.link/discord"),
        "bot_status": os.getenv("BOT_STATUS", "MADE BY SUBHAN"),
        "bot_status_type": os.getenv("BOT_STATUS_TYPE", "listening"),
        "bot_activity_name": os.getenv("BOT_ACTIVITY_NAME", "MADE BY SUBHAN"),
        "max_queue_size": int(os.getenv("MAX_QUEUE_SIZE", 100)),
        "default_volume": int(os.getenv("DEFAULT_VOLUME", 80)),
        "auto_leave_empty": str(os.getenv("AUTO_LEAVE_EMPTY", "True")).lower() in ("true", "1", "yes"),
        "auto_leave_timeout": int(os.getenv("AUTO_LEAVE_TIMEOUT", 300)),
        "search_results_limit": int(os.getenv("SEARCH_RESULTS_LIMIT", 5))
    }
