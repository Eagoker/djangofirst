from django.contrib import admin
from .models import Stars, Profession


class StarsAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "age", "condition", "profession", "views")
    list_display_links = ('name',)
    readonly_fields = ('profession', 'views')
    

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("profession",)
    list_display_links = ("profession",)


admin.site.register(Stars, StarsAdmin)
admin.site.register(Profession, ProfessionAdmin)