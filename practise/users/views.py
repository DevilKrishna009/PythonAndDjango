from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views,status
# Create your views here.

data = {
    "name" : "First API",
    "format" : "json",
    "category" : "http",
    "framework" : "django"
}

def dummy_api(request):
    return JsonResponse(data)

class DummyRestAPIView(views.APIView):
    def get(self, request):
        return Response(data)
    def post(self, request):
        req_data = request.data
        return Response(req_data)
    def put(self, request):
        req_data = request.data
        return Response(req_data)
    def delete(self, request):
        return Response({"message" : "ID is deleted"})
    
class DummyRestAPIIDView(views.APIView):
    def get(self, request, id):
        return Response({"id": id})