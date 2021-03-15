from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect

def favicon_view(request):
	return HttpResponseRedirect('/static/favicon.ico')

class ApplicationView(TemplateView):
	template_name = "application.html"