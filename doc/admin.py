from django.contrib import admin
from django import forms
from django.db import models
from .models import User, Doc, Services, Reception, Event
from django.contrib.admin.models import LogEntry
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


admin.site.register(User)
LogEntry.objects.all().delete()

class FlatPagesAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(label='Основна частина', widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality','image')


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'annotation', 'date')


admin.site.site_title = 'MedCentre'
admin.site.site_header = 'MedCentre'

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPagesAdmin)