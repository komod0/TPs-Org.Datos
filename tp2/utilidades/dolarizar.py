import pandas as pd
import numpy as np


def obtener_precios():
    dolar = pd.read_csv("data/precios_dolar.csv", names=["fecha", "valor"], parse_dates=["fecha"])

    # Me quedo con el precio del dolar promedio para cada mes
    # Convierto a el formato (anio, mes, dia)
    dolar["fecha"] = dolar["fecha"].apply(lambda x: (x.year, x.month,x.day))

    cotizacion = dolar.set_index("fecha")["valor"].to_dict()
    # Relleno los dias faltantes(los fines de semana no hay cotizacion)
    fechas_pos = list(pd.date_range(start="2012-1-1", end="2016-12-31"))
    for i in range(len(fechas_pos)):
        if not esta(fechas_pos[i], cotizacion):
            if i > 2:
                cotizacion[ymd(fechas_pos[i])] = cotizacion_ant(fechas_pos, i, cotizacion)
            else:
                cotizacion[ymd(fechas_pos[i])] = cotizacion_pos(fechas_pos, i, cotizacion)
    return cotizacion


def esta(fecha, dic):
    return ymd(fecha) in dic


def cotizacion_ant(fechas_pos, i, dic):
    while i >= 0 and not esta(fechas_pos[i], dic):
        i -= 1
    return dic[ymd(fechas_pos[i])]


def cotizacion_pos(fechas_pos, i, dic):
    while i < len(fechas_pos) and not esta(fechas_pos[i], dic):
        i += 1
    return dic[ymd(fechas_pos[i])]


def ymd(fecha):
    return (fecha.year, fecha.month, fecha.day)


def dolarizar(df):
    valor_dolar = obtener_precios()
    df["precio"] = df.apply(lambda x: x["precio"]/valor_dolar[(x["anio"], x["mes"], x["dia"])], axis=1)
    return df


def desdolarizar(df, y):
    df["precio"] = y
    valor_dolar = obtener_precios()
    df["precio"] = df.apply(lambda x: x["precio"]*valor_dolar[(x["anio"], x["mes"], x["dia"])], axis=1)
    return df["precio"].values
