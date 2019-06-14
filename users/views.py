from django.shortcuts import render, HttpResponseRedirect
from django.db import connection
from pprint import pprint
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from .models import FormData, DataSchema


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

        formdata_obj = FormData()
        dataschema_obj = DataSchema()

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

        # Form info save to users_formdata DB

        formdata_obj.lead_gen = datafield1
        formdata_obj.company_name = datafield2
        formdata_obj.company_address = datafield3
        formdata_obj.company_city = datafield4
        formdata_obj.company_state = datafield5
        formdata_obj.company_country = datafield6
        formdata_obj.company_url = datafield7
        formdata_obj.company_linkedin = datafield8
        formdata_obj.company_phone = datafield9
        formdata_obj.company_email = datafield10
        formdata_obj.f_name = datafield11
        formdata_obj.l_name = datafield12
        formdata_obj.owner_linkedin = datafield13
        formdata_obj.owner_title = datafield14

        # Form info save to users_formdata DB
        dataschema_obj.company_name = datafield2
        dataschema_obj.company_url = datafield7
        dataschema_obj.company_email = datafield10
        dataschema_obj.f_name = datafield11
        dataschema_obj.l_name = datafield12
        dataschema_obj.city_name = datafield4

        formdata_obj.save()
        dataschema_obj.save()

        return TemplateResponse(request, 'home.html')



