from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect,render, HttpResponseRedirect  
import re
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import RequestContext
import models
import urlparse
import urllib
from string import Template
from agiliq import settings
import requests
import urlparse
import json
import oauth_details


def agiliq_oauth(request):
	redirect_uri = 'http://localhost:8000/response/'
	url = oauth_details.get_redirect_url(redirect_uri)
	print url
	return redirect(url)

def agiliq_response(request):
	print dir(request)
	code = request.GET['code']
	redirect_url = 'http://localhost:8000/response/'
	data = oauth_details.get_details(code,redirect_url)
	return redirect(data)