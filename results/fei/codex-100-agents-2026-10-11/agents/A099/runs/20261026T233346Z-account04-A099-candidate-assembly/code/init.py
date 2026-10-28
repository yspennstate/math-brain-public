from pathlib import Path
import json, hashlib, shutil
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
OLD=A/'runs/20261023T131709Z-account03-A099-candidate-assembly'
ROOT=Path(r'~\brain_workers\FEI100_20261011')
for sub in ['out','out/sources']: (R/sub).mkdir(parents=True,exist_ok=True)
def save(n,d): (R/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
receipts=[]
def read(p,copy=False):
 raw=p.read_bytes()
 try: s=raw.decode('utf-8-sig')
 except UnicodeDecodeError: s=raw.decode('cp1252')
 receipts.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
 if copy:
  name=p.parent.name+'-'+p.name
  (R/'out/sources'/name).write_bytes(raw)
 return s
base=Path(r'math-open-problems/reports\fei-2026-10-11')
for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']: read(base/n)
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']: read(sup/n)
for p in (sup/'sources').glob('*'):
 if p.is_file() and p.suffix in ['.md','.tex','.json','.txt']: read(p)
for p in (ROOT/'context').glob('*.txt'):
 s=read(p)
 lines=s.splitlines()
 matches=[(i+1,x[:200]) for i,x in enumerate(lines) if any(w in x.lower() for w in ['proposition 8.6','relative entropy','singular','composition identit'])]
 print(p.name, matches[:8])
for p in [ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',A/'STATUS.md',OLD/'REPORT.md']: read(p)
sources=[('A096','20261023T140303Z-account03-A096-live-gap-ledger',['DERIVATION.md','CLAIMS.json','REPORT.md']),('A097','20261023T143952Z-account03-A097-cross-route-transfer',['PROOF.md','CLAIMS.json','REPORT.md']),('A093','20261026T202338Z-account04-A093-literature-and-priority',['DERIVATION.md','CLAIMS.json']),('A098','20261026T203914Z-account04-A098-resource-reallocation',['REVIEW.md','CLAIMS.json'])]
for a,run,files in sources:
 for n in files: read(ROOT/'agents'/a/'runs'/run/n,True)
for src,dst in [('CANDIDATE_MANUSCRIPT.tex','out/BASELINE_v10.tex'),('CLAIMS.json','out/BASELINE_CLAIMS.json'),('out/PROOF_DEPENDENCIES.json','out/BASELINE_DAG.json'),('code/prior_exact.py','code/exact.py')]:
 shutil.copyfile(OLD/src,R/dst)
save('out/READ_RECEIPTS.json',receipts)
save('out/FROZEN_SPEC.json',dict(helper_version='A099-v11 exact.py byte-copy v10, checker source SHA256 recorded before launch',family='All labelled Boolean signs n=0..3, all coordinates; inherited three-witness references, fair and deterministic ghost splits; finite rational floor profiles',domain='pilot n<=2; main n<=3; b=1/2, weights 1/8,1/8,1/4, witness labels 0,last,last; floor grid denominator 8 and 12',case_count='278 Boolean tables total; 786 coordinate queries times 2 ghost kernels; 432 admissible floor profiles',symmetry='none',arithmetic='integer Walsh, Fraction, exact prime-log linear identities and outward rational log bounds; analytic proofs for all dimensions/trees',memory_estimate_MB=110,max_runtime_seconds=55,pilot_max_seconds=55,automatic_escalation=False))
print('Initial receipts and frozen specification saved:',len(receipts))
