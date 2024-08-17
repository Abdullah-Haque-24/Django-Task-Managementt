from django.shortcuts import render
from tasks import models
def home(request):
    data = models.Task.objects.all()
    # print(data)
    return render(request, 'home.html', {"data" : data})