from instamojo_wrapper import Instamojo
from digitalShop.settings import PAYMENT_API_KEY, PAYMENT_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_AUTH_TOKEN, 
endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
response = api.payment_request_create(
        amount='20',
        purpose='Testing',
        send_email=True,
        email="sushantapatra92@gmail.com",
        redirect_url="https://www.programminghubs.com"
    )
# print the long URL of the payment request.
url= response['payment_request']['longurl']
# print the unique ID(or payment request ID)
id= response['payment_request']['id']

print(url,id)
