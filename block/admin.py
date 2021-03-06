from django.contrib import admin

from models import Block
# Register your models here.

class BlockAdmin(admin.ModelAdmin):
    list_display=("title","des","owner","create_timestamp","last_update_timestamp")
    list_filter = ('title',)
admin.site.register(Block,BlockAdmin)