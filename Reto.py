# Crear en python que me pida una fruta (1 manzana, 2 pina, 3 fresa)
# los precios de cada una son manzana $1, pina $3, fresa 5 $2
# deben pedir la cantidad
# y sacar el total

fruta = input("Que futa deea? seleccione 1 para manzana, 2 para pina o 3 para fresa:")
cantidad = int(input("Cuantas desea?"))

manzanaP = 1
pinaP = 3
fresaP = float(0.4)

if fruta == "1":
    total = cantidad * manzanaP
    print(f"su total es de {total}")

if fruta == "2":
    total = cantidad * pinaP
    print(f"su total es de {total}")

if fruta == "3":
    total = float(cantidad * fresaP)
    print(f"su total es de ${total:.2f}")


# Solucion adicion con else if (elif)
# if fruta == "1":
#     total = cantidad * 1.0
# elif fruta == "2":
#     total = cantidad * 3.0
# elif fruta == "3":
#     total = cantidad * 0.4
# print(f"total: {total:.2f}")
# else:
#     print("Error - intente de nuevo")


# Para un loop infinito
while True:
    print("-" * 80)
    fruta = input(
        "Que futa deea? seleccione 1 para manzana, 2 para pina o 3 para fresa:"
    )
    total1 = 0.0

    if fruta in "0123":
        if fruta == "0":
            break

        cantidad = int(input("Cuantas desea?"))

        if fruta == "1":
            total1 = cantidad * 1.0
        elif fruta == "2":
            total1 = cantidad * 3.0
        elif fruta == "3":
            total1 = cantidad * 0.4
    else:
        total1 = 0
        print("Error - intente de nuevo")

    print(f"total: {total1:.2f}")
    print("-" * 80)
