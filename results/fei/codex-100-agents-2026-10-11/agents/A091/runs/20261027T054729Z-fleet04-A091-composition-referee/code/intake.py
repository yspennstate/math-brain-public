from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
sources=[]
def read(p,role):
    p=Path(p); raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252'); enc='cp1252'
    sources.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc,role=role))
    return s
base=Path('math-open-problems/reports/fei-2026-10-11')
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    read(base/name,'campaign protocol/navigation read in full by intake; relevant excerpts reviewed')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    s=read(supp/name,'supplement intake'); print(name, len(s), s[:220].replace('\n',' '))
context=Path('context')
loc=[]
for p in context.glob('*.txt'):
    s=read(p,'paper baseline locator refresh, no new literature claim')
    hits=[(i+1,line[:230]) for i,line in enumerate(s.splitlines()) if re.search('composition|shared.data|pivotal|stopping',line,re.I)]
    loc.append(dict(path=str(p),hits=hits[:18]))
agents=Path('agents')
for agent,run in [('A059','20261026T223551Z-fleet04-A059-decomposition-depth'),('A060','20261027T011815Z-fleet04-A060-composition-sharpness')]:
    for name in ['REPORT.md','PROOF.md','CLAIMS.json']:
        read(agents/agent/'runs'/run/name,'direct load-bearing source read by referee')
for p in (supp/'sources').glob('*'):
    if p.is_file() and p.suffix in ['.md','.txt','.tex','.json']: read(p,'supplement source inventory/intake')
for name in ['PROOF.md','ONESHOT_PROOF.md','CLAIMS.json']:
    read(agents/'A091/runs/20261023T140242Z-fleet03-A091-composition-referee'/name,'prior stage dependency')
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCES.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
(ROOT/'out/PAPER_LOCATORS.json').write_text(json.dumps(loc,indent=2),encoding='utf-8')
print('Source records',len(sources))
