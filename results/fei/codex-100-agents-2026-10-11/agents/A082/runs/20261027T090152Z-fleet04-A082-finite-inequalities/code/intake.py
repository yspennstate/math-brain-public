from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
OWNER=Path('~')
paths=[OWNER/'AGENTS.md']
base=OWNER/'mop_fei100/reports/fei-2026-10-11'
paths += [base/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
paths += list(base.glob('*.tex'))
push=OWNER/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
paths += [push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((push/'sources').glob('*.txt'))
paths += list((OWNER/'brain_workers/FEI100_20261011/context').glob('*.txt'))
peer=OWNER/'brain_workers/FEI100_20261011/agents/A096/runs'
latest=sorted(peer.iterdir())[-1]
paths += [latest/x for x in ['REPORT.md','CLAIMS.json','DERIVATION.md','PROOF.md'] if (latest/x).exists()]
records=[]
for p in paths:
    if not p.exists():
        records.append({'path':str(p),'missing':True});continue
    b=p.read_bytes()
    try:s=b.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:s=b.decode('cp1252');encoding='cp1252 (source not UTF8)'
    records.append({'path':str(p),'bytes':len(b),'encoding':encoding,'sha256':hashlib.sha256(b).hexdigest()})
    if p.parent==latest:
        print('\nSOURCE',p,'\n',s[:24000])
    elif p.suffix=='.txt':
        lines=s.splitlines()
        hits=[(i+1,x[:220]) for i,x in enumerate(lines) if any(t in x.lower() for t in ['composition identit','proposition 8.6','singular','entropy of threshold'])]
        print(str(p),hits[:6])
    else:
        print(str(p),len(b),'bytes decoded')
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
