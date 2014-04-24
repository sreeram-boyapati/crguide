from django.conf.urls import patterns, include, url
from .views import AddQuestionView, ListQuestionsView, QuestionView, AddAnswerView, EditQuestionView
urlpatterns = patterns('',
		url(r'^addquestion', AddQuestionView.as_view(), name='add_question'),
		url(r'^addanswer', AddAnswerView.as_view(), name='add_answer'),
		url(r'^listquestions', ListQuestionsView.as_view(), name='list_question'),
		url(r'^questionview', QuestionView.as_view(), name='question'),
		url(r'^updatequestion/(?P<id>\d+)/$', EditQuestionView.as_view(), name="Edit Question"),
	)