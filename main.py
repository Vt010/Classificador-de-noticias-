import json

from grafo import Grafo
from preprocessamento import tokenizar
from classificador import ClassificadorNoticias


def carregarBaseTreino(caminhoJson):
    with open(caminhoJson, "r", encoding="utf-8") as f:
        return json.load(f)


def construirGrafoTreino(noticias):
    grafo = Grafo()

    for noticia in noticias:
        palavras = tokenizar(noticia["texto"])
        grafo.adicionarVertice(
            idTexto=noticia["id"],
            palavras=palavras,
            categoria=noticia["categoria"],
        )
        grafo.conectarATodos(noticia["id"])

    return grafo


def classificarTextoNovo(grafo, classificador, idTemporario, texto):
    palavras = tokenizar(texto)
    grafo.adicionarVertice(idTexto=idTemporario, palavras=palavras, categoria=None)
    grafo.conectarATodos(idTemporario)

    categoriaPrevista = classificador.classificar(idTemporario)
    vizinhosOrdenados = sorted(grafo.vizinhos(idTemporario).items(), key=lambda x: x[1], reverse=True)[:3]

    grafo.removerVertice(idTemporario)

    return categoriaPrevista, vizinhosOrdenados


def main():
    noticiasTreino = carregarBaseTreino("dados/noticias.json")
    grafo = construirGrafoTreino(noticiasTreino)
    classificador = ClassificadorNoticias(grafo)

    print(f"Grafo construído com {len(grafo)} textos de treino.\n")

    print("=" * 70)
    print("CLASSIFICADOR DE NOTÍCIAS POR GRAFO")
    print("=" * 70)
    print("Digite uma notícia para classificar (ou 'sair' para encerrar).\n")

    contadorTeste = 1
    while True:
        texto = input("Notícia: ").strip()

        if texto.lower() in ("sair", "exit", "q", ""):
            print("Encerrando.")
            break

        categoria, _ = classificarTextoNovo(
            grafo, classificador, f"teste_{contadorTeste}", texto
        )
        contadorTeste += 1

        print(f"  -> Categoria prevista: {categoria.upper() if categoria else 'INDEFINIDA'}\n")


if __name__ == "__main__":
    main()