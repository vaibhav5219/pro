from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}       
        return render(request, 'game/index.html',data)
    return render(request, 'game/index.html')

def home2(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}                    
        return render(request, 'game/index2.html',data)
    return render(request, 'game/index2.html')

def home3(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}                    
        return render(request, 'game/index3.html',data)
    return render(request, 'game/index3.html')

def home4(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}                    
        return render(request, 'game/index4.html',data)
    return render(request, 'game/index4.html')

def home5(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}                    
        return render(request, 'game/index5.html',data)
    return render(request, 'game/index5.html')

def home6(request):
    if request.method=="POST":
        result =int( request.POST['result'] )
        i=j=k=[1,2,3,4,5,6,7,8,9]
        data={"a":i, "b":j,"c":k, 'result':result}                    
        return render(request, 'game/index6.html',data)
    return render(request, 'game/index6.html')