from google_adverts.configuration import GoogleAds

def get_camp(customer_id):
    google_ads_client_instance = GoogleAds()
    google_ads_client = google_ads_client_instance.get_google_ads_client()
    print(google_ads_client)
    ga_service = google_ads_client.get_service("GoogleAdsService")

    query = """
        SELECT
          campaign.id,
          campaign.name
        FROM campaign
        ORDER BY campaign.id"""

    # Issues a search request using streaming.
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    print(stream)
    for batch in stream:
        for row in batch.results:
            print(
                f"Campaign with ID {row.campaign.id} and name "
                f'"{row.campaign.name}" was found.'
            )
