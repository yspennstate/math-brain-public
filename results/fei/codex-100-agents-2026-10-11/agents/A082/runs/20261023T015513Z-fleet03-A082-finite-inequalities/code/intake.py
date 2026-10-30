from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
HOME=Path('~')
for n in ('out','code'):(ROOT/n).mkdir(exist_ok=True)
old=ROOT.parent/'20261021T230321Z-fleet03-A082-finite-inequalities/out/SOURCE_RECEIPTS.json'
paths=[Path(x['path']) for x in json.loads(old.read_text(encoding='utf-8'))]
latest=HOME/'brain_workers/FEI100_20261011/agents/A096/runs/20261023T010221Z-fleet03-A096-live-gap-ledger'
paths += [latest/n for n in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
paths += [ROOT.parent/'20261021T230321Z-fleet03-A082-finite-inequalities/REPORT.md',HOME/'.claude/compute/compute_state.json',HOME/'.claude/compute/interventions.tsv']
rows=[]
for p in dict.fromkeys(paths):
 raw=p.read_bytes()
 try:s=raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252'
 rows.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc))
 if p.name=='interventions.tsv':print('INTERVENTIONS',s[-600:])
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
spec=dict(helper_version='A082-prime-log-v1',family='Every labelled Boolean source on n=2 pilot and n=3 final; calibrated matching/uniform/spiked source references with occupied-support D and supplied Q',domain='gamma=1/2,1; 2 complete Q fills; 3 stopped adaptive tree shapes; all subsets of each frontier',case_count='256*3*2*2=3072 source/floor instances; policy count recorded exactly',symmetry='none',arithmetic='integer direct-character spectra; Fraction probabilities; exact prime-log forms and rational atanh sign bounds',memory_estimate_mb=120,max_runtime_seconds=60,pilot_max_runtime_seconds=60,bridge='analytic subprobability chain and martingale variance proof; finite tests are independent validation only')
(ROOT/'out/FROZEN_REVIEW_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
spec=dict(helper_version='A082-prime-log-nested-v1',family='f(x0,x1,x2,x3)=h(x0,x1,x2) if x3=0 else +1, all256 h',domain='matching, uniform-nonempty and singleton-spiked normalized root references calibrated at true vacuum; every ordered two-query branch and selected second child',case_count='at most36864 histories; pilot first16 source tables',symmetry='none; all physical coordinate labels and outcomes retained',arithmetic='exact prime-log forms with rational interval signs; actual Boolean truth tables',memory_estimate_mb=120,max_runtime_seconds=60,stopping_rule='stop at first rigorously positive cost minus original CE with nonconstant retained sibling; no dimension escalation',target='test unproved extension of A096 transfer to nested ORIGINAL-source resets at gamma=1; not an FEI counterexample')
(ROOT/'out/FROZEN_NESTED_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('Intake and two frozen specifications saved;',len(rows),'source receipts')
