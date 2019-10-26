def validar(X, y, metodo, transf=True):

    """
    X: datos de entrenamiento
    y: target de X
    metodo: Algoritmo a utilizar
    transf: Si aplicarle log al precio(normaliza el precio) antes de entrenar
    """
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import KFold
    import pandas as pd
    import numpy as np
    # Se hace K-fold cross-validation
    kfold = KFold(5, True, 42)
    for i, (train_index, test_index) in enumerate(kfold.split(X)):
        # Se parte el dataset en dos, train y test, con el train entreno
        # y con el test evaluo como predice mi algoritmo
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        if transf:
            y_train = np.log(y_train)
        # Me creo una instancia del modelo y luego lo entreno con los datos(con fit(X,y))
        reg_t = metodo()
        reg_t.fit(X_train, y_train)
        predicciones_t = reg_t.predict(X_test)
        if transf:
            predicciones_t = np.exp(predicciones_t)

        # Me fijo como me da el resultado
        print(f"Error de fold N°{i} es : {mean_absolute_error(y_test, predicciones_t)}")
