import urllib.request,urllib.parse,pathlib,json
url='https://api.openalex.org/works/https://doi.org/10.1007/s00440-013-0524-x'
try:
 with urllib.request.urlopen(url,timeout=40) as r:t=r.read().decode();code=r.status
except Exception as e:t=str(e);code='ERROR'
pathlib.Path('search_openalex_correct_doi.txt').write_text(t,encoding='utf8')
p=pathlib.Path('search_log.json');a=json.loads(p.read_text());a.append(dict(service='openalex_correct_doi',url=url,status=code,date='2026-10-12',file='search_openalex_correct_doi.txt'));p.write_text(json.dumps(a,indent=2),encoding='utf8')
print(code,t[:600])
