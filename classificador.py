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

        nivelEmAnalise = 1
        contagemNivel = Counter()

        while not fila.vazia():
            verticeAtual, nivelAtual = fila.desenfileirar()

            if nivelAtual >= niveis:
                continue

            for vizinhoId in self.grafo.vizinhos(verticeAtual):
                if vizinhoId in visitados:
                    continue

                visitados.add(vizinhoId)
                categoriaVizinho = self.grafo.vertices[vizinhoId]["categoria"]
                proximoNivel = nivelAtual + 1

                if proximoNivel > nivelEmAnalise:
                    vencedora = self.obterVencedora(contagemNivel, categoriasCandidatas)
                    if vencedora is not None:
                        return vencedora

                    nivelEmAnalise = proximoNivel
                    contagemNivel = Counter()

                if categoriaVizinho is not None:
                    contagemNivel[categoriaVizinho] += 1

                fila.enfileirar((vizinhoId, proximoNivel))

        vencedora = self.obterVencedora(contagemNivel, categoriasCandidatas)
        if vencedora is not None:
            return vencedora

        vencedora = self.desempatarPorSomaPesosDiretos(idOrigem, categoriasCandidatas)
        if vencedora is not None:
            return vencedora

        return sorted(categoriasCandidatas)[0]

    def obterVencedora(self, contagemCategorias, categoriasCandidatas):
        contagemFiltrada = {
            categoria: contagemCategorias.get(categoria, 0)
            for categoria in categoriasCandidatas
        }

        maiorContagem = max(contagemFiltrada.values())
        categoriasVencedoras = [
            categoria
            for categoria, contagem in contagemFiltrada.items()
            if contagem == maiorContagem
        ]

        if maiorContagem > 0 and len(categoriasVencedoras) == 1:
            return categoriasVencedoras[0]

        return None

    def desempatarPorSomaPesosDiretos(self, idOrigem, categoriasCandidatas):
        somaPorCategoria = Counter()

        for vizinhoId, peso in self.grafo.vizinhos(idOrigem).items():
            categoria = self.grafo.vertices[vizinhoId]["categoria"]

            if categoria in categoriasCandidatas:
                somaPorCategoria[categoria] += peso

        return self.obterVencedora(somaPorCategoria, categoriasCandidatas)
