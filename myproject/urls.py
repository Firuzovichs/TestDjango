"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test_app.views import RandomTestQuestionsAPIView,TestResultListCreateAPIView,TimeApiView


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/random-tests/', RandomTestQuestionsAPIView.as_view(), name='random-tests'),
    path('api/v1/test-results/', TestResultListCreateAPIView.as_view(), name='test-results'),
    path('api/v1/times/', TimeApiView.as_view(), name="time-get")
]
