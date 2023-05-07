import wikipediaapi

# Instancionando a biblioteca da Wikipedia em Português
wiki_pt = wikipediaapi.Wikipedia('pt')

# Função que retorna o primeiro parágrafo do artigo da Wikipedia
def get_wikipedia_summary(topic):
    page = wiki_pt.page(topic)
    if page.exists():
        summary = page.summary[0:page.summary.find('\n')]
        return summary
    else:
        return None
