from django.contrib import admin
from notices.models import Notice, NoticeBranchYear
# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title','faculty','category','created_at')

admin.site.register(Notice,NoticeAdmin)
