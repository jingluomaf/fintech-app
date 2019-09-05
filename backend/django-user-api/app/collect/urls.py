# from django.urls import path, include
from django.urls import path
# from rest_framework.routers import DefaultRouter
from collect import views


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'{}'.format(ticker), views.HistoryViewSet)
# print('collect url run')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', include(router.urls)),
    path('<ticker>/', views.HistoryViewSet.as_view())
]
