from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')
def analyze(request):
    # Get text and options from the request
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')  # Added this line to fetch newlineremover

    if removepunc == "on":
        # Define the set of punctuations
        punctuations = '''.,?!:;'\"()[]{}…—-/_@&*^~|='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        param = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif newlineremover == "on":
        # Process for newline removal
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":  # Remove newline and carriage return
                analyzed += char.upper()
        param = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    else:
        return HttpResponse("Error: No valid option selected.")


def capfirst(request):
    return HttpResponse("capitalize first")
def spaceremove(request):
    return HttpResponse("remove spece <a href='/'>Back</a>")