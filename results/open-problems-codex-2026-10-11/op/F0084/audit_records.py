from pathlib import Path
import json, xml.etree.ElementTree as E
root=Path(__file__).resolve().parent
p=root/'LITERATURE.md'; s=p.read_text(encoding='utf8')
marker='\n## Complete request ledger'
s=s.split(marker)[0]
rows=['', '## Complete request ledger', '', 'Every row was requested on 2026-10-11. Failed requests provide no negative evidence. Full bodies are preserved when received; the filename suffix for some JSON responses is `.xml`.', '', '| Service / purpose | Exact request | Outcome |', '|---|---|---|']
for x in json.loads((root/'search_log.json').read_text()):
 outcome=str(x.get('status',x.get('error','unknown'))).replace('|','/')
 rows.append(f"| {x['service']} | `{x['url']}` | {outcome} |")
rows += ['', '## Additional exact arXiv references and lead screening', '']
ns={'a':'http://www.w3.org/2005/Atom'}; seen=set()
keep=['Poisson Matching','A Poisson allocation of optimal tail','Hyperuniform and rigid stable matchings','A Factor Matching of Optimal Tail Between Poisson Processes','Subcritical regimes in some models of continuum percolation']
for f in ['arxiv.xml','lead_metadata.xml']:
 try:
  tree=E.parse(root/f)
  for e in tree.findall('a:entry',ns):
   title=' '.join(e.find('a:title',ns).text.split())
   if title not in keep or title in seen:continue
   seen.add(title)
   authors=', '.join(x.find('a:name',ns).text for x in e.findall('a:author',ns))
   ident=e.find('a:id',ns).text; date=e.find('a:published',ns).text[:10]
   rows.append(f'- {authors}. *{title}*. {ident}, first posted {date}.')
 except (OSError,E.ParseError): pass
rows += ['', 'Poisson point matching and optimal allocation rules are not the Euclidean stable Poisson–Lebesgue rule. Subcritical percolation addresses other parameters and observables. These are leads rather than printed solutions to F0084. See the individual screening notes above.', '']
p.write_text(s+'\n'.join(rows),encoding='utf8')
claims=[json.loads(x) for x in (root/'CLAIMS.jsonl').read_text().splitlines()]
assert all(x['problem_id']=='F0084' for x in claims)
assert all(x['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for x in claims)
assert all((root/f).exists() for f in ['STATUS.md','ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl'])
print('Requests:',len(json.loads((root/'search_log.json').read_text())),'Claims:',len(claims),'Record validation passed.')
for f in ['hyperuniform.txt']:
 if (root/f).exists():
  lines=(root/f).read_text(encoding='utf8').replace(chr(0),'').splitlines()
  print('\nLEAD',f,'\n'+'\n'.join(lines[:100]))
  for i,line in enumerate(lines):
   if any(word in line.lower() for word in ['critical','lebesgue','tail bound']): print(i+1,'\n'.join(lines[max(0,i-2):i+7]))
