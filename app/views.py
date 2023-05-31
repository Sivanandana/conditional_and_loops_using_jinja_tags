from django.shortcuts import render
def condition(request):
    d={'name':'siva','a':200,'b':30,'c':15}
    return render(request,'condition.html',d)


# Create your views here.
