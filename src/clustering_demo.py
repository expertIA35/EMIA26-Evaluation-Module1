\"\"\"
Démonstration de K-Means pour la segmentation client
Basé sur le contexte de MesLivres.com
\"\"\"

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    \"\"\"Simulation de données clients pour démonstration\"\"\"
    
    print("=" * 50)
    print("DÉMONSTRATION K-MEANS - MESLIVRES.COM")
    print("=" * 50)
    
    # 1. Génération de données synthétiques
    print("\n1. Génération des données clients...")
    np.random.seed(42)
    n_clients = 4000
    
    data = {
        'frequence_achat': np.random.gamma(2, 2, n_clients),
        'panier_moyen': np.random.gamma(5, 10, n_clients),
        'temps_site': np.random.gamma(3, 20, n_clients),
        'taux_retour': np.random.beta(2, 5, n_clients),
        'anciennete': np.random.gamma(2, 3, n_clients)
    }
    
    df = pd.DataFrame(data)
    print(f"   ✓ {n_clients} clients générés")
    print(f"   ✓ Variables: {list(df.columns)}")
    
    # 2. Normalisation
    print("\n2. Normalisation des données...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    print("   ✓ Données normalisées")
    
    # 3. Entraînement avec K=4
    print("\n3. Entraînement du modèle K-Means (K=4)...")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['segment'] = kmeans.fit_predict(X_scaled)
    
    # 4. Analyse des segments
    print("\n4. Analyse des segments obtenus:")
    print("-" * 40)
    
    stats = df.groupby('segment').mean().round(2)
    print(stats)
    print("-" * 40)
    
    print("\n" + "=" * 50)
    print("DÉMONSTRATION TERMINÉE")
    print("=" * 50)
    
    return df

if __name__ == "__main__":
    df = main()
    df.to_csv("segmentation_resultats.csv", index=False)
    print("\n✓ Résultats sauvegardés")
