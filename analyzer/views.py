from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Analysis
from .orchestrator import run_agents
import threading

def index(request):
    if request.method == 'POST':
        idea = request.POST.get('idea')
        industry = request.POST.get('industry', '')

        analysis = Analysis.objects.create(
            idea=idea,
            industry=industry,
            status='pending'
        )

        thread = threading.Thread(target=run_agents, args=(analysis.id,))
        thread.start()

        return redirect(f'/loading/{analysis.id}/')

    return render(request, 'index.html')


def loading(request, analysis_id):
    analysis = Analysis.objects.get(id=analysis_id)
    return render(request, 'loading.html', {'analysis': analysis})


def status(request, analysis_id):
    analysis = Analysis.objects.get(id=analysis_id)
    return JsonResponse({'status': analysis.status})


def result(request, analysis_id):
    analysis = Analysis.objects.get(id=analysis_id)
    result_data = analysis.get_result()
    return render(request, 'result.html', {
        'analysis': analysis,
        'result': result_data
    })

def history(request):
    analyses = Analysis.objects.all().order_by('-created_at')
    return render(request, 'history.html', {'analyses': analyses})