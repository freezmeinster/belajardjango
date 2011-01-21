from django.http import HttpResponse,Http404
from belajardjango.pools.models import Poll
from django.shortcuts import render_to_response

def index(request):
    latest = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('pools/index.html',{'latest' : latest})

def detail(response,pool_id):
    try : 
        p = Poll.objects.get(pk=pool_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('pools/detil.html',{'poll' : p})
    

def results(request,pool_id):
    return HttpResponse('Anda sedang melihat pool dengan id %s' % pool_id)

def vote(request,pool_id):
    return HttpResponse('Anda akan melakuka vote untuk %s ' % pool_id)
