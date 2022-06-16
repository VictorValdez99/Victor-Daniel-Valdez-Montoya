capacidad_camion = 3254
capacidad_camion_min = 1627
costal_yeso = 40
costal_cemento = 30

pedido_yeso = int(input("ingrese la cantidad de costales de yeso: "))
peso_total_yeso = pedido_yeso * costal_yeso
pedido_cemento = int(input("ingrese la cantidad de costales de cemento: "))
peso_total_cemento = pedido_cemento * costal_cemento


peso_totalpedido = peso_total_yeso + peso_total_cemento
print("El peso total de su pedido es: ", peso_totalpedido)

if peso_totalpedido > capacidad_camion_min:
  print ("True")
elif peso_totalpedido > capacidad_camion:
  print ("False")