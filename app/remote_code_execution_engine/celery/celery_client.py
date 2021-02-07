from celery import Celery

celery_client = Celery('code-executions-tasks', broker='pyamqp://guest@rabbit//', backend='amqp://guest@rabbit//')
