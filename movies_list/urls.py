from django.urls import path, include
from .views import CollectionsView, MoviesView
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
# router.register(r'collections', CollectionsView)


urlpatterns = [
    path('', include(router.urls)),
    path('movies/',MoviesView.as_view()),
    path('collections/',CollectionsView.as_view()),
    path('collections/<int:pk>/',CollectionsView.as_view()),

]