from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from utils import 

from models import forms

logger = get_task_logger(__name__)


@periodic_task(
	run_every=(crontab(minute='*/5')),
	name="send_signup_email_task",
	ignore_result=True
)
def task_send_signup_email(email, message):
    """sends an email when singup form is filled successfully"""
    send_signup_email()
    logger.info("Sent signup email")
    return send_signup_email(email, message)
