from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class FrenchCourse(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'Beginner (A1)'),
        ('A2', 'Elementary (A2)'),
        ('B1', 'Intermediate (B1)'),
        ('B2', 'Upper Intermediate (B2)'),
        ('C1', 'Advanced (C1)'),
        ('C2', 'Proficient (C2)'),
    ]

    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, null=True, blank=True)  # Optional for non-level courses
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    duration_months = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}" if self.category else self.name
