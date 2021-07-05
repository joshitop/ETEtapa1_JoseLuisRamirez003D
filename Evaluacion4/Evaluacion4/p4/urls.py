from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('proveedores/',views.proveedores, name='proveedores'),
    path('crear_proveedor/',views.crearProveedor, name='crearProveedor'),
    path('modificar_proveedor/<id>',views.modificarProveedor, name='modificarProveedor'),
    path('eliminar_proveedor/<id>',views.eliminarProveedor, name='eliminarProveedor')
]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)