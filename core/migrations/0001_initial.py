# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteConfig'
        db.create_table(u'core_siteconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 19, 0, 0), auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['SiteConfig'])


    def backwards(self, orm):
        # Deleting model 'SiteConfig'
        db.delete_table(u'core_siteconfig')


    models = {
        'core.siteconfig': {
            'Meta': {'object_name': 'SiteConfig'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 19, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']