#!/usr/bin/python
#-​*- encoding: utf-8 -*​-

import praw
import webbrowser

r = praw.Reddit('OAUTH testing example by u/_Daimon_ ver 0.1 see'\
'https://praw.readthedocs/io/en/latest/'\
'pages/oauth.html for source')

r.set_oauth_app_info(client_id='e-_T3gZHhJlbbg',\
client_secret='yytNl10xHTbkuhwMSocCxYRk_CA',\
redirect_uri='http://127.0.0.1:65010/'
'authorize_callback')

url = r.get_authorize_url('uniqueKey',\
'identity',\
True)

webbrowser.open(url)

access_information = r.get_access_information('cTuIrFUO-XHr_eeXcuFgjdv2dsQ')
print(access_information)
