from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta = data_fim - data_inicio

print(delta.days, delta.seconds, delta.microseconds)
print(data_fim)
print(data_fim + timedelta(seconds=60, minutes=10))