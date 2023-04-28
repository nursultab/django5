from rest_framework.viewsets import ModelViewSet

from mainapp.models import (
    Planets,
)


from mainapp.serializers import(
    PlanetsSerializer,
)

class PlanetsView(ModelViewSet):
    queryset=Planets.objects.all()
    serializer_class=PlanetsSerializer
