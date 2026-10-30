from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[3]
camp=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
paths=[camp/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))
paths += list((BASE/'context').glob('*.txt'))+[BASE/'BOARD.md',BASE/'claude/B20/STREAM_NOTES.md']
paths += [BASE/'agents/A097/STATUS.md',BASE/'agents/A097/LEARNED.md']
dirs=[('A096','20261023T010221Z-fleet03-A096-live-gap-ledger',['DERIVATION.md','CLAIMS.json','REPORT.md','code/check.py']),('A097','20261021T232544Z-fleet03-A097-cross-route-transfer',['DERIVATION.md','CLAIMS.json','REPORT.md']),('A085','20261022T234859Z-fleet03-A085-certificate-adversary',['PROOF.md','CLAIMS.json','REPORT.md']),('A099','20261022T231100Z-fleet03-A099-candidate-assembly',['REPORT.md','CLAIMS.json']),('A073','20261022T211534Z-fleet03-A073-certified-logarithms',['DERIVATION.md','CLAIMS.json'])]
for who,run,files in dirs:paths += [BASE/'agents'/who/'runs'/run/f for f in files]
records=[];selected=[]
for p in paths:
 if not p.is_file():records.append({'path':str(p),'status':'MISSING'});continue
 data=p.read_bytes()
 try:txt=data.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError:txt=data.decode('cp1252');encoding='cp1252 legacy PDF export; bytes unchanged'
 records.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':encoding,'lines':len(txt.splitlines())})
 if p.name in ['BOARD.md','STREAM_NOTES.md','DERIVATION.md','PROOF.md']:
  hits=[f'{i+1}: {line}' for i,line in enumerate(txt.splitlines()) if any(k in line.lower() for k in ['original source','original-source','current reference','current inherited','a097','first unsupported'])]
  selected.append('\nSOURCE '+str(p)+'\n'+'\n'.join(hits[:15]))
(RUN/'out/SOURCES.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
(RUN/'out/INTAKE_EXTRACTS.txt').write_text('\n'.join(selected),encoding='utf-8')
print(json.dumps({'sources':len(records),'missing':[r['path'] for r in records if r.get('status')=='MISSING']}))
