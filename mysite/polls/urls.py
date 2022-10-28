from django.urls import path
from . import views
# This is where linking happens....
urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('createcard', views.createcard, name="createcard"),
    #path('(?P<question_id>[0-9]+)/$',views.detail, name="detail"),
    #path('(?P<question_id>[0-9]+)/results$',views.results, name="results"),
    #path('(?P<question_id>[0-9]+)/vote$',views.vote, name="vote"),
    #path('(?P<question_id>[0-9]+)/edit$',views.edit, name="edit"),
    ]
app_name = 'polls'

# We define how the URL should be
# As per that HttpResquest is triggered with appropriate value.
# Then using that in view , appropriate function is called , value is passed &
# Response as HttpResponse.
'''
^$ - dont add anything to a url
Understand the above as : ^ - Include
                          $ - nothing
i.e. 127.0.0.1/polls/---
Do not write anything after polls/
let it remain as 127.0.0.1/polls/

2nd parameter - What to display.
Views.index - display whatever there in index.

3rd parameter - Name of URL | Basically searches function of name index
    with imported view content
--------------------------------------------------------
Expln:- DETAIL | initializing a URL
r'^(?P<question_id>[0-9]+)/$
?P - Represent string
Represented string = <question_id>[0-9] value range from 0-9 then end.
eg: 127.0.0.1/polls/2 or 1 or 9 etc...

Expln:- RESULTS | initializing a URL
r'^(?P<question_id>[0-9]+)/results$
?P - Represent string
Represented string = <question_id>[0-9] value range from 0-9 then end.
eg: 127.0.0.1/polls/2/results

Expln:- VOTE | initializing a URL
r'^(?P<question_id>[0-9]+)/vote$
?P - Represent string
Represented string = <question_id>[0-9] value range from 0-9 then end.
eg: 127.0.0.1/polls/2/vote

'''

