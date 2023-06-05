from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

def home_page(request):
    context = {
        "page_data": "Home Page"
    }
    return render(request, "playground/raw_page.html", context)


def about_page(request):
    print(request.Get["branch_name"])
    context = {
        "page_data": "About Page"
    }
    return render(request, "playground/raw_page.html", context)


# String Message
def test_api(request):
    return HttpResponse("First API")


# Json Message -> Static  API
def test_json_api(request):
    data = {
        "name": "First Json API",
        "framework": "Python-Django",
        "university": "Sit"
    }
    return JsonResponse(data)


# HTMl Template
def test_html_page(request):
    context = {
        "name": "Sit",
        "framework2024": "Python-Django",
        "framework2023": "Java-Spring-Boot",
        "year": 2025
    }
    return render(
        request,
        "playground/index.html",
        context)


# Hello, {{name}}
def test_hello_name(request, name):
    return HttpResponse(f"Hello, {name}")


# for loop
def test_html_for_page(request):
    context = {
        "data": [{
            "name": "SIT",
            "framework": "Python-Django",
            "year": 2023
        }, {
            "name": "SIT",
            "framework": "Java-Spring-Boot",
            "year": 2024
        }]
    }
    return render(request, "playground/for_loop.html", context)
