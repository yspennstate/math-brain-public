from pathlib import Path
import json,xml.etree.ElementTree as ET
p=Path('LITERATURE.md')
with p.open('a',encoding='utf-8') as f:
 f.write('\n## Complete HTTP search and fetch log\n\nAll requests below were made on 2026-10-12 using Python urllib from the shell. Raw successful responses are retained in this folder; search_log.jsonl contains the same request ledger. Errors are search limitations, not negative literature evidence.\n\n')
 for line in Path('search_log.jsonl').read_text(encoding='utf-8').splitlines():
  r=json.loads(line)
  f.write(f"- {r['date']} — {r['service']}: `{r['url']}`. Outcome: {r.get('error',str(r.get('status'))+'; '+str(r.get('bytes'))+' bytes')}.\n")
 f.write('\n## Titles returned by the relevant arXiv queries\n\nThese are search hits, not theorem verification. Author names and version dates are copied from returned Atom metadata.\n\n')
 ns={'a':'http://www.w3.org/2005/Atom'}
 seen=set()
 for name in ['arxiv_api.xml','arxiv_independence.json','arxiv_kane.json']:
  try:root=ET.parse(name)
  except Exception:continue
  for e in root.findall('a:entry',ns):
   id=e.find('a:id',ns).text
   if id in seen:continue
   seen.add(id)
   title=' '.join(e.find('a:title',ns).text.split())
   authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
   date=e.find('a:updated',ns).text[:10]
   f.write(f'- {authors}. {title}. {id}; version date {date}.\n')
print('Literature ledger appended.',flush=True)
