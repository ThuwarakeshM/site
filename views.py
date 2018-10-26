from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stax_official/index.html', {})

def about(request):
    return render(request, 'stax_official/about.html', {})


def careers(request):
    return render(request, 'stax_official/careers.html', {})


def contactus(request):
    return render(request, 'stax_official/contactus.html', {})


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