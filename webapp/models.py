from django.core.validators import MinLengthValidator
from django.db import models


class file(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(limit_value=7,
                                                                           message="Меньше 7")])
    upload_file = models.FileField(upload_to='doc/', blank=True, null=True)
    access = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class folder(models.Model):
    DEPARTMENT = [
        ("KO", "Коммерческий"),
        ("FI", "Финансовый"),
        ("MA", "Маркетинговый"),
    ]
    title = models.CharField(max_length=20, validators=[MinLengthValidator(limit_value=5,
                                                                           message="Меньше 5")])
    department = models.CharField(max_length=2,
                                  choices=DEPARTMENT,
                                  default=None, )
    files = models.ForeignKey(file, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
