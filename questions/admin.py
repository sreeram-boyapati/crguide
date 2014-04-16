from django.contrib import admin
from .views import Question, Answer


admin.site.register(Question)
admin.site.register(Answer)