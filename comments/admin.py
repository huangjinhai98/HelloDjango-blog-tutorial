from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    # 修改添加数据时的条目
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    # 数据展示的字段
    fields = ['name', 'email', 'url', 'text', 'post']


# 模型类控制字段的详细信息，admin中控制具体要展示的字段
admin.site.register(Comment, CommentAdmin)
