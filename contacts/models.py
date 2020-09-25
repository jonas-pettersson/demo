from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(
        'Company', related_name='contacts', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})


class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})
