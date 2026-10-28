from pathlib import Path
import json, hashlib, shutil
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
for d in ['out','code']: (R/d).mkdir(exist_ok=True)
old=A/'runs/20261023T135604Z-account03-A051-near-extremizer-definition/code/exact_utils.py'
shutil.copyfile(old,R/'code/exact_utils.py')
root=Path(r'~\mop_fei100')
sources=[]
paths=list((root/'reports/fei-2026-10-11').glob('*.json'))+list((root/'reports/fei-2026-10-11').glob('*.md'))+list((root/'reports/fei-2026-10-11').glob('*.tex'))
sup=root/'research_pushes/2026-10-11-full-fei-100-agents'
paths += [sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((sup/'sources').glob('*.txt'))
base=A.parents[1]
paths += list((base/'context').glob('*.txt'))
paths += [base/'BOARD.md',base/'claude/B11/STREAM_NOTES.md']
paths += [base/'agents/A054/runs/20261026T222013Z-account04-A054-connectedness-alternatives/PROOF.md',base/'agents/A055/runs/20261027T011322Z-account04-A055-extremal-obstruction-referee/PROOF.md']
for p in paths:
 if not p.exists(): sources.append({'path':str(p),'status':'MISSING'});continue
 raw=p.read_bytes()
 try: s=raw.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError: s=raw.decode('cp1252');encoding='cp1252'
 # Refresh full source bytes and locate the present mathematical interface.
 lines=s.splitlines()
 hits=[(i+1,l[:220]) for i,l in enumerate(lines) if any(t in l.lower() for t in ['critical','near-extrem','log-sobolev','composition','entropy','a051'])]
 sources.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,'scope':'source-byte refresh and relevant line scan; not a new complete paper audit','locators':hits[:12]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
spec={'helper':'exact_utils.py copied unchanged from A051 preceding stage; hash '+hashlib.sha256((R/'code/exact_utils.py').read_bytes()).hexdigest(),'family':'all labelled Boolean signs n=0..3','domain':{'roots':278,'proper_blocks':1568,'rates':[2,3,4,8,16],'events':'all nonempty proper subsets of the queried pattern alphabet, at C=4'},'case_count':{'budgets':7840,'event_splits':12352},'symmetry':'none','arithmetic':'integer Walsh, Fraction probabilities, prime-log vectors; rational atanh sign bounds','memory_estimate_mb':110,'max_runtime_seconds':55,'pilot':'all n<=2 and n3 table IDs 0,17,...255; excluded from final full count','dimension_escalation':False}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('SOURCE_RECEIPTS',len(sources),'FROZEN_SPEC saved')
