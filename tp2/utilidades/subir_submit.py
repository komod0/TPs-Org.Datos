def subir(archivo, mensaje, competicion="Inmuebles24"):
    """
    archivo: nombre del archivo, sin extension, el archivo en cuestion se debe encontrar en la carpeta de submits
    mensaje: Mensaje para adjuntar junto al submit
    competicion: nombre de la competicion, por defecto es la del tp

    Para poder ejecutar el script se debe tener instalado el modulo kaggle que se puede instalar mediante pip y
    haberse autenticado generando y ubicado donde corresponda el archivo kaggle.json, instruccion aca: \
            https://github.com/Kaggle/kaggle-api#api-credential
    """
    msj1 = "Asegurate de tener instalado kaggle crack, sino lo tenes usa algo como: pip install --user kaggle"
    msj2 = "Te olvidaste de generar el archivo de autenticacion para eso segui las instrucciones en: https://github.com/Kaggle/kaggle-api#api-credential"
    try:
        import kaggle
    except ModuleNotFoundError:
        raise ModuleNotFoundError(msj1)
    except OSError:
        raise OSError(msj2)
    sesion = kaggle.KaggleApi()
    sesion.authenticate()
    sesion.competition_submit(f"../submits/{archivo}.csv", mensaje, competicion)
    print("Score de cada submit hecho:\n")
    sesion.competition_submissions_cli(nombre)
    print("\nLeaderboard de la competicion\n")
    sesion.competition_leaderboard_cli(competicion, view=True)
