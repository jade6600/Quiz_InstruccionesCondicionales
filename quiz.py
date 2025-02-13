# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = float(input("Digite el valor del lado a:"))
b = float(input("Digite el valor del lado b:"))
c = float(input("Digite el valor del lado c:"))
                
# processing and #output
if a + b <= c :
    print("No se puede formar un triangulo")
elif a + c <= b :
    print("No se puede formar un triangulo")
elif b + c <= a :
    print("No se puede formar un triangulo")
else : 
    print("Si se puede formar un triangulo")
pass

            
 
    

       
 

