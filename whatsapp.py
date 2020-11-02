from twilio.rest import Client
########################################################################################################################################
account_sid = 'YOUR ACCOUNT SID'
auth_token = 'YOUR TOKEN'
########################################################################################################################################

def whatsappmsg(message,phno):
    phno="whatsapp:"+phno
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                                  body=message,
                                  from_='whatsapp:+14155238886',
                                  to=phno
                              )
    
    print(message.sid)
