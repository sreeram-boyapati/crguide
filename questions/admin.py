from django.contrib import admin
from .views import Question, Answer

class AnswerAdmin(admin.ModelAdmin):
	list_display = ['answer', 'answer_to', 'answered_by']
	search_fields = ['answer_to', 'answered_by']
	list_filter = list_display[1:]

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question', 'category', 'asked_by')
	search_fields = ('asked_by', 'category')
	list_filter = ('category', 'asked_by')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)