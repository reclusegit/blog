from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from record.models import User, IssueType, IssueRecord
from record.form import UserForm 


def regist(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			User.objects.create(username = username, password = password)
			return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render_to_response('regist.html', {'uf':uf})


def login(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.filter(username__exact = username, password__exact = password)
			if user:
				req.session['username'] = username
				# read issue type from db
				issue = IssueType.objects.all()
				#return HttpResponseRedirect('/index/', {'issue':issue})
				return render_to_response('index.html', {'issue':issue})
			else:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render_to_response('login.html', {'uf':uf})


def index(req):
	username = req.session.get('username', 'anybody')
	return render_to_response('index.html', {'username':username})


def logout(req):
	session = req.session.get('username', False)
	if session:
		del req.session['username']
		return render_to_response('logout.html', {'username':session})
	else:
		return HttpResponse('please login!')


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        issueRecord = IssueRecord.objects.filter(issueName__icontains = q)
        return render_to_response('search_results.html', {'issueRecord':issueRecord})
    else:
    	return HttpResponse('Please submit a search term.')
