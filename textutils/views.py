# I have created this file - Anish
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
# Get the text
    djtext=request.POST.get('text','default')

# Check checkbox values
    removepunctuation = request.POST.get('removepunctuation','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countchar = request.POST.get('countchar','off')

# Check which checkbox is on
    if removepunctuation== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed

# Analyze the text
        # return render(request,'analyze.html', params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
             if not (djtext[index] == " " and djtext[index + 1] == " "):
                 analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunctuation != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and countchar != "on"):
        return HttpResponse("Please select the Operation!")

    return render(request, 'analyze.html', params)