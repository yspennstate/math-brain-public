"""Symbolic component cancellation and mandatory donor audit, A072 v1."""
from continue_spent import *
from collections import Counter
from itertools import product

checks=0
def test(p):
    global checks
    assert p
    checks+=1

def add(*terms):
    out={}
    for p in terms:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def times(p,r):return {k:v*r for k,v in p.items() if v*r}
def minus(p,q):return add(p,times(q,F(-1)))
def mean(ps):return times(add(*ps),F(1,len(ps)))
def entp(masses):
    out={}
    for z in masses:
        if z and z!=1:out[z]=out.get(z,F(0))-z
    return out

def evalp(p):
    out=(0,0)
    for k,v in p.items():out=plus(out,signed((Q,Q) if k is None else log2(k),v))
    return out

@lru_cache(None)
def corep(t):
    # Independent integer character sums, followed by integer inverse and edge counts.
    N=len(t);n=(N-1).bit_length()
    w=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(N)]
    test(sum(z*z for z in w)==N*N)
    for x,y in enumerate(t):test(sum(z*(-1 if (s&x).bit_count()%2 else 1) for s,z in enumerate(w))==N*y)
    ds=[]
    for i in range(n):
        edges=sum(t[x]!=t[x|(1<<i)] for x in range(N) if not x>>i&1)
        di=F(edges,N//2);test(di==sum(F(w[s]*w[s],N*N) for s in range(N) if s>>i&1));ds.append(di)
    h=entp([F(z*z,N*N) for z in w]);slack=add({None:4*sum(ds)},times(h,F(-1)))
    test(evalp(slack)[0]>=0)
    return h,slack,ds

def symbolic(p,j):
    hcs=[corep(t)[0] for t in p['ts']];scs=[corep(t)[1] for t in p['ts']]
    qs=p['op']['q'];vs=[4*c['p']*(1-c['p']) for c in p['cs']]
    C=add(entp(p['op']['masses']),* [times(entp([v,1-v]),-q) for v,q in zip(vs,qs)])
    Hfull=add(C,*[times(h,q) for h,q in zip(hcs,qs)])
    U=times(scs[j],qs[j]);A=add(*[times(scs[k],qs[k]) for k in range(6) if k!=j])
    M=minus(A,C);S=add(U,M)
    test(S==add({None:4*p['I']},times(Hfull,F(-1))))
    overlaps(evalp(C),p['op']['C']);overlaps(evalp(S),p['S'])
    mi=evalp(M)
    test(mi[0]>0 or mi[1]<0 or not M)
    W=M if mi[0]>0 else {};V=minus(S,W)
    test(evalp(V)[0]>=0)
    return dict(C=C,H=Hfull,U=U,A=A,M=M,S=S,W=W,V=V)

def pack(p):return {('constant' if k is None else str(k)):str(v) for k,v in p.items()}

def allocation_boundaries():
    count=0
    for v0,v1,w0,w1 in product(range(3),repeat=4):
        V=[F(v0),F(v1)];W=[F(w0),F(w1)];S=[V[c]+W[c] for c in range(2)]
        bv=sum(V)/2;bw=sum(W)/2
        for k in range(int(sum(S))+1):
            T=F(k,2)
            if T<=bv:d=[T*x/bv if bv else F(0) for x in V]
            else:d=[V[c]+(T-bv)*W[c]/bw for c in range(2)]
            test(sum(d)/2==T and all(0<=d[c]<=S[c] for c in range(2)))
            donor=sum(max(d[c]-V[c],F(0)) for c in range(2))/2
            test(donor==max(F(0),T-bv))
            # Independent vertex minimization of the piecewise linear cost.
            xs=[F(0),2*T,S[0],2*T-S[1],V[0],2*T-V[1]]
            feasible=[x for x in xs if 0<=x<=S[0] and 0<=2*T-x<=S[1]]
            test(bool(feasible))
            best=min((max(x-V[0],F(0))+max(2*T-x-V[1],F(0)))/2 for x in feasible)
            test(best==donor)
            if T:
                old=[(T+1)*x/T for x in d];new=[-x/T for x in d]
                test(sum(old)/2==T+1 and sum(new)/2==-1)
                test(all(old[c]+new[c]==d[c] for c in range(2)))
            if T==sum(S)/2:test(d==S)
            count+=1
    test(count==405)
    return count

def main():
    start=time.perf_counter();boundary_cases=allocation_boundaries();root,first,second,third,debits,D,e1,e2,e3=setup()
    pilot='--pilot' in sys.argv
    choices=[(b,j,i) for b in range(2) for j in range(1,6) for i in range(6)]
    if pilot:choices=choices[:2]
    records=[];failure=Counter();positive_W=Counter();saturated_subsidies=[]
    for b,j,i in choices:
        p=third[b];cs,e,d=split(p,j,i)
        par=symbolic(p,j);leaves=[symbolic(c,j) for c in cs]
        ep=add(par['H'],times(mean([z['H'] for z in leaves]),F(-1)),{None:-4*d})
        avgS=mean([z['S'] for z in leaves]);avgV=mean([z['V'] for z in leaves]);avgW=mean([z['W'] for z in leaves])
        test(avgS==add(par['S'],ep))
        test(avgV==minus(avgS,avgW))
        # Other core banks average exactly: ONLY the newly queried core changes.
        test(par['A']==mean([z['A'] for z in leaves]))
        test(minus(ep,minus(mean([z['U'] for z in leaves]),par['U']))==minus(par['C'],mean([z['C'] for z in leaves])))
        overlaps(evalp(ep),e)
        T=plus(debits[b],e);R=sub(p['S'],debits[b]);shortfall=sub(T,evalp(avgV))
        rhs=sub(evalp(avgW),R);overlaps(shortfall,rhs)
        test(shortfall[0]>0 or shortfall[1]<0)
        if shortfall[0]>0:failure[b]+=1
        if evalp(avgW)[0]>0:positive_W[b]+=1
        for z in leaves:test(evalp(z['S'])[0]>0)
        if b==0:
            # D=S_parent by inherited booking, so donor expenditure is forced.
            exact_shortfall=minus(add(par['S'],ep),avgV)
            test(exact_shortfall==avgW)
            test(evalp(avgW)[0]>0)
            saturated_subsidies.append(evalp(avgW))
            allocation=[evalp(z['S']) for z in leaves]
            donor=[evalp(z['W']) for z in leaves]
            rule='saturated: all child capacity forced'
        elif shortfall[0]>0:
            # Optimal donor use: first use V, then the necessary fraction of W.
            theta=div(shortfall,evalp(avgW));test(0<theta[0]<=theta[1]<Q)
            donor=[mul(theta,evalp(z['W'])) for z in leaves]
            allocation=[plus(evalp(z['V']),x) for z,x in zip(leaves,donor)]
            rule='V plus theta W'
        else:
            theta=div(T,evalp(avgV));test(0<theta[0]<=theta[1]<Q)
            allocation=[mul(theta,evalp(z['V'])) for z in leaves]
            donor=[(0,0),(0,0)]
            rule='theta V; zero donor'
        overlaps(avg(allocation),T)
        target_donor=(0,0) if shortfall[1]<0 else (evalp(avgW) if b==0 else shortfall)
        overlaps(avg(donor),target_donor)
        if b==1:
            for z,a in zip(leaves,allocation):test(sub(evalp(z['S']),a)[0]>0)
        # Preserve every old label and the signed newly booked excess by the
        # same factors; this is an interval diagnostic of the exact formulas.
        old=[mul(div(debits[b],T),a) for a in allocation]
        new=[mul(div(e,T),a) for a in allocation] if e[0]>0 else None
        overlaps(avg(old),debits[b])
        if new is not None:overlaps(avg(new),e)
        records.append(dict(terminal=b,block=j,coordinate=i,physical_influence=str(d),
            incoming_debit=debits[b],query_excess=evalp(ep),unused_parent=R,
            selected_shortfall=shortfall,mandatory_mean_other_subsidy=evalp(avgW),
            child_V=[evalp(z['V']) for z in leaves],child_W=[evalp(z['W']) for z in leaves],
            child_full_S=[evalp(z['S']) for z in leaves],
            optimal_rule=rule,optimal_child_debits=allocation,optimal_child_donors=donor,
            exact_profiles=dict(mean_W=pack(avgW),e=pack(ep),parent_S=pack(par['S']),mean_V=pack(avgV))))
        (ROOT/'out'/('COMPONENT_PILOT_CASES.json' if pilot else 'COMPONENT_CASES.json')).write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
        test(time.perf_counter()-start<55)
    if not pilot:test(len(records)==60 and failure=={0:30,1:6})
    result=dict(version='A072-component-shortfall-v1',cases=len(records),exact_assertions=checks,
        inherited_engine_assertions=engine.tests,independent_core_tables=corep.cache_info().currsize,boundary_allocation_cases=boundary_cases,
        selected_only_failures=dict(failure),positive_other_mean_cases=dict(positive_W),
        saturated_subsidy_range=[min(z[0] for z in saturated_subsidies),max(z[1] for z in saturated_subsidies)],
        scale_bits=192,runtime_seconds=time.perf_counter()-start,full_fei='OPEN',
        rung='exact finite certificate plus symbolic accounting proof; independent review pending')
    (ROOT/'out'/('COMPONENT_PILOT.json' if pilot else 'COMPONENT_VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':main()
