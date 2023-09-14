from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('submit/',lost_item_submit,name="submit"),
    path('',view_lost_items,name="viewlostitems"),
    path('search/',search,name="Search")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)