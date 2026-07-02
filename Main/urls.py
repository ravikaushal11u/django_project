from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
     path('todo', views.todo, name='todo'),

    path('', include('app.urls')),
    path('ai/', include('ai.urls')),
    path('chat/', include('chat.urls')),
    path('chats/', include('conversations.urls')),
    path('login/', include('accounts.urls')),
    path('api/',include('api.urls')),
    path('atm/',include('automation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )