from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     param = {'name':'Osama', 'Countary':'Nepal'}
#     return render(request,'index.html' , param)
#     # return HttpResponse( "Hellow G") 

# def about(request):
#     djtext = request.GET.get('text','defult')
#     analyze = djtext
#     if len(djtext)<5:
#         prams = {'disc':'Tu bahut Alsi Haire baba tere se nahi hoga tu nikal'}
#         return render(request,'about.html',prams)
#     else:
#         param = {'name':'osama', 'count':len(djtext), 'Countary':analyze}
#         return render(request,'about.html' , param)
        
        
    # return HttpResponse('''<a href="/">Back</a>''' )