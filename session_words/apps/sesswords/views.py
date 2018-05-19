from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
  # the index function is called when root is visited
def index(request):
    context = {
        'time': strftime("%I: %M %p, %Y-%m-%d ", gmtime())
    }
    
    return render(request, 'sesswords/index.html', context)

def addword(request):
    if request.method == "POST":
        if not 'info' in request.session:
            request.session['info'] = []
        if not 'font' in request.POST:
            request.session['font'] = ''
        else:
            request.session['font'] = 'big'
        request.session['word'] = request.POST['word']
        request.session['color'] = request.POST['color']
        request.session['info'].append((request.session['color'], request.session['font'], request.session['word']))
        return redirect ('/session_words')



def clear(request):
    request.session.clear()
    return redirect('/session_words')