import json,time
from pathlib import Path
from fractions import Fraction as F
from collections import deque
import exact_library as e
import phase_library as p
ROOT=Path(__file__).resolve().parents[1];checks=0
def ck(x):
    global checks
    checks+=1
    if not x:raise AssertionError(checks)
def sg(v,c=0):return e.sign(v,c)
def upper_bits(v):
    if not v:return F(0)
    if set(v)<={2}:return v.get(2,F(0))
    lo,hi=e.enclosure(v);l2,h2=e.lnprime(2)
    top=max(F(x,y) for x in (lo,hi) for y in (l2,h2));scale=1<<64
    return F(-(-top.numerator*scale//top.denominator),scale)
def flow(v,charges,K):
    N=len(v);n=N.bit_length()-1;records=[];feasible=True;positive=0
    for sign in (-1,1):
        P=[x for x in range(N) if v[x]==sign];source=N;sink=N+1;size=N+2
        cap=[[F(0)]*size for _ in range(size)]
        for x in P:
            b=charges[x]
            if b>0:cap[source][x]=b;positive+=1
            elif b<0:cap[x][sink]=-b
            for i in range(n):
                y=x^(1<<i)
                if v[y]==sign:cap[x][y]=F(K,2)
        res=[list(row) for row in cap];value=F(0)
        while True:
            prev=[-1]*size;prev[source]=source;q=deque([source])
            while q and prev[sink]<0:
                x=q.popleft()
                for y in range(size):
                    if prev[y]<0 and res[x][y]>0:prev[y]=x;q.append(y)
            if prev[sink]<0:break
            path=[];y=sink
            while y!=source:path.append((prev[y],y));y=prev[y]
            delta=min(res[x][y] for x,y in path);value+=delta
            for x,y in path:res[x][y]-=delta;res[y][x]+=delta
        demand=sum(cap[source]);ok=value==demand;feasible &=ok
        edges=[];div={x:F(0) for x in P}
        for x in P:
            for i in range(n):
                y=x^(1<<i)
                if y>x and v[y]==sign:
                    a=cap[x][y]-res[x][y];ck(abs(a)<=F(K,2))
                    div[x]+=a;div[y]-=a
                    if a:edges.append([x,y,str(a)])
        if ok:
            for x in P:ck(div[x]>=charges[x])
        reachable=[x for x in P if prev[x]>=0]
        records.append({'sign':sign,'feasible':ok,'demand':str(demand),'flow_value':str(value),
                        'vertices':P,'charges_upper':[str(charges[x]) for x in P],
                        'net_flow_edges':edges,'divergences':{str(x):str(z) for x,z in div.items()},
                        'failure_cut_vertices':reachable if not ok else []})
    return feasible,positive,records
def prepare(n):
    N=1<<n;data=[]
    for code in range(1<<N):
        v=[1 if code>>x&1 else -1 for x in range(N)];w=e.fwht(v);ck(w==e.direct(v))
        H=p.entropy([F(a*a,N*N) for a in w]);I=F(sum(v[x]!=v[x^(1<<i)] for x in range(N) for i in range(n)),N)
        ck(I==sum(F(s.bit_count()*a*a,N*N) for s,a in enumerate(w)))
        g=[];piv=[]
        for x in range(N):
            z={}
            for s,a in enumerate(w):
                if a:z=p.add(z,p.lograt(F(a*a,N*N)),F(a*v[x]*(-1 if (x&s).bit_count()%2 else 1),N))
            g.append(z);piv.append(sum(v[x]!=v[x^(1<<i)] for i in range(n)))
        ck(p.add(sum_vectors(g),p.scale(H,N))=={})
        data.append(dict(v=v,H=H,I=I,g=g,piv=piv))
    return data
def sum_vectors(vs):
    ans={}
    for v in vs:ans=p.add(ans,v)
    return ans
def main():
    start=time.perf_counter();maxima={};total=edits=cutchecks=flowchecks=positivefeasible=0;firstpositive=None;guards=[]
    for n in (1,2,3):
        N=1<<n;data=prepare(n);maxrows={}
        for K in (1,2,3,4):
            best=0;ties=[0];D=[p.add(a['H'],{2:K*a['I']},-1) for a in data]
            for code in range(1,len(data)):
                comparison=sg(p.add(D[code],D[best],-1))
                if comparison>0:best=code;ties=[code]
                elif comparison==0:ties.append(code)
            maxrows[K]=ties;maxima[f'n{n}_K{K}']={'D_natural_log_vector':p.enc(D[best]),'tables':ties}
        for code,a in enumerate(data):
            if time.perf_counter()-start>50:raise RuntimeError('Pilot 55-second stopping guard')
            total+=1;v=a['v'];g=a['g'];sums=[{}]*(1<<N);bound=[0]*(1<<N);same=[False]*(1<<N)
            for E in range(1,1<<N):
                bit=E&-E;x=bit.bit_length()-1;prev=E^bit
                sums[E]=p.add(sums[prev],g[x]);bound[E]=bound[prev]+sum(v[x]*v[x^(1<<i)]*(1-2*bool(prev>>(x^(1<<i))&1)) for i in range(n))
                signs={v[y] for y in range(N) if E>>y&1};same[E]=len(signs)==1
            strong={K:True for K in (1,2,3,4)};relaxed=dict(strong);mono=dict(strong)
            for E in range(1<<N):
                size=E.bit_count();delta=F(size,N);edited=data[code^E]
                editexpr=p.add(p.add(edited['H'],a['H'],-1),sums[E],-F(4,N))
                ck(sg(editexpr,8*delta)>=0)
                ck(edited['I']-a['I']==F(2*bound[E],N));edits+=1
                for K in (1,2,3,4):
                    expr=p.add(sums[E],{2:F(K*bound[E],2)},-1)
                    if sg(expr,-2*size)>0:strong[K]=False
                    relaxexpr=p.add(expr,{2:3*size},-1);viol=sg(relaxexpr)>0
                    relaxed[K]&=not viol
                    if same[E]:mono[K]&=not viol
                    cutchecks+=1
            for K in (1,2,3,4):
                ck(relaxed[K]==mono[K])
                charges=[upper_bits(g[x])-3+F(K*a['piv'][x],2) for x in range(N)]
                ok,pos,cert=flow(v,charges,K);ck(ok==relaxed[K]);flowchecks+=1
                if ok and pos:
                    positivefeasible+=1
                    if firstpositive is None:
                        firstpositive={'n':n,'code':code,'K':K,'certificate':cert}
                if code in maxrows[K]:
                    ck(strong[K]);ck(ok)
                    out={'n':n,'truth_code':code,'K':K,'maximal_deficit':True,
                         'truth_values':v,'potential_natural_log_vectors':[p.enc(x) for x in g],
                         'pivot_degrees':a['piv'],'flow_certificate':cert}
                    (ROOT/f'out/certs/n{n}_K{K}_table{code}.json').write_text(json.dumps(out,indent=2)+'\n')
                if n==3 and code in (105,150) and K==3:
                    ck(not strong[K]);ck(not ok);guards.append({'code':code,'K':K,'flow':cert})
    ck(len(guards)==2)
    result={'status':'PASS','truth_tables':total,'all_vertex_edit_pairs':edits,'signed_cut_checks':cutchecks,
            'two_sign_flow_problems':2*flowchecks,'feasible_with_positive_charge':positivefeasible,
            'first_positive_charge_flow':firstpositive,'maximal_deficits':maxima,'parity_guards':guards,
            'assertions':checks,'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('first_positive_charge_flow','maximal_deficits','parity_guards')}))
if __name__=='__main__':main()
