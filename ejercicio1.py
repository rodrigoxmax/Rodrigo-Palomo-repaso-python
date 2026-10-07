codigo_env:str="GL-921"
peso_or:float=14.5
Modalidad:bool=True
Volumen:float=0.048

def globallogic(codigo,peso,Mod,vol):
    pesok=round(peso*0.453592,2)
    pesof=None
    
    if Mod==True:
        pesof=round(pesok*9.80,2)
    else:
        pesof=round(pesok*5.20,2)
    print(f"Codigo de envio es: {codigo}")
    print(f"Peso en libras: {peso}")
    print(f"Peso en Kilogramos: {pesok} kg")
    print(f"Modalidad del paquete si es urgente: {Mod}")
    print(f"Volumen estimado: {vol} metros cubicos ")
    print(f"importe final: {pesof} euros ")


globallogic(codigo_env,peso_or,Modalidad,Volumen)




