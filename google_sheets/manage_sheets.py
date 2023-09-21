from google_sheets.sheet_utils import get_doc, get_worksheet_id
import gspread

def manage_sheet(google_sheet_link):
    spread_sheet_data = get_doc(google_sheet_link)
    # print(spread_sheet_data)
    if spread_sheet_data:
            worksheet_id = get_worksheet_id(google_sheet_link)
            if worksheet_id:
                try:
                    worksheet_id = int(worksheet_id) 
                    # print("Worksheet ID:", worksheet_id)
                    #? iterate over the list to get the desried the worksheet id as gspread uses 0 indexing
                    worksheet_list =spread_sheet_data.worksheets()
                    # print("work sheet lists", worksheet_list)
                    cnt=0
                    for id in worksheet_list:
                        # print(id)
                        if id.id == worksheet_id:
                            break
                        else:
                            cnt+=1
                    return cnt
                except Exception as e:
                    print(f'error occured while fetching the index{e}')