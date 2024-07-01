from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

def all_chai(request):
    chai_data = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais' : chai_data})

def chai_detail(request, chai_id):
    
    chai = get_object_or_404(ChaiVarity, pk =chai_id)
    return render(request, 'chai/chai_detail.html', {'chai' : chai})