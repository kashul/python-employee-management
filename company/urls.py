from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [
    path('list', views.lists, name='list'),
    path('form/<int:id>', views.forms, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
