from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
REPORT=Path('math-open-problems/reports/fei-2026-10-11')
PUSH=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
files=[REPORT/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
files+=list(REPORT.glob('*.tex'))
files += [PUSH/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((BASE/'context').glob('*.txt'))
files += [BASE/'agents/A086/runs/20261023T140222Z-account03-A086-joint-code-referee'/x for x in ['CLAIMS.json','RECONSTRUCTION.md','SELECTOR_EXPOSURE.md','A011_ACCOUNTING_OBJECTION.md']]
files += [BASE/'agents/A011/runs/20261023T134844Z-account03-A011-representation-existence'/x for x in ['CLAIMS.json','DERIVATION.md']]
files += [BASE/'agents/A094/runs/20261023T131208Z-account03-A094-proof-chain-challenger'/x for x in ['CLAIMS.json','DERIVATION.md']]
receipts=[]
for p in files:
 if not p.exists():
  receipts.append({'path':str(p),'missing':True});continue
 b=p.read_bytes()
 try: s=b.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError: s=b.decode('cp1252');enc='cp1252 (UTF8 decode rejected; historical paper extraction)'
 receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'encoding':enc,'access':'read; selected passages extracted, not a new full-paper audit'})
 if p.name=='CLAIMS.json' and 'agents' in str(p):
  data=json.loads(s)
  print(str(p)+'\n'+json.dumps(data,ensure_ascii=False)[:13000])
 elif p.name not in ['DERIVATION.md','RECONSTRUCTION.md','SELECTOR_EXPOSURE.md','A011_ACCOUNTING_OBJECTION.md']:
  lines=s.splitlines(); picked=[(i+1,l[:400]) for i,l in enumerate(lines) if any(t in l.lower() for t in ['a094','c024','source','open','theorem 8','composition','stopping','universal'])][:5]
  print(str(p)+'\n'+json.dumps(picked,ensure_ascii=False))
ROOT.joinpath('out').mkdir(exist_ok=True)
ROOT.joinpath('out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('SOURCES',len(receipts))
