from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # output = ', '.join([q.question_text for q in latest_question_list])
  # template = loader.get_template('polls/index.html');
  context = {
    'latest_question_list': latest_question_list
  }
  response = render(request, 'polls/index.html', context)
  # return HttpResponse(template.render(context, request));
  return response

def detail(request, question_id):
  return HttpResponse("You're looking at question %s" % question_id);

def results(request, question_id):
  response = "You're looking at the results of question %s"
  return HttpResonse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s" % question_id)


  