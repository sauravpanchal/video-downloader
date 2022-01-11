from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print("home")
    return render(request, "index.html")

def get_video(request):
    # # return HttpResponse("<script>alert('Hii')</script>")
    # return render(request, "index.html")
    if request.POST["inputPLATFORM"] == "YouTube":
        
        from pytube import YouTube

        link = request.POST["inputURL"]
        path = "C:\\Users\\Public"
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(path)
    else:
        return HttpResponse("<h1>Twitter Downloads will be available soon !</h1>")
    # return HttpResponse("<h1>Video Downloaded, Successfully !</h1> <br> <h3>Path: C:\\Users\\Public</h3>")
    return render(request, "get_video.html")
