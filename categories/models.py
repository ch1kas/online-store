from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent} --> {self.title}"
        return self.title

