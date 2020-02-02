from django.core import serializers
from .models import Schedule

from django.core.serializers.json import DjangoJSONEncoder

data = serializers.serialize("json", Schedule.objects.all())

