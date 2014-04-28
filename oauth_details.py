from django.utils import simplejson
from string import Template
import requests
import logging as log


#=========== FIll in these details ==========
CLIENT_ID = "TkkXBqhnamgv7IptmiWRZr6aGi5fcWEnxl7PO5YN1lj7GhDkCU"
CLIENT_SECRET = "oBdoCVNxePD6RB6UCFzSJeK083HbEE7zNhvcf2bWdYgpWD5JoG"

REDIRECT_URL = Template("""http://join.agiliq.com/oauth/authorize?client_id=$client_id&redirect_uri=$redirect_uri&response_type='code'""")

ACCESS_TOKEN_URL = Template("""http://join.agiliq.com/oauth/access_token/?client_id=$client_id&client_secret=$client_secret&redirect_uri=$redirect_uri&code=$code&grant_type='authorization_code'""")

URL = "http://join.agiliq.com/api/resume/upload/?access_token="

def get_redirect_url(url):
	return REDIRECT_URL.substitute(client_id=CLIENT_ID,redirect_uri=url)

def get_access_token(code,rurl):
	url = ACCESS_TOKEN_URL.substitute(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=rurl,code=code)
	resp = requests.get(url)
	return resp

def get_details(code,url):
	resp = get_access_token(code,url)
	return resp

def get_url():
	return URL