# Classificador de Notícias por Grafo

Trabalho da disciplina de Estrutura de Dados 2 — UnB.

## Descrição do problema

Sistema de classificação automática de notícias em categorias
(Esporte, Política, Moda e Investigação) utilizando uma representação
em grafo das relações entre os textos.

## Modelagem do grafo

- **Vértices:** cada notícia é um vértice do grafo.
- **Arestas:** não direcionadas, ligando todo par de textos. O peso
  da aresta é a quantidade de palavras em comum entre os dois textos.
- **Classificação de um texto novo:** o texto é inserido como vértice
  e conectado a todos os textos já existentes na base. A categoria do
  vizinho com a aresta de maior peso é atribuída ao novo texto.
- **Critério de desempate:** caso o maior peso esteja empatado entre
  categorias diferentes, é feita uma Busca em Largura(BFS) a partir
  do novo texto, e a categoria majoritária entre os "vizinhos dos vizinhos"
  é escolhida.

## Estrutura de dados adicional

Tabela hash(dicionário) utilizada na lista de adjacência do grafo,
garantindo acesso O(1) aos vizinhos de qualquer vértice. Também usada
no pré-processamento para contagem de palavras.

## Estrutura do projeto

```
.
├── dados/
│   └── noticias.json        #base de treino(notícias fictícias)
├── preprocessamento.py      #tokenização e remoção de stopwords
├── fila.py                  #fila implementada do zero(apoio à BFS)
├── grafo.py                 #estrutura de grafo(lista de adjacência)
├── classificador.py         #lógica de classificação + desempate BFS
├── main.py                  #modo interativo(digita notícia no terminal)
```

## Como executar

### Pré-requisitos
- Python 3.x instalado

### Passos

1. Clone o repositório
```
git clone https://github.com/Vt010/Classificador-de-noticias-
cd Classificador-de-noticias-
```
2. Execute o programa
```
python main.py
```
## Integrantes do grupo

- DANILO SARMENTO BARROS
- JOAO VITOR TAVARES DE SA LIMA (222006866)
- KAUA RICHARD DE SOUZA CAVALCANTE
- MARIO VINICIUS BELEZA CARNEIRO
- Nathan Pontes Romao
