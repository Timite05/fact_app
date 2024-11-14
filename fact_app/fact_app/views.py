from django.shortcuts import render
from django.views import View 
from . models import * # type: ignore

class HomeView(View):
    templates_name = 'index.html'
    invoices = Invoice.objects.select_related('customer','save_by').all()

    context = {
        'invoice': invoices
    }
    
    def get(self, request, *args, **kwargs):

        return render(request, self.templates_name, self.context)
    
    def post(self, request, *args, **kwargs):

        return render(request, self.templates_name, self.context)