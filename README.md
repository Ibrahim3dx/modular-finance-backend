# Modular Finance Backend 💸

A plug-and-play backend for handling financial transactions from any input (Telegram, Web, CLI) and saving to Google Sheets.

## 🔧 Setup

1. **Create a Google Cloud Project**
2. Enable the Google Sheets API
3. Create a Service Account and download `credentials.json`
4. Share your Google Sheet with the service account
5. Set your `sheet_url` in `output_destinations/google_sheets.py`

## 🧪 Test

Run this:

```bash
python output_destinations/google_sheets.py
