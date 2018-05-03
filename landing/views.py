from django.shortcuts import render
from .forms import ClientForm
# Create your views here.
def index(request):
    form = ClientForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'landing/index.html', locals())