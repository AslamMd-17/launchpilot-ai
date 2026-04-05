from django.shortcuts import render ,redirect
from .models import Analysis
def index(request):
    if request.method == 'POST':
        idea = request.POST.get('idea')
        industry = request.POST.get('industry' , ' ')

        analysis = Analysis.objects.create(
            idea = idea ,
            industry = industry,
            status = 'pending'
        )
        return redirect(f'/result/{analysis.id}/')
    return render(request, 'index.html')

def result(request, analysis_id):
    analysis = Analysis.objects.get(id = analysis_id)
    return render(request , 'result.html' , {'analysis':analysis})