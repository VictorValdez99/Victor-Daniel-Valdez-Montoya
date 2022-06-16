municipio1 =input("ingrese un municipio del estado de sinaloa: ")
poblacion1 = int(input('ingrese la poblacion del municipio: '))

municipio2 =input("ingrese un segundo municipio del estado de sinaloa: ")
poblacion2 = int(input('ingrese la poblacion del municipio: '))

municipio3 =input("ingrese un tercer municipio del estado de sinaloa: ")
poblacion3 = int(input('ingrese la poblacion del municipio: '))

municipios = [municipio1, municipio2, municipio3]
habitantes = [poblacion1, poblacion2, poblacion3]

total_habitantes= poblacion1 + poblacion2 + poblacion3
print("La poblacion total de los municipios seleccionados es: ", total_habitantes)

promedio_habitantes = poblacion1 + poblacion2 + poblacion3 / 3
print("El promedio de la poblacion de los municipios seleccionados es: ", promedio_habitantes)