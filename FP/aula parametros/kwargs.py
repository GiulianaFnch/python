# kwargs -> múltiplos argumentos nomeados (key=valor)

# kwargs -- captura argumentos nomeados extras num dicionário

def imprime_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

imprime_info(nome="Ana", idade=25, cidade="Lisboa")