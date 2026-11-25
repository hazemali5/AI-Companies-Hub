import os, json, datetime, gspread
from google.oauth2.service_account import Credentials
from notifier import send_telegram_alert

def get_sheet_client():
    creds_raw = os.environ["GOOGLE_CREDENTIALS_JSON"]
    creds_dict = json.loads(creds_raw)
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

def run_adam():
    sheet_id = os.environ["MODEL_SHEET_ID"].strip()
    client = get_sheet_client()
    wb = client.open_by_key(sheet_id)
    ws = wb.worksheet("Social_Queue")

    records = ws.get_all_records()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # إذا كان الجدول فارغاً يضيف صف اختبار أولي ليؤكد نجاح الاتصال
    if len(records) == 0:
        ws.append_row([
            now_str,
            "منشور تعريفي تجريبي لمكتب MODEL الهندسي (تصميم، إشراف، حصر كميات).",
            "",
            "Ready_For_Review",
            "Draft",
            "TEST-001"
        ])
        send_telegram_alert("MODEL - آدم", "تم الاتصال بالجدول وإضافة مسودة اختبار أولى.")
        print("✅ Connected to Social_Queue and added initial test row.")
    else:
        print(f"✅ Connected to Social_Queue successfully. Existing rows: {len(records)}")

if __name__ == "__main__":
    run_adam()
