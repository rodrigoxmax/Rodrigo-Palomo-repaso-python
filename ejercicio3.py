
def calcular(longitudes_str):
    try:
        
        cadena=longitudes_str.split("x")
        if len(cadena)!=3:
            raise TypeError("Error: tiene que haber por lomnos 3 argumentos")
            return None

    
        alto=float(cadena[0])
        ancho=float(cadena[1])
        largo=float(cadena[2])

        if alto<=0 or ancho<=0 or largo<=0:
         raise ValueError("Error: tipo de dato invalido ")
            return None  
        resultado=alto*ancho*largo

        return round(resultado,2)
    except(ValueError,TypeError) as e:
       print(f"error: {e}")
    


casosdeprueba=[
    "50x40x30", 
    "15.5x20x10", 
    "50x40", 
    "50-40-30", 
    "ancho x alto",
    "50x-10x20"
]

for casos in casosdeprueba:
   resultado1=calcular(casos)
   print(f"Casos {casos} resultado {resultado1}")

    
