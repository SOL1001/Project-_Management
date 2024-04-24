from django.shortcuts import render
from .models import ProjectUpload
def home(request):
    projectUploads = ProjectUpload.objects.all()

    context = {
         'projectUploads' : projectUploads
    }
    return render(request, 'home.html', context)
def join(request):
     return render(request, 'join.html', {})

def searchbar(request):
     if request.method == 'GET':
          query= request.GET.get('query')
          if query:
               projectUploads = ProjectUpload.objects.filter( areaOfStudy__icontains=query)
               return render(request, 'searchbar.html',{'projectUploads': projectUploads})
          else:
               print("No information found")
               return render(request, 'searchbar.html', {})