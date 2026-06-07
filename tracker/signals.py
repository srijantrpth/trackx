from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Project
from .tasks import send_completion_email_task


@receiver(post_save, sender=Task)
def update_project_timestamp(sender, instance, created, **kwargs):
    instance.project.save()
    if instance.status== 'DONE':
        send_completion_email_task.delay(instance.id)


