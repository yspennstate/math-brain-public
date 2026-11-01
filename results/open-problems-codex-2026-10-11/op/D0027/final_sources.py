from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json,pymupdf,xml.etree.ElementTree as E
qs={'cmrt_correct':'https://arxiv.org/pdf/math/0610106','fa2013_correct':'https://arxiv.org/pdf/1205.4584','arxiv_since_source':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('cat:math.PR AND (all:"facilitated" OR all:"kinetically constrained") AND submittedDate:[202510230000 TO 202610112359]')+'&max_results=100&sortBy=submittedDate&sortOrder=descending','crossref_exp':'https://api.crossref.org/works/10.1007/s10959-018-0812-6'}
def fetch(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45) as r:b=r.read()
  fn=k+('.pdf' if 'arxiv.org/pdf' in u else '.response');Path(fn).write_bytes(b)
  return [k,u,'OK',len(b)]
 except Exception as e:return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,qs.items()))
j=json.loads(Path('search_log.json').read_text());j['results']+=rows;Path('search_log.json').write_text(json.dumps(j,indent=2),encoding='utf8')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Verified identifiers and date-filtered search\n\n')
 for k,u,st,info in rows:f.write(f'- 2026-10-11 — {k}: {u}; {st}: {info}.\n')
for row in rows:
 print(row,flush=True)
 if row[2]=='OK' and row[0] in ['cmrt_correct','fa2013_correct']:
  d=pymupdf.open(row[0]+'.pdf');txt='\n'.join(p.get_text() for p in d);Path(row[0]+'.txt').write_text(txt,encoding='utf8');print(txt[:800],flush=True)
  if row[0]=='cmrt_correct':
   for i,p in enumerate(d):
    text=p.get_text()
    if ('Theorem 6.3' in text or 'Theorem 6.1' in text or 'Theorem 6.2' in text):print('PAGE',i+1,text[:6500],flush=True)
 elif row[2]=='OK' and row[0]=='arxiv_since_source':
  ns={'a':'http://www.w3.org/2005/Atom'};root=E.fromstring(Path(row[0]+'.response').read_bytes())
  for e in root.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns),flush=True)
 elif row[2]=='OK' and row[0]=='crossref_exp':
  x=json.loads(Path(row[0]+'.response').read_text())['message'];print(x.get('title'),x.get('author'),x.get('link'),x.get('abstract'),flush=True)
x=json.loads(Path('crossref_source_title.response').read_text())['message']['items'];print('SOURCE DOI candidates',[(a.get('title'),a.get('DOI')) for a in x],flush=True)
