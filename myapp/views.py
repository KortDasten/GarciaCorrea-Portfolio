# myapp/views.py
from django.shortcuts import render
# from .models import Profile # 🔴 Kailangan i-import ang Profile model

def home(request):
    # 🔴 Kinukuha ang lahat ng profile records (Garcia at Correa) mula sa database
    # profiles = Profile.objects.all()
    
    # Ipinapasa ang data (profiles) sa template
    # context = {'profiles': profiles}
    
    # Tiyakin na ang template name ay tama (sps_portfolio.html o home.html)
    return render(request, 'home.html', {})