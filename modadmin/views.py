from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Function, JobPosition, Department


class IndexView(generic.ListView):
    template_name = 'modadmin/index.html'
    context_object_name = 'latest_department_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Department.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Department
    template_name = 'modadmin/detail.html'
    def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Department.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Department
    template_name = 'modadmin/results.html'


def vote(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    try:
        selected_function = department.function_set.get(pk=request.POST['function'])
    except (KeyError, Function.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'modadmin/detail.html', {
            'department': department,
            'error_message': "You didn't select a function.",
        })
    else:
        selected_function.votes += 1
        selected_function.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('modadmin:results', args=(department.id,)))