from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    params = {'name': 'Debjit', 'place': 'Earth'}
    return render(req,'index.html',params)

def analyze(req):
    text = req.POST.get('text', 'default')
    removePunc = req.POST.get('removepunc','off')
    fullcaps = req.POST.get('fullcaps', 'off')
    countchar = req.POST.get('countchar', 'off')
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if(removePunc == 'on'):
        res = ""
        for char in text:
            if char not in puncs:
                res += char
        params = {'purpose': 'Removed Punctuations','analyzed_text': res}
        return render(req,'analyze.html',params)
    elif(fullcaps == 'on'):
        res = ''
        for char in text:
            res += char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': res}
        return render(req, 'analyze.html', params)

    elif (countchar == 'on'):
        res = 0
        for char in text:
            if not(char == " "):
                res += 1
        params = {'purpose': 'Count characters', 'analyzed_text': res}
        return render(req, 'analyze.html', params)

    else:
        return HttpResponse('Error')