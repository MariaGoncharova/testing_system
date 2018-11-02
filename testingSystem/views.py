from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def post_list(request):
    return render(request, 'testingSystem/post_list.html', {})


# Create your views here.
