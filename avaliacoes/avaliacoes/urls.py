from django.urls import path
from core import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('', views.EmpresaListView.as_view(), name='home'),
    path('empresa/<int:pk>/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('empresa/<int:pk>/avaliar/', views.avaliar_empresa, name='avaliar_empresa'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)