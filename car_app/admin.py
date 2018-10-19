from django.contrib import admin

from car_app.models import TruckModel, TruckNumber, Post

# Register your models here.

admin.site.register(Post)


class TruckModelAdmin(admin.ModelAdmin):

    fields = ['model_name', 'max_capacity']
	



class TruckNumberAdmin(admin.ModelAdmin):

    fields = ['bort_number',  'max_capacity']
	
	
admin.site.register(TruckModel, TruckModelAdmin)
admin.site.register(TruckNumber, TruckNumberAdmin)