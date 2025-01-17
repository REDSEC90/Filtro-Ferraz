# Função para filtrar os resultados com base em um critério
def filtrar_resultados(arquivo_entrada, arquivo_saida, filtro):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as file:
            linhas = file.readlines()  # Lê todas as linhas do arquivo
        
        resultados_filtrados = []
        
        for linha in linhas:
            elementos = linha.strip().split()  # Divide a linha em partes
            if len(elementos) < 4:
                continue  # Ignora linhas inválidas
            
            # Captura o campo [4], que é o último da linha
            resultado = elementos[-1]
            
            # Verifica se o resultado atende ao filtro
            if filtro in resultado:
                resultados_filtrados.append(linha.strip())
        
        # Salva os resultados filtrados em um novo arquivo
        with open(arquivo_saida, 'w', encoding='utf-8') as file_out:
            file_out.write('\n'.join(resultados_filtrados))
        
        print(f"Filtragem concluída! {len(resultados_filtrados)} resultados encontrados.")
        print(f"Resultados salvos no arquivo: {arquivo_saida}")
    
    except FileNotFoundError:
        print("Erro: O arquivo de entrada não foi encontrado!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Configuração
arquivo_entrada = "lista.txt"  # Nome do arquivo de entrada
arquivo_saida = "resultados_filtrados.txt"  # Nome do arquivo de saída
filtro = "✅"  # Resultado a ser filtrado (exemplo: "✅", "⛔️", etc.)

# Chamada da função
filtrar_resultados(arquivo_entrada, arquivo_saida, filtro)
