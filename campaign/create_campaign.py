from exception.handle_google_ads_exception import handle_google_ads_exception
from google.ads.googleads.errors import GoogleAdsException
from ad_group.create_ad_group import create_ad_grp
from ad.create_ad import create_advert
from keywords.add_keywords import add_keywords_in_ad_group


def create_camp(google_ads_client, camp_data, worksheet):
    try:
        
        print("Here to create a campaign for given data - ", camp_data, google_ads_client)
        print("\n")
        campaign_service = google_ads_client.get_service("CampaignService")
        
        # Create campaign.
        campaign_operation = google_ads_client.get_type("CampaignOperation")
        campaign = campaign_operation.create
        
        #? extracting the values from camp_data to initialize the campaign
        customer_id = str(camp_data["customer_id"])
        campaign_name = camp_data["name"]
        campaign.name = campaign_name
        campaign.advertising_channel_type = (
            google_ads_client.enums.AdvertisingChannelTypeEnum.SEARCH
        )
        
        campaign.status = google_ads_client.enums.CampaignStatusEnum.PAUSED
        
        # Set the bidding strategy and budget.
        campaign.maximize_conversions = {}
        
        # Create campaign budget and add it to the campaign
        campaign_budget_service = google_ads_client.get_service("CampaignBudgetService")

        # Create a budget, which can be shared by multiple campaigns.
        campaign_budget_operation = google_ads_client.get_type("CampaignBudgetOperation")
        campaign_budget = campaign_budget_operation.create
        campaign_budget.name = f"{campaign_name} Budget"
        campaign_budget.delivery_method = (
            google_ads_client.enums.BudgetDeliveryMethodEnum.STANDARD
        )
        campaign_budget.amount_micros = int(camp_data["campaign_budget"])*1000000
        campaign_budget.explicitly_shared = False

        # Add budget.
        campaign_budget_response = campaign_budget_service.mutate_campaign_budgets(
            customer_id=customer_id, operations=[campaign_budget_operation]
        )
        campaign.campaign_budget = campaign_budget_response.results[0].resource_name
        
        # Set the campaign network options.
        campaign.network_settings.target_google_search = True
        campaign.network_settings.target_search_network = True
        # campaign.network_settings.target_partner_search_network = True It is allowed only for some google partners
        campaign.network_settings.target_content_network = False

        # Optional: Set the start and end date.
        # if camp_data["start_time"]:
        #     campaign.start_date = datetime.date.strftime(camp_data["start_time"], _DATE_FORMAT)
        
        # if camp_data["end_time"]:
        #     campaign.end_date = datetime.date.strftime(camp_data["end_time"], _DATE_FORMAT)
        
        # Add the campaign.
        campaign_response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
        print(f"Created campaign {campaign_response}.")
        campaign_id = None
        # campaign_id = "20551584238"
        if campaign_response and campaign_response.results[0] and campaign_response.results[0].resource_name:
            campaign_id = campaign_response.results[0].resource_name.split('/')[-1]
        print(campaign_id)
        camp_data["campaign_id"] = campaign_id
        ad_group_id = create_ad_grp(google_ads_client, camp_data)
        camp_data["ad_group_id"] = ad_group_id
        print(ad_group_id)
        
        
        create_advert(google_ads_client, camp_data)
        add_keywords_in_ad_group(google_ads_client, camp_data)
    except GoogleAdsException as ex:
        handle_google_ads_exception(ex)
    except Exception as err:
        print(f"Caught an exception while creating a  campaign for {camp_data} - {err}")
        return None
    
    
    
    
