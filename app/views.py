from django.views.generic import ListView, DetailView

from .models import Project, Category


class ProjectIndexView(ListView):
    context_object_name = 'projects'

    def get_queryset(self):
        query = self.request.GET.get('search')
        category = self.request.GET.get('category')

        if query:
            return Project.search(query)
        elif category:
            return Category.objects.get(name=category).projects.all()

        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        projects = self.get_queryset()
        sub_cats = []
        for p in projects:
            sub_cats.extend(p.sub_categories.all())
        context['sub_categories'] = set(sub_cats)
        return context


class ProjectDetailView(DetailView):

    model = Project
    context_object_name = 'project'
