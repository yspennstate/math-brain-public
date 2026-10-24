from pathlib import Path
import json,xml.etree.ElementTree as E
r=Path(__file__).resolve().parent
ns={'a':'http://www.w3.org/2005/Atom'}
lit=r/'LITERATURE.md'
entries=[]
for fn in ['arxiv_higher.xml','arxiv_critical.xml']:
 for e in E.parse(r/fn).findall('a:entry',ns):
  id=e.find('a:id',ns).text
  if any(x in id for x in ['2501.12679','2504.20721','2307.05303','2605.15744','1802.06436']):
   authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
   entries.append(f'- {authors}. *'+e.find('a:title',ns).text.replace('\n',' ')+f'*. {id}; first posted '+e.find('a:published',ns).text+'. Lead only; not a matching operator-convergence theorem.')
with lit.open('a',encoding='utf8') as f:
 f.write('\n## Exact metadata for later/related leads\n\n'+'\n'.join(entries)+'\n')
 f.write('\n## Complete HTTP search audit\n\n')
 for fn in ['search_log.json','followup_search_log.json']:
  for item in json.loads((r/fn).read_text(encoding='utf8')):
   f.write(f"- {item['date']}: {item['service']}: {item['url']} — {item['result']}\n")
 f.write('\nTargeted source searches/downloads, 2026-10-12: https://arxiv.org/pdf/1306.4832; https://arxiv.org/pdf/0901.2473; arXiv API title query `ti:"Universality of a double scaling limit near singular edge points"`, max_results=5, found math-ph/0607043v1; downloaded https://arxiv.org/pdf/math-ph/0607043v1. Exact query URL in targeted_search_log.json.\n')
 f.write('\nBibliographic correction: the survey points to reference [38] (Ramirez-Rider-Virag) for precision, but its explicit nonregular-edge Conjecture 45 is in KRV ([31] in the survey). Both source bibliography entries were inspected. The counterexample uses actual eigenvalue densities to fix all potential-normalization factors, irrespective of notation conventions in the surveys.\n')
old=(r/'ATTEMPT.md').read_text(encoding='utf8')
(r/'EXPLORATORY_NOTES.md').write_text(old,encoding='utf8')
counter=(r/'COUNTEREXAMPLE.md').read_text(encoding='utf8')
partial=old[old.index('## A partial theorem:'):old.index('## Precise remaining gap')]
tail=old[old.index('## A new tail obstruction,'):]
tail=tail[:tail.index('For k=1, exponent')]
(r/'ATTEMPT.md').write_text('# Final outcome: counterexample to D0043\n\nThe conjecture as posed is false for k=1,beta=2. The full proof follows. No matching literature solution was certified; this is a counterexample derived from published local-kernel convergence and a Gaussian form bound. No mathematical gap remains in this argument. The correct replacement operator is not identified.\n\n'+counter+'\n\n# Auxiliary operator results\n\n'+partial+'\n'+tail,encoding='utf8')
claims=[]
for line in (r/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines():
 if not line.strip():continue
 c=json.loads(line)
 if c['status']=='conjecture':
  c.update(claim='For k=1,beta=2 and the explicit critical quartic W, no gamma>0 gives the conjectured lowest-eigenvalue convergence to S_2,1; hence the proposed general edge-operator limit is false.',status='counterexample',proof_location='ATTEMPT.md: full counterexample; COUNTEREXAMPLE.md',remaining_gap='',checks='Exact CV Example 1.2 and Theorem 1.7 hypotheses; RH positive-axis estimate and Lax derivative bound; finite-interval count and Portmanteau; Gaussian trial-function lower bound; exact_checks.json. Lean algebra check reported separately.')
 elif 'To refute matrix convergence' in c.get('remaining_gap',''):
  c['remaining_gap']='';c['checks']+=' Matrix contradiction completed separately in COUNTEREXAMPLE.md.'
 claims.append(c)
(r/'CLAIMS.jsonl').write_text('\n'.join(json.dumps(c,ensure_ascii=False) for c in claims)+'\n',encoding='utf8')
print('Full proof consolidated; claim records and complete literature/search audit saved.',flush=True)
print('Claims',len(claims),'exact checks',json.loads((r/'exact_checks.json').read_text()),flush=True)
print('Lean log exists:',(r/'lean_check.txt').exists(),flush=True)
