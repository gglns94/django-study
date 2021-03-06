from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

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
  try:
    question = Question.objects.get(pk=question_id)
  except:
    raise Http404("Question does not exist")
  # return HttpResponse("You're looking at question %s" % question_id);
  response = render(request, 'polls/detail.html', {'question': question})
  return response

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return HttpResponse(render(request, 'polls/results.html', {'question': question}))

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice"
    })
  else:
    selected_choice.votes += 1
    selected_choice.save();
  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
  # return HttpResponse("You're voting on question %s" % question_id)
  
