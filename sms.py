from twilio.rest import Client
########################################################################################################################################
account_sid = 'TWILIO SID'
auth_token = 'TWILIO AUTH TOKEN'
########################################################################################################################################
def send_sms(message,phno):
    client = Client(account_sid, auth_token) 
     
    message = client.messages.create( 
                                  from_='+15206368169',  
                                  body=message,
                                  to=phno
                              ) 
     
    print(message.sid)
