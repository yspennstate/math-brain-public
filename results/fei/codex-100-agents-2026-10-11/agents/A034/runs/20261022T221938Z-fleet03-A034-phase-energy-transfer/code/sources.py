from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
base=Path(r'math-open-problems/reports\fei-2026-10-11')
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'context')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((sup/'sources').glob('*.md'))
paths += sorted(ctx.glob('*.txt'))
paths += [Path(r'BOARD.md'),Path(r'claude\B07\STREAM_NOTES.md')]
receipts=[]; extracts=[]
for p in paths:
    data=p.read_bytes()
    try: text=data.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError: text=data.decode('cp1252'); encoding='cp1252'
    receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':encoding,'scope':'full file loaded; selected relevant locators inspected, no assertion every page mathematically reconstructed'})
    hits=[]
    for i,line in enumerate(text.splitlines()):
        if any(term in line.lower() for term in ['a034','phase','affine','conditional spectral','theorem 3.1','corollary 8.2','c018','c024']):
            hits.append({'line':i+1,'text':line[:450]})
    extracts.append({'path':str(p),'locators':hits[:12]})
(RUN/'out'/'source_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/'source_extracts.json').write_text(json.dumps(extracts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files_loaded':len(receipts),'paper_encodings':[{ 'path':r['path'],'encoding':r['encoding']} for r in receipts if r['path'].endswith('.txt')],'relevant_sources':[x for x in extracts if x['path'].endswith('ROUTE_MAP_CURATED.md') or x['path'].endswith('threshold_paper_38pp.txt') or x['path'].endswith('FEI_100_agent_research_plan.tex')]}))
