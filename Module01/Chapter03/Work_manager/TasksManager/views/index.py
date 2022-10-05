# -*- Coding: utf-8 -*-
from django.http import HttpResponse
# View for index page.
def home(request) :
	return HttpResponse ("Hello world!" )