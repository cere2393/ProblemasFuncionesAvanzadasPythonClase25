def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

def main():
    # Solicitar entradas al usuario
    total_cuenta = float(input("Ingresa el total de la cuenta: "))
    porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))
    numero_personas = int(input("Ingresa el número de personas que compartirán la cuenta: "))

    # Calcular propina y total a pagar
    propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)

    # Calcular el monto que le corresponde a cada persona
    if numero_personas > 0:
        monto_por_persona = total_pagar / numero_personas
    else:
        monto_por_persona = total_pagar  # Si hay 0 personas, no tiene sentido dividir, se asume que es para una sola persona

    # Mostrar resultados
    print(f"Debes dejar una propina de: ${propina:.2f}")
    print(f"El total a pagar es: ${total_pagar:.2f}")
    print(f"Cada persona debe pagar: ${monto_por_persona:.2f}")

# Ejecutar el programa
main()
