from django import forms

from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, ButtonHolder, Button, Submit, Field, HTML, Div
from crispy_forms.bootstrap import FormActions
from core.models import ContactUs
from django.core.mail import send_mail


class ContactUsForm(forms.Form):
    name = forms.CharField(label='', required=True)
    email = forms.CharField(label='', required=True)
    message = forms.CharField(widget=forms.Textarea, label='', required=True)

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = u'John Smith'
        self.fields['email'].widget.attrs['placeholder'] = u'jsmith@abc.com'
        self.fields['message'].widget.attrs['placeholder'] = u'Your message goes here.'

        self.helper = FormHelper()
        self.helper.layout = Layout()

        self.helper.layout.append(Div('name'))
        self.helper.layout.append(Div('email'))
        self.helper.layout.append(Div('message'))

        self.helper.layout.append(FormActions(
            Submit('emailBtn', 'Submit', css_class='btn btn-primary btn-lg'),
        ))

    def save(self, *args, **kwargs):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        contact_us = ContactUs(name=name, email=email, message=message)
        send_mail('New Contact for DeepScrub Sponges from ' + name, email + '\n' + message, email,
                   ['deepscrub.sponge@gmail.com'], fail_silently=False)

        contact_us.save()