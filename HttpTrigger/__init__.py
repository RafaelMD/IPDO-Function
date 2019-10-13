import logging
import pandas as pd
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Inicio')

    try:
        url = req.get_json().get('url')
        excel = pd.read_excel(url,sheet_name="IPDO", header=None, usecols = "K:X") # https://drive.google.com/uc?authuser=0&id=1bz6wcKcc6wY4xSRmGLvjJpCdPxgs7Ea1&export=download

        objeto = {
            "atributo" : excel[10][7],
            "valor1" : excel[12][7],
            "valor2" : excel[14][7]
        }

        return func.HttpResponse(json.dumps(objeto))
    except Exception:
        return func.HttpResponse(
             "Erro",
             status_code=400
        )
