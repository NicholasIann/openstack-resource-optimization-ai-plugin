import numpy as np
from sklearn.linear_model import LinearRegression

# Dati di esempio: carico di lavoro e risorse allocate
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([1, 2, 2, 3, 4, 4, 5, 6, 7, 8])

# Creiamo e alleniamo il modello
model = LinearRegression()
model.fit(X, y)

def optimize_resources():
    """Funzione per ottimizzare le risorse in base al carico di lavoro previsto."""
    user_input = input("Inserisci il carico di lavoro previsto (es. richieste di CPU): ")
    try:
        workload = float(user_input)
        recommended_resources = model.predict(np.array([[workload]]))
        print(f"Per un carico di lavoro di {workload}, si raccomandano {recommended_resources[0]:.2f} risorse.")
    except ValueError:
        print("Per favore, inserisci un numero valido.")
