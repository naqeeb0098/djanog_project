from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # context basicaly hum ny ik dictionary create ki hy agar hum ny poython sy html k andar direct value pass karwani ho koi
    context = {
        'variable1':'helo this is naqeeb card1 is here',
        'variable2':'helo tis is me card no 2 is here'
        
    }
    return render(request,'index.html',context)
    # return HttpResponse("the is index page")

def about(request):
    return HttpResponse("the is about page")

def services(request):
    return HttpResponse("the is services page")

def contact(request):
    return HttpResponse("the is contact page")