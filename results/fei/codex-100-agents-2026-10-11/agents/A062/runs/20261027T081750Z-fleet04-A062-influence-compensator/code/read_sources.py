from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
base=Path(r'~\brain_workers\FEI100_20261011')
campaign=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
reports=Path(r'math-open-problems/reports\fei-2026-10-11')
files=list((base/'context').glob('*.txt'))+list((campaign/'sources').glob('*.md'))
files += [campaign/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [reports/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
rows=[]
for p in files:
    b=p.read_bytes()
    try: s=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252'); enc='cp1252'
    lines=s.splitlines()
    locators=[{'line':i+1,'text':l.strip()[:240]} for i,l in enumerate(lines)
              if any(k in l.lower() for k in ['affine','total correlation','martingale','8.6','restriction'])]
    rows.append(dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),encoding=enc,bytes=len(b),locators=locators[:12]))
(root/'out/SOURCE_READS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
for row in rows[:16]:
    print(Path(row['path']).name,row['encoding'],row['locators'][:2])
print('READ_METADATA',len(rows),'files; excerpts locate background only, no new paper theorem dependency')
compute=Path(r'~\.claude\compute')
ledger=list(compute.glob('*interven*'))
print('INTERVENTION_LEDGER_PATHS',[str(p) for p in ledger])
for p in ledger:
    if p.is_file(): print(p.name,p.read_text(encoding='utf-8')[-1500:])
