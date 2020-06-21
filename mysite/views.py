from django.shortcuts import render

def index(request):
    return render(request,"mysite/index.html")

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcaps','default')
    newlineremover=request.POST.get('newlineremover','default')
    extraspaceremover=request.POST.get('extraspaceremover','default')
  
    
    if(removepunc == "on"):
        analyzed = ""
        punctuation="!#%"
        
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char.upper()

        params={"purpose":"Remove Punctuation","analyzetext":analyzed}
        
        return render(request,"mysite/analyze.html",params)

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="/n":
                analyzed = analyzed +char.upper()
        
        params={"purpose":"Remove new line","analyzetext":analyzed}
        return render(request,"mysite/analyze.html",params)
        


    elif(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext [index+1]==" "):
                analyzed = analyzed + char
        params={"purpose":"Remove new line","analyzetext":analyzed}
        return render(request,"mysite/analyze.html",params)
        


               
