from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views.generic import View
from django.core.mail import send_mail
from models import *
from forms import ContactUsForm
from django.views.generic.edit import FormView


class HomeView(FormView):
    template_name = 'main.html'
    form_class = ContactUsForm
    success_url = '/'

    # def get(self, request):
    #     strong_sponges = Sponge.objects.filter(type=SpongeType.STRONG)
    #     gentle_sponges = Sponge.objects.filter(type=SpongeType.GENTLE)
    #     contactus_form = ContactUsForm(request)
    #
    #     return render(request, 'main.html', {'strong_sponges': strong_sponges,
    #                                          'gentle_sponges': gentle_sponges,
    #                                          'contactus_form': contactus_form})

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        strong_sponges = Sponge.objects.filter(type=SpongeType.STRONG)
        gentle_sponges = Sponge.objects.filter(type=SpongeType.GENTLE)

        context['strong_sponges'] = strong_sponges
        context['gentle_sponges'] = gentle_sponges

        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(HomeView, self).form_valid(form)

    # def post(self, request):
    #     form = ContactUsForm(request.POST)
    #     #if form.is_valid():
    #     form.save()
    #      #   print 'yerp'
    #     #else:
    #       #  return HttpResponse('Invalid Data!')


def product_detail_view(request, pk):
    sponge = Sponge.objects.get(pk=pk)

    return render(request, 'product_detail.html', {'sponge': sponge})
