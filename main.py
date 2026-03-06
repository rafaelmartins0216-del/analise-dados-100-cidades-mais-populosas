from src.loader import carregar_arquivo
from src.analise import resumo, renomear_colunas_pt_br, grafico_habitantes ,densidade_demografica, cidades_mais_densas,grafico_densidade

def menu():
    print("\n=== MENU INICIAL ===")
    print("1 - Enviar Arquivo")
    print("2 - Sair")

def menu_analise():
    print("\n=== MENU ANÁLISE ===")
    print("1 - Resumo da tabela")
    print("2 - Densidade Demográfica")
    print("3 - Cidades Mais densas")
    print("4 - Gráficos") #em desenvolvimento
    print("5 - Voltar")

def menu_graficos():
    print("\n=== MENU Gráficos ===")
    print("1 - Gráfico Densidade")
    print("2 - Gráfico Habitantes")
    print("3 - Sair")

def executar_menu_analise(df):
    while True:
        menu_analise()
        op = input("Escolha: ").strip()

        if op == "1":
            print(resumo(df))

        elif op == "2":
            print("Habitantes por Km²\n",densidade_demografica(df).head(10))

        elif op == "4":
            executar_menu_grafico(df)
            pass

        elif op == "3":
            print(cidades_mais_densas(df))

        elif op == "5":
            break

        else:
            print("Opção inválida")


def executar_menu_grafico(df):
    while True:
        menu_graficos()
        op=input("Escolha uma opção:")

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
                caminho = input("Digite o caminho da planilha: ").strip()
                df = carregar_arquivo(caminho)
                print("Arquivo carregado com sucesso!")
                df=renomear_colunas_pt_br(df)
                executar_menu_analise(df)
            except Exception as e:
                print(f"Erro ao carregar arquivo: {e}")

        elif op == "2":
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()