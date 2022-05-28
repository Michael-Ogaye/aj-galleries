
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('singleimg',views.search_results,name='search_img'),
    path('image/<int:id>', views.specific, name='specific'),
    path('del/<int:id>', views.delete_img, name='del'),
    path('update/<int:id>', views.update_img, name='update'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    