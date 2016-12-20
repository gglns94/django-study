# django-study

# Django Tutorial
*Part 3*

```python
  from django.http improt HttpResponse
  from django.template import loader

  template = loader.get_template('polls/index.html')
  context = {'key' : value}
  response = HttpResponse(template.render(context, request))
  
  return response
```

```python
  from django.shortcuts import render
  
  ...

  response = render(request, 'polls/index.html', context) 
  return response
```

```python
  from django.http import Http404
  from django.shortcuts import render
  
  ...

  try:
    question = Question.objects.get(pk=question_id)
  except:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'question':question})

```

```python
  from django.shortcuts import get_object_or_404

  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls.detail.html', {'question' : question})
```

```html
  <li><a href="{% url 'detail' question.id %}></a></li>
  <li><a href="{% url 'polls:detail' question.id %}</a></li>
```

