from datetime import datetime
from django.shortcuts import render

def page(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'index.html', {'current_time': current_time})

