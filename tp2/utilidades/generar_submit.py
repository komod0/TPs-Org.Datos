def generar_submit(X, y, metodo, test, nombre, transf=True):
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
    from utilidades.limpiar import limpiar

    if transf:
        y = np.log(y)
    reg = metodo()
    reg.fit(X, y)

    ids = test["id"]
    test = limpiar(test)
    y_pred = reg.predict(test)
    if transf:
        y_pred = np.exp(y_pred)

    submit = pd.DataFrame(y_pred, columns=["target"])
    submit.insert(0, "id", ids)
    submit.to_csv(f"submits/{nombre}.csv", index=False)
