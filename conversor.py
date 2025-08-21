temperatura = float(input("Ingrese Temperatura:"))
escala = input("Es Fahrenheit(F) o es Celsius(C)?:").lower()

if escala == "f":
    celsiusc = (temperatura - 32) * 5/9
    print(celsiusc)
elif escala == "c":
    fahrenheit = temperatura * 1.8 * 32
    print(fahrenheit)
else:
    print("Escala Incorrecta")

# Prueba de cambio
# Segundo Cambio