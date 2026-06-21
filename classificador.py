from collections import Counter

from fila import Fila


class ClassificadorNoticias:
    def __init__(self, grafo):
        self.grafo = grafo

    def classificar(self, idTextoNovo):
        vizinhos = self.grafo.vizinhos(idTextoNovo)

        if not vizinhos:
            return None  #não há base suficiente para classificar

        pesoMaximo = max(vizinhos.values())

        #pega todas as categorias que possuem algum vizinho com o peso máximo encontrado
        categoriasNoTopo = set()
        for vizinhoId, peso in vizinhos.items():
            if peso == pesoMaximo:
                categoria = self.grafo.vertices[vizinhoId]["categoria"]
                categoriasNoTopo.add(categoria)

        #sem empate: uma única categoria
        if len(categoriasNoTopo) == 1:
            return categoriasNoTopo.pop()

        #empate entre categorias diferentes: desempata com BFS.
        return self.desempatarComBfs(idTextoNovo, categoriasNoTopo)

    def desempatarComBfs(self, idOrigem, categoriasCandidatas, niveis=2):
        visitados = {idOrigem}
        fila = Fila()
        fila.enfileirar((idOrigem, 0))  #(vértice, nível atual)

        contagemCategorias = Counter()

        while not fila.vazia():
            verticeAtual, nivelAtual = fila.desenfileirar()

            if nivelAtual >= niveis:
                continue

            for vizinhoId in self.grafo.vizinhos(verticeAtual):
                if vizinhoId in visitados:
                    continue

                visitados.add(vizinhoId)
                categoriaVizinho = self.grafo.vertices[vizinhoId]["categoria"]

                if categoriaVizinho is not None:
                    contagemCategorias[categoriaVizinho] += 1

                fila.enfileirar((vizinhoId, nivelAtual + 1))

        # Filtra apenas as categorias que estavam empatadas.
        contagemFiltrada = {
            categoria: contagemCategorias.get(categoria, 0)
            for categoria in categoriasCandidatas
        }

        categoriaVencedora = max(contagemFiltrada, key=contagemFiltrada.get)
        return categoriaVencedora
