from pathlib import Path
import time,json
import independent as ind
ROOT=Path(__file__).resolve().parents[1]; ind.RECEIPTS=[]; start=time.perf_counter()
for policy in ('one0','one1'): ind.fixture(0,(1,0,0,0),2,policy)
rows=ind.RECEIPTS
out={'status':'PASS','cases':2,'assertions':ind.count,'seconds':time.perf_counter()-start,'physical_rows':rows,
     'positive_raw_rows':sum(ind.bounds({int(k):ind.F(v) for k,v in r['raw_kappa'].items()})[0]>0 for r in rows)}
(ROOT/'out/FIXTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='physical_rows'}))
