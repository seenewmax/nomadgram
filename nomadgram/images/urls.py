from django.conf.urls import url
from . import views

urlpatterns = [
    all(
        regex=r'^all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    )
]