from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, Paper
from django.urls import reverse_lazy


# Create your views here.


class JobListView(ListView):
    model = Job
    template_name = 'home.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'post_detail.html'

class JobCreateView(CreateView):
    model = Job
    template_name = 'post_new.html'
    fields = ['job_name', 'notes', 'client', 'start_time', 'end_time', 'paper', 'copies', 'sides', 'oversized', 'color', 'mark_up', 'finishing', 'package']

class JobUpdateView(UpdateView):
    model = Job
    template_name = 'post_edit.html'
    fields = ['job_name', 'client', 'notes', 'start_time', 'end_time']

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class PaperCreateView(CreateView):
    model = Paper
    template_name = 'post_paper_new.html'
    fields = ['paper_name', 'cost']

class PaperUpdateView(UpdateView):
    model = Paper
    template_name = 'post_paper_edit.html'
    fields = ['paper_name', 'cost']

class PaperDeleteView(DeleteView):
    model = Paper
    template_name = 'post_paper_delete.html'
    success_url = reverse_lazy('home')

class PaperDetailView(DetailView):
    model = Paper
    template_name = 'post_paper_detail.html'

class PaperListView(ListView):
    model = Paper
    template_name = 'paper_home.html'



    