from django.contrib import admin

from models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ("owner", "jobname", "jobnumber", "slots", "ru_maxrss", "ru_wallclock", "exit_status")
    list_filter = ("owner", "slots", "exit_status")

admin.site.register(Job, JobAdmin)
