maiz_grano = 285.55
pepino = 334.72
tomate_verde = 129
costo_envio = 1500

pedido_id = int (input("ingrese el ID del producto a vender: "))
print("pedidos mayores a 100 cajas incluye un costo de envio de $1500")
pedido_cajas = int(input("ingrese el numero de cajas a vender: ",))


if pedido_id == 1 and pedido_cajas >100:
  print("el producto es maiz en grano")
  print("el precio de la caja es 285.55")
  print("el costo total a pagar es: ", pedido_cajas * maiz_grano)
elif pedido_id == 1 and pedido_cajas <100:
  print("el producto es maiz en grano")
  print("el precio de la caja es de 285.55")
  print("el costo total del producto es: ", pedido_cajas * maiz_grano + costo_envio)

if pedido_id == 2 and pedido_cajas >100:
  print("el producto es pepino")
  print("el precio de la caja es 334.72")
  print("el costo total a pagar es: ", pedido_cajas * pepino)
elif pedido_id == 2 and pedido_cajas <100:
  print("el producto es pepino")
  print("el precio de la caja es de 334.72")
  print("el costo total del producto es: ", pedido_cajas * pepino + costo_envio)

if pedido_id == 3 and pedido_cajas >100:
  print("el producto es tomate verde")
  print("el precio de la caja es 129")
  print("el costo total a pagar es: ", pedido_cajas * tomate_verde)
elif pedido_id == 3 and pedido_cajas <100:
  print("el producto es tomate verde")
  print("el precio de la caja es de 129")
  print("el costo total del producto es: ", pedido_cajas * tomate_verde + costo_envio)

print("Su ID no es valido ingrese un ID del 1 al 3")