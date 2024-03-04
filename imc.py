import sys

peso=int(sys.argv[1])
talla=int(sys.argv[2])

talla=talla/100

IMC=(peso/((talla)**2))

Imc2=round(IMC,2)
print(f"su IMC es {Imc2}")

if Imc2<18.5:
    print("La clasificacion OMS es Bajo peso")
elif Imc2>=18.5 and Imc2<25:
    print("La clasificacion OMS es Adecuado")
elif Imc2>=25 and Imc2<30:
    print("La clasificacion OMS es Sobrepeso")
elif Imc2>=30 and Imc2<35:
    print("La clasificacion OMS es Obesidad Grado I")
elif Imc2>=35 and Imc2<40:
    print("La clasificacion OMS es Obesidad Gado II")
else:
    print("La clasificacion OMS es Obesidad Gado III")
    

