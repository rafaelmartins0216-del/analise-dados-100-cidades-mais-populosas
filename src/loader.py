import pandas as pd


#Vamos utilizar essa função (le todos os formatos possíveis)
#Já transfroma em Data Frame
def carregar_arquivo(caminho: str):
    ext = str(caminho.split(".")[-1])

    if ext == "csv":
        return pd.read_csv(caminho)
    elif ext in ["xlsx", "xls"]:
        return pd.read_excel(caminho)
    elif ext == "json":
        return pd.read_json(caminho)
    else:
        raise ValueError(f"Formato não suportado: {ext}")
    

