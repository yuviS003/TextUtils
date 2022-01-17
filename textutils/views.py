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

    # check which checkbox values is on
    if removepunc=="on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext=analyzed
    if newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char !='\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        params={'purpose':'Removed all the spaces','analyzed_text':analyzed}
        djtext=analyzed
    if charcount=='on':
        analyzed=0
        for char in djtext:
            if not(char==' '):
                analyzed=analyzed+1
        params={'purpose':'The number of characters are','analyzed_text':analyzed}
    if (removepunc!="on" and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on'and charcount!='on'):
        return HttpResponse("ERROR")
    else:
        return render(request, 'analyze.html', params)