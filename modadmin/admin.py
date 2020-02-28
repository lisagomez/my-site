from django.contrib import admin

from .models import Function, JobPosition, Department

class JobPositionInline(admin.TabularInline):
    model = JobPosition
    extra = 3

class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['department_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [JobPositionInline, ]
    list_display = ('department_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['deparment_name']

admin.site.register(Department, DepartmentAdmin)