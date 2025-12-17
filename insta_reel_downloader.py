import yt_dlp
import os
import sys

# ========= COLORS =========
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ========= BANNER =========
BANNER = f"""
{CYAN}{BOLD}========================================
   Instagram Reel Downloader
   Termux • Progress Bar • Gallery Save
========================================{RESET}
"""

# ========= PROGRESS BAR =========
def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "")
        eta = d.get("_eta_str", "")
        sys.stdout.write(
            f"\r{YELLOW}⬇ Downloading: {percent} | {speed} | ETA {eta}{RESET}"
        )
        sys.stdout.flush()

    elif d["status"] == "finished":
        print(f"\n{GREEN}✔ Download finished, processing file...{RESET}")

# ========= DOWNLOAD FUNCTION =========
def download_reel(url):
    save_folder = "/storage/emulated/0/Download/reels"
    os.makedirs(save_folder, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{save_folder}/%(title)s.%(ext)s",
        "format": "mp4",
        "progress_hooks": [progress_hook],
        "quiet": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        print(f"{GREEN}✅ Saved to Gallery:{RESET}")
        print(f"{BOLD}{file_path}{RESET}\n")

    except Exception as e:
        print(f"{RED}❌ Error:{RESET} {e}\n")

# ========= MAIN =========
def main():
    os.system("clear")
    print(BANNER)

    print(f"{CYAN}Paste Instagram Reel URLs (one per line){RESET}")
    print(f"{CYAN}Type 'done' and press Enter to start download{RESET}\n")

    urls = []
    while True:
        link = input("> ").strip()
        if link.lower() == "done":
            break
        if link:
            urls.append(link)

    if not urls:
        print(f"{RED}❌ No URLs provided{RESET}")
        return

    print(f"\n{GREEN}🚀 Starting downloads ({len(urls)} reels)...{RESET}\n")

    for idx, url in enumerate(urls, start=1):
        print(f"{BOLD}{CYAN}[{idx}/{len(urls)}]{RESET} Processing reel...")
        download_reel(url)

    print(f"{GREEN}{BOLD}🎉 All downloads completed!{RESET}")
    print(f"{CYAN}Check Gallery → Download → reels{RESET}")

# ========= RUN =========
if __name__ == "__main__":
    main()
