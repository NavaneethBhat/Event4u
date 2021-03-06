from django.template import Context, loader
from manager.models import Event, Role, Team, Task
from django.http import HttpResponse
# from django.core.context_processors import csrf
from django.shortcuts import render_to_response , redirect
from django.template import RequestContext
from django.views.generic.edit import CreateView
from manager.forms import EventForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from manager.forms import TaskForm, TeamForm


from django.contrib.auth import logout



def NotAuthenticated(request):
	"""The error module"""
	return HttpResponse("Please log in to view the page.")

def defineRole(user,event,a_level):
	""" Create a Role associated with a perticular user """
	# user = User.objects.filter(id = user.pk )
	role_obj = Role(user_id = user.pk,event_id = event.pk, roles = a_level) #(AUTH_LEVELS = a_level)
	role_obj.save()
	print role_obj.roles

def EventCreate(request):
	"""Event Creation module"""
	if request.user.is_authenticated():
		if request.method == 'POST': # If the form has been submitted
			event_form = EventForm(request.POST) # A form bound to the POST data
			if event_form.is_valid():
				new_event = event_form.save()
				defineRole(request.user,new_event,'E')
				# return render_to_response('add_teams.html') # Redirect after POST
				# return redirect('addTeam', eid = new_event.pk)
				# addTeam(request , event_id = new_event.pk)
				url = "/events/add/"+str(new_event.pk)
				return HttpResponseRedirect(url)

		else:
			event_form = EventForm() # An unbound form

		return render_to_response('event_form.html', {
			'event_form': event_form,
		},context_instance=RequestContext(request))
	
	else:
		return render_to_response('errorpage.html')

def showProfile(request):
	""" Shows an event list with a create event option """
	if request.user.is_authenticated():
		event_dict = dict()  	#create a dictionary of { event primary key : even name }
		user_profile = Role.objects.filter(user_id=request.user.pk)
		for role in user_profile:
			eid = role.event_id
			event = Event.objects.get(event_id = eid)
			event = event.event_name
			event_dict[eid] = event.encode("ascii")
		for event_id in event_dict:
			print event_id , event_dict[event_id]
		template = loader.get_template('userprofile.html')
		context = Context({
			'event_dict': event_dict,
		})
		return HttpResponse(template.render(context))
		
	else:
		return render_to_response('errorpage.html')

def todo(request,team_id): 	#needs fix
	"""The todo processor"""
	items = list()
	if request.user.is_authenticated():
		item = list()
		if request.method== 'POST':
			task_form=TaskForm(request.POST)
			if task_form.is_valid():
				task = task_form.save()
				task.team_id = team_id
				task.save()
				items = Task.objects.filter(team_id = team_id)
				for i in items:
					print i.task_descr , i.team_id
				return render_to_response("todo.html",{'items':items},context_instance=RequestContext(request))
		else:
			autherise_level = Role.objects.filter(roles = 'E' or 'T' )
			my_events = []
			# for user in autherise_level:
			# 	my_events.append(user.event_id)
			items = Task.objects.filter(team_id = team_id)
			for i in items:
				print i.task_descr , i.team_id
			task_form=TaskForm()
		return render_to_response('todo.html',{'task_form':task_form,'items':items},context_instance=RequestContext(request))

	else:
		return render_to_response('errorpage.html')

def addTeam(request , event_id):
	""" A function to add teams to an authenticated user """
	# print "Calles add team"
	default_teams = ['Food','Logistics','Campaigning','Technical']
	if request.user.is_authenticated():	
		print "Calles add team"
		if request.method== 'POST':
			team_form = TeamForm(request.POST)
			if team_form.is_valid():
				try:
					# print team_form.cleaned_data["team_name"]
					event = Event.objects.get(event_id = event_id)
					team = Team(event_id = event.pk)
					team.team_name = team_form.cleaned_data["team_name"]
					team.save()
					return HttpResponse("Kudos!! Teams have been succesfully added!!")
				except BaseException as E:
					print E
					return HttpResponse("Error")
		else:
			team_form = TeamForm()
		return render_to_response('add_teams.html',{'team_form':team_form,'default_teams':default_teams},context_instance=RequestContext(request))

def eventView(request,event_id):
	if request.user.is_authenticated():
		user_role = Role.objects.filter(user=request.user.pk,event=event_id)
		for i in user_role:
			user = i
			break

		if user.roles=='C':
			return HttpResponse("Chief's page")
		elif user.roles=='E':
			return render_to_response("EventManager.html")
		elif user.roles=='T':
			return render_to_response("Teamhead.html")
		elif user.roles=='V':
			return render_to_response("Volunteer.html")
		else:
			print "Role not defined"
			return render_to_response("errorpage.html")
	else:
		return render_to_response('errorpage.html')

def addTask(request):
	if request.user.is_authenticated():
		autherise_level = Role.objects.filter(roles = 'E' or 'T')
		my_events = []
		for user in autherise_level:
			my_events.append(user.event_id)
		print my_events
		return HttpResponse("")

def view_teams(request,event_id):
	if request.user.is_authenticated():
		uid = request.user.pk
		eid = event_id
		teams = Team.objects.filter(event_id = eid)
		for team in teams:
			print team.team_name
		return render_to_response('teams_view.html',{'teams':teams , 'event_id':eid},context_instance=RequestContext(request))


	else:
		return render_to_response('errorpage.html')

def logout_view(request):
    logout(request)
    return HttpResponse("Logged out")