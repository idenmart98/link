from django.db import models
import random
import string
from django.conf import settings

class Link(models.Model):
    old_link = models.URLField(verbose_name="Старая ссылка")
    new_link = models.CharField(max_length=10, verbose_name="Новая ссылка")

    def save(self, *args, **kwargs):
        if not self.new_link:
            self.new_link = self.get_codes()
        super(Link, self).save(*args, **kwargs)

    def get_codes(self):
        current_links = list(Link.objects.values_list(
            'new_link', flat=True))
        while True:
            link = self.generate_new_link()
            if link not in current_links:
                break
            else:
                continue
        return link

    def generate_new_link(self):
        new_link=''
        for i in range(4):
            new_link+=random.choice(string.ascii_letters)
        return new_link

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'