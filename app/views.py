from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import SubmissionForm

from .models import Project, Category, SubCategory


class ProjectIndexView(ListView):
    context_object_name = 'projects'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('search')
        category = self.request.GET.get('category')
        sub_cats = self.request.GET.get('sub_cat')
        # as_list = self.request.GET.get('as_list')

        if query:
            projects_list = Project.search(query)
        elif category and not sub_cats:
            projects_list = Category.objects.order_by('name').get(name=category)\
                .projects.order_by('-featured').all()
        elif category and sub_cats:
            projects_list = Category.objects.get(name=category)\
                .projects.order_by('-featured').filter(sub_categories__pk__in=sub_cats.split(','))
        else:
            projects_list = Project.objects.order_by('-featured').all()

        return projects_list

    def get_context_data(self, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        category_name = self.request.GET.get('category')
        selected_sub_cats = self.request.GET.get('sub_cat')

        if category_name:
            category = Category.objects.get(name=category_name)
            context['category'] = category
            context['sub_categories'] = category\
                .sub_categories.all()

        if selected_sub_cats:
            context['selected_sub_categories'] = SubCategory.objects.filter(pk__in=selected_sub_cats.split(','))

        return context


class ProjectDetailView(DetailView):

    model = Project
    context_object_name = 'project'

    query_pk_and_slug = True


DEFAULT_FROM_EMAIL = 'contact@consocollaborative.com'
MANAGERS = ['vincent.poulain2@gmail.com', 'contact@consocollaborative.com ']


def credits(request):
    return render(request, 'app/credits.html')


def submit_project(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            msg_plain = render_to_string('emails/submission.txt', form.cleaned_data)
            msg_html = render_to_string('emails/submission.html', form.cleaned_data)
            send_mail('[Annuaire CC] - Demande d\'ajout de projet : {}'.format(form.cleaned_data['project_name']),
                      msg_plain,
                      DEFAULT_FROM_EMAIL,
                      MANAGERS,
                      html_message=msg_html)
        return render(request, 'app/project_submission_sent.html')
    else:
        form = SubmissionForm()

    return render(request, 'app/project_submission.html', {'form': form})
