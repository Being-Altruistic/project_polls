from django.shortcuts import render, get_object_or_404, redirect
# It's like a database that manages VIEWS as per HTML.
# Create your views here.
from django.http import HttpResponse
from . models import Question

def home(request):
    latest_questions = Question.objects.get()
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/home.html', context)


def index(request):
    return render(request,'polls/index.html')
'''
Expla:- getting all questions object only 5 rows & sorting ( *NOTE: if an attribute has '-' as preceeding char, then
        the sorting pattern will be latest 1st approach else vice versa. i.e. sorting by old 1st approach.
'''
'''
def detail(request ,  question_id):
    # returns a row
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html',{'question':question})
def results(request ,  question_id):
    return HttpResponse('These are the results of the question: %s' % question_id)
def vote(request ,  question_id):
    return HttpResponse('Vote on question: %s' % question_id)
'''
def createcard(request):
    return render(request,'polls/createcard.html')