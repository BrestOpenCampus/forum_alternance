import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    with open(csv_file_path, mode='r', encoding='utf-8-sig', newline='') as csv_file:
        header_line = csv_file.readline().strip().rstrip(';')
        fieldnames = header_line.split(';')

        csv_reader = csv.DictReader(csv_file, delimiter=';', fieldnames=fieldnames)

        for row in csv_reader:
            row = {k: (v if v is not None else "") for k, v in row.items() if k not in (None, "")}

            if not any(str(v).strip() for v in row.values()):
                continue

            postes_raw = (row.get("Liste poste") or "").strip()
            postes = [p.strip() for p in postes_raw.split("|") if p.strip()] if postes_raw else []

            desc_raw = row.get("Description") or ""
            description = desc_raw.replace("\n", " ").replace("\r", " ").strip()

            nb_raw = (row.get("Nb poste") or "").strip()
            nb_poste = int(nb_raw) if nb_raw.isdigit() else 0

            data.append({
                "Ville": (row.get("Ville") or "").strip(),
                "Ecole": (row.get("Ecole") or "").strip(),
                "Entreprise": (row.get("Entreprise") or "").strip(),
                "URL Entreprise": (row.get("URL Entreprise") or "").strip(),
                "Logo entreprise": (row.get("Logo entreprise") or "").strip(),
                "Horaire présence": (row.get("Horaire présence") or "").strip(),
                "Evenement": (row.get("Evenement") or "").strip(),
                "Nb poste": nb_poste,
                "Liste poste": postes,
                "Description": description
            })

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Fichier JSON généré : {json_file_path} ({len(data)} entrées)")

csv_file_path = 'BDD_Forum_Alt_OC.csv'
json_file_path = 'BDD_Formu_Alt_OC.json'
csv_to_json(csv_file_path, json_file_path)
