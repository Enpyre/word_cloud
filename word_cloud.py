import os
from os import path
from wordcloud import WordCloud

directory = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

excluded_words = ["de", "a", "não", "que", "e", "o", "é", "uma", "por", "um", "em", "na", "com", "da", "se", "os", "as", "foi", "era", "sem", "eu", "mais", "no", "dos", "muito", "além", "sempre", "colocar", "outras", "acho", "seja", "alunos", "só", "são", "algumas", "suas", "forma", "bem", "me", "parte", "pra", "nada", "acredito", "maneira", "bastante", "todos", "até", "pelo", "apc,", "nunca", "importante,", "do", "necessário", "tão", "você", "conhecidas", "ainda,", "/", "cada", "faz,", "especificamente,", "também,", "onde", "etc", "programar", "pythonic", "como", "vinha", "desses", "caras,", "passado", "tinha", "super,", "deu", "bugada", "legal", "época", "quando", "chegou", "tentar", "manter", "vez", "pede", "termos", "grandes,", "repetitivos", "padrões", "funcionais", "entraves", "psicológicos", "criados", "durante", "graduação", "relação", "infelizmente,", "cheguei", "faculdade", "tive", "suporte,", "péssimo", "professor", "aplicava", "medo", "ensinava", "direito", "ter", "background", "apresentada", "pros", "calouros", "equivocada.", "aplicações", "específicas,", "limitar", "quantidade", "sinceramente,", "das", "linguagens", "programação", "estudar.", "entanto,", "momento,", "tenho", "recursivas", "anônimas", "(lambda).", "aulas", "rápidas", "objetivas", "vão", "direto", "ao", "ponto", "enrolação", "\"independente", "minhas", "maiores", "dificuldades,", "códigos.", "que,", "exigido", "mas,", "disciplina", "nas", "provas,", "permitido", "consulta.", "então,", "certa", "forma,", "precisavam", "ter,", "memorizada,", "caso", "python.", "disso,", "mesmo,", "gostei", "nada.", "achei,", "pessoa", "ser", "capaz,", "processar", "informação,", "ela", "qual", "for.", "repetir,", "papagaio", "faz!", "gostei,", "ver", "meus", "estudos,", "depois", "pegam", "disciplina,", "chamada", "ed(estrutura", "dados).", "maioria", "alunos,", "fizeram", "crud", "vida,", "página", "html/css,", "javascript", "ou", "qualquer", "outra", "coisa", "deixar,", "saem", "curso,", "estarem", "preparados", "pro", "lógico", "base", "universidade", "dá,", "falta", "pouco", "entre", "mesmo", "disciplinas,", "matemática.\"", "auto", "explicativas", "elas", "jeito", "certinho", "para", "achei", "tranquila!", "detalhista", "quanto", "parada", "indentação", "ajuda", "visualizar", "mensagens", "erro", "também", "concisas", "claras", "teste", "mão", "massa,", "fácil,", "problema", "computacional,", "desconectados", "professora", "importava", "todos,", "quem", "já", "sabia", "linguagem.", "primeiro", "dia", "aula", "lembro", "dito", "programação,", "avançariam", "igualmente", "mas", "maior", "mentira", "pregada,", "menos", "roda,", "dificuldades", "sanadas,", "dúvidas", "comuns", "eram", "levadas", "sério.", "enfim,", "provando", "ainda", "elitismo", "unb", "altas", "taxas", "evasão", "cursos", "ti", "lá."]

texts = [
    {'ferramentas': open(path.join(directory, "ferramentas.txt")).read()},
    {'dificuldades': open(path.join(directory, "dificuldades.txt")).read()},
    {'all': open(path.join(directory, "all.txt")).read()}
]

# Generate a word cloud image
for text in texts:
    name, value = list(text.items())[0]
    without_excluded_words = " ".join([word for word in value.lower().split() if word not in excluded_words])
    WordCloud().generate(
        without_excluded_words
    ).to_file(path.join(directory, f"{name}.png"))

# Count words of all
all_words = texts[2]['all'].lower().split()
all_words = [word for word in all_words if word not in excluded_words]
all_words_count = {}
for word in all_words:
    if word in all_words_count:
        all_words_count[word] += 1
    else:
        all_words_count[word] = 1

# Sort words count
all_words_count = {k: v for k, v in sorted(all_words_count.items(), key=lambda item: item[1], reverse=True)}

# Print words count into a file
with open(path.join(directory, "all_words_count.txt"), "w") as file:
    for word, count in all_words_count.items():
        file.write(f"{word}: {count}\n")
