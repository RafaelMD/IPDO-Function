import logging
import pandas as pd
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Inicio')

    try:
        url = req.get_json().get('url')
        excel = pd.read_excel(url,sheet_name=1, header=None, usecols = "A:L") # http://sdro.ons.org.br/SDRO/DIARIO/2019_10_10/Html/DIARIO_10-10-2019.xlsx
        lista = []
        lista.extend(getValuesList("sin", excel.iloc[5:11, 1:5]))
        lista.extend(getValuesList("norte", excel.iloc[17:20, 2:6], False))
        lista.extend(getValuesList("nordeste", excel.iloc[17:21, 8:12], False))
        lista.extend(getValuesList("sudeste", excel.iloc[26:30, 8:12], False))
        lista.extend(getValuesList("sul", excel.iloc[35:38, 8:12], False))
        return func.HttpResponse(json.dumps(lista))
    except Exception:
        return func.HttpResponse("Erro", status_code=400)

def getValuesList(regiao, df, inverso = True):
    lista = []
    for item in df.values:
        objeto = {
            "regiao": regiao,
            "tipo" : item[0].strip(),
            "programado" : item[1] if inverso else item[3],
            "verificado" : item[2],
            "desvio": item[3] if inverso else item[1]
        }
        lista.append(objeto)
    return lista