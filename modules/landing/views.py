from django.views.generic.edit import FormView
from modules.landing.forms import SignupForm


class SignupView(FormView):
    template_name = '/contact.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(SignupView, self).form_valid(form)
