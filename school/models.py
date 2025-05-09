from django.db import models
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO

from .validators import cep_validator, cpf_validator, phone_validator


class Class(models.Model):
    CLASS_CHOICES = (
        ("1A", "1° Ano A"),
        ("1B", "1° Ano B"),
        ("1C", "1° Ano C"),
        ("2A", "2° Ano A"),
        ("2B", "2° Ano B"),
        ("2C", "2° Ano C"),
        ("3A", "3° Ano A"),
        ("3B", "3° Ano B"),
        ("3C", "3° Ano C"),
    )

    ITINERARY_CHOICES = (
        ("DS", "Desenvolvimento de Sistemas"),
        ("CN", "Ciencias da Natureza"),
        ("JG", "Desenvolvimento de Jogos"),
    )

    class_choices = models.CharField(max_length=50, choices=CLASS_CHOICES)
    itinerary_choices = models.CharField(max_length=50, choices=ITINERARY_CHOICES)

    def __str__(self):
        return f"{self.get_class_choices_display()} - {self.get_itinerary_choices_display()}"


class Student(models.Model):
    full_name = models.CharField(
        max_length=200, verbose_name="Student's full name", null=True
    )

    registration_number = models.CharField(
        max_length=6, unique=True, verbose_name="Student's registration"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Student's phone number (XX) 9XXXX-XXXX",
        validators=[phone_validator],
    )
    email = models.EmailField(max_length=100, verbose_name="Student's email")
    cpf = models.CharField(
        max_length=11,
        verbose_name="Student's CPF",
        unique=True,
        validators=[cpf_validator],
    )
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100, validators=[cep_validator])
    class_choice = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Student's class",
        related_name="student_class",
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.full_name


class Guardian(models.Model):
    full_name = models.CharField(
        max_length=200, verbose_name="Guardian's full name", null=True
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Guardian's student",
        related_name="guardian_student",
        blank=False,
        null=True,
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Guardian's phone number (XX) 9XXXX-XXXX",
        validators=[phone_validator],
    )
    email = models.EmailField(max_length=100, verbose_name="Guardian's email")
    cpf = models.CharField(
        max_length=11,
        verbose_name="Guardian's CPF",
        unique=True,
        validators=[cpf_validator],
    )
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100, validators=[cep_validator])

    def __str__(self):
        return self.full_name


class Professor(models.Model):
    full_name = models.CharField(
        max_length=200, verbose_name="Professor's full name", null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Professor's phone number (XX) 9XXXX-XXXX",
        validators=[phone_validator],
    )
    email = models.EmailField(max_length=100, verbose_name="Professor's email")
    cpf = models.CharField(
        max_length=11,
        verbose_name="Professor's CPF",
        unique=True,
        validators=[cpf_validator],
    )
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100, validators=[cep_validator])
    class_choice = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Student's class",
        related_name="professor_class",
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.full_name


class Bulletin(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Student's name",
        related_name="bulletins",
        blank=False,
        null=True,
    )

    grades = models.JSONField(
        verbose_name="JSON Values of Grades",
        blank=False,
        null=True,
    )

    def __str__(self):
        return f"{self.student.full_name}'s Bulletin"


class Contract(models.Model):
    guardian = models.ForeignKey(
        Guardian,
        on_delete=models.CASCADE,
        verbose_name="Guardian's name",
        related_name="contract_guardian",
        blank=False,
        null=True,
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Student's name",
        related_name="contract_student",
        blank=False,
        null=True,
    )

    def generate_contract_pdf(self):
        html_string = render_to_string("contract_template.html", {"contract": self})
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_buffer)
        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)

        pdf_buffer.seek(0)
        response = HttpResponse(pdf_buffer, content_type="application/pdf")
        response["Content-Disposition"] = (
            f'attachment; filename="contract_{self.id}_{self.guardian.full_name}-{self.student.full_name}.pdf"'
        )
        return response

    def __str__(self):
        return f"Contract: {self.guardian.full_name.upper()} e {self.student.full_name.upper()}"
