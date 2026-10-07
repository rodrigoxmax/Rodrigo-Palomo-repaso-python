manifiesto_carga = [
    {"id": 101, "destino": "Madrid", "peso_kg": 6.8, "fragil": True,
    "estado": "PENDIENTE"},
    {"id": 102, "destino": "Barcelona", "peso_kg": 3.2, "fragil": False,
    "estado": "EN_TRANSITO"},
    {"id": 103, "destino": "Madrid", "peso_kg": 8.4, "fragil": False,
    "estado": "PENDIENTE"},
    {"id": 104, "destino": "Sevilla", "peso_kg": 12.0, "fragil": True,
    "estado": "PENDIENTE"},
    {"id": 105, "destino": "Madrid", "peso_kg": 2.5, "fragil": True,
    "estado": "PENDIENTE"},
]
for m in manifiesto_carga:
    if m["destino"]=="Madrid" and m["peso_kg"] > 5.0:
        print(f" ids de los paquetes cuyo destino es Madrid y superan los 5.0 kg de peso {m['id']}")

totalfra:int=0
totalpesofra:float=0

for c in  manifiesto_carga:
    if c["fragil"]==True and c["estado"]=="PENDIENTE":
        totalfra=totalfra+1
        totalpesofra+=c["peso_kg"]

print(f" cantidad total de bultos fragiles es de {totalfra}")
print(f"El peso totall de esos bultos fragiles es de {totalpesofra:.2f}")