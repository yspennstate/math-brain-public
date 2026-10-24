from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from math import comb
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); ASSERTIONS=0
PILOT='--pilot' in sys.argv
LIMIT=60 if PILOT else 180
def check(b):
    global ASSERTIONS
    ASSERTIONS+=1
    assert b,ASSERTIONS
    if time.perf_counter()-START>LIMIT: raise RuntimeError('frozen runtime cap reached')
def product(xs):
    z=Q(1)
    for x in xs:z*=x
    return z
def spectrum(table,ps):
    cs=list(map(Q,table)); n=len(ps)
    for i,p in enumerate(ps):
        for s in range(1<<n):
            if s>>i&1: continue
            a,b=cs[s],cs[s|(1<<i)]
            cs[s]=(1-p)*a+p*b; cs[s|(1<<i)]=(b-a)/2
    vs=[4*p*(1-p) for p in ps]
    masses=[cs[s]**2*product(vs[i] for i in range(n) if s>>i&1) for s in range(1<<n)]
    check(sum(masses)==1)
    return cs,masses,vs
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def divide(a,b):
    assert b[0]>0
    corners=[x/y for x in a for y in b]
    return min(corners),max(corners)
def outward(iv,digits=24):
    unit=10**digits
    lo=(iv[0].numerator*unit)//iv[0].denominator
    hi=-((-iv[1].numerator*unit)//iv[1].denominator)
    return Q(lo,unit),Q(hi,unit)
@lru_cache(None)
def reduced_ln(u):
    z=(u-1)/(u+1); zz=z*z; t=z; lo=Q(0); N=32
    for k in range(N):
        lo+=2*t/(2*k+1);t*=zz
    err=2*t/((2*N+1)*(1-zz))
    return lo,lo+err
@lru_cache(None)
def ln(x):
    assert x>0
    k=0;u=x
    while u<1:u*=2;k-=1
    while u>=2:u/=2;k+=1
    return add(reduced_ln(u),scale(reduced_ln(Q(2)),k))
@lru_cache(None)
def log2(x):return outward(divide(ln(x),ln(Q(2))))
def entropy(ms):
    z=(Q(0),Q(0))
    for a in ms:
        if a:z=add(z,scale(log2(1/a),a))
    return z
def h(p):return entropy([p,1-p])
def stats(sp):
    cs,ms,vs=sp;hp=(Q(0),Q(0));I=Q(0);V=Q(0)
    for s,a in enumerate(ms):
        if not s:continue
        I+=s.bit_count()*a;V+=a
        if a:hp=add(hp,scale(log2(product(vs[i] for i in range(len(vs)) if s>>i&1)/a),a))
    return hp,I,V
def tab(n,fn):return [fn([(x>>i)&1 for i in range(n)]) for x in range(1<<n)]
def pack(iv):
    iv=outward(iv,18)
    return {'lower':str(iv[0]),'upper':str(iv[1]),'diagnostic_midpoint':float((iv[0]+iv[1])/2)}
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def form_add(a,b,c=Q(1)):
    z=dict(a)
    for arg,coef in b.items():z[arg]=z.get(arg,Q(0))+c*coef
    return {arg:coef for arg,coef in z.items() if coef and arg!=1}
def entropy_form(ms):
    z={}
    for a in ms:
        if a:z[a]=z.get(a,Q(0))-a
    return {arg:coef for arg,coef in z.items() if coef and arg!=1}
def hp_form(sp):
    _,ms,vs=sp;z={}
    for s,a in enumerate(ms):
        if not s or not a:continue
        z=form_add(z,{a:-a})
        for i,v in enumerate(vs):
            if s>>i&1:z=form_add(z,{v:a})
    return z
def encode_case(kind,n,ps,tax,sp,query_coeff,detail):
    hp,I,V=stats(sp);D=I-V;check(D>=0)
    out={'kind':kind,'n':n,'detail':detail,'biases':[str(p) for p in ps],'I':str(I),'Var':str(V),'D':str(D),'raw_tax':pack(tax),'stopped_tax':pack(query_coeff),'Hplus':pack(hp)}
    if D:
        out.update(raw_ratio=pack(scale(tax,1/D)),stopped_ratio=pack(scale(query_coeff,1/D)),corrected_ratio=pack(scale(hp,1/D)))
    else:
        out.update(raw_ratio='UNDEFINED_D_ZERO',stopped_ratio='UNDEFINED_D_ZERO',corrected_ratio='UNDEFINED_D_ZERO')
    return out
@lru_cache(None)
def queries(n,t,p):
    # Stop once a constant/literal leaf has corrected entropy and deficit zero.
    if t<=0 or t>n or n<=1:return Q(0)
    return 1+(1-p)*queries(n-1,t,p)+p*queries(n-1,t-1,p)
def independent_ck(n,t,p,sp):
    cs,ms,vs=sp
    # Mixed-difference computation from actual threshold cofactor values.
    for k in range(n+1):
        c=Q(0)
        for j in range(n-k+1):
            w=comb(n-k,j)*p**j*(1-p)**(n-k-j)
            delta=sum((-1)**(k-r)*comb(k,r)*(1 if j+r>=t else -1) for r in range(k+1))
            c+=w*delta/Q(2)**k
        for s in range(1<<n):
            if s.bit_count()==k:check(cs[s]==c)
def node_ledger(table,ps,i):
    n=len(ps);other=[j for j in range(n) if j!=i];pp=ps[i]
    children=[]
    for b in [0,1]:
        children.append([table[sum(((x>>k)&1)<<j for k,j in enumerate(other))+(b<<i)] for x in range(1<<(n-1))])
    sp=spectrum(table,ps); sg,sh=[spectrum(x,[ps[j] for j in other]) for x in children]
    cg,pg,vg=sg;ch,ph,vh=sh
    q=[(1-pp)*x+pp*y for x,y in zip(pg,ph)]
    for t in range(len(q)):
        s=sum(((t>>k)&1)<<j for k,j in enumerate(other))
        check(sp[1][s]+sp[1][s|(1<<i)]==q[t])
    M=sub(entropy(sp[1]),entropy(q))
    J=sub(entropy(q),add(scale(entropy(pg),1-pp),scale(entropy(ph),pp)))
    hp,I,V=stats(sp);hg,Ig,Vg=stats(sg);hh,Ih,Vh=stats(sh)
    D=I-V;childD=(1-pp)*(Ig-Vg)+pp*(Ih-Vh)
    influence=sum(a for s,a in enumerate(sp[1]) if s>>i&1)
    singleton=sp[1][1<<i]
    check(D-childD==influence-singleton)
    # Formal term table cancels exactly: ordinary H decomposition plus normalization.
    # The interval certificate below is a regression check; analytic chain rules prove equality.
    h0drop=sub(entropy([sp[1][0]]),add(scale(entropy([pg[0]]),1-pp),scale(entropy([ph[0]]),pp)))
    rhs=sub(add(add(M,J),scale(log2(4*pp*(1-pp)),influence)),h0drop)
    lhs=sub(hp,add(scale(hg,1-pp),scale(hh,pp)))
    check(overlap(lhs,rhs))
    formalL=form_add(form_add(hp_form(sp),hp_form(sg),-(1-pp)),hp_form(sh),-pp)
    ordinary=form_add(form_add(entropy_form(sp[1]),entropy_form(pg),-(1-pp)),entropy_form(ph),-pp)
    empty=form_add(form_add(entropy_form([sp[1][0]]),entropy_form([pg[0]]),-(1-pp)),entropy_form([ph[0]]),-pp)
    formalR=form_add(form_add(ordinary,{4*pp*(1-pp):influence}),empty,-1)
    check(formalL==formalR)
    return M,J,sub(J,M),rhs,lhs,influence,singleton

ms=[5,6] if PILOT else [5,6,8,10,14]
grid=[]
for m in ms:
    p=1-(1-Q(1,2**m))**2;t=Q(1,2**(m+1))
    tax=sub(h(p),scale(h(t),2));check(tax[0]>0)
    grid.append((str(m),p,tax))
grid.append(('fair',Q(1,2),(Q(0),Q(0))))
rows=[];ledgers=[];boundaries=[]
for label,p,tax in grid:
    for n in range(1,4 if PILOT else 7):
        for t in range(1,n+1):
            table=tab(n,lambda x:1 if sum(x)>=t else -1)
            sp=spectrum(table,[p]*n)
            if n<=4:independent_ck(n,t,p,sp)
            coeff=queries(n,t,p)
            row=encode_case('threshold',n,[p]*n,scale(tax,n),sp,scale(tax,coeff),{'threshold':t,'m':label,'expected_nonaffine_queries':str(coeff)})
            rows.append(row)
            if n<=3:
                M,J,corr,rhs,lhs,inf,sg=node_ledger(table,[p]*n,0)
                ledgers.append({'n':n,'t':t,'m':label,'M':pack(M),'J':pack(J),'J_minus_M':pack(corr),'corrected_decrement':pack(lhs),'spectral_influence':str(inf),'singleton_mass':str(sg),'D_decrement':str(inf-sg)})
    scenarios=[(p,p,tax,tax)]
    if label!='fair':scenarios.extend([(Q(1,2),p,(Q(0),Q(0)),tax),(p,Q(1,2),tax,(Q(0),Q(0)))])
    for a in [1,2]:
        n=a+2**a
        for r,s,tr,ts in scenarios:
            table=tab(n,lambda x:2*x[a+sum(x[i]<<i for i in range(a))]-1)
            ps=[r]*a+[s]*(2**a);sp=spectrum(table,ps)
            raw=add(scale(tr,a),scale(ts,2**a));stopped=scale(tr,a)
            row=encode_case('address',n,ps,raw,sp,stopped,{'a':a,'m':label,'selector_bias':str(r),'data_bias':str(s),'policy':'addresses first, then stop at literal'})
            check(stats(sp)[1]-stats(sp)[2]==8*a*r*(1-r)*s*(1-s))
            if r==Q(1,2):
                hp,I,V=stats(sp);check(overlap(hp,(4*(I-V),4*(I-V))));check(stopped==(Q(0),Q(0)))
            rows.append(row)
    if label!='fair':
        table=tab(2,lambda x:1 if all(x) else -1);sp=spectrum(table,[p,p]);hp,I,V=stats(sp);D=I-V
        M,J,corr,rhs,lhs,inf,sg=node_ledger(table,[p,p],0)
        check(D==4*p*p*(1-p)**2)
        R=add((Q(2),Q(2)),scale(log2(1/p),4*p/(1-p)))
        check(overlap(scale(hp,1/D),R))
        check(corr[0]>0)
        normalized=divide(scale(corr,1/D),log2(1/p))
        boundaries.append({'m':label,'p':str(p),'D':str(D),'raw_tax_over_D':pack(scale(tax,2/D)),'best_stopped_tax_over_D':pack(scale(tax,1/D)),'actual_J_minus_M_over_D':pack(scale(corr,1/D)),'actual_over_D_log':pack(normalized),'Hplus_over_D':pack(R),'full_normalization_identity':'PASS_INTERVAL_REGRESSION_WITH_ANALYTIC_PROOF'})
    # Persist results after each frozen bias instead of relying on end-of-run output.
    (ROOT/'out'/('PILOT_CHECKPOINT.json' if PILOT else 'CHECKPOINT.json')).write_text(json.dumps({'last_bias':label,'cases_completed':len(rows),'assertions':ASSERTIONS}),encoding='utf-8')

trends=[]
for n in range(2,4 if PILOT else 7):
    rr=[r for r in rows if r['n']==n and r['kind']=='threshold' and r['D']!='0']
    w=max(rr,key=lambda x:Q(x['raw_ratio']['lower']))
    tied=[r for r in rr if r['D']==w['D'] and r['biases']==w['biases']]
    cert=all(Q(w['raw_ratio']['lower'])>Q(r['raw_ratio']['upper']) for r in rr if r not in tied)
    check(cert)
    trends.append({'n':n,'finite_grid_worst_thresholds':[r['detail'] for r in tied],'ratio':w['raw_ratio'],'max_certified_by_exact_ties_and_disjoint_intervals':True})
out={'status':'PASS','helper_version':'A045-tax-deficit-audit-v2.1','pilot':PILOT,'assertions':ASSERTIONS,'threshold_cases':sum(r['kind']=='threshold' for r in rows),'address_cases':sum(r['kind']=='address' for r in rows),'total_cases':len(rows),'boundary_cases':boundaries,'worst_threshold_ratios_by_arity':trends,'cases':rows,'normalization_ledgers':ledgers,'runtime_seconds':time.perf_counter()-START,'ln_cache':str(ln.cache_info())}
name='PILOT.json' if PILOT else 'CHECK_OUTPUT.json'
(ROOT/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','pilot','assertions','threshold_cases','address_cases','runtime_seconds','boundary_cases','worst_threshold_ratios_by_arity']},indent=2))
