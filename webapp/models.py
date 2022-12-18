from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from django.db import models



DEPARTMENT = [
        ("KO", "Коммерческий"),
        ("FI", "Финансовый"),
        ("MA", "Маркетинговый"),
    ]

class file(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(limit_value=7,
                                                                           message="Меньше 7")], verbose_name= "Название")
    parent_directory = models.ForeignKey('folder', on_delete=models.CASCADE, related_name='Каталог',
                                          verbose_name='Каталог', default=None, blank=True, null=True)
    upload_file = models.FileField(upload_to='doc/', verbose_name='Загрузить файл')
    access = models.BooleanField(default=False, verbose_name='Доступ')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"
        ordering = ['title']


class folder(models.Model):
    title = models.CharField(max_length=20, validators=[MinLengthValidator(limit_value=5,
                                                                           message="Меньше 5")], verbose_name='Название')
    department = models.CharField(max_length=2,
                                  choices=DEPARTMENT,
                                  default=None, verbose_name="Отдел")
    # files = models.ForeignKey(file, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Файл')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Каталоги"
        verbose_name_plural = "Каталоги"




class CustomUser(AbstractUser):
    FIO = models.CharField(max_length=100,
                           verbose_name="ФИО")
    email = models.EmailField(unique=True,
                              verbose_name="Почта")
    department_user = models.CharField(choices=DEPARTMENT,
                                       max_length=2,
                                       verbose_name="Отдел")
    date_birth = models.DateField(verbose_name="Дата рождения",
                                  blank=True, null=True)
    access_level = models.BooleanField(default=0,
                                        blank=True,
                                        null=True,
                                        verbose_name='Уровень доступа')
    register_time = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["password", "email"]
    # USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

# class User(AbstractBaseUser, PermissionsMixin):
#     # username_validator = UnicodeUsernameValidator()
#     # username = models.CharField(
#     #     max_length=150,
#     #     unique=True,
#     #     validators=[username_validator],
#     # )
#     email = models.EmailField(unique=True)
#     # password = models.CharField(max_length=20)
#     full_name = models.CharField(max_length=255)
#     department_user = models.CharField(choices=DEPARTMENT,
#                                        max_length=2)
#     birthday = models.DateField(
#         null=True,
#         blank=True
#     )
#     access = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     register_time = models.DateTimeField(auto_now_add=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'full_name']
#     objects = UserManager()
#     def __str__(self):
#         return self.full_name
#     def get_short_name(self):
#         return self.username
#     def get_full_name(self):
#         return self.full_name
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         send_mail(subject, message, from_email, [self.email], **kwargs)


# class UserManager(BaseUserManager):
#     use_in_migrations = True
#     def _create_user(self, email, username, full_name, password, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         if not username:
#             raise ValueError('The given username must be set')
#         if not full_name:
#             raise ValueError('The given full name must be set')
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(
#             email=email, username=username, full_name=full_name,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_user(self, email, username, full_name, password, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(
#             email, username, full_name, password, **extra_fields
#         )
#     def create_superuser(self, email, username, full_name, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(
#             email, username, full_name, password, **extra_fields
#         )