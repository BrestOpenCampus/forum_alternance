import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = {}

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for index, row in enumerate(csv_reader):
            try:
                postes = [poste.strip() for poste in row["Liste poste"].split("|")] if row["Liste poste"] else []
                description = row["Description"].replace("\n", " ").replace("\r", " ") if row["Description"] else ""

                data[index] = {
                    "Ville": row["Ville"],
                    "Ecole": row["Ecole"],
                    "Entreprise": row["Entreprise"],
                    "URL Entreprise": row["URL Entreprise"],
                    "Logo entreprise": row["Logo entreprise"],
                    "Horaire présence": row["Horaire présence"],
                    "Evenement": row["Evenement"],
                    "Nb poste": len(postes),
                    "Liste poste": postes,
                    "Description": description
                }
            except Exception as e:
                print(f"Erreur lors du traitement de la ligne {index + 1}: {e}")

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Fichier JSON généré : {json_file_path}")

csv_file_path = 'BDD_Forum_Alt_OC.csv'
json_file_path = 'BDD_Formu_Alt_OC.json'
csv_to_json(csv_file_path, json_file_path)