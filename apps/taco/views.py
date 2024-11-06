# apps/taco/views.py
import os

from django.shortcuts import render
from django.http import JsonResponse
import requests
from .forms import TacoForm
from djangoProject1.settings import ENDPOINT_BACK

def taco_view(request):
    if request.method == 'POST':
        form = TacoForm(request.POST)
        if form.is_valid():
            param = form.cleaned_data['param']
            amount = form.cleaned_data['amount']
            endpoint = f"{ENDPOINT_BACK}/taco/taco/{param}/{amount}/"
            token = os.getenv('TOKEN_TEMP')
            headers = {
                'Authorization': f'Bearer {token}'
            }

            response = requests.get(endpoint, headers=headers)
            data = response.json()
            return JsonResponse(data)
    else:
        form = TacoForm()
    return render(request, 'taco/taco_form.html', {'form': form})