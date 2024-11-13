from rest_framework import viewsets, permissions
from .models import Staff, Shift, Attendance
from .serializers import StaffSerializer, ShiftSerializer, AttendanceSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        staff = Staff.objects.get(user=request.user)
        shift = Shift.objects.filter(staff=staff).first()

        # Check shift timing for attendance
        now = timezone.now().time()
        if shift.shift_start <= now <= shift.shift_end:
            # Capture image and save attendance record
            return super().create(request, *args, **kwargs)
        return Response({"detail": "Not within shift timing"}, status=400)
