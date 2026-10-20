registro=[
    ("GL-1001", "Valencia", 4.50, 23.40),
    ("GL-1002", "Bilbao", 12.80, 66.56),
    ("GL-1003", "Zaragoza", 1.20, 6.24),
    ("GL-1004", "Sevilla", 7.60, 39.52)
]
with open("auditoria_envios.csv","w") as a:
    for codigo,ciudad , peso ,precio in registro:
        a.write(f"{codigo},{ciudad},{peso},{precio}\n")
      


with open("auditoria_envios.csv","r") as a:
    envios=0
    kgtotal=0
    codigo2=""
    ciudad2=""
    peso2=0
    precio2=0
    pesof=0
    costef=0
    coste2=0
    for linea in a:
        codigo2,ciudad2,peso2,precio2=linea.split(",")
        pesof=float(peso2)
        costef=float(precio2)
        kgtotal=kgtotal+pesof
        coste2=coste2+costef

        print(linea.strip())
        envios=envios+1
costexkg=coste2/kgtotal 

print (f"Cantidad de envios leidos: {envios}")
print (f"peso global de los paquetes: {kgtotal:.2f}")
print (f"elcoste total porkilogramo es de : {costexkg:.2f}")
