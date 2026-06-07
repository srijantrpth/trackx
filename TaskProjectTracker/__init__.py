from .celery import app as celery_app
__all__ = ('celery_app',)
CELERY_BROKER_URL = 'redis://default:6KUBa7AYbHH3QkHmiYTyRCyZO3xuKnfZ@redis-16762.crce263.ap-south-1-1.ec2.cloud.redislabs.com:16762'


