from django.contrib import admin
from image_auto_tag.models import Images
from taggit.admin import Tag



# Register your models here.


admin.site.unregister(Tag)
admin.site.register(Images)
class ImagessAdmin(admin.ModelAdmin):
 
    def save_model(self, request, obj, form, change):
        obj.save()