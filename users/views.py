from django.shortcuts import render, HttpResponse
from django.db import connection

# Create your views here.


def index(request):
    return render(request)


def create(request):
    print(request.method)
    if request.method == "POST":
        input_text = request.POST['search']
        cursor = connection.cursor()
        cursor.execute("SELECT city_name FROM users_dataschema where company_name=%s", [input_text])
        row = cursor.fetchall()
        if row:
            print(row)
        else:
            return HttpResponse("No such Data Available")
        return HttpResponse(row)

