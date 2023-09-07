from django.shortcuts import render
from datetime import datetime

now = datetime.now()

# Create your views here.
def index(request):
    return render(request, "new_year/index.html", {
        "new_year" : now.month == 1 and now.day == 1
    })
