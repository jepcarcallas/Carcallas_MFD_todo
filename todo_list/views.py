from django.shortcuts import render
from .models import List


def home(request):
    all_items = List.objects.all()
    context = {'all_items': all_items}
    return render(request, 'home.html', context)


def about(request):
    context = {'myname': 'Bob'}
    return render(request, 'about.html', context)


def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
		all_items = List.objects.all()
		context = {'all_items': all_items}
		return render(request, 'home.html', context)
	else:
		all_items = List.objects.all()
		context = {'all_items': all_items}
		return render(request, 'home.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')