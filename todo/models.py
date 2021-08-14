from django.db.models import *

# Create your models here.


class Todo(Model):
    name=CharField(max_length=300)
    created_at=DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
