from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import Schedule, Discussion
from cms.forms import ScheduleForm, DiscussionForm
from django.views.generic.list import ListView


def schedule_list(request):
    # list of schedule
    schedules = Schedule.objects.all().order_by('id')
    return render(request,
                  'cms/schedule_list.html',  # html template
                  {'schedules': schedules})  # data which will be sent to template


def schedule_edit(request, schedule_id=None):
    # edit schedule
    if schedule_id:  # schedule_id is defined(modified)
        schedule = get_object_or_404(Schedule, pk=schedule_id)
    else:  # schedule_id is not defines(added)
        schedule = Schedule()

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)  # make a form from POST request data.
        if form.is_valid():  # check if it is valid
            schedule = form.save(commit=False)
            schedule.save()
            return redirect('cms:schedule_list')
    elif request.method == "GET":
        form = ScheduleForm(instance=schedule)  # make a form from schedule instance

    return render(request, 'cms/schedule_edit.html', dict(form=form, schedule_id=schedule_id))


def schedule_del(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return redirect('cms:schedule_list')


class DiscussionList(ListView):
    context_object_name = 'discussions'
    template_name = 'cms/discussion_list.html'
    paginate_by = 5  # max paging = 5

    def get(self, request, *args, **kwargs):
        schedule = get_object_or_404(Schedule, pk=kwargs['schedule_id'])  # read schedule as parent
        discussions = schedule.discussions.all().order_by('id')  # read discussion as child
        self.object_list = discussions

        context = self.get_context_data(object_list=self.object_list, schedule=schedule)
        return self.render_to_response(context)


def discussion_del(request, schedule_id, discussion_id):
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    discussion.delete()
    return redirect('cms:discussion_list', schedule_id=schedule_id)


def discussion_edit(request, schedule_id, discussion_id=None):
    schedule = get_object_or_404(Schedule, pk=schedule_id)  # read schedule as a parent
    if discussion_id:  # discussion_id is defined (modify)
        discussion = get_object_or_404(Discussion, pk=discussion_id)
    else:  # discussion_id is not defined (adding)
        discussion = Discussion()

    if request.method == 'POST':
        form = DiscussionForm(request.POST, instance=discussion)  # make a form from request data
        if form.is_valid():  # check if it is valid
            discussion = form.save(commit=False)
            discussion.schedule = schedule  # set schedule as parent
            discussion.save()
            return redirect('cms:discussion_list', schedule_id=schedule_id)
    else:  # GET
        form = DiscussionForm(instance=discussion)  # make a form from discussion instance

    return render(request,
                  'cms/discussion_edit.html',
                  dict(form=form, schedule_id=schedule_id, discussion_id=discussion_id))
