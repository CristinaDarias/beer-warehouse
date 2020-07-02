# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def beer_list_view(request):
    context = {
        'sample_var': 'ejemplo'
    }

    return render(request, 'beers.html', context)


def beer_detail_view(request):
    context = {
        'sample_var': 'ejemplo'
    }

    return render(request, 'beers.html', context)
