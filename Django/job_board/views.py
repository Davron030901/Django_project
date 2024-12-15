from django.shortcuts import render,get_list_or_404
from .models import JobPosting
# Create your views here.
def index(request):
    # job=JobPosting.objects.all()
    active_posting=JobPosting.objects.filter(is_active=True)
    contex={
        'job_posting':active_posting
    }
    # print(job)
    return render(request,'job_board/index.html',contex)

def job_detail(request,pk):
    job_posting=JobPosting.objects.get(pk=pk)
    # job_posting=get_list_or_404(JobPosting,pk=pk,is_active=True)
    context={
        'posting':job_posting
    }
    return render(request,'job_board/deteil.html',context)