from django.shortcuts import render, HttpResponse
from django.db import connection
from pprint import pprint
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from .models import DataSchema

# Create your views here.


def index(request):
    return render(request)


def create(request):
    x = []
    print(request.method)
    if request.method == "POST":
        input_text = request.POST['search']
        cursor = connection.cursor()
        cursor.execute("SELECT company_name,company_url, company_email, f_name, l_name, city_name  FROM users_dataschema where company_name =%s", [input_text])
        data = cursor.fetchall()
        pprint(data)
        for item in data:
            x.extend(item)
        # alldata = DataSchema.objects.all()
        if data:
            print(x)
            return TemplateResponse(request, 'home.html', {'data': x})
            # return HttpResponse(row)
        else:
            # return HttpResponse("No such Data Available")
            return TemplateResponse(request, 'home.html', {'data': x})

