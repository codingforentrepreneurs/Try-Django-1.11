from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
    html_var = 'f strings'
    html_ = f"""<!DOCTYPE html>
    <html lang=en>

    <head>
    </head>
    <body>
    <h1>Hello World!</h1>
    <p>This is {html_var} coming through</p>
    </body>
    </html>
    """
    #f strings
    return HttpResponse(html_)
    #return render(request, "home.html", {})#response