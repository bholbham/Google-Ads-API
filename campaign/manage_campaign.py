from google_adverts.configuration import GoogleAds
from google_sheets.sheet_utils import get_doc, get_worksheet_id
from campaign.create_campaign import create_camp

def manage_camp(google_sheet_link):
    google_ads_client_instance = GoogleAds()
    print(google_ads_client_instance)
    google_ads_client = google_ads_client_instance.get_google_ads_client()
    spread_sheet_data = get_doc(google_sheet_link)
    # print(spread_sheet_data)
    if spread_sheet_data:
        try:
            worksheet_id = get_worksheet_id(google_sheet_link)
            if worksheet_id:
                worksheet_id = int(worksheet_id) 
                # print("Worksheet ID:", worksheet_id)
                worksheet_list =spread_sheet_data.worksheets()
                print("work sheet lists", worksheet_list)
                cnt=0
                for id in worksheet_list:
                    # print(id)
                    if id.id == worksheet_id:
                
                        
                        break
                    else:
                        cnt+=1
                worksheet = spread_sheet_data.get_worksheet(cnt)
                worksheet_rows = worksheet.get_all_records()
                for row in worksheet_rows:
                    match row['operation']:
                        case 'CREATE_CAMPAIGN':
                            create_camp(google_ads_client, row, worksheet)
                        case _:
                            print("No such case to handle - ", row['operation'])    
                worksheet = spread_sheet_data.get_worksheet(worksheet_id)
                worksheet_rows = worksheet.get_all_records()
        except Exception as e:
            print("An error occurred:", str(e))

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
        else:
            return "Not able to access worksheet"
    else:
        return "Not able to access spread sheet"
    
    
    
