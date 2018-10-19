from django.conf.urls import url

from car_app import views
from django.conf.urls.static import static

from django.conf import settings



app_name = 'car_app'


urlpatterns = [
	#ex: /truck/
	

    # ex: /truck/5/
    url(r'^(?P<truck_id>[0-9]+)/$', views.truck_number_detail, name='truck_number_detail'),
    
    
    url(r'^model/new/$', views.model_new, name='model_new'),
    
    url(r'^number/new/$', views.number_new, name='number_new'),
    
    # 
    url(r'^(?P<model_id>[0-9]+)/$', views.truck_model_detail, name='truck_model_detail'),
    
    url(r'^post/new/$', views.post_new, name='post_new'),
    
    
    url(r'^post/$', views.post_list, name='post_list'),



]