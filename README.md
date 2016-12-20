# django-study

# Django Tutorial
* Part 3 *
'''python
  from django.http improt HttpResponse
  from django.template import loader

  template = loader.get_template('polls/index.html')
  context = {'key' : value}
  response = HttpResponse(template.render(context, request))
  
  return response
'''

'''python

  from django.shortcuts import render
  
  ###
  
  response = render(request, 'polls/index.html', context) 
  return response
'''
