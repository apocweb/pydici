# coding:utf-8
"""
Django administration setup
@author: Sébastien Renard <Sebastien.Renard@digitalfox.org>
@license: GPL v3 or newer
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from pydici.staffing.models import Mission, Holiday, Timesheet


class MissionAdmin(admin.ModelAdmin):
    list_display = ("lead", "description", "nature", "probability", "deal_id", "active", "update_date")
    search_fields = ("lead__name", "description", "deal_id", "lead__client__organisation__company__name",
                   "lead__client__contact__name")
    ordering = ("lead", "description")
    date_hierarchy = "update_date"
    list_filter = ["nature", "probability", "active"]
    actions = None

class HolidayAdmin(admin.ModelAdmin):
    list_display = ("day", "description")
    date_hierarchy = "day"
    actions = None


admin.site.register(Mission, MissionAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Timesheet)