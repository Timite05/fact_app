from django.shortcuts import render
from django.views import View 
from . models import * # type: ignore
from django.contrib import messages

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
    
class AddCustomerView(View):

    template_name ='add_customer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'sex': request.POST.get('sex'),
            'age': request.POST.get('age'),
            'city': request.POST.get('city'),
            'zip_code': request.POST.get('zip_code'),
            'save_by': request.user
        }
        try:
            created = Customer.objects.create(**data)
            if created:
                messages.success(request, "Customer registred successfully.")
            else:
                messages.error(request, "Sorry try again the sent data is corrupt")

        except Exception as e:
           messages.error(request,f"Sorry our system is detecting the following issue {e}." )
        
        return render(request, self.template_name)