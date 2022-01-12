from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from trackApp.models import Nema, Returnformnema
# @admin.register(Nema)
# class NemaAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Nema)
# class NemaAdmin(ImportExportModelAdmin):
#     pass

@admin.register(Nema)
class NemaAdmin(ImportExportModelAdmin):
    list_display = ("nema_id", "devui")
    pass

@admin.register(Returnformnema)
class Nemareturnform(admin.ModelAdmin):
    list_display = ("id", "dateuninstall")
    pass

