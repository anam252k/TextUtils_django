# created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    # check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
            djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (fullcaps=="on"):
        analyzed=""

        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (newlineremover=="on"):
        analyzed=""

        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        
        params = {'purpose':'Remove newlines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (extraspaceremover=="on"):
        analyzed=""

        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        
        params = {'purpose':'Remove newlines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (charcount=="on"):
        analyzed=0

        for char in djtext:
            if char in djtext:
                analyzed=analyzed+1
        
        params = {'purpose':'Remove newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
    