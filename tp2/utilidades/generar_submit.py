def generar_submit(X, y, metodo, test, nombre, transf=True, **kwargs):
    """
    X: datos de entrenamiento
    y: target de X
    metodo: Algoritmo a utilizar
    test: Datos a predecir
    nombre: Nombre para el csv a generar
    transf: Si aplicarle log-transform a los datos antes de predecir
    """
    import pandas as pd
    import numpy as np

    if transf:
        y = np.log(y)
    reg = metodo(**kwargs)
    reg.fit(X, y)

    test_ori = pd.read_csv("../data/test.csv")

    ids = test_ori["id"]
    y_pred = reg.predict(test)
    if transf:
        y_pred = np.exp(y_pred)

    submit = pd.DataFrame(y_pred, columns=["target"])
    submit.insert(0, "id", ids)
    submit.to_csv(f"submits/{nombre}.csv", index=False)
