from google_adverts.configuration import GoogleAds
from exception import handle_google_ads_exception
from google_sheets.sheet_utils import get_doc, get_worksheet_id
import re


def fetch_keywords(google_sheet_link):
    try:
        spread_sheet_data=get_doc(google_sheet_link)
        if spread_sheet_data:
            worsksheet_id = get_worksheet_id(spread_sheet_data)
            if worsksheet_id:
                worsksheet_id=int(worsksheet_id)
                print(worsksheet_id) #! printing worsksheet_id
                current_sheet=spread_sheet_data.get_worksheet(worsksheet_id)
                worksheet_rows=current_sheet.get_all_records()
                print(worksheet_rows) #! printing all records
                keyword_data=[]
                for row in worksheet_rows:
                    if row == 'Keyword':
                        for cols in row['Keywords']:
                            keyword_data.append(cols)
                
                static_keywords=[]
                # Define a regular expression pattern to match strings inside double quotes
                pattern = r'"(.*?)"'

                for keywords in keyword_data:
                    for item in keywords:
                        # Use re.findall to extract all matching strings and store them in an array
                        static_keyword=re.findall(pattern, )
                        static_keywords.extend(static_keyword)
                
                # Print the extracted strings
                print(static_keywords)
            else:
                print("Cannot acccess worksheet id")
        else:
            print("cannot acccess spread sheet data")
                                           
    except handle_google_ads_exception as e:
         print(f"error occurred while processing work sheet data of keywords {e.message}")
         
