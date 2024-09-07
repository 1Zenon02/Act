from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .forms import ContactForm
from .models import Project, Contact

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('thank_you')
    return render(request, 'contact.html', {'form': form})

class InquiryDashboardView(ListView):
    model = Contact
    template_name = 'portfolio/inquiry_dashboard.html'
    context_object_name = 'inquiries'

class ThankYouView(TemplateView):
    template_name = 'thank_you.html'
