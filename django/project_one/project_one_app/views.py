from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def default(request):
    return HttpResponse("<h1>Hello Boss, Django is working!</h1>")


def list_test(request):
    names=['shikhar','rashi','ayush','antra','anjali','pankaj','ashu']
    response = ""

    for name in names:
        response += f"<h2>{name}</h2>"

    return HttpResponse(response)


def dict_test(request):
    names = {
        'name1': 'rahul',
        'name2': 'shikhar',
        'name3': 'ayush',
        'name4': 'rashi',
        'name5': 'antra',
        'name6': 'pankaj',
        'name7': 'jai prakash',
        'name8': 'rosey',
        'name9': 'harsh',
    }

    response = "<ul>"

    for naam in names.values():
        response += f"<li>{naam}</li>"

    response += "</ul>"

    return HttpResponse(response)     


def string_test(request):
    string="shikhar"
    list1=[] 
    for i in range(len(string)):
        list1.append(string[i])
    return HttpResponse(str(list1))


# Create a view that shows numbers from 1 to 20 using HttpResponse.
def shows_number(request,n):
    numbers = ""

    for i in range(1,n+1):
        if i%2==0:  
            if i<n-1:
                numbers += str(i) + ","
            else:
                numbers+=str(i)+"."
    return HttpResponse(numbers)



def string_reverse(request, name):
    reversed_string = name[::-1]   # reverse the string
    return HttpResponse(f"Original: {name} | Reversed: {reversed_string}")


def htmlrender(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        country = request.POST.get("country")

        return HttpResponse(
            f"Form submitted!<br>"
            f"Username: {username}<br>"
            f"Email: {email}<br>"
            f"Password: {password}<br>"
            f"Gender: {gender}<br>"
            f"Country: {country}"
        )
    else:
        # Render the HTML form template
        return render(request, "index.html")