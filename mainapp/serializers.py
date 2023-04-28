from  rest_framework import serializers

from mainapp.models import(
    Planets,
)

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields=(
           'id','name','number','life',
        )