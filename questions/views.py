# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View
from django.shortcuts import render
from .forms import AddQuestionForm, AddAnswerForm
from .models import Question, Answer
from django.http.response import HttpResponse
from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin



class AddQuestionView(LoginRequiredMixin, CreateView):
    template_name = 'add_question.html'
    model = Question
    form_class = AddQuestionForm

    def form_valid(self, form):
        form.instance.asked_by = self.request.user
    	form.save()
        return HttpResponse('Question is added')

    def form_invalid(self, form):
    	return HttpResponse('Question format is invalid')

#    def get_form_kwargs(self):
#    	kwargs = super(AddQuestionView, self).get_form_kwargs()
#    	kwargs['asked_by'] = self.request.user


class AddAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AddAnswerForm

    def form_valid(self, form):
        form.instance.answered_by = self.request.user
        form.save()
        return HttpResponse('Answer is added')

    def form_invalid(self, form):
        print form.errors
        return HttpResponse('Answer is invalid')

class ListQuestionsView(AjaxResponseMixin, JSONResponseMixin, ListView):
    template_name='ListQuestions.html'
    paginate_by = '9'

    def get_object(self):
        return question

    def get_queryset(self):
        return Question.objects.all()

    def get_ajax(self, *args, **kargs):
        qset = self.get_queryset()
        json_dict = list(qset.values('id', 'question', 'category', 'asked_by'))
        return self.render_json_response(json_dict)

class QuestionView(View):

    def get_answer_set(self, question):
        return Answer.objects.filter(answer_to = question)

    #Give the question and its respective answers.
    def get(self, request, *args, **kwargs):
        question_id = request.GET['question_id']
        question = Question.objects.get(id=question_id)
        answers = self.get_answer_set(question)
        print answers
        context = {'questionObj' : question, 'answersObj': answers}
        return render(request, 'questionview.html', context)

    

