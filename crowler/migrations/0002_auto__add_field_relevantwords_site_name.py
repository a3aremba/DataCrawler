# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RelevantWords.site_name'
        db.add_column(u'crowler_relevantwords', 'site_name',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RelevantWords.site_name'
        db.delete_column(u'crowler_relevantwords', 'site_name')


    models = {
        'core.siteconfig': {
            'Meta': {'object_name': 'SiteConfig'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'html_content': ('django.db.models.fields.TextField', [], {'default': "' '", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'crowler.relevantwords': {
            'Meta': {'object_name': 'RelevantWords'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteConfig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SiteConfig']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '255', 'null': 'True'}),
            'tag_history': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['crowler']