from dateutil.relativedelta import relativedelta
from datetime import datetime

fmt = '%d/%m/%Y'

date_init = datetime(2020, 12, 20)
date_finally = date_init + relativedelta(years=5)
loans = 1000000.00

delta = relativedelta(date_finally, date_init)
months_period = delta.years * 12 + delta.months
loan_month = loans / months_period
actual_date = date_init

for i in range(months_period):
    print(f'{actual_date.strftime(fmt)} R$ {loan_month:.2f}')
    actual_date = actual_date + relativedelta(months=1)

print()
print(f'Você pegou {loans:.2f} para pagar em {months_period} meses em parcelas de R$ {loan_month:.2f}')