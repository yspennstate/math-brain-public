from pathlib import Path
from fractions import Fraction as F
import json,time
from check_rank_pair import root,children,entropy,inf,add,constant,hamp,positive,interval,walsh
R=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter(); checks=0; rows=[]
    def ck(t):
        nonlocal checks
        checks+=1
        if not t: raise AssertionError(checks)
    cores=[('literal',[1,-1]),('point2',[-1,1,1,1]),('bent2',[1,1,1,-1])]
    for name,h in cores:
        f0=root(2); f=[f0[x&63]*h[x>>6] for x in range(64*len(h))]
        N=len(f); n=N.bit_length()-1
        direct=[sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(N)) for s in range(N)]
        ck(direct==walsh(f)); checks+=N
        Hd=add(*[(hamp(F(a,N)),1) for a in direct]); ck(Hd==entropy(f))
        ck(Hd==add((entropy(f0),1),(entropy(h),1)))
        physical=F(sum(f[x]!=f[x^(1<<j)] for x in range(N) for j in range(n)),N)
        ck(physical==inf(f)); ck(inf(f)==inf(f0)+inf(h))
        qs=F(sum(f[x]!=f[x^(1<<j)] for x in range(N) for j in [0,1]),N)
        ck(qs==F(1,4))
        gs=children(f); resets=[]
        for u,g in enumerate(gs):
            gp=[g[x^(((x>>1)&1)<<0)] for x in range(len(g))] if u==1 else g[:]
            ck(entropy(gp)==entropy(g)); ck(inf(g)-inf(gp)==(F(1,4) if u==1 else 0))
            ck(entropy(g)==add((entropy(children(f0)[u]),1),(entropy(h),1)))
            physical_child=F(sum(gp[x]!=gp[x^(1<<j)] for x in range(len(gp)) for j in range(n-2)),len(gp))
            ck(physical_child==inf(gp)); resets.append(gp)
        rho=sum(inf(g)-inf(gp) for g,gp in zip(gs,resets))/4
        ck(rho==F(1,16))
        L=add((Hd,1),*[(entropy(g),F(-1,4)) for g in gs]); K=F(15,4)
        paid=add((constant(K*(qs+rho)),1),(L,-1))
        ck(positive(add((paid,1),(constant(F(5,512)),-1))))
        D=add((Hd,1),(constant(K*inf(f)),-1))
        S=add(*[(constant(K*inf(g)),F(1,4)) for g in resets],*[(entropy(g),F(-1,4)) for g in resets])
        ck(add((D,1),(S,1),(paid,1))=={})
        rows.append({'core':name,'rho':str(rho),'paid_margin_bits':[str(x) for x in interval(paid)],'all_four_terminals':'retained'})
        ck(time.perf_counter()-start<52)
    out={'status':'PASS','checks':checks,'roots':3,'original_terminals':12,'reset_terminals':12,'rows':rows,'seconds':time.perf_counter()-start}
    (R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__': main()
