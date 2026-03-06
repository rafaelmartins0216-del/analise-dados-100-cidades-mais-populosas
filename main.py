import os
from src.loader import carregar_arquivo
from src.analise import (
    resumo,
    renomear_colunas_pt_br,
    grafico_habitantes,
    densidade_demografica,
    cidades_mais_densas,
    grafico_densidade,
)


def menu():
    print("\n=== MENU INICIAL ===")
    print("1 - Começar Análise")
    print("2 - Sair")


def menu_analise():
    print("\n=== MENU ANÁLISE ===")
    print("1 - Resumo da tabela")
    print("2 - Densidade Demográfica")
    print("3 - Cidades Mais Densas")
    print("4 - Gráficos")
    print("5 - Voltar")


def menu_graficos():
    print("\n=== MENU GRÁFICOS ===")
    print("1 - Gráfico Densidade")
    print("2 - Gráfico Habitantes")
    print("3 - Voltar")


def executar_menu_analise(df):
    while True:
        menu_analise()
        op = input("Escolha: ").strip()

        if op == "1":
            print("\nResumo da tabela:")
            print(resumo(df))

        elif op == "2":
            print("\nHabitantes por Km²:")
            print(densidade_demografica(df).head(10))

        elif op == "3":
            print("\nCidades mais densas:")
            print(cidades_mais_densas(df))

        elif op == "4":
            executar_menu_grafico(df)

        elif op == "5":
            break

        else:
            print("Opção inválida")


def executar_menu_grafico(df):
    while True:
        menu_graficos()
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            grafico_densidade(df)

        elif op == "2":
            grafico_habitantes(df)

        elif op == "3":
            break

        else:
            print("Opção inválida")


def main():
    while True:
        menu()
        op = input("Escolha: ").strip()

        if op == "1":
            try:
                if os.name == "nt":  # Windows
                    caminho = "data\\Top 100 Worlds Largest Cities.csv"
                else:  # Linux / Mac
                    caminho = "data/Top 100 Worlds Largest Cities.csv"

                df = carregar_arquivo(caminho)
                print("Arquivo carregado com sucesso!")
                df = renomear_colunas_pt_br(df)
                executar_menu_analise(df)

            except Exception as e:
                print(f"Erro ao carregar arquivo: {e}")

        elif op == "2":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()