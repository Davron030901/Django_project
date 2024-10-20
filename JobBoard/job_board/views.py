from django.shortcuts import render,get_object_or_404
from .models import JobPosting

def index(request):
    # jobs = JobPosting.objects.all()
    # jobs = JobPosting.objects.filter(is_active=True)
    # print(jobs)
    active_postings=JobPosting.objects.filter(is_active=False)
    context={
        "job_postings":active_postings
    }
    return render(request,'job_board/index.html',context)

def job_detail(request, pk):
    # job_posting=JobPosting.objects.get(pk=pk)
    job_posting=get_object_or_404(JobPosting, pk=pk,is_active=False)
    context={
        "posting":job_posting
    }
    return render(request,"job_board/detail.html",context)
