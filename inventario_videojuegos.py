"""
CONTROL DE INVENTARIO DE UNA TIENDA DE VIDEOJUEGOS
Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay que reponerlo.
El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, mostrar si se necesita hacer un nuevo pedido o no.
"""

stock_valorant = int(input("Ingrese la cantidad actual en stock de Valorant: "))

if stock_valorant >= 50:
    print("Tenemos muchas copias del juego")
elif stock_valorant < 50 and stock_valorant >= 10:
        print("Tenemos copias del juego")
elif stock_valorant >= 1 and stock_valorant < 10:
        print("Tenemos pocas copias del juego")
else:
        print("Hay que reponer stock del juego, ya que se acabaron las copias.")