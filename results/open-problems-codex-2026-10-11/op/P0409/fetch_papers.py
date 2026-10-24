import urllib.request,concurrent.futures,pathlib,pymupdf,json
p=pathlib.Path('.')
ids=['2606.26049','2606.30517','2602.06906','2609.10007','2408.10009']
def fetch(a):
 try:
  u='https://arxiv.org/pdf/'+a
  with urllib.request.urlopen(u,timeout=60) as r:p.joinpath('paper_'+a+'.pdf').write_bytes(r.read())
  doc=pymupdf.open(str(p/'paper_'+a+'.pdf'));s='\n'.join(f'=== PDF PAGE {i+1} ===\n'+pg.get_text() for i,pg in enumerate(doc))
  p.joinpath('paper_'+a+'.txt').write_text(s,encoding='utf-8')
  hits=[]
  for term in ['neighboring','neighbouring','Question 7.3','Palm','typical vertex','typical vertices']:
   pos=0
   while (i:=s.lower().find(term.lower(),pos))>=0:
    hits.append((term,s[max(0,i-150):i+350]));pos=i+len(term)
  return a,len(doc),hits[:25]
 except Exception as e:return a,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(fetch,ids))
p.joinpath('followup_hits.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for a in out:print(a)
for k in ['openalex_citing_arxiv','openalex_citing_journal']:
 j=json.loads(p.joinpath('search_'+k+'.txt').read_text(encoding='utf-8'));print(k,[(x['title'],x['id']) for x in j['results']])
