from django.db import models
from django.urls import reverse



class Detail(models.Model):
    AP = models.DateField()
    Ramadaan = models.DateField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(blank=True,)
    end_time = models.DateTimeField(blank=True,)


    

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
