from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /posts/fbv/
    path("fbv/", views.indexFBV, name="index"),
    # ex: /posts/fbv/5/
    path("fbv/<int:post_id>/", views.detailFBV, name="detail"),
    # ex: /posts/cbv/
    path("cbv/", views.IndexCBV.as_view(), name="index"),
    # ex: /posts/cbv/5/
    path("cbv/<int:post_id>/", views.DetailCBV.as_view(), name="detail"),
    # ex: /posts/create/
    path("create/", views.PostCreateCBV.as_view(), name="create_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
