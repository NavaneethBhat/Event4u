from django.template import Context, loader
from manager.models import Event, Role
from django.http import HttpResponse
# from django.core.context_processors import csrf
from django.shortcuts import render_to_response , redirect
from django.template import RequestContext
from django.views.generic.edit import CreateView
from manager.forms import EventForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def NotAuthenticated(request):
	return HttpResponse("Pehle, authentication to karlo bhai:)")

def defineRoll(user,event,a_level):
	""" Create a roll associated with a perticular user """
	# user = User.objects.filter(id = user.pk )
	role_obj = Role(user_id = user.pk,event_id = event.pk, roles = a_level) #(AUTH_LEVELS = a_level)
	role_obj.save()

def EventCreate(request):
	if request.user.is_authenticated():
		if request.method == 'POST': # If the form has been submitted
			event_form = EventForm(request.POST) # A form bound to the POST data
			if event_form.is_valid():
				event_form.event_creator_id = request.user.pk
				new_event = event_form.save()
				# try:
				defineRoll(request.user,new_event,'E')
				# except BaseException as E:
					# return HttpResponse("Something went wrong:(")
				print request.user.pk
				print request.user
				# event_form.
				# m = Role(user_id=,)
				# return HttpResponse("Thanks!!")
				return render_to_response('profile.html') # Redirect after POST
		else:
			event_form = EventForm() # An unbound form

		return render_to_response('event_form.html', {
			'event_form': event_form,
		},context_instance=RequestContext(request))
	
	else:
		return HttpResponse("Pehle, authentication to karlo bhai:)")

def showProfile(request):
	if request.user.is_authenticated():
		event_list = list()
		user_profile = Role.objects.filter(user_id=request.user.pk)
		for role in user_profile:
			eid = role.event_id
			event = Event.objects.get(event_id = eid)
			event = event.event_name
			event_list.append(event.encode("ascii"))
		template = loader.get_template('userprofile.html')
		context = Context({
			'event_list': event_list,
		})
		return HttpResponse(template.render(context))
		
	else:
		return HttpResponse("Pehle, authentication to karlo bhai:)")

