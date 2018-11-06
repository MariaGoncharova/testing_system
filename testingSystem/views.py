from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from testingSystem.models import Test


def tests(request):
    tests = Test.objects.all()
    return render(request, 'testingSystem/base.html', {'tests': tests})


