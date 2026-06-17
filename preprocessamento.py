import re

#lista de stopwords em português, pode ser expandida conforme necessário ao observar os resultados do classificador.
STOPWORDS = {
    "a", "o", "e", "é", "de", "da", "do", "das", "dos", "em", "no",
    "na", "nos", "nas", "um", "uma", "uns", "umas", "para", "por",
    "com", "sem", "sob", "sobre", "entre", "até", "após", "ante",
    "que", "se", "como", "mas", "ou", "também", "já", "ainda",
    "muito", "mais", "menos", "tão", "quando", "onde", "quem",
    "qual", "quais", "este", "esta", "isso", "esse", "essa", "aquele",
    "aquela", "seu", "sua", "seus", "suas", "meu", "minha", "nosso",
    "nossa", "ele", "ela", "eles", "elas", "eu", "tu", "você", "nós",
    "vocês", "lhe", "lhes", "ao", "aos", "à", "às", "pelo", "pela",
    "pelos", "pelas", "num", "numa", "será", "foi", "são", "está",
    "estão", "ser", "estar", "ter", "tem", "têm", "havia", "houve",
}


def tokenizar(texto):

    #recebe um texto bruto e retorna um conjunto (set) de palavras relevantes (em minúsculas, sem pontuação e sem stopwords).

    texto = texto.lower()

    #mantem apenas letras e espaços.
    texto = re.sub(r"[^a-zà-ú\s]", " ", texto)

    palavras = texto.split()

    palavrasRelevantes = {p for p in palavras if p not in STOPWORDS and len(p) > 2}

    return palavrasRelevantes