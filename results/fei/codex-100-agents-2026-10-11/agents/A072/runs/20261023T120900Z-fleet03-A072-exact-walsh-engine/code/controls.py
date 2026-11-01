from drift import *
import drift

def main():
    start=time.perf_counter();cases=[]
    inputs=[
      ('constant',(g(2),g(1)),(1,)*4),
      ('projection',(g(2),g(2)),tuple(1 if not x&1 else -1 for x in range(4))),
      ('parity',(g(3),g(2)),tuple((-1)**x.bit_count() for x in range(4))),
      ('opposite_bias_AND',(g(2),tuple(-v for v in g(2))),tuple(1 if x==0 else -1 for x in range(4))),
      ('parity_with_dummy_core',(g(2),(1,)*2,g(1)),tuple((-1)**x.bit_count() for x in range(8))),
      ('negated_AND',(g(3),g(2),g(1)),tuple(-1 if x==0 else 1 for x in range(8)))
    ]
    for name,ts,h in inputs:
        p=compose(ts,h);rows=[row(p,j,i) for j in range(len(ts)) for i in range(p['ns'][j])]
        cases.append(dict(name=name,n=sum(p['ns']),q=[str(q) for q in p['q']],C=rec(p['C']),rows=rows))
        ck(time.perf_counter()-start<55)
        save('CONTROLS_PARTIAL.json',cases)
    out=dict(verdict='PASS',cases=len(cases),physical_rows=sum(len(z['rows']) for z in cases),checks=drift.CHECKS,runtime_seconds=time.perf_counter()-start,zero_influence_query_checked=any(F(rr['influence'])==0 for c in cases for rr in c['rows']),cases_detail=cases)
    save('CONTROLS.json',out);print(json.dumps({k:v for k,v in out.items() if k!='cases_detail'}))
if __name__=='__main__':main()
