import datetime
import time
from ANTClient import config
import requests

body = {'message': 'register_session', 'id': '001'}
r = requests.post(url=config.url+'/register_session', json=body)
msg = r.text