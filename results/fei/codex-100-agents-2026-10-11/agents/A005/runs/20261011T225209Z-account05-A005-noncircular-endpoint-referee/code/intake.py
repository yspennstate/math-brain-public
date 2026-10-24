from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
team=Path('~/brain_workers/FEI100_20261011')
paths=[campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))+list((team/'context').glob('*.txt'))
paths += [team/'BOARD.md',team/'claude/B01/STREAM_NOTES.md']
paths += list((campaign/'runs').rglob('REPORT.md'))
for agent in ['A001','A002','A082','A086']:
    paths+=list((team/'agents'/agent/'runs').glob('*/REPORT.md'))
records=[]
for path in paths:
    b=path.read_bytes()
    try: s=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252');enc='cp1252'
    records.append({'path':str(path),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':len(s.splitlines()),'encoding':enc})
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2))
spec={'helper_version':'A005-v1','family':'all labelled Boolean seeds on n=1,2,3; tensor point activations without balancing literal',
      'domain':'k=1,2; m=1,2 for n<=2; m=1 for all n=3; additionally m=2 for truth-table integers 1,23,105,150 at n=3',
      'case_count_full':600,'pilot':'n<=2, 80 cases, max dimension 6',
      'symmetry':'none','arithmetic':'integer FWHT and Fraction; exact rational coefficients of log2 primes',
      'estimated_memory_MB':60,'maximum_runtime_seconds':60,'maximum_dimension':8,'no_automatic_escalation':True}
(ROOT/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2))
print(json.dumps({'sources_loaded':len(records),'spec_saved':True}))
