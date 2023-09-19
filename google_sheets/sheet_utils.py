import gspread
import re

credentials = {
    "type": "service_account",
    "project_id": "cellular-cortex-277310",
    "private_key_id": "c739231d112c3585343b21e9f839dc8af58148ad",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQClRFVs9YbszNCo\nSWPYOTrujJoM1X54NJJA7IPWn6b2oRpiR4BaosFZeLNto8I0tBTbCYHARZDE3Mw5\nO7asVpt8XvrmvjopSzdCqdV375yuGk88IhewSiqSTuLrZRV3ua8ztXlo3lxI+X6V\nSNbtSHxgXg7KqIGVjSUsfv0BAADqSFi/jVqFKlTeUAliGqToCR5zhRXRPYLPH3Rr\n4QAgpp9wcdsy3gJpBFFSvub5nfgXYJPWPsqmW3UNBE/GORxb41lIzzyEqMVrImBp\nWKXl+uz4KH3aKg67OBHgqOj5QEzP5kNhaxgCM+KV70HPVFwbJYNEv8KNNN6im9oc\nX+kdM3L1AgMBAAECggEAEQU8HQgeWLXxSVuhlkuyl43QccDtEPktFNWm8Ewp+F14\nJ6YAgJUhf5LwO7rxTdc8DKDqhYBEnBm3SK+vLQmQYtsvUONHfyg5bTqrevoo8z9P\naLyEHwpMXxwTv7V95AIyGou2kMfRzkwvrrU9OVvNP2mAcXuwONQ7/1ymttsmvPoD\nEYjlGd+g16DQe7QnZueOslNX1A4LBPhzsCWh0g2F8jQ0rdv3f8VoV2kNFPzvdmuf\nRdb7Z5NEKp7MyKkbrtKfkuoKB0hu7cbuBnCgLsGKUnkDCkkLA6Fwczeopxo2/hw+\n0BGynXalNKTnITOmA8Q0/juIaIBuD+jWZF4aH0NQAQKBgQDUwvYZ0jSrNnyiOfLa\nGp4C1mGQ+zWrZUwr6jo4lECtf/kQcT1NCWauP3dp1W0l2QXLxbebvfaCbe/aoBzq\nnCJPBGLa4Gg8Ao0V2FINkUi35ofPccghwNQC8SG/1SRie5tZbNk0lbLXp2Z+QE5b\nsQsFTRs175Y2JOCXCHm3FIA69QKBgQDG2m/47X5xy7gqeF6YX7rjGrz93tqbzs/J\nq0Qgyai3+cI1IAIFIOxQ3yZ433aS9wbDFBCSII9wDlhaixl4KpZzNvRR9v69x7a7\noxL5YEGEn7cKLxtixzUxv5Ad53wn6cebhphZJgXJb9RFBkLGMnQgdNNZFpSkfuk9\nOpsPG1NYAQKBgBo5hbgdDtzjtG0Sk3qKuVtELXZ/YFgl/kOTdWWv8GDyWzLJonKy\na/OiYweqhO+bVnmNf1o1CgN9pYjfH3FTmW7/7WdpLa/n6Jf+t+5wL/Rq9+Z78d0n\nNXq/WheZIAj7j2RwZD11DjxCqAF7z6zBn8ghfu8g/vThisVTCB2m6z9ZAoGABFFT\n4xTNDQ1+VzW74BUcCrhW6DBBkOaBroBQf2HBjxUWOW8TfCcF2o+t1ywK+A/zDqNN\n5M5eLvGwy25/xBMwpxnHXkw9pcNDXXmh/NYxNf79y3PQZWmr5wOgznVrRbaWxfK7\nNhxUPdZ2xnTnWERaLyY6PJH38kZrLBAss7xFKAECgYAXsFmKDjnr/Qk1AKI4nlON\nUs4I1hsoITqs/MbszalIv4mpnsmrE1K4ezapkr6r8xfPFT5Nm7PnFbN9SjpmutJf\nNAhwILpC9lbbCag0SzguTZkKjsb5NBiuCkpQ3mK4xvfiTP53yC4N1hIPClvvB1h+\nSthUwvnCIWRCvUP2f030oA==\n-----END PRIVATE KEY-----\n",
    "client_email": "serviceaccountforgooglesheet@cellular-cortex-277310.iam.gserviceaccount.com",
    "client_id": "107290500308067165780",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/serviceaccountforgooglesheet%40cellular-cortex-277310.iam.gserviceaccount.com"
}

def get_doc(google_sheet_link):
    try:
        gspread_instance = gspread.service_account_from_dict(credentials)
        spread_sheet_data = gspread_instance.open_by_url(google_sheet_link)
        return spread_sheet_data
    except Exception as err:
        print(f"Caught an exception while authenticating and getting spread sheet data: {err}")
        print(err)
        return None
    
# def get_worksheet_id(google_sheet_link):
#     try:
#         return google_sheet_link.split('/')[-1].replace('edit#gid=', '')
#     except Exception as err:
#         print(f"Caught an exception while getting work sheet id - {err}")
#         return None

def get_worksheet_id(google_sheet_link):
    # Define a regular expression pattern to extract the worksheet ID
    worksheet_id_pattern = r"/d/([^/]+)/edit#gid=(\d+)"

    # Use re.search to find the worksheet ID in the link
    match = re.search(worksheet_id_pattern, google_sheet_link)

    if match:
        spreadsheet_id = match.group(1)
        worksheet_id = match.group(2)

    # Now you have the spreadsheet ID and worksheet ID
    # print("Spreadsheet ID:", spreadsheet_id)
    # print("Worksheet ID:", worksheet_id)
        return worksheet_id
    else:
        print("Worksheet ID not found in the link.")



    