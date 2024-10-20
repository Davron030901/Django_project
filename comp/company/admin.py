from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'date')
	search_fields = ('title', 'description',)
	list_filter = ('id', 'title', 'description', 'date')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'date', 'message')
	search_fields = ('name', 'email', 'message')
	list_filter = ('date',)


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'surname', 'age', 'position')
	search_fields = ('name', 'surname', 'age', 'position')
	list_filter = ('age', 'position')
