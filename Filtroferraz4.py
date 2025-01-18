import sys
import re
import argparse

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
    regex_emoji = re.compile("|".join([re.escape(emoji) for emoji in emojis_proibidos]))
    return [linha for linha in lista_original if not regex_emoji.search(linha)]

# Função para tratar argumentos da linha de comando
def tratar_argumentos():
    parser = argparse.ArgumentParser(description="Filtra uma lista de texto com emojis proibidos.")
    parser.add_argument("-l", "--lista", type=str, help="Caminho para o arquivo com a lista de texto", required=False)
    parser.add_argument("-e", "--emojis", type=str, nargs='+', help="Lista de emojis proibidos", required=False)
    args = parser.parse_args()
    return args

# Função para ler lista de arquivo
def ler_lista_de_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []

# Função para salvar a lista filtrada em um arquivo
def salvar_lista_em_arquivo(lista_filtrada, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.writelines([linha + '\n' for linha in lista_filtrada])
        print(f"Lista filtrada salva em {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função para exibir estatísticas da filtragem
def exibir_estatisticas(lista_original, lista_filtrada):
    removidos = len(lista_original) - len(lista_filtrada)
    print(f"Linhas totais: {len(lista_original)}")
    print(f"Linhas removidas: {removidos}")
    print(f"Linhas restantes: {len(lista_filtrada)}")

# Função principal
def main():
    args = tratar_argumentos()
    exibir_banner()  # Exibe o banner
    print("Olá, seja bem-vindo!")

    if args.lista:
        lista_original = ler_lista_de_arquivo(args.lista)
    else:
        lista_original = obter_lista()  # Função para obter a lista de entrada

    emojis_proibidos = args.emojis if args.emojis else [
        "⛔️", "🚫", "❌️", "✖️", "⛔ ",  # Emojis básicos
        "⛔️¹", "⛔️²", " ⛔️", "✖️²", "✖️¹", "✖️ ",  # Emojis adicionais
    ]

    lista_filtrada = filtrar_lista(lista_original, emojis_proibidos)
    exibir_estatisticas(lista_original, lista_filtrada)
    salvar_lista_em_arquivo(lista_filtrada, "lista_filtrada.txt")

    print("\nResultado: Lista filtrada")
    for linha in lista_filtrada:
        print(linha)

    print("\nFiltragem concluída!\n")

# Função para obter a lista de entrada
def obter_lista():
    print("\nDigite ou cole sua lista de texto. Para finalizar, pressione ENTER duas vezes:")
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
