from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json,xml.etree.ElementTree as ET
jobs={
'followup_arxiv_lp':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"invariant density" OR all:"invariant densities") AND (all:"integrability" OR all:"Lp") AND all:"switching"')+'&max_results=20',
'followup_crossref_lp':'https://api.crossref.org/works?query='+urllib.parse.quote('Lp integrability invariant densities random switching stable linear flows')+'&rows=8'}
def run(z):
 k,u=z
 try:
  with urllib.request.urlopen(u,timeout=40) as h:b=h.read()
  Path(k+'.json').write_bytes(b);return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(run,jobs.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 f.write('\n\n## Follow-up searches, 2026-10-12\n\nThese narrowly test whether the proposed finite-p classification is explicitly covered; no originality claim is made.\n')
 for k,u,s,n in r:f.write(f'\n- {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(r,indent=2))
if Path('followup_arxiv_lp.json').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.parse('followup_arxiv_lp.json').findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text)
