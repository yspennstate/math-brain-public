import pathlib,urllib.request,json,pymupdf
u='https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/docs/kn-results.pdf'
try:
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=35) as r:d=r.read()
 pathlib.Path('site_manuscript.pdf').write_bytes(d)
 doc=pymupdf.open(stream=d,filetype='pdf')
 pathlib.Path('site_manuscript_plain.txt').write_text('\n'.join(f'\n[PDF PAGE {i+1}]\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 res={'service':'site_manuscript_pdf','url':u,'bytes':len(d),'pages':len(doc)}
 for i,p in enumerate(doc):
  s=p.get_text()
  if any(t in s.lower() for t in ['stretched','critical site','no site percolation','site criticality','critical parameter']):print('PAGE',i+1,s[:10000])
except Exception as e:res={'service':'site_manuscript_pdf','url':u,'error':str(e)}
with open('followup_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps({'date':'2026-10-11',**res})+'\n')
print(res)
for file in ['site_manuscript_tex.txt','site_comparator_challenge.txt','site_comparator_solution.txt']:
 s=pathlib.Path(file).read_text()
 print('\nFILE',file)
 if 'manuscript' in file:
  for term in ['stretched','criticality','site percolation','Cerf']:
   pos=0
   for j in range(4):
    i=s.lower().find(term.lower(),pos)
    if i<0:break
    print(term,s[max(0,i-200):i+2000]);pos=i+len(term)
 else: print(s)
