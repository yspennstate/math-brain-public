from pathlib import Path
import urllib.request,concurrent.futures,json,xml.etree.ElementTree as E,pymupdf
ns={'a':'http://www.w3.org/2005/Atom'};r=E.fromstring(Path('arxiv_since_source.response').read_bytes())
meta=[]
for e in r.findall('a:entry',ns):
 t=e.findtext('a:title',namespaces=ns);s=e.findtext('a:summary',namespaces=ns)
 if any(x in (t+' '+s).lower() for x in ['kinetically constrained','fredrickson','andersen']):
  meta.append({'id':e.findtext('a:id',namespaces=ns),'title':t,'authors':[x.findtext('a:name',namespaces=ns) for x in e.findall('a:author',ns)],'published':e.findtext('a:published',namespaces=ns),'summary':s})
Path('postsource_relevant.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding='utf8');print([(x['id'],x['authors'],x['title']) for x in meta],flush=True)
qs={'oriented_2026':'https://arxiv.org/pdf/2609.30585','mountford_valle_html':'https://link.springer.com/article/10.1007/s10959-018-0812-6'}
def fetch(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45) as z:b=z.read()
  Path(k+('.pdf' if k=='oriented_2026' else '.response')).write_bytes(b);return [k,u,'OK',len(b)]
 except Exception as e:return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:rows=list(ex.map(fetch,qs.items()))
j=json.loads(Path('search_log.json').read_text());j['results']+=rows;Path('search_log.json').write_text(json.dumps(j,indent=2),encoding='utf8')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Date-filtered post-source candidates\n\nThe math.PR query over 2025-10-23 through 2026-10-11 returned 32 entries. Metadata of all model-relevant hits is in postsource_relevant.json. These include a new oriented-model theorem, which is being checked for scope.\n\n')
 for x in meta:f.write('- '+', '.join(x['authors'])+', *'+x['title']+'*, '+x['id']+'; submitted '+x['published']+'.\n')
 for row in rows:f.write(f'- 2026-10-11 retrieval: {row[1]}; {row[2]}: {row[3]}.\n')
for row in rows:print(row,flush=True)
if Path('oriented_2026.pdf').exists():
 d=pymupdf.open('oriented_2026.pdf');txt='\n'.join(p.get_text() for p in d);Path('oriented_2026.txt').write_text(txt,encoding='utf8');print(txt[:14500],flush=True)
