import sys
import re

# Função para exibir o banner
def exibir_banner():
    banner = """
     _______  _______  _______  _______  _______  _______  _______
    (  __   )/  __   )/  __   )/  __   )/  __   )/  __   )/  __   )
    | (  )  |(  (   |(  (   |(  (   |(  (   |(  (   |(  (   |
    | | /   | | /    | | /    | | /    | | /    | | /    | | /    |
    | (/ /)  | |     | |     | |     | |     | |     | |     |
    |   |  | | |     | |     | |     | |     | |     | |     |
    |   |  | | |____ | |____  | |____ | |____ | |____ | |____  |
    |___|  |(_______)(_______)(_______)(_______)(_______)(_______)

     ____   ____   ____   ____
    |    | |    | |    | |    |
    |____| |____| |____| |____|

    """
    print(banner)
    print("Trader Ferraz")
    print("\n" + "="*50 + "\n")

# Função para filtrar a lista de acordo com emojis proibidos
def filtrar_lista(lista_original, emojis_proibidos):
    # Convertendo emojis proibidos para uma expressão regular eficiente
    regex_emoji = re.compile("|".join([re.escape(emoji) for emoji in emojis_proibidos]))

    # Filtra a lista removendo linhas que contêm qualquer emoji proibido
    lista_filtrada = [linha for linha in lista_original if not regex_emoji.search(linha)]

    return lista_filtrada

# Função principal
def main():
    exibir_banner()  # Exibe o banner
    print("Olá, seja bem-vindo!")
    print("Digite 1 para filtrar uma lista.")
    print("Digite 0 para sair.")

    while True:
        try:
            # Captura a escolha do usuário
            escolha = input("Escolha: ").strip()

            if escolha == '1':
                # Chama a função de filtro
                lista_original = obter_lista()  # Função para obter a lista de entrada
                emojis_proibidos = [
                    "⛔️", "🚫", "❌️", "✖️", "⛔ ",  # Emojis básicos
                    "⛔️¹", "⛔️²", " ⛔️", "✖️²", "✖️¹", "✖️ ",  # Emojis adicionais
                ]
                lista_filtrada = filtrar_lista(lista_original, emojis_proibidos)
                print("\nResultado: Lista filtrada")
                for linha in lista_filtrada:
                    print(linha)
                print("\nFiltragem concluída!\n")

            elif escolha == '0':
                print("Saindo do programa. Até logo!")
                sys.exit()  # Sai do programa
            else:
                print("Opção inválida! Tente novamente.")
        except KeyboardInterrupt:
            print("\nEncerrando o programa.")
            sys.exit()

# Função para obter a lista de entrada
def obter_lista():
    print("\nDigite ou cole sua lista de texto. Para finalizar, pressione ENTER duas vezes:")

    # Lista para armazenar as linhas inseridas
    lista_original = []
    while True:
        linha = input()  # Captura cada linha
        if linha == "":  # Duplo ENTER para finalizar
            break
        lista_original.append(linha)

    return lista_original

# Executa o programa principal
if __name__ == "__main__":
    main()
