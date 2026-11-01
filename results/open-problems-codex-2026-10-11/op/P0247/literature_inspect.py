from pathlib import Path
import xml.etree.ElementTree as ET,json,urllib.request,concurrent.futures
p=Path(__file__).parent;ns={'a':'http://www.w3.org/2005/Atom'}
for file in ['arxiv_last.txt','arxiv_transitive.txt']:
 for e in ET.parse(p/file).getroot().findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),'; AUTHORS:',','.join(a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)))
  print(e.findtext('a:summary',namespaces=ns))
for w in json.loads((p/'crossref.txt').read_text())['message']['items'][:2]:print('RELEVANT CROSSREF',json.dumps(w,ensure_ascii=False))
text=(p/'source_full.txt').read_text(encoding='utf-8')
for phrase in ['7.1 Symmetric','7.1.1','last new','Lovász','Winkler']:
 pos=0;count=0
 while count<8:
  i=text.find(phrase,pos)
  if i<0:break
  print('SOURCE CONTEXT',phrase,text[max(0,i-200):i+1600]);pos=i+len(phrase);count+=1
for line in (p/'inspection.txt').read_text(encoding='utf-8').splitlines():
 if line.startswith('LEDGER'):print(line)
qs=[('directed_landing','https://doi.org/10.47443/dml.2022.158'),('lovasz_landing','https://doi.org/10.1002/jgt.3190170505')]
def get(q):
 name,url=q
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0247-research'}),timeout=30) as r:data=r.read()
  (p/(name+'.html')).write_bytes(data);res='OK '+str(len(data))
 except Exception as e:res=repr(e)
 print(name,res,flush=True)
 with (p/'LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'\n- 2026-10-12 DOI fetch: {url}; {res}.\n')
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(get,qs))
