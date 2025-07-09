from django.urls import path

from . import views as vue_views

app_name = "vueforms"

urlpatterns = [
    path(
        "", vue_views.IntelligentSearchSettingsView.as_view(), name="intelligent_search"
    ),
]
