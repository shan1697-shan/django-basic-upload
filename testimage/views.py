from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        caption = request.POST.get('caption','')
        image = request.FILES.get('image','')
        # print(caption, image)
        img = Imageupload(caption=caption, image=image)
        img.save()
        return render(request, 'testimage/index.html')
    data = Imageupload.objects.all()
    pdata = [{"image":i.image,"caption":i.caption} for i in data]
    return render(request, 'testimage/index.html', {"data":data})