from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('careers', views.careers, name="careers"),
    path('contactus', views.contactus, name="contactus"),
    path('digitalstrategy', views.digitalstrategy, name="digitalstrategy"),
    path('growthstrategy', views.growthstrategy, name="growthstrategy"),
    path('investorfacilitation', views.investorfacilitation, name="investorfacilitation"),
    path('leantransformation', views.leantransformation, name="leantransformation"),
    path('marketentry', views.marketentry, name="marketentry"),
    path('ourclients', views.ourclients, name="ourclients"),
    path('projectimplementation', views.projectimplementation, name="projectimplementation"),
    path('services', views.services, name="services"),
    path('blog', views.blogs, name="blogs"),
    path('blog/<int:pk>', views.blog, name="blog"),
]