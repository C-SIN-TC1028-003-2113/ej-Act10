# Conversiones

def equivalente(horas, minutos, segundos):
    minutosAsegundos = minutos * 60
    horasAsegundos = horas * 60 * 60

    totalsegundos = segundos + minutosAsegundos + horasAsegundos

    return totalsegundos
# Pedir datos para 1 proceso
def tiempoProceso(proceso):
    print(proceso)
    horas = int(input("Dame las horas del "+proceso+":"))
    minutos = int(input("Dame los minutos del "+proceso+":"))
    segundos = int(input("Dame los segundos del "+proceso+":"))

    print("Total de segundos del " +proceso + "=" + str(equivalente(horas,minutos, segundos)))

# Funcion principal
def main():
    #escribe tu código abajo de esta línea
    # (equivalente(2,20,8))

    tiempoProceso("Proceso-1")
    tiempoProceso("Proceso-2")
    

if __name__=='__main__':
    main()
