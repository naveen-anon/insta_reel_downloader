import yt_dlp
import os

# ========== COLORS ==========
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ========== BANNER ==========
BANNER = f"""
{CYAN}{BOLD}====================================
   Instagram Reel Downloader
   Works on Termux (Android)
===================================={RESET}
"""

def download_reel(url):
    save_folder = "reels"
    os.makedirs(save_folder, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{save_folder}/%(title)s.%(ext)s",
        "format": "mp4",
        "quiet": False,
    }

    try:
        print(f"\n{YELLOW}⏳ Downloading reel...{RESET}\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        print(f"\n{GREEN}✅ Download Successful!{RESET}")
        print(f"{CYAN}📂 Saved at:{RESET}")
        print(f"{BOLD}{os.path.abspath(file_path)}{RESET}")

    except Exception as e:
        print(f"\n{RED}❌ Error occurred:{RESET}")
        print(f"{RED}{e}{RESET}")


def main():
    os.system("clear")  # Termux screen clear
    print(BANNER)

    reel_url = input(f"{CYAN}Enter Instagram Reel URL: {RESET}").strip()

    if not reel_url:
        print(f"{RED}❌ No URL provided{RESET}")
        return

    download_reel(reel_url)


if __name__ == "__main__":
    main()
