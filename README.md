# django-study

# Django Tutorial
*Part 3: models and admin*

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
  <li><a href="{% url 'detail' question.id %}"></a></li>
  <li><a href="{% url 'polls:detail' question.id %}"</a></li>
```
*Part 4: forms*

```html
<h1>{{question.question_text}}</h1>
{% if error_message %} {{ error_message }} {% endif %}

```

*Part 5: Testing*

```python

# in polls/test.py
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

``

```shell
python manage.py test polls
````
