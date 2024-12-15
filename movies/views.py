from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'movies/index.html',{})

def about(request):
    contex={'movies':['Gladiatot','Topgun','Casino Royale']}
    return render(request,'movies/about.html',contex)
    # return render(request,'movies/about.html',{'movie':'Gladiatot'})