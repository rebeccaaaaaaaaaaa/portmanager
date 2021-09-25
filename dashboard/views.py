from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def listProjects(request):
        if not request.user.is_authenticated:
         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        else:
         return render(request, 'dashboard/list.html')

