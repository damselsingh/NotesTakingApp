from django.contrib import admin
from .models import note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display=('id', 'date','title',)


admin.site.register(note, NoteAdmin)
