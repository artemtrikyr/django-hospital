🏥 Django Hospital Project

🧠 Сутності
- Doctor (лікар)
- Appointment (запис до лікаря)

🔗 Зв'язки
- Один лікар → багато записів (ForeignKey)

Ось список команд які я використовував для перевірки роботоздатності проекту:
(venv) husll@Old-MacBook-2019 hospital % python manage.py shell
14 objects imported automatically (use -v 2 for details).

Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Doctor.objects.all()
<QuerySet [<Doctor: Іваненко Іван Іванович>, <Doctor: Свириденко Михайло Павлович>, <Doctor: Федьо Катерина Олександрівна>]>
>>> Appointment.objects.all()
<QuerySet [<Appointment: Василь Пупко - 2026-04-15 12:15:44+00:00>]>
>>> Doctor.objects.filter(experience__gt=10)
<QuerySet [<Doctor: Іваненко Іван Іванович>, <Doctor: Федьо Катерина Олександрівна>]>
>>> Appointment.objects.filter(appointment_date__date='2026-04-15')
<QuerySet [<Appointment: Василь Пупко - 2026-04-15 12:15:44+00:00>]>
>>> doctor = Doctor.objects.first()
>>> Appointment.objects.filter(doctor=doctor)
<QuerySet [<Appointment: Василь Пупко - 2026-04-15 12:15:44+00:00>]>
>>> Appointment.objects.filter(patient_name__icontains="Василь")
<QuerySet [<Appointment: Василь Пупко - 2026-04-15 12:15:44+00:00>]>
>>> exit()
now exiting InteractiveConsole...


