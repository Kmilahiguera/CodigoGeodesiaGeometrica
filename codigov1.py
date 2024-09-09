import math 

print("Escoga lo que desea calcular")
print("1. Elipsoide")
print("2. Elpise ")
print("3. Problema inverso")
print("4. Biseccion")
MenuUno= int(input("Escoja: "))
if MenuUno==1:
    print("Cual es el angulo inicial")
    print("1. Phi")
    print("2. Teta")
    print("3. w")
    MenuDos= int(input("Seleccione:  "))
    if MenuDos==1:
        print("Ingrese la Latitud:")
        graPhi = float(input("Grados: "))
        miPhi = float(input("Minutos: "))
        sePHI = float(input("Segundos: "))
        latPHI = graPhi+(miPhi/60)+(sePHI/3600)
        latPHI_rad=math.radians(latPHI)
        print("Ingrese la Longitud:")
        graLon = float(input("Grados: "))
        miLon = float(input("Minutos: "))
        seLon = float(input("Segundos: "))
        LonPHI = graLon+(miLon/60)+(seLon/3600)
        lonPHI_rad= math.radians(LonPHI)
        print("Ingrese el valor de a: ")
        a= float(input("Valor: "))
        print("Ingrese el valor de f^-1: ")
        f= float(input("Valor: "))
        print("Ingrese el valor de H: ")
        H= float(input("Valor: "))
        finv= 1/f
        e_cua = 2 * (finv) - (finv) ** 2
        w= math.sqrt(1 - (e_cua*math.sin(latPHI_rad)**2))
        N= a/w
        N_=N+H
        xgeod=N_*math.cos(latPHI_rad)*math.cos(lonPHI_rad)
        ygeod=(N_*math.cos(latPHI_rad)*(math.sin(lonPHI_rad)))
        zgeod=(N_*(1-e_cua)*(math.sin(latPHI_rad)))
       
        b=(a*math.sqrt(1-e_cua))
        tetaRadianes=math.atan((b/a)*math.tan(latPHI_rad))
        tetaGrados=math.degrees(tetaRadianes)
        xpar=a*math.cos(lonPHI_rad)

        print("==================================")
        print("COORDENADAS GEODESICAS")
        print(f"El valor de e es: {e_cua}")
        print(f"El valor de W es: {w}")
        print(f"El valor de N es: {N}")
        print(f"El valor de X es: {xgeod}")
        print(f"El valor de Y es: {ygeod}")
        print(f"El valor de Z es: {zgeod}")
        print("==================================")
        print("==================================")
        print("COORDENADAS PARAMETRICAS")
        print(f"El valor de teta es: {tetaGrados}")
        print(f"El valor de b es: {b}")
        print(f"El valor de a es: {a}")
        print(f"El valor de X es: {xgeod}")
        print(f"El valor de Y es: {ygeod}")
        print(f"El valor de Z es: {zgeod}")
        print("==================================")
        print("COORDENADAS GEOCENTRICAS")
        print(f"El valor de W es: {tetaGrados}")
        print(f"El valor de RGxyz es: {b}")
        print(f"El valor de a es: {a}")
        print(f"El valor de X es: {xgeod}")
        print(f"El valor de Y es: {ygeod}")
        print(f"El valor de Z es: {zgeod}")
        print("==================================")
if MenuUno==2:
    print("hola")

if MenuUno==3:
   
  print("Problema inverso :D")
  print("ingresa la coordenada en X con su respectivo signo:  ")
  x=float(input("Valor: "))
  print("ingresa la coordenada en y con su respectivo signo:  ")
  y=float(input("Valor: "))
  print("ingresa la coordenada en z con su respectivo signo:  ")
  z=float(input("Valor: "))
  print("ingresa la coordenada el valor de a:  ")
  a=float(input("Valor: "))
  print("ingresa la coordenada el valor de f:  ")
  finv=float(input("Valor: "))
  f=(1/finv)
  e_cua=(2*f)-(f**2)
  b=(a*math.sqrt(1-e_cua))
  e_prim= math.sqrt((a**2 - b**2) / b)
  Long=math.atan(y/x)
  Long_deg=math.degrees(Long)

  if x>0 and y>0:
    Long_deg= Long_deg
    long=abs(Long_deg)
    lonGra = int(long)
    longMin = int((long - lonGra) * 60)
    longSeg = (long - lonGra - longMin / 60) * 3600
    print("===================")
    print(f"El valor de Long en decimal es: {Long_deg}")               
    print(print(f"Longitud: {lonGra}° {longMin}' {longSeg:.2f}''""E"))

  if x>0 and y<0:
    Long_deg=Long_deg+90
    long=abs(Long_deg)
    lonGra = int(long)
    longMin = int((long - lonGra) * 60)
    longSeg = (long - lonGra - longMin / 60) * 3600
    print("===================")
    print(f"El valor de Long en decimal es: {Long_deg}")               
    print(print(f"Longitud: {lonGra}° {longMin}' {longSeg:.2f}''""E"))

  if x<0 and y>0:
    Long_deg=Long_deg+180
    long=abs(Long_deg)
    lonGra = int(long)
    longMin = int((long - lonGra) * 60)
    longSeg = (long - lonGra - longMin / 60) * 3600
    print("===================")
    print(f"El valor de Long en decimal es: {Long_deg}")               
    print(print(f"Longitud: {lonGra}° {longMin}' {longSeg:.2f}''""W"))

  if  x<0 and y<0:
    Long_deg=Long_deg+90
    long=abs(Long_deg)
    lonGra = int(long)
    longMin = int((long - lonGra) * 60)
    longSeg = (long - lonGra - longMin / 60) * 3600
    print("===================")
    print(f"El valor de Long en decimal es: {Long_deg}")               
    print(print(f"Longitud: {lonGra}° {longMin}' {longSeg:.2f}''""W"))

  gamma = math.atan2(z, math.sqrt(x**2 + y**2))
  gamma_degrees = math.degrees(gamma)

  phi = math.atan(
    (z + (e_prim**2 * math.sin(gamma)**3)) / 
    (math.sqrt(x**2 + y**2) - (e_cua * a * math.cos(gamma)**3))
  )

  phideg=math.degrees(phi)
  lat=abs(phideg)
  latgra = int(lat)
  latmin = int((lat - latgra) * 60)
  latseg = (lat - latgra - latmin / 60) * 3600
  print("===================")
  print(f"El valor de Lat en decimal es: {phideg}")               
  print(print(f"Latitud: {latgra}° {latmin}' {latseg:.2f}''"))
  radG=(math.sqrt((x**2)+(y**2)+(z**2)))

  w= math.sqrt(1 - (e_cua*math.sin(phi)**2))
  N= a/w

  alth=((math.sqrt((x**2 )+ (y**2)))/(math.cos(phi)))-N

  print(f"El valor de N : {N}") 
  print(f"El valor de altura : {alth}") 
  print(f"El valor del radio Geocentrico : {radG}") 

if MenuUno==4:
    print("ingresa el valor de NA:  ")
    NA=float(input("Valor: "))
    print("ingresa el valor de EA:  ")
    EA=float(input("Valor: "))
    print("ingresa el valor de NB:  ")
    NB=float(input("Valor: "))
    print("ingresa el valor de EB:  ")
    EB=float(input("Valor: "))
    print("ingresa el valor de ALPHA (ang de a):  ")
    AlP=float(input("Valor: "))
    print("ingresa el valor de BETA (ang de b):  ")
    BET=float(input("Valor: "))

    AlP_rad = math.radians(AlP)
    BET_rad = math.radians(BET)

    cot_alpha = 1 / math.tan(AlP_rad)
    cot_beta = 1 / math.tan(BET_rad)
    print(f"cot_alpha: {cot_alpha}")
    print(f"cot_beta: {cot_beta}")


    numerador = (EA - EB) + (NA * cot_beta) + (NB * cot_alpha)
    denominador = cot_alpha + cot_beta

    NP = numerador / denominador
    print(f"El valor de la norte del punto P es: {NP}")


    numerador2 = (NB - NA) + (EA * cot_beta) + (EB * cot_alpha)
    denominador2 = cot_alpha + cot_beta


    EP = numerador2 / denominador2
    print(f"El valor del este del punto P es: {EP}")