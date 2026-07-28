
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('home', views.api, name='api'),
]
