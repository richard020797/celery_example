from django import forms
from modules.landing.tasks import task_send_signup_email


class SignupForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'rows': 5}))
    #honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        #if self.cleaned_data['honeypot']:
        #    return False
        task_send_signup_email.delay(self.cleaned_data['email'], self.cleaned_data['message'])
