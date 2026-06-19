class Grafo:
    def __init__(self):
        #tabela hash: idTexto -> dados do vértice
        #cada vértice guarda a categoria (texto treino) e o conjunto de palavras-chave do texto.
        self.vertices = {}

        #lista de adjacência: idTexto -> { idVizinho: peso }
        #implementada como dicionário de dicionários (tabela hash aninhada), permitindo consultar o peso de uma aresta específica em tempo O(1).
        self.adjacencia = {}

    def adicionarVertice(self, idTexto, palavras, categoria=None):
        if idTexto in self.vertices:
            raise ValueError(f"Vértice '{idTexto}' já existe no grafo.")

        self.vertices[idTexto] = {
            "palavras": set(palavras),
            "categoria": categoria,
        }
        self.adjacencia[idTexto] = {}

    def calcularPeso(self, palavrasA, palavrasB):
        #calcula o peso da aresta entre dois textos: a quantidade de palavras que eles têm em comum.
        return len(palavrasA & palavrasB)

    def adicionarAresta(self, idA, idB, peso):
        if peso <= 0:
            return

        self.adjacencia[idA][idB] = peso
        self.adjacencia[idB][idA] = peso

    def conectarATodos(self, idTexto):
        palavrasNovo = self.vertices[idTexto]["palavras"]

        for outroId in list(self.vertices.keys()):
            if outroId == idTexto:
                continue

            palavrasOutro = self.vertices[outroId]["palavras"]
            peso = self.calcularPeso(palavrasNovo, palavrasOutro)
            self.adicionarAresta(idTexto, outroId, peso)

    def vizinhos(self, idTexto):
        
        return self.adjacencia.get(idTexto, {})

    def removerVertice(self, idTexto):
        if idTexto not in self.vertices:
            return

        for vizinhoId in list(self.adjacencia[idTexto].keys()):
            del self.adjacencia[vizinhoId][idTexto]

        del self.adjacencia[idTexto]
        del self.vertices[idTexto]

    def __len__(self):
        return len(self.vertices)