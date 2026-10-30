import json,time,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261011T234647Z-fleet05-A032-boolean-phase-realizability'
def walsh(h):
    a=list(h); step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
        step*=2
    return a
def load():
    rows=json.loads((OLD/'out/mixed_slices_m4.json').read_text())['records']
    for r in rows:
        a=walsh(r['truth_h']);z=sum(v*v for v in a)
        marg=[sum(v*v for s,v in enumerate(a) if s>>i&1) for i in range(4)]
        r['N']=sum(t not in (0,z) and 2*t!=z for t in marg)
    return rows
if __name__=='__main__':
    start=time.monotonic();rows=load();stats=collections.Counter((r['norm_integer'],r['N']) for r in rows)
    out={'rows':len(rows),'norm_N_counts':[[k,n,c] for (k,n),c in sorted(stats.items())],'max_N':max(r['N'] for r in rows),'seconds':time.monotonic()-start}
    (ROOT/'out/pilot.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
