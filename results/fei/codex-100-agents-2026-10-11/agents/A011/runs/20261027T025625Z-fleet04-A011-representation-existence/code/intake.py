from pathlib import Path
import hashlib,json,re

RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
ROOT=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
SUP=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
files=[Path(r'~\AGENTS.md'),ROOT/'BOARD.md',ROOT/'claude/B03/STREAM_NOTES.md',RUN.parents[1]/'STATUS.md',RUN.parents[1]/'LEARNED.md',RUN.parents[1]/'WORKLOG.md',Path(r'~\brain_workers\PRIMARY_DIRECTIVE.md'),Path(r'~\<private-repo>\12_cognitive_architecture\scheduled_tasks\README.md')]
files += [CAN/f for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
files += list(CAN.glob('*.tex'))
files += [SUP/f for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [p for p in (SUP/'sources').glob('*') if p.suffix in ('.txt','.md','.json','.tex')]
files += list((ROOT/'context').glob('*.txt'))
for stream in [(CAN/'runs/B03'),(CAN/'runs')]:
    if stream.exists():
        files += sorted(stream.glob('*/REPORT.md'))[-2:]
for name,run in [('A011','20261023T134844Z-fleet03-A011-representation-existence'),('A094','20261026T232939Z-fleet04-A094-proof-chain-challenger'),('A086','20261023T140222Z-fleet03-A086-joint-code-referee'),('A100','20261027T023227Z-fleet04-A100-release-and-continuation-ledger')]:
    d=ROOT/'agents'/name/'runs'/run
    files += [d/f for f in ['REPORT.md','CLAIMS.json','DERIVATION.md'] if (d/f).exists()]
rows=[];excerpts=[]
for p in dict.fromkeys(files):
    if not p.exists():
        rows.append({'path':str(p),'missing':True});continue
    raw=p.read_bytes()
    try:t=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:t=raw.decode('cp1252');enc='cp1252-explicit-fallback'
    rows.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'access':'full bytes decoded; selected relevant lines inspected, no fresh full literature audit'})
    if p.name in ['LEARNED.md','STREAM_NEXT_ACTIONS.json','CURRENT_STATUS.md','README.md'] or p.suffix=='.txt':
        lines=t.splitlines(); sel=[]
        for i,l in enumerate(lines):
            if re.search(r'A011|query.KL|contraction|signed|reset|composition|Theorem A|entropy.*influence|owner instruction',l,re.I):
                sel.append(f'{i+1}: {l[:400]}')
                if len(sel)>=12:break
        excerpts.append({'path':str(p),'lines':sel})
(RUN/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(RUN/'out/INTAKE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'files_read':len(rows),'missing':[r['path'] for r in rows if r.get('missing')],'paper_texts':[r['path'] for r in rows if r['path'].endswith('.txt')],'selected':[e for e in excerpts if 'LEARNED' in e['path'] or 'context' in e['path']]},ensure_ascii=False)[:15000])
