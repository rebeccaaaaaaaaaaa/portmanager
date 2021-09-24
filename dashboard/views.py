from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def listProjects(request):
        return render(request, 'dashboard/list.html')

