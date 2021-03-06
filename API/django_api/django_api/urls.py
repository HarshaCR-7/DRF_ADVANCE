"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from user.views import UserProfileViewSet,CustomUserViewSet
from test_app.views import SimpleViewset
from event_controller.views import EventMainView,EventAttenderView
from gate_way.views import LoginView, RegisterView,RefreshView,TestException
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register("simple",SimpleViewset)
router.register("profile",UserProfileViewSet)
router.register("user",CustomUserViewSet)
router.register("event",EventMainView)
router.register("event-attender", EventAttenderView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path("login/",LoginView.as_view()),
    path("register/",RegisterView.as_view()),
    path("refresh/",RefreshView.as_view()),
    path("test/",TestException.as_view())
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    