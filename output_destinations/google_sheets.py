import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetWriter:
    def __init__(self, sheet_url: str, credentials_path: str = "credentials.json"):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        client = gspread.authorize(creds)

        self.sheet = client.open_by_url(sheet_url).worksheet("Transactions")

    def write_transaction(self, data: dict):
        row = [
            data.get("date", ""),
            data.get("type", ""),
            data.get("category", ""),
            data.get("amount", ""),
            data.get("note", "")
        ]
        self.sheet.append_row(row)
if __name__ == "__main__":
    sheet_url = "https://docs.google.com/spreadsheets/d/1zplggzU2igMKks7s9zLly0kXDMrElzk92rIdj6e71_U/edit?gid=0#gid=0"
    test_data = {
        "date": "2025-07-24 14:00",
        "type": "Expense",
        "category": "Books",
        "amount": 45.50,
        "note": "Python for Beginners"
    }
    writer = GoogleSheetWriter(sheet_url)
    writer.write_transaction(test_data)
    print("✅ Written to sheet.")
