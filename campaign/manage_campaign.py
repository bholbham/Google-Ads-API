from google_adverts.configuration import GoogleAds
from google_sheets.sheet_utils import get_doc, get_worksheet_id
from campaign.create_campaign import create_camp
from keywords.keyword_fetch  import manage_sheet
import gspread

def manage_camp(google_sheet_link):
    google_ads_client_instance = GoogleAds()
    print(google_ads_client_instance)
    google_ads_client = google_ads_client_instance.get_google_ads_client()
    work_sheet_number= manage_sheet(google_sheet_link)
    
    spread_sheet_data = get_doc(google_sheet_link)
    worksheet = spread_sheet_data.get_worksheet(work_sheet_number)
    worksheet_rows = worksheet.get_all_records()
    for row in worksheet_rows:
        match row['operation']:
            case 'CREATE_CAMPAIGN':
                create_camp(google_ads_client, row, worksheet)
            case _:
                print("No such case to handle - ", row['operation'])    
    
# ? work sheet access method

        # worksheet_id = get_worksheet_id(google_sheet_link)
        # if worksheet_id:
        #     worksheet_id = int(worksheet_id)
        #     print(worksheet_id)
        #     worksheet = spread_sheet_data.get_worksheet(worksheet_id)
        #     worksheet_rows = worksheet.get_all_records()
        #     for row in worksheet_rows:
                
                # match row['operation']:
                #     case 'CREATE_CAMPAIGN':
                #         create_camp(google_ads_client, row, worksheet)
                #     case _:
                #         print("No such case to handle - ", row['operation'])
    
#? temporary code
    # # print(spread_sheet_data)
    # if spread_sheet_data:
    #         worksheet_id = get_worksheet_id(google_sheet_link)
    #         if worksheet_id:
    #             try:
    #                 worksheet_id = int(worksheet_id) 
    #                 # print("Worksheet ID:", worksheet_id)
    #                 #? iterate over the list to get the desried the worksheet id as gspread uses 0 indexing
    #                 worksheet_list =spread_sheet_data.worksheets()
    #                 print("work sheet lists", worksheet_list)
    #                 cnt=0
    #                 for id in worksheet_list:
    #                     # print(id)
    #                     if id.id == worksheet_id:
    #                         break
    #                     else:
    #                         cnt+=1
    
    # except Exception as e:
    #                 print("An error occurred while fetching the proper index", str(e))
    #         else:
    #             return "Not able to access worksheet"
    # else:
    #     return "Not able to access spread sheet"
    
