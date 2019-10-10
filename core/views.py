from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Client
from django.template import RequestContext
from .forms import SignUpForm,UpdateProfile
import json
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.template.loader import render_to_string
from django.db.models import Q


def indexx(request):
     return render(request, 'layout.html') 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm((request.POST))
        if form.is_valid():
            client_name= form.cleaned_data['client_name']
            contact_name = form.cleaned_data['contact_name']
            email = form.cleaned_data['email']
            street_name= form.cleaned_data['street_name']
            suburb = form.cleaned_data['suburb']
            postcode = form.cleaned_data['postcode']
            state = form.cleaned_data['state']
            contact_no = form.cleaned_data['contact_no']
            Client.objects.create(client_name=client_name,contact_name=contact_name,email=email,street_name=street_name,suburb=suburb,postcode=postcode,state=state,contact_no=contact_no)
            return redirect('clientlist')
    else:
         form = SignUpForm()    
    return render(request, "add.html", {'form': form})




def get_user_profile(request,id):
    user = Client.objects.get(id=id)
    return render(request, 'profile.html', {"user":user})

    
def update_profile(request,id):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES , instance=Client.objects.get(id=id))
        
        if (form.is_valid()):
           
            form.save()            
            return HttpResponseRedirect(reverse('get_user_profile',args=(id,)))
        
    else:
        form = UpdateProfile(instance=Client.objects.get(id=id))
    return render(request, 'update_profile.html', {
        'form': form
    })



def clientlist(request):
    orderby = request.GET.get('order_by') 
    direction = 'desc'
    if request.GET.get('direction'):
        direction = request.GET.get('direction')
        if direction == 'desc':
            orderby = "-" + orderby  
            direction = 'asc'
            print("ds") 
    
        elif direction == 'asc':
            orderby = orderby   
            direction = 'desc'

    if orderby is None:
        dta = Client.objects.all().order_by('id')
        return render(request,'sl.html',{'dta':dta })

    else:
        dta=Client.objects.all().order_by(orderby)
        return render(request,'sl.html',{'dta':dta,'direction':direction })







def get_queryset(request): 
    query = request.GET.get('q')
    dta= Client.objects.filter(Q(client_name__icontains=query)|Q(email__icontains=query)|Q(contact_no__icontains=query)|Q(suburb__icontains=query)).order_by('client_name')
    return render(request,'sl.html',{'dta':dta})


