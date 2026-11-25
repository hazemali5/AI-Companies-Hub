import os, requests
def send_telegram_alert(tag, msg):
    t, c = os.getenv('TELEGRAM_BOT_TOKEN'), os.getenv('TELEGRAM_CHAT_ID')
    if t and c: requests.post(f'https://api.telegram.org/bot{t}/sendMessage', json={'chat_id': c, 'text': f'[{tag}] {msg}'})
