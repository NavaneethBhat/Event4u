from manager import models
from django.forms import ModelForm

# class Event(models.Model):
#     event_name = forms.CharField(max_length=20)
#     event_descr = forms.CharField(max_length=70)
#     venue = forms.CharField(max_length=70)
#     budget = forms.DecimalField(max_digits=20,decimal_places=10)
# 	def __unicode__(self):
# 		return self.event_name

class EventForm(ModelForm):
	class Meta:
		model = models.Event
		exclude = ('event_id',)

class TeamForm(ModelForm):
	class Meta:
		model = models.Team
		exclude = ('team_id','event_id',)
