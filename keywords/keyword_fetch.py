from google_sheets.sheet_utils import get_doc,get_worksheet_id
from google_sheets.manage_sheets import manage_sheet
import gspread


def fetch_keywords(google_sheet_link):
    try:
        spread_sheet_data=get_doc(google_sheet_link)
        # print(spread_sheet_data) 
        worksheet_id=manage_sheet(google_sheet_link)
        print("fetching the worksheet data:",worksheet_id)
        worksheet=spread_sheet_data.get_worksheet(worksheet_id)
        # print(worksheet)
        
        keyword_columns=worksheet.col_values(1)
        # print(keyword_columns)
        
        static_keywords=set()
        dynamic_keywords=set()
        for col in keyword_columns:
            if "+" in col:
                values=col.split('+')
                for value in values:
                    if '"' in value:
                        static_keywords.add(value)
                    else:
                        dynamic_keywords.add(value)
            else:
                dynamic_keywords.add(col)
                            
        print("static keywords\n",static_keywords)    
        print("dynamic keywords\n",dynamic_keywords)          
    except Exception as e:
        print(f'error occured while fetching the sheet data {e}')
        