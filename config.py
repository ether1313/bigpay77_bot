import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8287500389:AAG_6DWzvN_KrGXISzC2u7m9BbWsA2j8rmk")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/bigpay77au")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://bigpay77.net/RFBIGPAY77BOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://bigpay77.net/RFBIGPAY77BOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Bigpay77 Promo Bot"
BOT_DESCRIPTION = "Bigpay77 Marketing Assistant - Provides latest promotions and event information"
