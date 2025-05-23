import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'ZfwaFcGjPmv0SRZAyLMKcFDJwm7aEmGguGn20Tvfn4A7PGyS'
    consumer_secret = 'iEcuj1OPOeBvVY6FZFP47WoApTFUZD0aZHPGXmvX98yEKfAqQcWmyr2GEUqw8Qwl'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'



class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

# class MpesaAccessToken:
#     r = requests.get(
#         MpesaC2bCredential.api_URL,
#         auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret)
#     )
#     try:
#         mpesa_access_token = json.loads(r.text)
#         validated_mpesa_access_token = mpesa_access_token["access_token"]
#     except json.JSONDecodeError:
#         print("Failed to decode JSON. Response text:", r.text)
#         mpesa_access_token = {}
#         validated_mpesa_access_token = None
#     except KeyError:
#         print("Access token not found in response. Response JSON:", mpesa_access_token)
#         validated_mpesa_access_token = None


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')