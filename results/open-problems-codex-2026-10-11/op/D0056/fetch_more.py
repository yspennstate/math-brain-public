import urllib.request,concurrent.futures,pathlib,pymupdf,json
urls={
'stable':'https://arxiv.org/pdf/2006.06140',
'sustainability':'https://arxiv.org/pdf/2108.05610',
'openalex_retry':'https://api.openalex.org/works?search=A%20max-type%20recursive%20model&per_page=5',
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2609440919&per_page=100',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1705.04787?fields=title,citations.title,citations.year,citations.externalIds'
}
def get(k,u):
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Research/1.0'}),timeout=40).read();pathlib.Path(k+('.pdf' if k in ['stable','sustainability'] else '.json')).write_bytes(data)
  if k in ['stable','sustainability']:
   d=pymupdf.open(stream=data,filetype='pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return k,u,'OK '+str(len(data))
 except Exception as e:return k,u,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(lambda x:get(*x),urls.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for k,u,s in r:f.write(f'- {k}: `{u}` — {s}\n')
print(json.dumps(r,indent=2))
