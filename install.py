import sys
import subprocess
import os

# ✅ Check if running in Google Colab
try:
    from google.colab import output
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

# ✅ Auto-Install Required Modules
def install_modules():
    modules = ["yt-dlp", "pyrogram", "tgcrypto", "ffmpeg-python"]
    
    if IN_COLAB:
        print("🔄 Running in Google Colab, Installing Required Modules...")
        subprocess.run(["apt-get", "update"], check=True)
        subprocess.run(["apt-get", "install", "-y", "ffmpeg"], check=True)  # Install FFmpeg
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"⚡ Installing {module}...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--no-cache-dir", module], check=True)
    
    # ✅ Google Colab में sys.path को अपडेट करें
    if IN_COLAB:
        sys.path.append("/usr/local/lib/python3.10/dist-packages/")

install_modules()

# ✅ अब yt-dlp और बाकी पैकेज लोड होंगे
import yt_dlp
import ffmpeg
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

print("✅ All modules installed and loaded successfully!")
