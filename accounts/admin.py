from django.contrib import admin
from .models import Employer, Employee


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'paid_date')
    search_fields = ('full_name', 'phone')
    list_filter = ('paid_date',)
    ordering = ('-paid_date',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'employer')
    search_fields = ('name', 'phone', 'employer__name')
    list_filter = ('employer',)
    ordering = ('-created_date',)




