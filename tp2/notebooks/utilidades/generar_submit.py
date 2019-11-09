def generar_submit(X, y, metodo, test, nombre, **kwargs):
    """
    X: datos de entrenamiento
    y: target de X
    metodo: Algoritmo a utilizar
    test: Datos a predecir
    nombre: Nombre para el csv a generar
    """
    import pandas as pd
    import numpy as np

    y = np.log(y)
    reg = metodo(**kwargs)
    reg.fit(X, y)

    test_ori = pd.read_csv("../data/test.csv")
    # Generar un csv que tenga solo los ids
    ids = test_ori["id"]
    y_pred = reg.predict(test)
    y_pred = np.exp(y_pred)

    submit = pd.DataFrame(y_pred, columns=["target"])
    submit.insert(0, "id", ids)
    submit.to_csv(f"submits/{nombre}.csv", index=False)
