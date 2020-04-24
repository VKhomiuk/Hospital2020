from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import date

""" User """
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, full_name=None, is_active=True, is_staff=None,
                    is_admin=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=False)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=250)
    name = models.CharField(max_length=250, blank=True, null=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        if not self.id and not self.staff and not self.admin:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


""" Site models """
class Doc(models.Model):
    """ Description Doc """
    name = models.CharField("Ім'я", max_length=250)
    speciality = models.CharField("Спецальність", max_length=250)
    image = models.ImageField('Зображення', upload_to='image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = "Лікарі"
        ordering = ('-id',)


class Services(models.Model):
    """ Icon services """
    name = models.CharField("Назва", max_length=250)
    picture = models.ImageField("Іконка", upload_to="icon/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
        ordering = ('name',)

class Event(models.Model):
    """ news"""
    title = models.CharField('Заголовок', max_length=255)
    annotation = models.CharField('Короткий опис', max_length=255)
    # text = models.TextField('Основна частина')
    date = models.DateField('Дата', default=date.today())
    image = models.ImageField('Зображення', upload_to='news/', blank=True)
    slug = models.CharField('Посилання головна', max_length=50, blank=True, null=True)
    # slug1 = models.CharField('Посилання новини', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ('-date', 'title',)


class Reception(models.Model):
    name = models.CharField("ПІБ", max_length=250)
    phone = models.CharField("Номер телефону", max_length=250)
    email = models.CharField('Email', max_length=250)
    msg = models.TextField('Повідомлення')
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return '<<<Запис на прийом>>>\n\n\nДата: ' + str(self.date.strftime('%d.%m.%Y %H:%M')) + '\n\n' + 'ПІБ: ' + self.name + '\n\n' + \
               'Телефон: ' + self.phone + '\n\n' + 'Email: ' + self.email + '\n\n' + 'Повідмолення:\n' + self.msg

    class Meta:
        verbose_name = 'Запис на прийом'
        verbose_name_plural = 'Записи на прийом'
        ordering = ('date',)


