from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . models import Question

def index(request):
    latest_question=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question':latest_question}
    return render(request,'polls/index.html',context)
def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
def votes(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/details.html',{"question":question,"error_message":"Please select a choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results",args={question.id}))