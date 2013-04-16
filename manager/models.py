from django.db import models
# from allauth.utils import get_user_model
from django.contrib.auth.models import User

# Create your models here.
# User model to be used by get_user_model

# class User(models.Model):
# 	"""Represents the User table for Event4u"""
# 	user_id = models.AutoField(primary_key=True)
# 	user_name = models.CharField(max_length=25)


class Event(models.Model):
	"""Represents the Events table for Event4u"""
	event_id = models.AutoField(primary_key=True)
	event_name = models.CharField(max_length=30)
	event_descr = models.CharField(max_length=75)
	# event_creator_id = models.ForeignKey(User , default = -1)
	venue = models.CharField(max_length=70)
	budget = models.DecimalField(max_digits=20,decimal_places=10)

	def __unicode__(self):
		return unicode(self.event_name)

class Team(models.Model):
	"""Represents the Teams of actors of Event4u"""
	team_id = models.AutoField(primary_key=True)
	event_id = models.ForeignKey(Event)
	team_name = models.CharField(max_length=15)
	
	def __unicode__(self):
		return unicode(self.team_id)


class Task(models.Model):
	"""Task to be accomplished by Teams of Event4u"""
	task_id = models.AutoField(primary_key=True)
	team_id = models.ForeignKey(Team)
	STATS = (
		(u'D',u'Done'),
		(u'I',u'In progress'),
		(u'N',u'Not Started')
		)
	status = models.CharField(max_length=10,choices=STATS,default=u'Not Started')
	task_descr = models.TextField()

	def __unicode__(self):
		return unicode(self.task_id)

class Role(models.Model):
	"""Represents the Roles played by actors of Event4u"""
	role_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,default=-1)
	event = models.ForeignKey(Event,default=-1)
	team = models.ForeignKey(Team,default=0) 			#0 for Event manager,employee
	AUTH_LEVELS = (
		(u'C',u'chief'),
		(u'E',u'event_head'),
		(u'T',u'team_head'),
		(u'V',u'volunteer')
		)
	roles = models.CharField(max_length = 10,choices=AUTH_LEVELS)

	def __unicode__(self):
		return unicode(self.role_id)
# class Authorise(models.Model):
	# """Levels pf authorisation constant"""
	# root = 
