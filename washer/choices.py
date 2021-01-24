from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    Male = 1
    Female = 2
    Other = 3


class EmployeeRoleChoices(IntegerChoices):
    Owner = 1
    Manager = 2
    Washer = 3
    Cleaner = 4
    Other = 5
