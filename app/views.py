from django.views.generic import ListView, DetailView

from .models import Project


class ProjectIndexView(ListView):
    template_name = 'app/index.html'
    context_object_name = 'projects'
    model = Project


class ProjectDetailView(DetailView):

    model = Project
    template_name = 'app/detail.html'
    context_object_name = 'project'
