from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.core.mail import send_mail 
from django.http import HttpResponseRedirect

from .forms import SubmissionForm

from .models import Project, Category


class ProjectIndexView(ListView):
    context_object_name = 'projects'

    def get_queryset(self):
        query = self.request.GET.get('search')
        category = self.request.GET.get('category')
        sub_cat = self.request.GET.get('sub_cat')

        if query:
            return Project.search(query)
        elif category and not sub_cat:
            return Category.objects.get(name=category)\
                .projects.all()
        elif category and sub_cat:
            return Category.objects.get(name=category)\
                .projects.filter(sub_categories__pk=sub_cat)

        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        category_name = self.request.GET.get('category')
        if category_name:
            category = Category.objects.get(name=category_name)
            context['category'] = category
            context['sub_categories'] = category\
                .sub_categories.all()
        return context


class ProjectDetailView(DetailView):

    model = Project
    context_object_name = 'project'

DEFAULT_FROM_EMAIL = 'annuaire@consocollaborative.com'
MANAGERS = ['vincent.poulain2@gmail.com']


def submit_project(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            send_mail('[Annuaire CC] - Demande d\'ajout de projet',
                      'Foobar',
                      DEFAULT_FROM_EMAIL,
                      MANAGERS)
        return render(request, 'app/project_submission_sent.html')
    else:
        form = SubmissionForm()

    return render(request, 'app/project_submission.html', {'form': form})
