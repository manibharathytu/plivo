#sudo pip3 install plivo

import plivo

p = plivo.RestClient(
    'MANTFIMZGZNMUWYZEWNT',
   'ZWI5ZTM0NTk1NzNlYWM2ZDc3ODUwMjE4NzU4MGQx'
 )


call_made = p.calls.create(
    from_='+1 805-723-9495',
    to_='918903646678',
     answer_url='http://plivodirectdial.herokuapp.com/response/sip/route/?DialMusic=real&CLID=+1805-723-9495',
   answer_method = "GET"
 )

# message_created = p.messages.create(
#     src='+1 805-723-9495',
#     dst='918903646678',
#     text='Hello, world!'
# )