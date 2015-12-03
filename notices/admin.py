from django.contrib import admin
from notices.models import Notice, NoticeBranchYear
# Register your models here.
admin.site.register(Notice)
admin.site.register(NoticeBranchYear)

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title','faculty','category','created_at')

admin.site.register(Notice,NoticeAdmin)
