from django import forms
from django.views.generic import FormView
from django.urls import reverse

from vueforms.models.intelligent_search import IntelligentSearchSetup


class SettingsForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, required=True)
    url = forms.URLField(label="URL", max_length=255, required=True)
    shared_secret = forms.CharField(label="Shared secret", max_length=128, required=True)
    index_setup = forms.JSONField(label="Index setup", required=False)

    def __init__(self, *args, intelligent_search=None, **kwargs):
        self.intelligent_search = intelligent_search
        kwargs["initial"] = {
            "name": intelligent_search.name if intelligent_search else "",
            "url": intelligent_search.url if intelligent_search else "",
            "shared_secret": intelligent_search.shared_secret if intelligent_search else "",
            "index_setup": intelligent_search.index_setup if intelligent_search else None,
        }
        super().__init__(*args, **kwargs)

    def save(self):
        if not self.intelligent_search:
            self.intelligent_search = IntelligentSearchSetup()

        self.intelligent_search.name = self.cleaned_data["name"]
        self.intelligent_search.url = self.cleaned_data["url"]
        self.intelligent_search.shared_secret = self.cleaned_data["shared_secret"]
        self.intelligent_search.index_setup = self.cleaned_data["index_setup"]
        self.intelligent_search.save()


class SettingsView(FormView):
    template_name = "intelligent_search/settings.html"
    form_class = SettingsForm

    def get_form_kwargs(self):
        return {
            **super().get_form_kwargs(),
            "intelligent_search": IntelligentSearchSetup.objects.first(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("vueforms:intelligent_search")
