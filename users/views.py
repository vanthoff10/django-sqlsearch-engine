from django.shortcuts import render, HttpResponse
from django.db import connection
from pprint import pprint
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from .models import FormData


# Create your views here.


def index(request):
    return render(request)


def create(request):
    x = []
    print(request.method)
    if request.method == "POST":
        input_text = request.POST['search']
        value_text = request.POST['prodId']
        cursor = connection.cursor()
        cursor.execute("SELECT company_name,company_url, company_email, f_name, l_name, city_name  FROM users_dataschema where company_name =%s", [input_text])
        data = cursor.fetchall()
        for item in data:
            x.extend(item)
        # alldata = DataSchema.objects.all()
        if data:
            print(x)
            return TemplateResponse(request, 'home.html', {'data': x})
            # return HttpResponse(row)
        else:
            # return HttpResponse("No such Data Available")
            return TemplateResponse(request, 'home.html', {'data_value': value_text})


def savedata(request):
    print(request.method)

    if request.method == "POST":

        formData_obj = FormData

        datafield1 = request.POST['data1']
        datafield2 = request.POST['data2']
        datafield3 = request.POST['data3']
        datafield4 = request.POST['data4']
        datafield5 = request.POST['data5']
        datafield6 = request.POST['data6']
        datafield7 = request.POST['data7']
        datafield8 = request.POST['data8']
        datafield9 = request.POST['data9']
        datafield10 = request.POST['data10']
        datafield11 = request.POST['data11']
        datafield12 = request.POST['data12']
        datafield13 = request.POST['data13']
        datafield14 = request.POST['data14']
        datafield15 = request.POST['data15']
        datafield16 = request.POST['data16']

        formData_obj.lead_gen = datafield1
        formData_obj.company_name = datafield2
        formData_obj.company_address = datafield3
        formData_obj.company_city = datafield4
        formData_obj.company_state = datafield5
        formData_obj.company_country = datafield6
        formData_obj.company_url = datafield7
        formData_obj.company_linkedin = datafield8
        formData_obj.company_phone = datafield9
        formData_obj.company_email = datafield10
        formData_obj.f_name = datafield11
        formData_obj.l_name = datafield12
        formData_obj.owner_linkedin = datafield13
        formData_obj.owner_title = datafield14

        formData_obj.save(request)

        return TemplateResponse(request, 'home.html')



