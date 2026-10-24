import urllib.request,urllib.parse,pathlib,concurrent.futures,json
qs=[('journal_pdf','https://link.springer.com/content/pdf/10.1007/s10959-024-01399-1.pdf'),('openalex_source_doi','https://api.openalex.org/works/https://doi.org/10.1007/978-3-7643-8458-6_9'),('openalex_citing_source','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:https://doi.org/10.1007/978-3-7643-8458-6_9','per-page':100})),('crossref_source','https://api.crossref.org/works/10.1007/978-3-7643-8458-6_9')]
def fetch(z):
 name,url=z
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'D0019-research/1.0'}),timeout=45);b=r.read();pathlib.Path(name+'.response').write_bytes(b);msg=f'HTTP {r.status}; {len(b)} bytes'
  if name=='journal_pdf' and b.startswith(b'%PDF'):
   pathlib.Path('journal.pdf').write_bytes(b)
   import pymupdf
   D=pymupdf.open('journal.pdf');pathlib.Path('journal.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(D)),encoding='utf8')
   for i in range(min(4,len(D))):print('JOURNAL PAGE',i+1,D[i].get_text())
 except Exception as e:msg=f'{type(e).__name__}: {e}';pathlib.Path(name+'.response').write_text(msg,encoding='utf8')
 return name,url,msg
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: rs=list(p.map(fetch,qs))
with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,msg in rs:f.write(f'\n- 2026-10-12 `{name}`: {url}\n  Outcome: {msg}.\n');print(name,msg)
# Save exact source and theorem blocks as plain unicode excerpts.
import pymupdf
for infile,outfile,pages in [('source.pdf','source_statement_excerpt.txt',[2,33]),('resolution_pdf.pdf','resolution_statement_excerpt.txt',[0,1,6])]:
 D=pymupdf.open(infile);pathlib.Path(outfile).write_text('\n'.join(f'PDF page {i+1}\n'+D[i].get_text() for i in pages),encoding='utf8')
