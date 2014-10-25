# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SiteConfig.content'
        db.add_column(u'core_siteconfig', 'content',
                      self.gf('django.db.models.fields.TextField')(default='Empty', null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SiteConfig.content'
        db.delete_column(u'core_siteconfig', 'content')


    models = {
        'core.siteconfig': {
            'Meta': {'object_name': 'SiteConfig'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'Empty'", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 25, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']