from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .validators import validate_icon_image_size, validate_image_file_extension

# icon upload category
def category_icon_upload_path(instance, filename):
    return f"category/{instance}/category_icon/{filename}"


# icon upload server
def server_icon_upload_path(instance, filename):
    return f"category/{instance}/server_icon/{filename}"


# banner upload server
def server_banner_upload_path(instance, filename):
    return f"category/{instance}/server_banner/{filename}"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # for svg icons, it doesn't support other fields. So, use FileField
    icon = models.FileField(upload_to=category_icon_upload_path,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if self.id:
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    # when deleting a category, delete the image also
    @receiver(models.signals.pre_delete, sender="server.Category")
    def category_delete_files(sender, instance, *args, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)
        
    

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField(max_length=250, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    banner = models.ImageField(null=True, blank=True, upload_to=server_banner_upload_path, validators=[validate_image_file_extension])
    icon = models.ImageField(null=True, blank=True, upload_to=server_icon_upload_path, validators=[validate_icon_image_size, validate_image_file_extension])

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(Server, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing.banner != self.banner:
                existing.banner.delete(save=False)
        super(Server, self).save(*args, **kwargs)

    # when deleting a channel, delete the image also
    @receiver(models.signals.pre_delete, sender="server.Server")
    def server_delete_files(sender, instance, *args, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon" or field.name == "banner":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)



    def __str__(self):
        return f"{self.name}"


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner")
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower();
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    