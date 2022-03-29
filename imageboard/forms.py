from django import forms
from .models import Thread, Reply
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ThreadForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Thread
        fields = ['name', 'subject', 'comment', 'image']


class ThreadEditForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['subject', 'comment']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'comment']
