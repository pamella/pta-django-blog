from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Post

# to learn more about Django Class Based Views (CBV)
# https://docs.djangoproject.com/en/2.0/topics/class-based-views/
# template view
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

