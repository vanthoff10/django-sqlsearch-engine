from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request)


def create(request):
    print(request.method)
    if request.method == "POST":
        input_text = request.POST['search']
        print(input_text)
        print('*'*50)
        return HttpResponse("welcome")