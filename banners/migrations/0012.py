# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('banners_banner', 'banner_file', 'image')

    def backwards(self, orm):
        db.rename_column('banners_banner', 'image', 'banner_file')

    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'destination_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_rollover': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'popup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banners.Slot']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'banners.slot': {
            'Meta': {'unique_together': "(('symbol', 'language'),)", 'object_name': 'Slot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'random': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['banners']
