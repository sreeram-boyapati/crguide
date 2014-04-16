# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import ListView
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
        json_dict = list(qset.values('question', 'category', 'asked_by'))
        return self.render_json_response(json_dict)

