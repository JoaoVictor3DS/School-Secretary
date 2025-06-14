from rest_framework import viewsets, filters
from rest_framework.decorators import action

from .models import Student, Grade, Guardian, Contract, Presence
from .serializers import (
    StudentSerializer,
    GradeSerializer,
    GuardianSerializer,
    ContractSerializer,
    PresenceSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "full_name",
        "registration_number",
        "phone_number",
        "email",
        "cpf",
    ]

    @action(detail=True, methods=["get"], url_path="download-grades")
    def download_grades_pdf(self, request, pk=None):
        student = self.get_object()
        return student.generate_grades_pdf()

    @action(detail=True, methods=["get"], url_path="download-presence")
    def download_presence_pdf(self, request, pk=None):
        student = self.get_object()
        return student.generate_presence_pdf()


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "student__full_name",
        "subject__name",
        "year",
        "bimester",
        "value",
    ]


class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "full_name",
        "student__full_name",
        "phone_number",
        "cpf",
        "email",
    ]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "guardian__full_name",
        "student__full_name",
    ]


class PresenceViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "student__full_name",
        "date",
        "presence",
    ]
