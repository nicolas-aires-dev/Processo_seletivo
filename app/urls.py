from django.contrib import admin
from django.urls import path
from search_people.views import pessoa_view, index_view, calcular_peso_ideal

urlpatterns = [
    path('admin/', admin.site.urls),


    path('search/', index_view, name='index'),
    path('api/pessoas/', pessoa_view, name='pessoa_api'),
    path('api/pessoas/<str:cpf>/', pessoa_view),
    path('api/pessoas/<int:pessoa_id>/calcular_peso_ideal/', calcular_peso_ideal),
]