from django.shortcuts import render
import requests
import sys
import os
from subprocess import run, PIPE
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Create your views here.
def home(request):
    return render(request, 'home.html')

def output(request):
    inp = request.POST.get('textinput')
    out = run([sys.executable, os.path.join(BASE_DIR, 'external\\chat_bot.py'), inp],shell=False,stdout=PIPE)
    var = str(out.stdout)
    var = var[2:-5]
    #{'data':out.stdout}
    return render(request, 'home.html', {'data': var} )