import urllib.request,pathlib,json,pymupdf
u='https://arxiv.org/pdf/1611.06493'; b=urllib.request.urlopen(u,timeout=40).read();pathlib.Path('hoze_holcman.pdf').write_bytes(b)
d=pymupdf.open('hoze_holcman.pdf');pathlib.Path('hoze_holcman.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps({'date':'2026-10-11','file':'hoze_holcman.pdf','url':u,'status':'OK','bytes':len(b)})+'\n')
print(pathlib.Path('hoze_holcman.txt').read_text(encoding='utf8')[:1800])
for e in json.load(open('crossref_survey.json',encoding='utf8'))['message']['items']:print(e.get('title'),e.get('DOI'),e.get('author'),e.get('published'))
