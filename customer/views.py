from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Customer
from .forms import CustomerForm

class CustomerListView(ListView):
    model = Customer
    template_name = "customer/customer_list.html"
    context_object_name = "customers"

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"

    def form_valid(self, form):
        form.save()
        customers = Customer.objects.all()  # Get updated list
        return render(self.request, "customer/customer_list.html", {"customers": customers})


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"

    def form_valid(self, form):
        form.save()
        customers = Customer.objects.all()  # Get updated list
        return render(self.request, "customer/customer_list.html", {"customers": customers})


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer_list")

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.delete()
        return JsonResponse({"deleted": True})