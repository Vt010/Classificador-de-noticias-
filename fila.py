class Fila:
    def __init__(self):
        self.dados = []
        self.inicio = 0

    def enfileirar(self, item):
        self.dados.append(item)

    def desenfileirar(self):
        if self.vazia():
            raise IndexError("Fila vazia.")

        item = self.dados[self.inicio]
        self.inicio += 1

        if self.inicio > 64 and self.inicio > len(self.dados) // 2:
            self.dados = self.dados[self.inicio:]
            self.inicio = 0

        return item

    def vazia(self):
        return self.inicio >= len(self.dados)

    def __len__(self):
        return len(self.dados) - self.inicio