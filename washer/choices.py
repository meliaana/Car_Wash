from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    Male = 1
    Female = 2
    Other = 3


class CarTypeChoices(IntegerChoices):
    Sedan = 1
    Van = 2
    Other = 3
