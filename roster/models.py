from django.db import models
from accounts.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_off_days = models.CharField(max_length=100)  # Comma-separated weekday names

class Shift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # E.g., "Monday"
    shift_start = models.TimeField()
    shift_end = models.TimeField()

class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    captured_image = models.ImageField(upload_to='attendance_images/')
