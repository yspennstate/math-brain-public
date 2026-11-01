"""Frozen seven profiles and the inherited-credit recursion for all core1 orders."""
from subsidy import *

def allocate(ss,A,T):
    ns=[pos(neg(s)) for s in ss];ps=[pos(s) for s in ss]
    N=avg(ns);P=avg(ps);gap=sub(N,A)
    ck(T[0]>=0)
    if gap[1]<0:
        if P[0]>0:
            kernel=[div(p,P) for p in ps]
            credits=[plus(n,mul(sub(A,N),k)) for n,k in zip(ns,kernel)]
        else:
            ck(all(s[1]<0 for s in ss));ck(N[0]>0)
            kernel=[div(n,N) for n in ns];credits=[mul(A,k) for k in kernel]
        flows=[(0,0),(0,0)];newgross=(0,0)
    elif gap[0]>0:
        ck(N[0]>0 and P[0]>0)
        kernel=[div(p,P) for p in ps]
        credits=[mul(div(A,N),n) for n in ns]
        flows=[sub(mul(div(gap,N),n),mul(gap,k)) for n,k in zip(ns,kernel)]
        newgross=gap
    else:
        # Exact-boundary branch only for the scalar grid; physical rows must be strict.
        raise RuntimeError('undecided N-A sign; no tolerance used')
    debits=[mul(T,k) for k in kernel]
    equalcheck(avg(kernel),const(1));equalcheck(avg(credits),A);equalcheck(avg(debits),T)
    equalcheck(avg(flows),(0,0))
    for s,a,f,d in zip(ss,credits,flows,debits):equalcheck(sub(plus(plus(s,a),f),d),(0,0))
    return dict(credits=credits,booked=debits,flows=flows,kernel=kernel,N=N,P=P,newgross=newgross)

def main():
    start=time.perf_counter();profiles={}
    for m in range(6):
        t=tuple(-1 if x==0 else 1 for x in range(1<<m))
        profiles[m]=full(((-1,-1),t,G,G,G,G));compare(profiles[m])
    stop=full(((-1,-1),(1,),G,G,G,G));compare(stop)
    (ROOT/'out/SEVEN_PROFILES.json').write_text(json.dumps(dict(profiles={str(m):dict(S=p['S'],H=p['H'],I=str(p['I'])) for m,p in profiles.items()},stop=dict(S=stop['S'],H=stop['H'],I=str(stop['I']))),indent=2)+'\n',encoding='utf-8')
    chains=[]
    for initial in [4,5]:
        A=neg(profiles[initial]['S']);D=(0,0);labels=[];rows=[]
        for m in range(initial,0,-1):
            p=profiles[m];children=[profiles[m-1],stop]
            d=p['op']['q'][1]*F(1,1<<(m-1))
            ck(p['I']-(children[0]['I']+children[1]['I'])/2==d)
            e=sub(sub(p['H'],avg([c['H'] for c in children])),const(4*d));T=plus(D,e)
            equalcheck(T,plus(avg([c['S'] for c in children]),A))
            row=dict(m=m,A=A,D=D,e=e,T=T,physical_influence=str(d),children_S=[c['S'] for c in children])
            if T[1]<0:
                row['failure']='negative required total booked debit; nonnegative-net model cannot apply'
                rows.append(row);break
            ck(T[0]>0)
            sol=allocate(row['children_S'],A,T);row.update(sol)
            # Distinct original query labels travel under one explicit mean-one kernel.
            old_labels=[D] if not labels else labels
            outgoing=[[mul(L,k) for k in sol['kernel']] for L in old_labels+[e]]
            for L,pair in zip(old_labels+[e],outgoing):equalcheck(avg(pair),L)
            row['label_children']=outgoing
            A=sol['credits'][0];D=sol['booked'][0];labels=[pair[0] for pair in outgoing]
            equalcheck(plus(profiles[m-1]['S'],A),D)
            rows.append(row)
            (ROOT/'out/ADAPTIVE_PARTIAL.json').write_text(json.dumps(chains+[dict(initial=initial,rows=rows)],indent=2)+'\n',encoding='utf-8')
            ck(time.perf_counter()-start<55)
        chains.append(dict(initial=initial,rows=rows,complete=(len(rows)==initial and 'failure' not in rows[-1])))
    result=dict(version='A071-all-core1-inherited-credit-v1',profiles=7,chains=chains,
      independent_states=independent.cache_info().currsize,engine_checks=engine.tests,
      runtime_seconds=time.perf_counter()-start)
    (ROOT/'out/ADAPTIVE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(profiles=7,runtime=result['runtime_seconds'],chains=[dict(initial=c['initial'],complete=c['complete'],rows=[dict(m=r['m'],A=display(r['A']),D=display(r['D']),e=display(r['e']),T=display(r['T']),gross=display(r.get('newgross',(0,0))),failure=r.get('failure')) for r in c['rows']]) for c in chains])))

if __name__=='__main__':main()
