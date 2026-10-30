from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
HOME=Path('~')
for name in ('out','code'): (ROOT/name).mkdir(exist_ok=True)
files=[HOME/'AGENTS.md',HOME/'brain_workers/FEI100_20261011/BOARD.md',HOME/'brain_workers/FEI100_20261011/claude/B17/STREAM_NOTES.md']
base=HOME/'mop_fei100/reports/fei-2026-10-11'
files += [base/f for f in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
sup=HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
files += [sup/f for f in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
files += list((sup/'sources').glob('*.md'))
files += list((HOME/'brain_workers/FEI100_20261011/context').glob('*.txt'))
for a,r in [('A096','20261021T210221Z-fleet03-A096-live-gap-ledger'),('A096','20261014T094929Z-fleet05-A096-live-gap-ledger'),('A097','20261014T050248Z-fleet05-A097-cross-route-transfer'),('A090','20261021T175538Z-fleet03-A090-independent-reconstruction')]:
 d=HOME/'brain_workers/FEI100_20261011/agents'/a/'runs'/r
 files += [d/f for f in ('REPORT.md','CLAIMS.json','DERIVATION.md') if (d/f).exists()]
rows=[]; excerpts=[]
for p in files:
 raw=p.read_bytes()
 try: txt=raw.decode('utf-8-sig'); enc='utf-8-sig'
 except UnicodeDecodeError: txt=raw.decode('cp1252'); enc='cp1252'
 rows.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc))
 if p.name=='AGENTS.md': excerpts.append(str(p)+'\n'+txt)
 elif 'context' in p.parts:
  ls=txt.splitlines(); hits=[i for i,l in enumerate(ls) if any(w in l.lower() for w in ['composition','cross-entropy','read-once','singular','entropy-influence'])]
  excerpts.append(str(p)+'\n'+'\n'.join(f'{i+1}: '+ls[i] for i in hits[:18]))
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(ROOT/'out/INTAKE_EXCERPTS.txt').write_text('\n\n'.join(excerpts),encoding='utf-8')
spec=dict(helper_version='A082-reset-review-v1',family='F=1-2A_a+2A_(a+b+r); arbitrary calibrated normalized source reference',domain='a=2,3; b=0,1; r=1,2; source references matching, uniform-nonempty, singleton-spike mixture',case_count='24 roots; all active labels and all on-cell active prefix lengths; 507 algebraic rational parameter fixtures',symmetry='none in physical checks; analytic v-monotonicity removes all reference coordinates except R({j})',arithmetic='integer direct character sums, Fraction probabilities, rational atanh logarithm intervals',memory_estimate_mb=60,max_runtime_seconds=60,pilot='first two roots, <=60 seconds',universal_bridge='analytic source-reference reduction and local-envelope induction, separately from finite validation')
(ROOT/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('READ',len(rows),'sources; frozen spec saved. Context locators:')
print('\n'.join(excerpts[1:])[-6500:])
