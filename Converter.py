import re

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

# Função para processar os sinais
def processar_lista(lista, timeframe):
    # Expressão regular para capturar os padrões sem caracteres especiais
    pattern = r"(\d{2}:\d{2})\s*([A-Z]{6})\s*(CALL|PUT)"
    resultados = []

    for linha in lista:
        # Procurar por correspondências na linha
        match = re.search(pattern, linha)
        if match:
            time, pair, direction = match.groups()
            # Montando a nova estrutura
            resultados.append(f"{time} {pair} {direction} {timeframe}")
    
    return resultados

if __name__ == "__main__":
    # Obtendo a lista de entrada
    lista_original = obter_lista()
    
    # Solicitando o timeframe
    timeframe = input("\nEscolha o timeframe (M1 ou M5): ").strip()
    if timeframe not in ["M1", "M5"]:
        print("\nErro: O timeframe deve ser 'M1' ou 'M5'.")
    else:
        # Processando a lista
        lista_convertida = processar_lista(lista_original, timeframe)
        
        # Exibindo os resultados no terminal
        print("\nLista convertida:")
        for linha in lista_convertida:
            print(linha)
