from django.urls import path
from .views import index, formulario, eliminar_usuario, editar_datos, principal, listado_usuarios, terror, accion, aventura, carreras, supervivencia, compra,listado_juegos, crear_juego, juegos_show, eliminar_juego, juegos_editar, logout_view, recuperar_contrasenna
urlpatterns = [
    # link Juegos
    path('princjuegos/principal', principal, name='principal'),
    path('princjuegos/juegosterror', terror, name="terror"),
    path('princjuegos/juegosaventura', aventura, name="aventura"),
    path('princjuegos/juegosaccion', accion, name="accion"),
    path('princjuegos/juegoscarreras', carreras, name="carreras"),
    path('princjuegos/juegossupervivencia', supervivencia, name="supervivencia"),
    path('princjuegos/juegoscompra', compra, name="compra"),
    path('princjuegos/listado_juegos', listado_juegos, name="listado_juegos"),
    path('princjuegos/crearjuego', crear_juego, name="crear_juego"),
    path('princjuegos/<int:id>/editarjuego', juegos_editar, name="juegos_editar"),
    path('princjuegos/<int:id>/juego_show', juegos_show, name="juegos_show"),
    path('princjuegos/<int:id>/eliminar_juego', eliminar_juego, name="eliminar_juego"),
    
    

    # link enlace formularios usuario
    path('formulario/', formulario, name="formulario"),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name="eliminar_usuario"),
    path('editar_datos/<int:id>/', editar_datos, name="editar_datos"),
    path('', index, name="index"),
    path('recuperar_contrasenna/', recuperar_contrasenna, name="recuperar_contrasenna"),
    path('princjuegos/listado_usuarios/', listado_usuarios, name="listado_usuarios"),
    path('logout/', logout_view, name="logout")

]