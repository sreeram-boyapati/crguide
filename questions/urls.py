from django.conf.urls import patterns, include, url
from .views import AddQuestionView, ListQuestionsView, QuestionView
urlpatterns = patterns('',
		url('^addquestion', AddQuestionView.as_view(), name='add_question'),
		url('^listquestions', ListQuestionsView.as_view(), name='list_question'),
		url('^questionview', QuestionView.as_view(), name='question'),
	)