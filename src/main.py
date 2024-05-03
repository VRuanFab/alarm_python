import sys
import time
from setar_alarme import Alarm_config



# print(f'alarme definido para {datetime.strptime(setting_alarm(), "%d-%m-%Y%H:%M:%S").strftime("%d-%m-%Y as %H:%M:%S")}')


alarme = Alarm_config()
alarme.setting_alarm()