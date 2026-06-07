from celery import shared_task
import time

@shared_task
def send_completion_email_task(task_id):
    print(f"Starting send_completion_email_task {task_id}")
    time.sleep(5)
    print(f"Successfully started send_completion_email_task {task_id}")
    return True
