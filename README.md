# 🛍️ Analyse du comportement d’achat des clients

Ce projet explore les habitudes de dépenses des clients d'une boutique en ligne à l'aide de statistiques descriptives, de visualisations et d'analyses de corrélation. Il vise à fournir des insights exploitables pour améliorer les stratégies marketing, le placement de produits et les offres promotionnelles.

---

## 📦 Contenu du projet

- `shopping_trends.csv` : Données transactionnelles clients
- `analyse_clients.ipynb` : Notebook d’analyse statistique
- `dashboard.py` : Interface Streamlit interactive
- `requirements.txt` : Liste des dépendances

---

## 🧠 Objectifs

1. Comprendre les tendances d’achat par segment (sexe, type de client, saison)
2. Identifier les variables les plus influentes sur le montant dépensé
3. Visualiser les distributions et les corrélations
4. Proposer des recommandations basées sur les données

---

## 🧪 Méthodologie

### 1. Chargement et nettoyage des données

- Suppression des valeurs manquantes
- Conversion des dates
- Identification des variables quantitatives et qualitatives

### 2. Statistiques descriptives

- Moyenne, médiane, mode
- Écart, variance, écart-type, IQR

### 3. Visualisations

- Histogrammes des montants d’achat
- Boîtes à moustaches par sexe
- Graphiques à barres par jour
- Nuages de points entre variables

### 4. Corrélations

- Corrélation de Pearson entre :
- Montant total et nombre d’articles
- Âge et montant total

---

## 📊 Exemple de résultats

| Métrique              | Valeur moyenne |
|---------------------  |----------------|
| Purchase Amount (USD) | 74.50 €        |
| Previous Purchases    | 3.2            |
| Age                   | 35.6 ans       |

- Les clients du segment "Premium" dépensent en moyenne 25% de plus
- Forte corrélation entre nombre d’articles et montant total (r = 0.82)

---

## 🚀 Lancer le dashboard Streamlit

```bash
streamlit run dashboard.py

🙋🏽‍♂️ Auteur
Koffi Modeste Konan
📍 Côte d’Ivoire, # 🔹DataCityIvoire

---
 💼.


