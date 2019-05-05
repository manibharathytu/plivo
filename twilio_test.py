from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7a85b4d2297472cfb3a1b98fb3d39dfb'
auth_token = '0e1a73f4567419e872a967c3ac5e2d65'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+918903646678',
                        from_='+12018176686'
                    )

print(call.sid)