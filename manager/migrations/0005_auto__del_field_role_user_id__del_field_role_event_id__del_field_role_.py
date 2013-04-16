# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Role.user_id'
        db.delete_column(u'manager_role', 'user_id_id')

        # Deleting field 'Role.event_id'
        db.delete_column(u'manager_role', 'event_id_id')

        # Deleting field 'Role.team_id'
        db.delete_column(u'manager_role', 'team_id_id')

        # Adding field 'Role.user'
        db.add_column(u'manager_role', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Role.event'
        db.add_column(u'manager_role', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['manager.Event']),
                      keep_default=False)

        # Adding field 'Role.team'
        db.add_column(u'manager_role', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['manager.Team']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Role.user_id'
        db.add_column(u'manager_role', 'user_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Role.event_id'
        db.add_column(u'manager_role', 'event_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['manager.Event']),
                      keep_default=False)

        # Adding field 'Role.team_id'
        db.add_column(u'manager_role', 'team_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['manager.Team']),
                      keep_default=False)

        # Deleting field 'Role.user'
        db.delete_column(u'manager_role', 'user_id')

        # Deleting field 'Role.event'
        db.delete_column(u'manager_role', 'event_id')

        # Deleting field 'Role.team'
        db.delete_column(u'manager_role', 'team_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'manager.event': {
            'Meta': {'object_name': 'Event'},
            'budget': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '10'}),
            'event_descr': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'event_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'manager.role': {
            'Meta': {'object_name': 'Role'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'default': '-1', 'to': u"orm['manager.Event']"}),
            'role_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roles': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['manager.Team']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '-1', 'to': u"orm['auth.User']"})
        },
        u'manager.task': {
            'Meta': {'object_name': 'Task'},
            'status': ('django.db.models.fields.CharField', [], {'default': "u'Not Started'", 'max_length': '10'}),
            'task_descr': ('django.db.models.fields.TextField', [], {}),
            'task_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manager.Team']"})
        },
        u'manager.team': {
            'Meta': {'object_name': 'Team'},
            'event_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manager.Event']"}),
            'team_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['manager']