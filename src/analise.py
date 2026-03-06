import pandas as pd
import matplotlib.pyplot as plt

#resumo data frame , quantidade de linhas e colunas
def resumo(df: pd.DataFrame):
    return (
        "\nResumo:\n"
        f"Nossa tabela tem: {len(df)} linhas\n"
        f"Nossa tabela tem: {len(df.columns)} colunas\n"
        f"Nome das colunas: {list(df.columns)}"
    )


#Renomear as colunas para portugues para melhor entendimento
def renomear_colunas_pt_br(df: pd.DataFrame):
    df.columns=['Colocação',"Cidade","Pais","População","Area(KM)"]
    return df


#Desidade Demográfica
def densidade_demografica(df: pd.DataFrame):
    df = df.copy()
    df["População"] = df["População"].str.replace(",", "").astype(int)
    df["Area(KM)"] = df["Area(KM)"].str.replace(",", "").astype(int)
    df["Habitantes por km²"] = (df["População"] / df["Area(KM)"]).astype(int)
    return df


#cidades mais densas Demográficamente
def cidades_mais_densas(df: pd.DataFrame):
    df=densidade_demografica(df)
    df.sort_values("Habitantes por km²", ascending=False)
    return(
        f"Cidades mais Densas Demográficamente\n{df.head(10)}"
    )

#Gráfico densidade
def grafico_densidade(df: pd.DataFrame):
    df=densidade_demografica(df)
    df_sorted = df.sort_values(by="Habitantes por km²", ascending=False)
    top10 = df_sorted.head(10)
    # Criar gráfico
    plt.figure()
    plt.bar(top10["Cidade"], top10["Habitantes por km²"])

    # Títulos
    plt.title("Top 10 cidades mais densas (Habitantes por km²)")
    plt.xlabel("Cidade")
    plt.ylabel("Habitantes por km²")

    # Rotacionar nomes das cidades
    plt.xticks(rotation=45)

    # Ajustar layout
    plt.tight_layout()

    # Mostrar gráfico
    plt.show()


def grafico_habitantes(df: pd.DataFrame):

    df = densidade_demografica(df)

    df_ordenado = df.sort_values(by="Habitantes por km²", ascending=False)
    top10 = df_ordenado.head(10)

    # Cidade + país em linhas separadas
    labels = top10["Cidade"] + "\n" + top10["Pais"]

    plt.figure()

    plt.barh(labels, top10["Habitantes por km²"])

    plt.title("Top 10 cidades com maior densidade populacional")
    plt.xlabel("Habitantes por km²")
    plt.ylabel("Cidade / País")

    plt.tight_layout()
    plt.show()