"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from kapsle import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('add/', views.UserCoinCreateView.as_view(), name='add'),
    path('admin/', admin.site.urls),
    path('list/<slug:slug>/<int:pk>/ignore/', views.IgnoreCoinCreateView.as_view(), name='ignorecoin-create'),
    path('list/<slug:slug>/<int:pk>/ignore/del/', views.IgnoreCoinDeleteView.as_view(), name='ignorecoin-delete'),
    path('list/<slug:slug>/<int:pk>/', views.CoinDetailView.as_view(), name='coin-detail'),
    path('list/<slug:slug>/', views.BreweryDetailView.as_view(), name='brewery-detail'),
    path('', views.BreweryListView.as_view(), name='brewery-list'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/delete/', views.UserCoinDeleteView.as_view(), name='usercoin-delete'),
    path('user/<int:pk>/', views.UserCoinUpdateView.as_view(), name='usercoin-edit'),
    path('user/', views.UserCoinListView.as_view(), name='user'),
    path('want-list/', views.WantListView.as_view(), name='want-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


