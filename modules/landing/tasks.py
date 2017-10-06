from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from modules.landing.utils import send_signup_email

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/1')), name="task_send_signup_email", ignore_result=True)
def task_send_signup_email(email, message):
    """sends an email when singup form is filled successfully"""
    send_signup_email()
    logger.info("Sent signup email")
    return send_signup_email(email, message)
