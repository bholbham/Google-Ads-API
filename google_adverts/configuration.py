from google.ads.googleads.client import GoogleAdsClient

# credentials = {
#     "developer_token": "6HQT8eShjwwNRQ09ttggzQ",
#     "refresh_token": "1//0gmjkrF5nIj-GCgYIARAAGBASNwF-L9Ira04XA5QOV1tMUGZhQ00roV73y5gOZ83VSuxCMpRFghWNRA74eCyWpuwNfcjKe3OytCs",
#     "client_id": "192111549996-b7oh4f6frrkbd1uls0onjhsf75eilko3.apps.googleusercontent.com",
#     "client_secret": "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",
#     "use_proto_plus": "True",
#     "login_customer_id":"2544551178" #? test manager id
# }

credentials = {
    "developer_token": "6HQT8eShjwwNRQ09ttggzQ",
    "refresh_token": "1//0gYq0Zpswq9MNCgYIARAAGBASNwF-L9IrWxDgdNGJ3t2EQnkkXUoC1Z4z_sgiYUbBgivF-wqAnRIL228pYvikdlBSsgln9Mds5Cc",
    "client_id": "78343152454-bcggfbqt3ombuei5g2dh9pgh954c037i.apps.googleusercontent.com",
    "client_secret": "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",
    "use_proto_plus": "True",
    "login_customer_id":"2544551178" #? test manager id
}

# credentials = {
#     "developer_token": "",
#     "refresh_token": "",
#     "client_id": "",
#     "client_secret": "",
#     "use_proto_plus": "",
#     "login_customer_id":"" #? manager id
# }


class GoogleAds:
    google_ads_client = None

    def __init__(self):
        if GoogleAds.google_ads_client is None:
            GoogleAds.google_ads_client = GoogleAdsClient.load_from_dict(credentials)

    def get_google_ads_client(self):
        return GoogleAds.google_ads_client


if __name__ == "__main__":
    google_ads_client_instance = GoogleAds()
    print(google_ads_client_instance.get_google_ads_client())
    google_ads_client_instance_two = GoogleAds()
    print(google_ads_client_instance_two.get_google_ads_client()) 
#     # ! why two different instances created here