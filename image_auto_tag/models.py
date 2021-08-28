from django.db import models

from django.db.models.signals import post_save

from image_auto_tag.utils.nlp_functions import get_categories




class Images(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    tags = models.CharField(default='', max_length=1000)
    categories = models.TextField(default='', editable=False)
    
    
    def __str__(self):
        return self.categories

# After Saving the model update categories using function get_categories(tagList)
    @staticmethod
    def post_save(sender, instance, **kwargs):
        allTags = instance.tags
        tagList = []
        for tag in allTags.split(','):
            tagList.append(tag)

        categories = get_categories(tagList, number=4)
        Images.objects.filter(pk=instance.id).update(categories='->'.join(categories))
        print('---------------------------')
        print('->'.join(categories))
        print('---------------------------')
post_save.connect(Images.post_save, Images, dispatch_uid="auto_tagging_system.image_auto_tag.models.Images") 
