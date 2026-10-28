from pathlib import Path
import time,json
import check as prod
ROOT=Path(__file__).resolve().parents[1]; rows=[]; original=prod.exact_phase
def serialize(e): return {str(k):str(v) for k,v in e.items()}
def wrapped(f,ref,idx,target):
    sigma,kappa,E,O=original(f,ref,idx,target)
    w=prod.fwht(f); pairs=[(s,s|(1<<idx)) for s in range(len(f)) if not s&(1<<idx)]
    rho=[]
    for b in (0,1):
        total=prod.Q(0)
        for s,t in pairs:
            den=w[s]*w[s]+w[t]*w[t]
            total+=(ref[s]+ref[t])*(prod.Q((w[s]+(-1)**b*w[t])**2,2*den) if den else prod.Q(1,2))
        rho.append(str(total))
    rows.append({'index':idx,'actual_rho':rho,'raw_kappa':serialize(kappa),'erasure_E':serialize(E),'outcome_O':serialize(O),'net_sigma':serialize(sigma),'raw_kappa_bounds':list(map(str,prod.bounds(kappa))),'net_sigma_bounds':list(map(str,prod.bounds(sigma)))})
    return sigma,kappa,E,O
prod.exact_phase=wrapped; start=time.perf_counter(); prod.case(2,0,(1,0,0,0),2)
out={'status':'PASS','cases':2,'assertions':prod.count,'seconds':time.perf_counter()-start,'physical_rows':rows,'positive_raw_rows':sum(prod.bounds({int(k):prod.Q(v) for k,v in r['raw_kappa'].items()})[0]>0 for r in rows)}
(ROOT/'out/FIXTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='physical_rows'}))
