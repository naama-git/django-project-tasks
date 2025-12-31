from django.db import models
from django.contrib.auth.models import AbstractUser



# user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

# admin
class Admin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin"
    )

    def __str__(self):
        return f"Admin: {self.user.username}"

# team
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# member
class Member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="member"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="memebers"
    )

    def __str__(self):
        return f"{self.user.username} ({self.team.name})"


# task
class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=500, null=True)
    due_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    # task belongs to a team
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    # task assigned to a member
    assigned_employee = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks"
    )

    #chansh status to in progress when assigned to member
    def save(self, *args, **kwargs):
        if self.assigned_employee and self.status == Task.Status.PENDING:
            self.status = Task.Status.IN_PROGRESS

        if 'update_fields' in kwargs and kwargs['update_fields'] is not None:
            kwargs['update_fields'] = set(kwargs['update_fields']) | {'status'}
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
