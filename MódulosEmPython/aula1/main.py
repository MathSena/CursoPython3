from datetime import datetime, timedelta

data = datetime(2021,4,20, 10, 54,20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data2 = datetime.strptime('20/07/2020', '%d/%m/%Y')
print(data2)

print(data.timestamp())
data_comTimestamp = datetime.fromtimestamp(1618926860.0)
print(data_comTimestamp)

d1 = datetime.strptime('16/11/1996 11:37:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('06/03/2021 23:59:59', '%d/%m/%Y %H:%M:%S')
dif = d2-d1
print('Diferença de segundos', dif.seconds)
print('Diferença de dias', dif.days)
