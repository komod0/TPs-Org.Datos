def limpiar(df):
    import pandas as pd
    # df.insert(3, "mes", pd.to_datetime(df["fecha"]))
    # df["mes"] = df["mes"].dt.year
    datos_categoricos = df[["tipodepropiedad", "provincia"]].copy()

    datos_categoricos["tipodepropiedad"] = datos_categoricos["tipodepropiedad"].fillna(datos_categoricos["tipodepropiedad"].mode()[0])
    datos_categoricos["provincia"] = datos_categoricos["provincia"].fillna(datos_categoricos["provincia"].mode()[0])
    datos_categoricos = pd.get_dummies(datos_categoricos)

    for column in ["garages", 'banos', 'habitaciones', 'gimnasio', 'usosmultiples', 'piscina', 'escuelascercanas', 'centroscomercialescercanos']:
        df[column] = df.groupby(['provincia', 'tipodepropiedad'])[column].apply(lambda x: x.fillna(x.mode()))
        df[column] = df[column].fillna(df[column].mode()[0])
        #df[column].fillna(df[column].mode()[0], inplace=True)

    for column in ['antiguedad', 'metroscubiertos', 'metrostotales']:
        df[column] = df.groupby(['provincia', 'tipodepropiedad'])[column].apply(lambda x: x.fillna(x.median()))
        df[column] = df[column].fillna(df[column].median())

    df = df.drop(["titulo", "descripcion", "direccion", "ciudad", "lat", "lng", "fecha", "idzona", "id", "tipodepropiedad", 'provincia'], axis=1)

    df = pd.concat([datos_categoricos, df], axis=1)

    #for colum in ["tipodepropiedad", "provincia"]:
    #    le = LabelEncoder()
    #    le.fit(df[colum])
    #    df[colum] = le.transform(df[colum])

    return df
