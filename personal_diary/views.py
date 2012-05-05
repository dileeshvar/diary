#from django.template import context, loader
from django.template import RequestContext
from personal_diary.models import Diary
from django.shortcuts import render_to_response,redirect
from django.utils import timezone

def home(request):
	if request.method == 'POST':
		diary_task = Diary(to_do_task=request.POST['task'], task_date = timezone.now())
		diary_task.save()
		return render_to_response('personal_diary/home.html',{'qualified_uri' : request.get_host(), 'message' : 'Task Added Successfully'},context_instance=RequestContext(request))
	else :
		return render_to_response('personal_diary/home.html',{'qualified_uri' : request.get_host()},context_instance=RequestContext(request))

def tasks(request):
	tasks_list = Diary.objects.all().order_by('-task_date')
	return render_to_response('personal_diary/tasks.html', {'tasks_list': tasks_list})
