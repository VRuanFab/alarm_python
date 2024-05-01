from datetime import datetime
import sys
from plyer import notification

# notification.notify(
#     title = "teste",
#     message= "boh jogar regezada"
# )


current_time = datetime.now()
time_print = current_time.strftime('%H:%M:%S')
day_print = current_time.strftime("%d-%m-%Y")

alarme = print('Que horas o alarme?\n')

hour = str(input('hora:') + ':')
minute = str(input('\nminuto:') + ':')
time = day_print + hour + minute + datetime.now().strftime('%S')

print(f'alarme definido para {datetime.strptime(time, "%d-%m-%Y%H:%M:%S").strftime('%d-%m-%Y as %H:%M:%S')}')

