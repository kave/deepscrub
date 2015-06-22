from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View

class HomeView(View):

    def get(self, request):
        return render_to_response('main.html')