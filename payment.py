import os
import razorpay
import dotenv

dotenv_file = os.path.join(".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

key_secret = os.environ['KEY_SECRET']
key_id = os.environ['KEY_ID']

client = razorpay.Client(auth = (key_id, key_secret))

data = {
    "amount" : 500,
    "currency" : "INR",
    "receipt" : "test_pay_receipt",
}

payment = client.order.create(data=data)

print(payment)

# params_dict = {
#     'razorpay_payment_id': 'pay_LfzA8ZoYhnRsL5',
#     'razorpay_order_id': 'order_Lfwq4s5smlsqHG',
#     'razorpay_signature': '2d845d5745e34682c696aeb222c7d4da926875bb064b9f6a3faf432e0d30ea2d',
# }

# test = client.utility.verify_payment_signature(params_dict)
# print(test)