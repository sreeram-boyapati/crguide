from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,Textarea
from offices.models import Office


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'category')

    def __init__(self, *args, **kwargs):
        super(AddQuestionForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Office.objects.all())

class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', )
        widgets = {
            'answer' : Textarea(attrs={'cols': 80, 'rows': 10})
        }

class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'category')

    def __init__(self, *args, **kwargs):
        self.fields['question'].required = True
        self.fields['category'].required = True
