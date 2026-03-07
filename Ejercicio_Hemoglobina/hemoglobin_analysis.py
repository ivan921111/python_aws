# hemoglobin_analysis.py
# Este script analiza la secuencia de la hemoglobina humana.
# Realiza cálculos de composición de aminoácidos, peso molecular y porcentaje de aminoácidos hidrofóbicos.

import json
import os

# Obtener el directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Leer la secuencia limpia
with open(os.path.join(script_dir, 'hemoglobin_clean.txt'), 'r') as file:
    sequence = file.read().strip()

# Información de la secuencia
print("Nombre de la proteína: Hemoglobina subunit beta [Homo sapiens]")
print(f"Longitud de la secuencia: {len(sequence)} aminoácidos")
print(f"Secuencia: {sequence}")

# Lista de aminoácidos únicos
amino_acids = list(set(sequence))
print(f"Aminoácidos únicos: {sorted(amino_acids)}")

# Conteo de aminoácidos
composition = {}
for aa in sequence:
    composition[aa] = composition.get(aa, 0) + 1
print("Composición de aminoácidos:")
for aa, count in sorted(composition.items()):
    print(f"{aa}: {count}")

# Pesos moleculares
weights = {
    'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.16,
    'Q': 146.15, 'E': 147.13, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
    'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
}

# Función para calcular peso molecular
def calculate_molecular_weight(seq, wt_dict):
    total_weight = 0.0
    for aa in seq:
        total_weight += wt_dict.get(aa, 0)
    return total_weight

molecular_weight = calculate_molecular_weight(sequence, weights)
print(f"Peso molecular calculado: {molecular_weight:.2f} Da")

# Aminoácidos hidrofóbicos
hydrophobic = ['A', 'V', 'I', 'L', 'M', 'F', 'W', 'Y']
hydrophobic_count = sum(composition.get(aa, 0) for aa in hydrophobic)
hydrophobic_percentage = (hydrophobic_count / len(sequence)) * 100
print(f"Porcentaje de aminoácidos hidrofóbicos: {hydrophobic_percentage:.2f}%")

# Guardar resultados en JSON
results = {
    "nombre_proteina": "Hemoglobina subunit beta [Homo sapiens]",
    "longitud_secuencia": len(sequence),
    "conteo_aminoacidos": composition,
    "peso_molecular": molecular_weight
}

with open(os.path.join(script_dir, 'hemoglobin_results.json'), 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Resultados guardados en hemoglobin_results.json en la siguiente ruta: '"+ script_dir+"'")