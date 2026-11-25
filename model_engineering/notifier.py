import os, requests

def send_telegram_alert(tag, msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print(f"[{tag}] {msg} (Telegram skipped - not configured yet)")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": f"[{tag}] {msg}"},
            timeout=15
        )
    except Exception as e:
        print(f"Telegram warning: {e}")
