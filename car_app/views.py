from django.shortcuts import render, get_object_or_404
from car_app.models import TruckModel, TruckNumber, Post
from car_app.forms import TruckModelForm, TruckNumberForm, PostForm

from django.db.models import FloatField

from django.db.models import Max



def index(request):
	all_truck_models = TruckModel.objects.all()
	all_truck_numbers = TruckNumber.objects.all()
	print('----')
	over_info = {}
	

	for tnum in all_truck_numbers:
		overload = ((tnum.current_weight - tnum.model_name.max_capacity) / tnum.model_name.max_capacity) * 100
		print(tnum.model_name.max_capacity, tnum.current_weight, int(overload))
		#over[tnum] = int(overload)
		over_info[tnum] = {'model': tnum.model_name, 'over': int(overload), 'max_capacity': tnum.model_name.max_capacity}
	
	#
	print('over_info = ', over_info)
	print()
	print()
	nnum = TruckNumber.objects.all().values('bort_number', 'current_weight', 'model_name')
	nmodel = TruckModel.objects.all().values('model_name', 'max_capacity')
	print('nnum = ', nnum)
	print()
	print('nmodel = ', nmodel)
	
	print('----')
	'''
	tt = TruckNumber.objects.annotate(
		overload = (('max_capacity' - 'current_weight') / 'max_capacity' * 100), output_field = FloatField())
	print('tt = ', tt)
	'''
	
	#tt = TruckNumber.objects.aggregate(max_cap = Max('max_capacity'))
	#print('tt = ', tt)
	

	d = {'all_truck_models': all_truck_models,
		'all_truck_numbers': all_truck_numbers, 
		'over_info': over_info}
	
	return render(request, 'car_app/index.html', d)
	
	
	
	
	
	

# truck_number_detail.html
def truck_number_detail(request, truck_id):
    number_info = get_object_or_404(TruckNumber, pk=truck_id)
    return render(request, 'car_app/truck_number_detail.html', {'number_info': number_info})






# truck_model_detail.html
def truck_model_detail(reaquest, model_id):
    model_info = get_object_or_404(TruckModel, pk=truck.model_name_id)
    return render(request, 'car_app/truck_model_detail.html', {'model_info': model_info})
    
    
    
    

def model_new(request):
	if request.method == 'POST':
		model_form = TruckModelForm(request.POST)
		if model_form.is_valid():
			model = form.save(commit=False)
			model.save()
			return redirect('model_detail', pk=model.pk)
	else:
		model_form = TruckModelForm()
		
	return render(request, 'car_app/model_edit.html', {'model_form':model_form})
	





def number_new(request):
	number_form = TruckNumberForm()
	return render(request, 'car_app/number_edit.html', {'number_form':number_form})
	


def post_list(request):
	all_posts = Post.objects.all()
	p = {'all_posts':all_posts}
	return render(request, 'car_app/post_list.html', p)	


def post_new(request):
    form = PostForm()
    return render(request, 'car_app/post_edit.html', {'form': form})







