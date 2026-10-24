from pathlib import Path
import json, xml.etree.ElementTree as ET
R=Path(__file__).parent
rows=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
assert len(rows)==3 and all(x['problem_id']=='C0160' for x in rows)
assert all(x['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for x in rows)
src=(R/'survey.txt').read_text(encoding='utf-8')
for s in ['Theorem 5.6','Theorem 9.2','Theorem 3.2']: assert s in src
idx=src.rfind('[42]'); print('REFERENCE 42',src[idx:idx+450])
out=['\n## Final response logs and inspected discovery results\n']
for name in ['search_log.json','more_log.json','final_search_log.json']:
 if (R/name).exists():
  out.append('### '+name+'\n\n```json\n'+(R/name).read_text(encoding='utf-8')+'\n```\n')
out.append('The final_search.py batch was run twice: the first run failed for all five requests (TLS or connection-aborted errors); the second response log above records the retry. Semantic Scholar citations and the recent arXiv query succeeded on retry; OpenAlex citing-works remained inaccessible.\n')
for name in ['arxiv','arxiv_recent_retry']:
 p=R/(name+'.txt')
 if not p.exists(): continue
 try:
  root=ET.fromstring(p.read_text(encoding='utf-8')); ns={'a':'http://www.w3.org/2005/Atom'}
  out.append('### Inspected '+name+' entries\n')
  for e in root.findall('a:entry',ns):
   title=' '.join(e.findtext('a:title',default='',namespaces=ns).split())
   authors=', '.join(a.findtext('a:name',default='',namespaces=ns) for a in e.findall('a:author',ns))
   out.append('* '+title+' — '+authors+' — '+e.findtext('a:id',default='',namespaces=ns)+' — '+e.findtext('a:published',default='',namespaces=ns)+'\n')
 except Exception as e: out.append(name+' response was not valid Atom: '+str(e)+'\n')
out.append('\nFetched 2024 paper authors: Tom Hutchcroft and Minghao Pan. Version arXiv:2409.12283v1; first-page manuscript date September 20, 2024.\n')
out.append('\nGitHub query returned SamuelHaleDev/Percolation (student finite Monte Carlo assignment) and AaagIndia123/Fire-Hoses-and-Accessories-Manufacturers (unrelated). Neither supplies relevant research evidence.\n')
try:
 citations=json.loads((R/'semantic_citations.txt').read_text(encoding='utf-8'))
 out.append('\n### Semantic Scholar citing papers inspected\n\nPagination metadata: '+str({k:v for k,v in citations.items() if k!='data'})+'\n\n')
 for row in citations.get('data',[]):
  x=row.get('citingPaper',{})
  title=x.get('title','')
  out.append('* '+title+' — '+str(x.get('year'))+' — '+', '.join(a.get('name','') for a in x.get('authors',[]))+' — '+str(x.get('url'))+'\n')
  if any(k in title.lower() for k in ['uniqueness','transitive','hyperbolic','critical','monotonic']): print('CITING LEAD',x)
except Exception as e: out.append('\nSemantic Scholar citation response could not be parsed: '+str(e)+'\n')
p=R/'LITERATURE.md'; t=p.read_text(encoding='utf-8'); marker='\n## Final response logs and inspected discovery results\n'; t=t.split(marker)[0]; p.write_text(t+''.join(out),encoding='utf-8')
(R/'record_audit.txt').write_text('Required claim JSON schema/IDs and source theorem presence checked. Three claims; mathematical scope audited in ATTEMPT.md.\n',encoding='utf-8')
print('record audit passed',flush=True)
