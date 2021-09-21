from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ProjectForm
from django.contrib import messages
import datetime

from .models import Project

@login_required
def projectList(request):
    return render(request, 'portifolio/list.html')