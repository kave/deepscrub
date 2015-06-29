from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.generic import View
from models import *


class HomeView(View):
    def get(self, request):
        strong_sponges = Sponge.objects.filter(type=SpongeType.STRONG)
        gentle_sponges = Sponge.objects.filter(type=SpongeType.GENTLE)
        return render(request, 'main.html', {'strong_sponges': strong_sponges,
                                             'gentle_sponges': gentle_sponges})


def product_detail_view(request, pk):
    sponge = Sponge.objects.get(pk=pk)

    return render(request, 'product_detail.html', {'sponge': sponge})
