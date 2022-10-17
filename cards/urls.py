from django.urls import path
from django.conf import settings
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('meaning', views.meaning, name='meaning'),
]


if settings.DEBUG:
    print(settings.MEDIA_ROOT)
    print("-----------------")
    # test mode
    from django.conf.urls.static import static
    #rlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)