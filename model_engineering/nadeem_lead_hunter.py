import os, json, gspread
from google.oauth2.service_account import Credentials
from notifier import send_telegram_alert

def run_nadeem():
    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])
    sheet_id = os.environ["MODEL_SHEET_ID"].strip()
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    wb = client.open_by_key(sheet_id)
    ws = wb.worksheet("Opportunities")

    rows = ws.get_all_values()
    print(f"✅ Connected to Opportunities tab. Total rows (including header): {len(rows)}")
    send_telegram_alert("MODEL - م. نديم", f"تم فحص تبويب الفرص بنجاح ({max(0, len(rows)-1)} فرصة مسجلة).")

if __name__ == "__main__":
    run_nadeem()
