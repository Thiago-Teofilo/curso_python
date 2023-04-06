import locale
import calendar

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

print(calendar.monthcalendar(2023, 5))
