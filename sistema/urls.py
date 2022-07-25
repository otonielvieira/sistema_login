from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticacao.urls')), # vai chamar as urls do app de atenticação
    path('plataforma/', include('web.urls')),# vai chamar as urls do app de atenticação

]
