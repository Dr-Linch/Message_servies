from django import forms
from django.forms import DateInput

from newsletter_app.models import Client, Newsletter, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class NewsletterForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(owner=user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Newsletter
        exclude = ('owner',)


class NewsletterFormModerator(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('status_send',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'