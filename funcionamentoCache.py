cache = {}

def pegaUrl(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pegaDadosServidor(url)
        cache[url] = dados
        return dados