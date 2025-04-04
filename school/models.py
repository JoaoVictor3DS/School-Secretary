from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF


def cpf_validator(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(
            ("%(value)s is not valid"),
            params={"value": value},
        )


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


class Guardian(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Guardian's first name")
    last_name = models.CharField(max_length=200, verbose_name="Guardian's last name")
    registration_number_student = models.CharField(
        max_length=6, unique=True, verbose_name="Student's registration"
    )
    phone_number = models.CharField(
        max_length=15, verbose_name="Guardian's phone number (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Guardian's email")
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100)
    class_choice = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Student's class",
        related_name="guardian_student",
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Student's first name")
    last_name = models.CharField(max_length=200, verbose_name="Student's last name")
    registration_number = models.CharField(
        max_length=6, unique=True, verbose_name="Student's registration"
    )
    phone_number = models.CharField(
        max_length=15, verbose_name="Student's phone number (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Student's email")
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100)
    class_choice = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Student's class",
        related_name="student_class",
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Professor(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Professor's first name")
    last_name = models.CharField(max_length=200, verbose_name="Professor's last name")
    phone_number = models.CharField(
        max_length=15, verbose_name="Professor's phone number (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Professor's email")
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    birthday = models.DateField(max_length=10)
    adress = models.CharField(max_length=100)
    class_choice = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Student's class",
        related_name="professor_class",
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


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
