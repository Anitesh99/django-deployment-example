from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hey dude!','number':100}
    return render(request,'first_app/index.html',context_dict)

def other(request):
    return render(request,'first_app/other.html')

def tagger(request):
    return render(request,'first_app/url_tagging.html')

