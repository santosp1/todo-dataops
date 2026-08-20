import json
import sys
from pathlib import Path


def resumir_dados(dados):
    print("Resumo do JSON")
    print("-" * 30)

    if isinstance(dados, dict):
        print(f"Tipo: objeto")
        print(f"Quantidade de campos: {len(dados)}")
        print("Campos:")

        for chave, valor in dados.items():
            tipo = type(valor).__name__
            print(f"  - {chave}: {tipo}")

    elif isinstance(dados, list):
        print(f"Tipo: lista")
        print(f"Quantidade de itens: {len(dados)}")

        if dados:
            tipos = {}

            for item in dados:
                nome_tipo = type(item).__name__
                tipos[nome_tipo] = tipos.get(nome_tipo, 0) + 1

            print("Tipos encontrados:")

            for tipo, quantidade in tipos.items():
                print(f"  - {tipo}: {quantidade}")

            primeiro_item = dados[0]

            if isinstance(primeiro_item, dict):
                campos = set()

                for item in dados:
                    if isinstance(item, dict):
                        campos.update(item.keys())

                print("Campos encontrados nos objetos:")
                for campo in sorted(campos):
                    print(f"  - {campo}")

    else:
        print(f"Tipo de dado: {type(dados).__name__}")
        print(f"Valor: {dados}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python resumo_json.py arquivo.json")
        sys.exit(1)

    caminho = Path(sys.argv[1])

    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho}' não foi encontrado.")
        sys.exit(1)

    except json.JSONDecodeError as erro:
        print(f"Erro: o arquivo não contém um JSON válido.")
        print(f"Linha {erro.lineno}, coluna {erro.colno}.")
        sys.exit(1)

    except OSError as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        sys.exit(1)

    resumir_dados(dados)


if __name__ == "__main__":
    main()
