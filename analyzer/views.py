from django.shortcuts import render, redirect
from .models import Analysis
from .orchestrator import run_agents

def index(request):
    if request.method == 'POST':
        idea = request.POST.get('idea')
        industry = request.POST.get('industry', '')

        analysis = Analysis.objects.create(
            idea=idea,
            industry=industry,
            status='pending'
        )

        run_agents(analysis.id)
        return redirect(f'/result/{analysis.id}/')

    return render(request, 'index.html')


def result(request, analysis_id):
    analysis = Analysis.objects.get(id=analysis_id)
    result_data = analysis.get_result()
    return render(request, 'result.html', {
        'analysis': analysis,
        'result': result_data
    })