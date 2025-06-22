def pedir_cantidad_notas():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de notas: "))
            if cantidad > 1:
                break
            else:
                print("Debes ingresar al menos una nota.")
        except:
            print("Valor no valido. Solo puedes ingresar numeros.")
    return cantidad

cantidad = pedir_cantidad_notas()

def leer_nota():
    notas = []
    contador = 0
    while contador < cantidad:
        try:
            nota = float(input("Ingresa tus notas: "))
            if nota >= 1 and nota <= 7:
                notas.append(nota)
                contador += 1
            else:
                print('Debe ingresar una nota entre 1 y 7')
        except:
            print('Valor no válido. Intente nuevamente.')
    return notas

notas = leer_nota()
print(notas)