import pathlib,json,xml.etree.ElementTree as E,requests,concurrent.futures,pymupdf
ns={'a':'http://www.w3.org/2005/Atom'}
for f in ['search_arxiv.txt','search_arxiv_source.txt']:
 print('\n',f)
 for e in E.fromstring(pathlib.Path(f).read_text(encoding='utf8')).findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:updated',namespaces=ns),e.findtext('a:title',namespaces=ns))
d=json.loads(pathlib.Path('search_crossref.txt').read_text());print('\nCROSSREF')
for w in d.get('message',{}).get('items',[])[:20]:print(w.get('title'),w.get('DOI'),w.get('published'))
print('\nGITHUB',json.loads(pathlib.Path('search_github.txt').read_text()).get('total_count'))
def get(q):
 name,url=q
 try:
  r=requests.get(url,timeout=50);r.raise_for_status();pathlib.Path(name+'.pdf').write_bytes(r.content);doc=pymupdf.open(name+'.pdf');pathlib.Path(name+'.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf8');print(name,len(doc),flush=True)
 except Exception as e:print(name,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(get,[('qu_valko','https://arxiv.org/pdf/2509.15446'),('assiotis_najnudel','https://arxiv.org/pdf/2602.08739'),('lewin','https://arxiv.org/pdf/2202.09240')]))
