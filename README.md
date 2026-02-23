# forum_alternance

## 1. Objectif global

Transformer un fichier **CSV** (base de données du forum alternance) en fichier **JSON** exploitable par le site, puis remplacer le fichier `content.json` du dépôt GitHub par le JSON généré.

Le script Python `Convertiseur.py` automatise cette conversion.

---

## 2. Prérequis

- Python installé sur le poste (commande `py` fonctionnelle)
- Accès au dépôt GitHub du projet
- Fichier CSV conforme

---

## 3. Structure des fichiers

Les fichiers suivants doivent se trouver **dans le dossier Webmarketing / Site Web / Plaquette_Forum_ALT** sur le réseau :

- `Convertiseur.py`
- `BDD_Forum_Alt_OC.csv`

Après conversion, le script génère automatiquement :

- `BDD_Formu_Alt_OC.json`

⚠️ Les noms de fichiers doivent être **strictement identiques**  
(majuscules, underscores, orthographe).

---

## 4. Format du fichier CSV

Lors de l’enregistrement ou de l’export du CSV :

- Séparateur : `;` (point-virgule)
- Encodage : **UTF-8**
- La première ligne doit contenir les en-têtes
- Une ligne = une entreprise / une offre

Colonnes attendues :

`Ville`;`Ecole`;`Entreprise`;`URL Entreprise`;`Logo entreprise`;`Horaire présence`;`Evenement`;`Nb poste`;`Liste poste`;`Description`

---

## 5. Lancer la conversion

1. Ouvrir un terminal (VS Code ou PowerShell)
2. Se placer dans le dossier contenant les fichiers **Webmarketing / Site Web / Plaquette_Forum_ALT**
3. Lancer la commande :

```bash
py Convertisseur.py
```

---

## 6. Résultat attendu

- Message dans le terminal :
```bash
Fichier JSON généré : BDD_Formu_Alt_OC.json (X entrées)
```
- Apparition /mise à jours du fichier `BDD_Formu_Alt_OC.json`

Vérifications rapides :
- le fichier commence par `[` et se termine par `]`
- `Nb poste` est un nombre
- `Liste poste` est une liste

---

## 7. Mise à jour du site (GitHub)

Le site utilise le fichier `content.json`.

Procédure recommandée :

1. Copier le contenu du fichier `BDD_Formu_Alt_OC.json`
2. Le coller dans le contenu du fichier `content.json` sur GitHub

---

## 8. Erreurs courantes

- **Fichier introuvable**  
  → Le fichier CSV est absent du dossier ou à un mauvais nom

- **JSON vide / 0 entrées**  
  → Il y a un souvent un problement au niveau du séparateur dans le fichier CSV (`,` au lieu de `;`)  
  → Ou alors le CSV à mal été exporté

- **Accents cassés**  
  → Le CSV n'a pas été encodé en UTF-8
