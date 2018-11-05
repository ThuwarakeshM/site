from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import Query

# Create your views here.
def index(request):
    return render(request, 'stax_official/index.html', {})

def about(request):
    return render(request, 'stax_official/about.html', {})


def careers(request):
    return render(request, 'stax_official/careers.html', {})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            entry = Query(
                name = form.cleaned_data["name"],
                company = form.cleaned_data["company"],
                phone = form.cleaned_data["phone"],
                job_title = form.cleaned_data["job_title"],
                description = form.cleaned_data["description"],
            )
            entry.save()
            return HttpResponseRedirect('/contactus?success=1')

    else:
        form = ContactForm()

    try:
        success = request.GET['success'][0]
        success = int(success)
    except:
        success = False
    
    return render(request, 'stax_official/contactus.html', {'form': form, 'success': success})


def digitalstrategy(request):
    return render(request, 'stax_official/digitalstrategy.html', {})

def growthstrategy(request):
    return render(request, 'stax_official/growthstrategy.html', {})


def investorfacilitation(request):
    return render(request, 'stax_official/investorfacilitation.html', {})


def leantransformation(request):
    return render(request, 'stax_official/leantransformation.html', {})


def marketentry(request):
    return render(request, 'stax_official/marketentry.html', {})

def ourclients(request):
    return render(request, 'stax_official/ourclients.html', {})


def projectimplementation(request):
    return render(request, 'stax_official/projectimplementation.html', {})


def services(request):
    return render(request, 'stax_official/services.html', {})

def blogs(request):
    return render(request, 'stax_official/blog.html', {})

def blog(request, pk):
    return render(request, 'stax_official/blogpost.html', {})
