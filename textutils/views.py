# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>Rahul </h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry">Youtube</a>''')
# def about(request):
#     return HttpResponse("about")



def index(request):
    # dictionary = {'name':'Rahul','profession': 'software engineer '}
    # return HttpResponse('''Home page''')
    # return render(request, 'index.html',dictionary)
    return render(request,'index.html')

# def removepunc(request):
#     # Get the text
#     djtext=request.GET.get('text','default')
#     # analyze the text
#     #it returns the text which values are you filled in name='text'. it means you fill the values in the textarea block.
#     print(djtext)
#     return HttpResponse('''Remove punch ''')

# def capfirst(request):
#     return HttpResponse('''Capitalize First Letter''')
# def newlineremove(request):
#     return HttpResponse('''newlineremove''')
# def spaceremove(request):
#     return HttpResponse('''spaceremove''')
# def charcount(request):
#     return HttpResponse('''charcount''')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newineremover = request.POST.get('newineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charCount = request.POST.get('charCount','off')
    print(removepunc)
    counter = 0
    if removepunc =='on' or extraspaceremover =='on' or charCount =='on' or fullcaps=='on' or newineremover=='on':
        if removepunc == 'on':
             analyzed =""
             punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
             for char in djtext:
                 if char not in punctuations:
                   analyzed = analyzed +  char 
             djtext=analyzed 
             params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed  ,'count_Characters': len(analyzed)}
            #  return render(request,'analyze.html', params)
        if fullcaps == 'on':
            analyzed =""
            for char in djtext:
                    analyzed = analyzed + char.upper()
            params = {'purpose': 'Changed to UpperCase','analyzed_text': analyzed  ,'count_Characters': len(analyzed)}
            djtext=analyzed
            # return render(request,'analyze.html', params)
        if newineremover == 'on':
            analyzed =""
            for char in djtext:
                if char == '\n' or char=='\r':
                    analyzed = analyzed +''
                else:
                    analyzed = analyzed + char
            params = {'purpose': 'Remove New Line','analyzed_text': analyzed ,'count_Characters': len(analyzed)}
            djtext=analyzed
            # return render(request,'analyze.html', params)
        if extraspaceremover == 'on':
            analyzed =""
            djtext = djtext.strip()
            for index, char in enumerate(djtext):
                if (char ==' ' and djtext[index-1]==' '):
                    continue
                else:
                    analyzed = analyzed + char
            djtext=analyzed
            params = {'purpose': 'Remove Extra Space','analyzed_text': analyzed,'count_Characters': len(analyzed)}
        params = {'purpose': 'Correct String','analyzed_text': analyzed,'count_Characters': len(djtext)}    
        return render(request,'analyze.html', params)
    else:
        return HttpResponse("Error")