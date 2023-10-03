from django.urls import path

from . import views

app_name="public" # sets the namespace for all urlpatterns to public so all references must start with the prefix public:name
urlpatterns = [
    path('', views.index, name='index'),
    path('experiments/', views.experiments, name='experiments'),
]