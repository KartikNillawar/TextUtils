from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index1.html')
#   render(request,filename)

def analyze(request):
    text1 = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepun','off')
    fullcap = request.GET.get('fullcaps','off')
    spaceremover = request.GET.get('spaceremover','off')
    newlineremove = request.GET.get('newlineremove','off')
    countchar = request.GET.get('countchar','off')

    print(removepunc)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcap=="on":
        analyzed =""
        for char in text1:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'charecter are capatalized', 'analyzed_text': analyzed}
        return  render(request,'analyze.html',params)
    elif spaceremover=="on":
        analyzed = ""
        for index,char in enumerate(text1):
            if not(text1[index]==" "and text1[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        return  render(request,'analyze.html',params)
    elif newlineremove=="on":
        analyzed = ""
        for char in text1:
            if char:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif countchar=="on":
        count = 0
        for char in text1:
            if char.isalpha():
                count = count + 1
        params = {'purpose': 'Total charecter', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
