"""All physical restriction states; exact formal prime-log arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
from itertools import product
import json,time,sys,hashlib
import previous_helpers as u
R=Path(__file__).resolve().parents[1]; OUT=R/'out'; checks=0
def save(name,v): (OUT/name).write_text(json.dumps(v,indent=2,default=str)+'\n',encoding='utf-8',newline='')
def ck(v,why):
    global checks
    checks+=1
    assert v,(checks,why)
def add(*terms):
    d={}
    for a in terms:
        for p,c in a.items(): d[p]=d.get(p,Q(0))+c
    return {p:c for p,c in d.items() if c}
def mul(a,c): return {p:x*c for p,x in a.items() if x*c}
def C(c): return {2:Q(c)} if c else {}
@lru_cache(None)
def factors(a):
    d={}; k=2
    while k*k<=a:
        while a%k==0: d[k]=d.get(k,0)+1; a//=k
        k+=1
    if a>1: d[a]=d.get(a,0)+1
    return d
@lru_cache(None)
def H(f):
    N=len(f); n=N.bit_length()-1; out={}
    for a,c in Counter(abs(z) for z in u.fwht(f)).items():
        if a:
            w=Q(c*a*a,N*N); out=add(out,C(2*n*w),mul(factors(a),-2*w))
    return out
def interval(a):
    lo=hi=Q(0)
    for p,c in a.items():
        l,h=u.log2_bounds(Q(p)); lo+=c*(l if c>0 else h); hi+=c*(h if c>0 else l)
    return lo,hi
def nonneg(a): return not a or interval(a)[0]>=0
@lru_cache(None)
def infs(f): return tuple(u.infs(f))
def I(f): return sum(infs(f),Q(0))

def family(m,t):
    raw=u.build(m,t)
    roots=[tuple(tuple(u.restrict(g,m,x)) for g in raw) for x in (0,1)]
    state_cache={}; data_cache={}
    def state(x,ys,ab):
        key=x,ys,ab
        if key in state_cache:return state_cache[key]
        dk=x,ys
        if dk not in data_cache:
            indices=[j for j in range(len(roots[x][0])) if all(b<0 or ((j>>i)&1)==b for i,b in enumerate(ys))]
            data_cache[dk]=tuple(tuple(g[j] for j in indices) for g in roots[x])
        cores=data_cache[dk]; free_y=[i for i,b in enumerate(ys) if b<0]
        ctrl=[i for i,b in enumerate(ab) if b<0]; pi=[Q(0)]*3; f=[]
        for row in range(1<<len(ctrl)):
            vals=list(ab)
            for j,k in enumerate(ctrl): vals[k]=(row>>j)&1
            label=0 if vals[0] else (1 if vals[1] else 2)
            pi[label]+=Q(1,1<<len(ctrl)); f.extend(cores[label])
        f=tuple(f); ht={}; it=Q(0)
        for p,g in zip(pi,cores): ht=add(ht,mul(H(g),p)); it+=p*I(g)
        hh=H(f); ll=add(hh,mul(ht,-1)); ss=add(C(8*it),mul(ht,-1))
        rr=sum((2*pi[j]*pi[k]*I(tuple(a*b for a,b in zip(cores[j],cores[k]))) for j in range(3) for k in range(j+1,3)),Q(0))
        nd=len(cores[0]).bit_length()-1; ic=sum(infs(f)[nd:],Q(0))
        v={'x':x,'ys':ys,'ab':ab,'cores':cores,'f':f,'pi':tuple(pi),'H':hh,'HT':ht,'IT':it,'L':ll,'S':ss,'R':rr,'IC':ic,'free_y':free_y,'ctrl':ctrl,'nd':nd}
        state_cache[key]=v; return v
    return roots,state,state_cache

def main():
    started=time.perf_counter(); summaries=[]; pilot='--pilot' in sys.argv
    domain=[(4,0)] if pilot else [(4,0),(4,1),(6,0),(6,1)]
    for m,t in domain:
        tic=time.perf_counter(); roots,node,cache=family(m,t); delta=Q(1,2**m); p=Q(1,2**t)
        ys0=(-1,)*m; ab0=(-1,-1); rts=[node(x,ys0,ab0) for x in (0,1)]
        S0=mul(add(*(v['S'] for v in rts)),Q(1,2)); L0=mul(add(*(v['L'] for v in rts)),Q(1,2)); H0=mul(add(*(v['H'] for v in rts)),Q(1,2)); IT0=sum((v['IT']/2 for v in rts),Q(0)); R0=sum((v['R']/2 for v in rts),Q(0))
        lower=p*(3*m+1+4*t); U=p*m*delta/2
        ck(R0==p*(3*m-1+3*t)*delta/4,'root bank activation')
        ck(nonneg(add(S0,C(-lower))),'root source admission')
        ck(nonneg(add(C(R0+10*p*delta),mul(L0,-1))),'root full control bill')
        local_nodes=local_edges=0
        for x in (0,1):
            for ys in product((-1,0,1),repeat=m):
                for ab in product((-1,0,1),repeat=2):
                    v=node(x,ys,ab); local_nodes+=1
                    ck(nonneg(v['L']),'full terminal entropy retained')
                    ck(nonneg(add(C(v['R']+10*v['IC']),mul(v['L'],-1))),'all controller specializations incl n=0')
                    for kind,coords in [('data',v['free_y']),('control',v['ctrl'])]:
                        for j in coords:
                            cc=[]
                            for b in (0,1):
                                yy=list(ys); aa=list(ab)
                                if kind=='data': yy[j]=b
                                else: aa[j]=b
                                cc.append(node(x,tuple(yy),tuple(aa)))
                            def avg(k):
                                if k in ('H','HT','L','S'):return mul(add(*(q[k] for q in cc)),Q(1,2))
                                return sum((q[k]/2 for q in cc),Q(0))
                            pos=v['free_y'].index(j) if kind=='data' else v['nd']+v['ctrl'].index(j)
                            d=infs(v['f'])[pos]; dd=add(v['H'],mul(avg('H'),-1)); earned=add(C(10*d),mul(dd,-1))
                            lhs=add(avg('S'),earned,mul(v['S'],-1))
                            rhs=add(C((2 if kind=='data' else 10)*d),mul(v['L'],-1),avg('L'))
                            ck(not add(lhs,mul(rhs,-1)),'exact prime-log signed transport identity')
                            ck(v['IT']-avg('IT')==(d if kind=='data' else 0),'physical data versus controller influence ownership')
                            ck(avg('R')<=v['R'],'bank contraction')
                            ck(nonneg(dd),'actual entropy decrement')
                            local_edges+=1
        # Representative complete cuts: all data, all controls, and variable-dependent mixed histories.
        def cut(policy):
            leaves=[]; pd=pc=Q(0)
            def walk(v,w):
                nonlocal pd,pc
                target=policy(v)
                if target is None:leaves.append((v,w)); return
                kind,j=target
                pos=v['free_y'].index(j) if kind=='data' else v['nd']+v['ctrl'].index(j)
                d=infs(v['f'])[pos]
                if kind=='data':pd+=w*d
                else:pc+=w*d
                for b in (0,1):
                    yy=list(v['ys']); aa=list(v['ab'])
                    if kind=='data':yy[j]=b
                    else:aa[j]=b
                    walk(node(v['x'],tuple(yy),tuple(aa)),w/2)
            for v in rts:walk(v,Q(1,2))
            ST={}; HT={}; LT={}; it=rr=ic=Q(0)
            for v,w in leaves:
                ST=add(ST,mul(v['S'],w)); HT=add(HT,mul(v['H'],w)); LT=add(LT,mul(v['L'],w)); it+=w*v['IT']; rr+=w*v['R']; ic+=w*v['IC']
            E=add(C(10*(pd+pc)),mul(H0,-1),HT); capacity=add(ST,E)
            exact=add(S0,C(2*pd+10*pc),mul(L0,-1),LT)
            ck(not add(capacity,mul(exact,-1)),'complete cut identity')
            ck(rr<=R0,'complete cut same bank')
            ck(nonneg(add(capacity,C(-rr-U),mul(S0,-Q(71,78)),C(-2*pd-10*pc))),'all-cut fixed ancestor source debit')
            return {'leaves':len(leaves),'data_cost':str(pd),'control_cost':str(pc),'S_interval':[str(q) for q in interval(ST)],'E_interval':[str(q) for q in interval(E)],'R':str(rr),'capacity_lower':str(interval(capacity)[0]),'IT':str(it)},(ST,E,LT,it)
        policies={
          'all_y':lambda v:('data',v['free_y'][0]) if v['free_y'] else None,
          'controls_first_then_y':lambda v:('control',v['ctrl'][0]) if v['ctrl'] else (('data',v['free_y'][0]) if v['free_y'] else None),
          'mixed_adaptive':lambda v: (('control',v['ctrl'][-1]) if v['ctrl'] and (sum(b==1 for b in v['ys'])+len(v['free_y']))%3==0 else (('data',v['free_y'][-1]) if v['free_y'] else None))
        }
        cuts={}
        for name,pol in policies.items():
            z,res=cut(pol); cuts[name]=z
            if name=='all_y':
                sf,ef,lf,itf=res
                ck(not add(lf,C(-2*p*delta)),'final actual controller entropy')
                ck(itf==p*(1+t),'final full terminal influence')
                ck(nonneg(add(ef,L0,C(-4*p*m))),'earned credit crosses final collapse')
        summaries.append({'m':m,'t':t,'node_states':local_nodes,'query_edges':local_edges,'root_S_lower':str(interval(S0)[0]),'root_control_bill_interval':list(map(str,interval(L0))),'cuts':cuts,'seconds':time.perf_counter()-tic})
        save('DIRECT.json',{'status':'RUNNING','cases':summaries,'assertions':checks})
        print(json.dumps({'m':m,'t':t,'nodes':local_nodes,'edges':local_edges,'seconds':time.perf_counter()-tic}),flush=True)
        if pilot:break
        ck(time.perf_counter()-started<60,'frozen runtime ceiling')
        # Each case's caches contain different point activation layouts; release them between cases.
        H.cache_clear(); infs.cache_clear()
    scalar=[]
    for m in range(4,102,2):
        for t in (0,m,3*m+1):
            delta=Q(1,2**m); p=Q(1,2**t); S=p*(3*m+1+4*t); R0=p*(3*m-1+3*t)*delta/4; U=p*m*delta/2
            loss=R0+10*p*delta; theta=2*delta/3+10*delta/(3*m+1+4*t)
            ck(R0+U+loss<=theta*S,'three separate original-source bookings')
            ck(theta<=Q(7,78),'uniform unused ancestor fraction')
            scalar.append({'m':m,'t':t,'fraction':str(theta),'remaining_fraction':str(1-theta)})
    save('SCALAR.json',{'status':'PASS','cases':len(scalar),'rows':scalar})
    save('PILOT.json' if pilot else 'DIRECT.json',{'status':'PASS','cases':summaries,'node_states':sum(x['node_states'] for x in summaries),'query_edges':sum(x['query_edges'] for x in summaries),'assertions':checks,'seconds':time.perf_counter()-started,'arithmetic':'exact prime-log expressions and certified rational intervals','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    print(json.dumps({'status':'PASS','pilot':pilot,'assertions':checks,'seconds':time.perf_counter()-started}),flush=True)
if __name__=='__main__':main()
