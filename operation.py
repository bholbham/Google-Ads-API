from google.ads.googleads.errors import GoogleAdsException
from campaign.manage_campaign import manage_camp;
from campaign.get_campaign import get_camp;

if __name__ == "__main__":
    try:
        # get_camp("7211435635")
        google_sheet_link = "https://docs.google.com/spreadsheets/d/1sok4RoKO4NcPNbo2kt_l7332EXmox0YP4zvcvcoffQ8/edit#gid=337718055"
        manage_camp(google_sheet_link)
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
    except Exception as e:
        print(f"Caught an exception while performing operation: {e}")



