from rest_framework.routers import DefaultRouter as DR 

from mainapp.views import(
    PlanetsView,
)

router = DR()

router.register('planets',PlanetsView)


urlpatterns = []

urlpatterns += router.urls
