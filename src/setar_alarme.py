from datetime import datetime
import time
import schedule
from win11toast import toast

current_time = datetime.now()
day_print = current_time.strftime("%d-%m-%Y")


def send_notification(title: str, message: str):
    toast(
        title,
        message,
        app_id = 'despertador python'
    )


class Alarm_config:
    def __init__(self):
        self.hour = int
        self.minute = int
        self.time = str

    def setting_alarm(self):
        print('A que horas deseja pôr o alarme? (por exemplo 08:20)\n')

        valid_hour = False
        while valid_hour == False:
            self.hour = input('Hora: ')

            if int(self.hour) > 25 or int(self.hour) < 0:
                print('Hora tem que ser um numero por exemplo 08, e tem que ser maior que 0 e menor que 24')
            else:
                hora = str(self.hour) + ':'
                valid_hour = True


        valid_minute = False
        while not valid_minute:
            self.minute = input('\nMinuto: ')

            if int(self.minute) > 60 or int(self.minute) < 0:
                print('minuto tem que ser um numero por exemplo 30, e tem que ser maior que 0 e menor que 60')
            else:
                minuto = str(self.minute)
                valid_minute = True
        self.time = day_print + hora + minuto + ':' + datetime.now().strftime('%S')

        title_alarm = input('título do alarme: ')


        print(f'\nalarme {title_alarm} está definido para {datetime.strptime(self.time, "%d-%m-%Y%H:%M:%S").strftime("%d-%m-%Y as %H:%M:%S")}')


        # print(hora + minuto)
        def calling_notification():
            send_notification(title=title_alarm, message='seu alarme está disparando ' + hora + minuto)

        schedule.every().day.at(hora + minuto).do(calling_notification)
        while True:
            schedule.run_pending()
            time.sleep(1)

