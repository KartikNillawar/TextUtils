from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index1.html')
#   render(request,filename)

def analyze(request):
    #get the response from html form
    text1 = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepun','off')
    fullcap = request.POST.get('fullcaps','off')
    spaceremover = request.POST.get('spaceremover','off')
    newlineremove = request.POST.get('newlineremove','off')
    countchar = request.POST.get('countchar','off')

    #apply function from the user input

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text1 = analyzed;

    if fullcap=="on":
        analyzed =""
        for char in text1:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'charecter are capatalized', 'analyzed_text': analyzed}
        text1 = analyzed;

    if spaceremover=="on":
        analyzed = ""
        for index,char in enumerate(text1):
            if not(text1[index]==" "and text1[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        text1 = analyzed;

    if newlineremove=="on":
        analyzed = ""
        for char in text1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        text1 = analyzed;

    if countchar=="on":
        count = 0
        for char in text1:
            if char.isalpha():
                count = count + 1
        params = {'purpose': 'Total charecter', 'analyzed_text': count}
        text1 = analyzed;

    if (removepunc != "on" and countchar != "on" and newlineremove != "on" and spaceremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
