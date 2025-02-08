

def get_urls(datas,site):
    urls = []
    for title in datas["mangas"]:
        if title['site'] == site:
            urls.append(title['url'])
    
    return urls
