import sys
import time
from win11toast import toast
from setar_alarme import Alarm_config

def send_notification(title: str, message: str):
    toast(
        title,
        message,
        app_id = 'despertador python'
    )

# print(f'alarme definido para {datetime.strptime(setting_alarm(), "%d-%m-%Y%H:%M:%S").strftime("%d-%m-%Y as %H:%M:%S")}')


alarme = Alarm_config()
alarme.setting_alarm()
