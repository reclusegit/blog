from django.contrib import admin
from record.models import User, IssueType, IssueRecord

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'password')

admin.site.register(User, UserAdmin)
admin.site.register(IssueType)
admin.site.register(IssueRecord)