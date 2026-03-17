---
marp: true
theme: uncover
size: 16:9
paginate: true
header: "Évaluation Module 1 - EMIA 26"
footer: "Bloc 1 & Bloc 2"
---

<!-- _class: lead -->
# Évaluation Module 1
## Bloc 1 : MesLivres.com
## Bloc 2 : SavoirPlus

---

## Bloc 1 - Contexte

**MesLivres.com**
- 4 000 clients
- Historique 12 mois
- Variables: fréquence, panier, catégories, temps, taux, canal, ancienneté
- Objectif: Segmentation client automatisée

---

## Q1 - Domaine IA

**Analyse de données structurées**
**Type de tâche: Clustering**

---

## Q2 - Modèle choisi

**K-Means**
- Algorithme non supervisé
- Partitionne en K groupes homogènes

---

## Q3 - Domaine IA correspondant

**Machine Learning classique**

---

## Q4 - Type d'apprentissage

**Non supervisé**
- Pas de labels
- Découverte automatique

---

## Q5 - Schéma

![width:900px](../images/schema_bloc1.png)

---

## Q6 - Réponse au directeur

**Avantages approche actuelle:**
- Simplicité
- Rapidité

**Limites:**
- 3 variables seulement
- Non évolutive

**Apports IA:**
- 7 variables analysées
- Mise à jour automatique

---

## Bloc 2 - SavoirPlus

**Contexte:**
- Résumés de réunions
- Transcription formateurs
- Proposition: fine-tuning Mistral 7B

---

## Q1 - Sources

1. Hugging Face Docs
2. Hu et al. - LoRA
3. Owen - Cost analysis

---

## Q2 - Analyse critique

**Alternative: Prompt Engineering + RAG**

| Critère | Fine-tuning | RAG |
|---------|-------------|-----|
| Coût | Élevé | Faible |
| Rapidité | Semaines | Jours |

---

## Q3 - Base de données

**Format JSONL:**
{ "input": "transcription", "output": "résumé" }

---

## Q4 - Contrer argument jargon

**Solution RAG:**
1. Détection acronymes
2. Recherche base connaissances
3. Prompt enrichi

---

## Q5 - Difficultés

**Risques:**
- Hallucinations
- Variabilité
- Confidentialité

**Processus Human-in-the-loop**

---

# Bibliographie

[1] Géron, A. Hands-On Machine Learning. O'Reilly, 2022.
[2] Hugging Face. Fine-tune a pretrained model.
