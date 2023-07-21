from django.shortcuts import render
from datetime import datetime, date

def index(request):
    context = {
        'name': 'John Doe',
        'day': str(date.today()) + datetime.now().strftime('%H-%M-%S-%f')
        
    }
    return render(request, 'jinja/index.html', context)