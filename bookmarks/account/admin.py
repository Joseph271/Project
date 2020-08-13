from django.contrib import admin
from .models import Profile,Pdfs


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']

@admin.register(Pdfs)
class PostAdmin(admin.ModelAdmin):
    list_display = ('university', 'branch', 'subject', 'pdf')

    search_fields = ('subject', 'pdf')
