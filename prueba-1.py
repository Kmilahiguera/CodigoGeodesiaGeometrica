
import math

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

if x<0 and y<0:
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