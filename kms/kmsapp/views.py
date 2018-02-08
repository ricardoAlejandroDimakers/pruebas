# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def Index(request):
	return render(request,'kmsapp/index.html')

def Formulario(request):
	return render(request,'kmsapp/formulario.html')
