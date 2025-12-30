from django.db import models
from django.contrib.auth.models import AbstractUser


# User
class User(AbstractUser):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username


# Admin
class Admin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin"
    )

    def __str__(self):
        return f"Admin: {self.user.username}"


# Team
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Employee
class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    def __str__(self):
        return f"{self.user.username} ({self.team.name})"


# Task
class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    # המשימה שייכת לצוות אחד
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    # עובד מבצע (אופציונלי)
    assigned_employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks"
    )

    def __str__(self):
        return self.title
