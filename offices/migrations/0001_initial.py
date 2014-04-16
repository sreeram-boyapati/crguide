# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'offices_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=10)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=10)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'offices', ['Location'])

        # Adding model 'Office'
        db.create_table(u'offices_office', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['offices.Location'])),
            ('type_office', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'offices', ['Office'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'offices_location')

        # Deleting model 'Office'
        db.delete_table(u'offices_office')


    models = {
        u'offices.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '10'})
        },
        u'offices.office': {
            'Meta': {'object_name': 'Office'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['offices.Location']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'type_office': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['offices']