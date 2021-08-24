# Calcula el area de un rectangulo----
def areaRect(largo, ancho):
    area = largo * ancho
    return area
# Calcula el perimetro de un rectangulo---
def perimetroRect(largo, ancho):
    perimetro = 2 * (largo + ancho)
    return perimetro

def main():
    largo = float(input("Dame el largo: "))
    ancho = float(input("Dame el ancho: "))

    respuesta = input("¿Que deseas calcular (a)Area (p)Perimetro?")

    if respuesta == 'a' or respuesta == 'A':
        print("El area del rectangulo es: " + str(areaRect(largo, ancho)))
    elif respuesta == 'p' or respuesta == 'P':
        print("El perimetro del rectangulo es: " + str(perimetroRect(largo, ancho)))
    else:
        print("Respuesta incorrecta")


if __name__=='__main__':
    main()
