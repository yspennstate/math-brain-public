from pathlib import Path
helper=Path(__file__).resolve().parents[2]/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(helper.read_text(encoding='utf-8').split("rows=[];candidates=0;sets=0;wins=")[0],str(helper),'exec'))
from profile import reference
from rigorous_log import lg
def CE(P,Q):
    lo=hi=F(0);scale=1<<40
    for p,q in zip(P,Q):
        if p:
            ck(q>0);low,high=lg(1/q)
            lo+=p*F(math.floor(low*scale),scale);hi+=p*F(math.ceil(high*scale),scale)
    return lo,hi
def spec(values):return [F(x*x,len(values)**2) for x in walsh(values)]
def restricted(values,i,bit):return [values[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(values)//2)]
pairs=queries=0;min_gap=None
for a in (1,2):
    b=3*a;n=a+b;universe=list(itertools.combinations(range(a),2));A=(1<<a)-1
    for mask in range(1<<len(universe)):
        H=tuple(e for j,e in enumerate(universe) if mask>>j&1);table,Z,qprof=reference(a,b,H)
        q=[F(0)]+[qprof[(S&A,(S>>a).bit_count())] for S in range(1,1<<n)]
        ck(sum(q)==1);projected=[]
        for i in range(n):
            def lift(T):return (T&((1<<i)-1))|((T>>i)<<(i+1))
            qi=q[1<<i];qb=[F(0)]+[(q[lift(T)]+q[lift(T)|(1<<i)])/(1-qi) for T in range(1,1<<(n-1))]
            ck(sum(qb)==1);projected.append(qb)
        for truth in range(1<<(1<<a)):
            g=[(truth>>x)&1 for x in range(1<<a)]
            values=[1-2*int((g[x&A] if x>>a==0 else 0)+(int(x&A==0 and (x>>a).bit_count()==1))) for x in range(1<<n)]
            p=spec(values);v=1-p[0];root=CE(p,[1-v]+[v*x for x in q[1:]])
            for i,qb in enumerate(projected):
                costs=[]
                for bit in (0,1):
                    pp=spec(restricted(values,i,bit));vv=1-pp[0];QQ=[1-vv]+[vv*x for x in qb[1:]]
                    ck(sum(QQ)==1);costs.append(CE(pp,QQ))
                gap=root[0]-(costs[0][1]+costs[1][1])/2
                ck(gap>=0);min_gap=gap if min_gap is None else min(min_gap,gap);queries+=1
            pairs+=1
out={'function_reference_pairs':pairs,'all_single_coordinate_queries':queries,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'minimum_certified_full_CE_decrease':outward((min_gap,min_gap)),'scope':'both complete projected/calibrated terminals; arbitrary histories use version6 theorem'}
(R/'out/history.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
