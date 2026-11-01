"""Exact nearest six-variable quadratic via Gray code and Walsh linear optimization."""
from pathlib import Path
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(a):
    a=a.copy();h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return a
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    f=json.loads((R/'out/boolean_counterexample.json').read_text(encoding='utf-8'))['truth_table']
    edges=[(i,j) for i in range(6) for j in range(i+1,6)]
    flips=[[x for x in range(64) if x>>i&1 and x>>j&1] for i,j in edges]
    v=f.copy();old=0;best=None;polar_best=None;count=0
    for k in range(256 if pilot else 32768):
        gray=k^(k>>1)
        if k:
            bit=(gray^old).bit_length()-1
            for x in flips[bit]:v[x]=-v[x]
        old=gray;w=walsh(v);linear=max(range(64),key=lambda s:abs(w[s]));cor=w[linear]
        rec={'correlation':abs(cor),'quadratic_edges':[edges[j] for j in range(15) if gray>>j&1],
             'linear_mask':linear,'constant':int(cor<0),'distance':(64-abs(cor))//2}
        if best is None or rec['distance']<best['distance']:best=rec
        if gray&31 and (polar_best is None or rec['distance']<polar_best['distance']):polar_best=rec
        count+=1
    for rec in [best,polar_best]:
        if rec is None:continue
        q=[(-1)**((rec['constant']+(x&rec['linear_mask']).bit_count()+sum((x>>i&1)*(x>>j&1) for i,j in rec['quadratic_edges']))%2) for x in range(64)]
        rec['edit_vertices']=[x for x in range(64) if q[x]!=f[x]]
        assert len(rec['edit_vertices'])==rec['distance']
    out={'status':'PASS','pilot':pilot,'quadratic_parts':count,'best':best,'best_selected_polar':polar_best,'elapsed_seconds':time.perf_counter()-start}
    (R/'out'/('quadratic_distance_pilot.json' if pilot else 'quadratic_distance.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out))
if __name__=='__main__':main()
