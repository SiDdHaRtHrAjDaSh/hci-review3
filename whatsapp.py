from twilio.rest import Client

account_sid = 'ACc1669714d56720604633d46a1b99e30a'
auth_token = '248aa4f9f31d1c7f694ab548f7fa1606'


def whatsappmsg(message,phno):
    phno="whatsapp:"+phno
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                                  body=message,
                                  from_='whatsapp:+14155238886',
                                  to=phno
                              )
    
    print(message.sid)