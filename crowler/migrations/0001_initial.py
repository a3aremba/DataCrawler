# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RelevantWords'
        db.create_table(u'crowler_relevantwords', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('siteConfig', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SiteConfig'])),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag_history', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('crowler', ['RelevantWords'])


    def backwards(self, orm):
        # Deleting model 'RelevantWords'
        db.delete_table(u'crowler_relevantwords')


    models = {
        'core.siteconfig': {
            'Meta': {'object_name': 'SiteConfig'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'crowler.relevantwords': {
            'Meta': {'object_name': 'RelevantWords'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteConfig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SiteConfig']"}),
            'tag_history': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['crowler']