from django.urls import path
from .views import catalogo,delivery,home,vista_prod,arroz,bebidas,busqueda,cafe,carritodecompras,chocolate,confort,desodoranteamb,detergente,dulceambroso,fiado,fideos,galleta,huevosdepascua,InicioSesion,jugos,lavaloza,leche,maruchan,mediosdepago,pastadedientes,productos,quienessomos,registrarse,salsatomate,te,yoghurt          


urlpatterns = [
    path('', home, name="home"),
    path('vista_prod/<id_prod>/', vista_prod, name="vista_prod"),
    path('arroz/', arroz, name="arroz"),
    path('bebidas/', bebidas, name="bebidas"),
    path('busqueda/', busqueda, name="busqueda"),
    path('cafe/', cafe, name="cafe"),
    path('carritodecompras/', carritodecompras, name="carritodecompras"),
    path('chocolate/', chocolate, name="chocolate"),
    path('confort/', confort, name="confort"),
    path('desodoranteamb/', desodoranteamb, name="desodoranteamb"),
    path('detergente/', detergente, name="detergente"),
    path('dulceambroso/', dulceambroso, name="dulceambroso"),
    path('fiado/', fiado, name="fiado"),
    path('fideos/', fideos, name="fideos"),
    path('galleta/', galleta, name="galleta"),
    path('huevosdepascua/', huevosdepascua, name="huevosdepascua"),
    path('InicioSesion/', InicioSesion, name="InicioSesion"),
    path('jugos/', jugos, name="jugos"),
    path('lavaloza/', lavaloza, name="lavaloza"),
    path('leche/', leche, name="leche"),
    path('maruchan/', maruchan, name="maruchan"),
    path('mediosdepago/', mediosdepago, name="mediosdepago"),
    path('pastadedientes/', pastadedientes, name="pastadedientes"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registrarse/', registrarse, name="registrarse"),
    path('salsatomate/', salsatomate, name="salsatomate"),
    path('te/', te, name="te"),
    path('yoghurt/', yoghurt, name="yoghurt"),
    path('delivery/', delivery, name="delivery"),
    path('catalogo/', catalogo, name="catalogo"),
]
