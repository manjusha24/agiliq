from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect,render, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import RequestContext
from string import Template
from agiliq_oauth.models import UploadForm
from agiliq import settings
import oauth_details


def agiliq_oauth(request):
	redirect_uri = 'http://localhost:8000/response/'
	url = oauth_details.get_redirect_url(redirect_uri)
	return redirect(url)

def agiliq_response(request):
	code = request.GET['code']
	redirect_url = 'http://localhost:8000/response/'
	data = oauth_details.get_details(code,redirect_url)
	token = data.text.split(':')[1].split(',')[0].split('"')[1]
	URL = oauth_details.get_url()
	url = URL+token
	print url
	c = {}
	form = UploadForm()
	c.update({'form' : form,'url':url,})
	c.update(csrf(request))
	if request.method == 'GET':
		return render(request,"form.html",c)