from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models he
admin.site.register(Todo,TodoAdmin)