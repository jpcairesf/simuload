import csv
from datetime import datetime
import os

def csv_save_curve(horas,consumo,fornecimento,curve):
    path = create_folder(curve)
    tag = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"{path}/{curve}_{tag}.csv", "w") as f:
        fieldnames = ['horas', 'consumo', 'fornecimento']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for x, y, z in zip(horas, consumo, fornecimento):
            writer.writerow({'horas': x, 'consumo': y, 'fornecimento': z})

def csv_save_single_curve(horas,consumo,curve):
    path = create_folder(curve)
    tag = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"{path}/{curve}_{tag}.csv", "w") as f:
        fieldnames = ['horas', 'consumo']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for x, y in zip(horas, consumo):
            writer.writerow({'horas': x, 'consumo': y})
        
def create_folder(curve):
    if not os.path.exists(f"curvas/{curve}"):
        os.makedirs(f"curvas/{curve}")
    return f"curvas/{curve}"
    
    
    