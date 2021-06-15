from datetime import datetime, timedelta
import pytz


def get_date():
    return str(datetime.now(pytz.timezone('Europe/Berlin')).strftime('%d.%m.%Y'))


def get_date_tmrw():
    return str((datetime.utcnow().date() - timedelta(days=1)).strftime('%d.%m.%Y'))