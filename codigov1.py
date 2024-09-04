import math as m

print ("El problema es de:")
print( "1. Elipse meridiana")
print( "2. Elipsoide")

MenuUno= int(input("El problema es de:"))
if MenuUno==1:          
    print("Es problema inverso")
    print("1. SI     2. NO")   
    MenuInverso= int(input("seleccione"))
    if MenuInverso==1:
        
else:
     print("Cual es el angulo inical")
     print("1. w (omega)")
     print("2. 0 (Teta)")
     print("1. phi (latitud)")
     AnguloDado= int(input("seleccione"))
     if AnguloDado==1:
          a_=1