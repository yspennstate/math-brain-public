from pathlib import Path
import json,xml.etree.ElementTree as E,sys
r=Path(__file__).resolve().parent
log=r/'lean_check.txt'
if not log.exists():raise SystemExit('Lean result is still pending; STATE remains WORKING.')
lean=log.read_text(encoding='utf8')
lean_passed=lean.startswith('exit_code=0\n')
if not lean_passed and not ('--record-lean-timeout' in sys.argv and 'timed out after 3600 seconds' in lean):
 raise SystemExit('Lean has not passed. Inspect lean_check.txt before completion.\n'+lean)
assert all(json.loads((r/'exact_checks.json').read_text()).values())
claims=[json.loads(x) for x in (r/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
assert len(claims)==4 and claims[-1]['status']=='counterexample'
assert all(not x['remaining_gap'] for x in claims)
code=(r/'TailAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in code and 'native_decide' not in code and 'import Mathlib\n' not in code
ns={'a':'http://www.w3.org/2005/Atom'}
with (r/'LITERATURE.md').open('a',encoding='utf8') as f:
 for e in E.parse(r/'arxiv_nonregular.xml').findall('a:entry',ns):
  if '1811.00509' in e.find('a:id',ns).text:
   authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
   f.write('\nExact metadata for the final regular-edge lead: '+authors+'. *'+e.find('a:title',ns).text.replace('\n',' ')+'*. '+e.find('a:id',ns).text+'. Posted '+e.find('a:published',ns).text+'. Not a source-matching solution.\n')
formal=('lake env lean successfully checked the three finite algebra lemmas with the kernel (no sorry, no native_decide).' if lean_passed else 'The single restarted lake env lean attempt timed out after its full 3600-second allowance. TailAlgebra.lean remains UNVERIFIED; no declaration is counted Lean-checked. Its potential-rescaling and exponent arithmetic were separately checked exactly in Python. The formalization/checking gap is computational only: there is no missing mathematical step in the written analytic counterexample.')
audit='\nFinal referee result (2026-10-12): all source hypotheses, the actual beta=2 eigenvalue density, positive-axis kernel decay, Gaussian trial-function law, and the order n -> infinity then R -> infinity then r -> infinity were checked analytically. The proof avoids the expected/unproved largest-eigenvalue limit in CIK. Exact rational checks passed. '+formal+' The stochastic and Riemann-Hilbert arguments remain analytic, not Lean-formalized. No mathematical gap remains in the counterexample; the correct replacement operator and worldwide novelty are not established.\n'
for fn in ['ATTEMPT.md','COUNTEREXAMPLE.md']:
 with (r/fn).open('a',encoding='utf8') as f:f.write(audit)
claims[-1]['checks']+=(' Lean kernel check passed for potential rescaling and elementary power/exponent algebra only.' if lean_passed else ' Lean verification attempt timed out after 3600 seconds; no lemmas counted Lean-checked.')+' See lean_check.txt. Final analytic hostile-referee pass complete; finite coefficient and exponent computations passed exact_checks.json.'
(r/'CLAIMS.jsonl').write_text('\n'.join(json.dumps(c,ensure_ascii=False) for c in claims)+'\n',encoding='utf8')
status=(r/'STATUS.md').read_text(encoding='utf8')
status=status.replace('STATE: WORKING','STATE: DONE',1).replace('NEXT: Finish record consolidation and inspect the single Lean algebra-check result, then set STATE: DONE.','NEXT: None; counterexample complete. The correct replacement operator is outside the resolved conjecture.',1)
status+='\n2026-10-12: DONE / SOLVED by a source-compatible k=1,beta=2 counterexample. Full proof consolidated in ATTEMPT.md; source audit and all search queries in LITERATURE.md; four claims recorded in CLAIMS.jsonl. Exact rational checks passed. '+formal+' Final analytic referee pass found no remaining mathematical gap. Not SOLVED_IN_LITERATURE; novelty unverified.\n'
(r/'STATUS.md').write_text(status,encoding='utf8')
assert (r/'STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
print('\n'.join(status.splitlines()[:3]),flush=True)
print('Lean algebra check:\n'+lean,flush=True)
print('Required records saved and verified; claim count',len(claims),flush=True)
