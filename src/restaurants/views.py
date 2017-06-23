import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home_old(request):
    html_var = 'f strings'
    num = random.randint(0, 100000000)
    html_ = f"""<!DOCTYPE html>
    <html lang=en>

    <head>
    </head>
    <body>
    <h1>Hello World!</h1>
    <p>This is {html_var} coming through</p>
    <p>This is a random number: {num}</p>
    </body>
    </html>
    """
    #f strings
    return HttpResponse(html_)

def home(request):
    num = random.randint(0, 100000000)
    return render(request, "base.html", {"html_var": True, "num": num})