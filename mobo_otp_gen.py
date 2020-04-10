import random
import requests
def otp_on_mobile(mono):
    otp=random.randrange(100001,999999)
    bdy="Your OTP is {} and you can use it to verify your account.".format(otp)

    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {'apikey':apiKey,'secret':secretKey,'usetype':useType,'phone': phoneNo,'message':textMessage,'senderid':senderId}
        return requests.post(reqUrl, req_params)
    response = sendPostRequest(URL, 'Enter_your_apiKey_here', 'Enter_secretKey_here', 'stage', mono, 'ZeeBnk', bdy)
 
    print("OPT send on your mobile ( +91{}***{} )".format(mono[0:3],mono[6:]))
    return otp


entered_mobile_no = input("Ënter valid Mobile No. : ")
generated_otp = otp_on_mobile(entered_mobile_no)

user_entered_otp = int(input("Ënter OTP : "))
if generated_otp == user_entered_otp:
    print("OTP matched")
else :
    print("OTP not matched")