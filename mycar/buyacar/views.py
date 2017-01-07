#from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import Context, Template
import datetime

def index(request):
    return HttpResponse("Hello, world. This is an attempt to build mycar.")

def currenttime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def testtemplate(request):
	raw_template = """<p>Dear {{ person_name }},</p>
	<p>
	    Thanks for placing an order from {{ company }}. It's scheduled to
	    ship on {{
	ship_date|date:"F j, Y"
	    }}.
	</p>
	{% if ordered_warranty %}
	<p>Your warranty information will be included in the packaging.</p>
	{% else %}
	<p>
	    You didn't order a warranty, so you're on your own when
	    the products inevitably stop working.
	</p>
	{% endif %}
	<p>Sincerely,<br />{{ company }}</p>"""
	t = Template(raw_template)
	c = Context({'person_name': 'John Smith','company': 'Outdoor Equipment','ship_date': datetime.date(2015, 7, 2),'ordered_warranty': False})
	return HttpResponse(t.render(c))




