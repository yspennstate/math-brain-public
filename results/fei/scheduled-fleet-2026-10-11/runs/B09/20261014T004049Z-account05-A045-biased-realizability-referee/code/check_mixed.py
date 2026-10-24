from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time,sys
ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv; START=time.perf_counter();checks=0
def ck(b):
    global checks
    checks+=1
    assert b,checks
    if time.perf_counter()-START>(60 if PILOT else 180):raise RuntimeError('frozen time cap')
def prod(xs):
    a=Q(1)
    for x in xs:a*=x
    return a
def table(n,fn):return [fn([(x>>i)&1 for i in range(n)]) for x in range(1<<n)]
def transform(tab,ps):
    c=list(map(Q,tab));n=len(ps)
    for i,p in enumerate(ps):
        for s in range(1<<n):
            if s>>i&1:continue
            a,b=c[s],c[s|(1<<i)]
            c[s]=(1-p)*a+p*b;c[s|(1<<i)]=(b-a)/2
    v=[4*p*(1-p) for p in ps]
    P=[c[s]**2*prod(v[i] for i in range(n) if s>>i&1) for s in range(1<<n)]
    ck(sum(P)==1)
    return c,P,v
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def outward(a,N=24):
    k=10**N
    return Q(a[0].numerator*k//a[0].denominator,k),Q(-((-a[1].numerator*k)//a[1].denominator),k)
@lru_cache(None)
def core_ln(u):
    z=(u-1)/(u+1);zz=z*z;term=z;lo=Q(0);N=24
    for j in range(N):lo+=2*term/(2*j+1);term*=zz
    return lo,lo+2*term/((2*N+1)*(1-zz))
@lru_cache(None)
def ln(x):
    assert x>0
    u=x;k=0
    while u<1:u*=2;k-=1
    while u>=2:u/=2;k+=1
    return outward(plus(core_ln(u),scale(core_ln(Q(2)),k)))
def enc(iv):
    a=outward(iv,18)
    return {'lower':str(a[0]),'upper':str(a[1]),'diagnostic_midpoint':float((a[0]+a[1])/2)}
def form_plus(a,b,c=Q(1)):
    z=dict(a)
    for arg,w in b.items():z[arg]=z.get(arg,Q(0))+c*w
    return {arg:w for arg,w in z.items() if arg!=1 and w}
def corrected_form(ms,norms):
    z={}
    for a,v in zip(ms,norms):
        if a:z=form_plus(form_plus(z,{v:a}),{a:-a})
    return z
def eval_form(z):
    a=(Q(0),Q(0))
    for x,w in z.items():a=plus(a,scale(ln(x),w))
    return a
def psi(a):return (Q(0),Q(0)) if not a else scale(ln(1/(a*a)),a*a)
def cofactor(tab,r,b):return [tab[u|(b<<r)] for u in range(1<<r)]
def mix_data(sp,r,s):
    c,P,v=sp;n=r+s;mask=(1<<r)-1
    a=[Q(0)]*(1<<r);b=[Q(0)]*(1<<s);M=Q(0);Dm=Q(0)
    DA=DB=Q(0);D=Q(0)
    vA=[prod(v[i] for i in range(r) if u>>i&1) for u in range(1<<r)]
    vB=[prod(v[r+j] for j in range(s) if t>>j&1) for t in range(1<<s)]
    mixed=[]
    for k,p in enumerate(P):
        u=k&mask;t=k>>r;du=u.bit_count();dt=t.bit_count()
        if k:D+=(du+dt-1)*p
        if u:DA+=(du-1)*p
        if t:DB+=(dt-1)*p
        if u and t:
            mixed.append((k,u,t,p));a[u]+=p;b[t]+=p;M+=p;Dm+=(du+dt-1)*p
    ck(D==DA+DB+M)
    if not M:return {'M':M,'D':D,'DA':DA,'DB':DB,'mixed':mixed,'vA':vA,'vB':vB,'Dm':Dm}
    qa=[x/M for x in a];qb=[x/M for x in b]
    ck(sum(qa)==sum(qb)==1);ck(Dm>=M)
    Qprod={k:qa[u]*qb[t] for k,u,t,p in mixed}
    ck(sum(Qprod.values())==1) # retain zero actual atoms in reference support
    Qdeg={k:(u.bit_count()+t.bit_count()-1)*qa[u]*qb[t]*M/Dm for k,u,t,p in mixed}
    ck(sum(Qdeg.values())==1)
    tc={};kd={};E={};Al=corrected_form(a,vA);Bl=corrected_form(b,vB)
    for k,u,t,p in mixed:
        if not p:continue
        E=form_plus(E,{vA[u]:p});E=form_plus(E,{vB[t]:p});E=form_plus(E,{p:-p})
        # Expand TC into the same primitive log arguments for exact cancellation.
        primitive=form_plus(form_plus(form_plus({p:Q(1)},{M:Q(1)}),{a[u]:Q(-1)}),{b[t]:Q(-1)})
        tc=form_plus(tc,primitive,p/M)
        kd=form_plus(kd,primitive,(u.bit_count()+t.bit_count()-1)*p/Dm)
        ck(Qprod[k]>0 and Qdeg[k]>0)
    RHS=form_plus(form_plus(form_plus(Al,Bl),{M:M}),tc,-M)
    ck(E==RHS)
    # Different normalized joint distributions have different KL averages.
    tciv=eval_form(tc);kdiv=eval_form(kd)
    ck(tciv[1]>=0 and kdiv[1]>=0)
    # Exact average degree under Qprod has the actual mixed deficit normalizer.
    Z=sum((u.bit_count()+t.bit_count()-1)*Qprod[k] for k,u,t,p in mixed)
    ck(Z==Dm/M)
    return {'M':M,'D':D,'DA':DA,'DB':DB,'mixed':mixed,'vA':vA,'vB':vB,'Dm':Dm,'a':a,'b':b,'qa':qa,'qb':qb,'Qprod':Qprod,'Qdeg':Qdeg,'E':E,'tc':tc,'kd':kd,'tciv':tciv,'kdiv':kdiv}

# Catalogs are computed from every actual truth table at the actual group bias.
biases=[Q(1,4),Q(1,2),Q(3,4)]
catalog={};catalog_cases=0
for n in [1,2,3]:
    for p in biases:
        laws={}
        for tid in range(1<<(1<<n)):
            tab=[1 if tid>>x&1 else -1 for x in range(1<<n)]
            law=tuple(transform(tab,[p]*n)[1]);laws.setdefault(law,tid);catalog_cases+=1
        catalog[n,p]=laws

scalar=0
for a,b,pi in itertools.product([Q(-1),Q(-3,4),Q(-1,4),Q(0),Q(1,4),Q(3,4),Q(1)],[Q(-1),Q(-3,4),Q(-1,4),Q(0),Q(1,4),Q(3,4),Q(1)],[Q(1,4),Q(1,2),Q(3,4)]):
    avg=pi*a+(1-pi)*b;variance=pi*a*a+(1-pi)*b*b-avg*avg
    left=psi(avg);right=plus(plus(scale(psi(a),pi),scale(psi(b),1-pi)),(3*variance,3*variance))
    if not variance:ck(a==b)
    else:ck(left[1]<=right[0])
    scalar+=1

rows=[];nonadmitted=0;all_mixed=0;one_example=None;degree_difference=None;physical_jensen=0
rs=[(1,1),(2,2)] if PILOT else [(r,s) for r in [1,2,3] for s in [1,2,3] if r+s<=5]
ws=[2] if PILOT else [2,3]
outrows=ROOT/'out'/('PILOT_CASES.jsonl' if PILOT else 'CASES.jsonl')
with outrows.open('w',encoding='utf-8') as f:
    for r,s,w in itertools.product([0],[0],[0]):pass # loop body below uses frozen group pairs
    for r,s in rs:
        for w in ws:
            for p,q in itertools.product(biases,repeat=2):
                ps=[p]*r+[q]*s
                for threshold in range(w*r+s+2):
                    tab=table(r+s,lambda x:1 if w*sum(x[:r])+sum(x[r:])>=threshold else -1)
                    sp=transform(tab,ps);md=mix_data(sp,r,s)
                    row={'r':r,'s':s,'w':w,'t':threshold,'pA':str(p),'pB':str(q),'M':str(md['M']),'Delta':str(md['D']),'Delta_mixed':str(md['Dm'])}
                    # Coherent amplitude Jensen on each pure-group higher-degree coefficient.
                    pure=(Q(0),Q(0));bound=(Q(0),Q(0))
                    for group in [0,1]:
                        ng=r if group==0 else s;outside=s if group==0 else r
                        bg=[p]*r if group==0 else [q]*s;bo=[q]*s if group==0 else [p]*r
                        pieces=[]
                        for y in range(1<<outside):
                            weight=prod(bo[j] if y>>j&1 else 1-bo[j] for j in range(outside))
                            ch=cofactor(tab,r,y) if group==0 else [tab[y|(t<<r)] for t in range(1<<s)]
                            cp=transform(ch,bg);pieces.append((weight,cp))
                        for U in range(1<<ng):
                            if U.bit_count()<2:continue
                            norm=prod(4*bg[i]*(1-bg[i]) for i in range(ng) if U>>i&1)
                            cc=[cp[0][U] for weight,cp in pieces]
                            weights=[weight for weight,cp in pieces]
                            ck(all(abs(c)<=1 for c in cc))
                            mean=sum(a*b for a,b in zip(weights,cc));variance=sum(a*b*b for a,b in zip(weights,cc))-mean*mean
                            joint_index=U if group==0 else U<<r
                            ck(sp[0][joint_index]==mean)
                            pure=plus(pure,scale(psi(mean),norm))
                            rhs=(Q(0),Q(0))
                            for a,b in zip(weights,cc):rhs=plus(rhs,scale(psi(b),norm*a))
                            rhs=plus(rhs,(3*norm*variance,3*norm*variance));bound=plus(bound,rhs)
                            if variance:ck(scale(psi(mean),norm)[1]<=rhs[0])
                            else:ck(all(b==mean for a,b in zip(weights,cc) if a))
                            physical_jensen+=1
                    # Baseline consequent; not finite extrapolation to the general theorem.
                    constant=plus((Q(460),Q(460)),scale(ln(Q(2)),80))
                    paid=plus(scale(constant,md['DA']+md['DB']),(6*md['M'],6*md['M']))
                    if md['D']:ck(pure[1]<=paid[0])
                    else:ck(pure==(Q(0),Q(0)))
                    if md['M']:
                        all_mixed+=1
                        admittedA=tuple(md['qa']) in catalog[r,p];admittedB=tuple(md['qb']) in catalog[s,q]
                        row.update(marginal_A_Boolean=admittedA,marginal_B_Boolean=admittedB,TC_spec=enc(md['tciv']),degree_KL=enc(md['kdiv']))
                        if not(admittedA and admittedB):
                            nonadmitted+=1
                            if one_example is None:one_example=dict(row,qa=[str(a) for a in md['qa']],qb=[str(a) for a in md['qb']])
                        dif=minus(md['kdiv'],md['tciv'])
                        if degree_difference is None and (dif[0]>0 or dif[1]<0):degree_difference=dict(row,difference=enc(dif),P=[str(a) for a in sp[1]])
                    else:row['conditioning']='SKIPPED_M_ZERO'
                    f.write(json.dumps(row)+'\n');f.flush();rows.append(row)
                    (ROOT/'out'/('PILOT_CHECKPOINT.json' if PILOT else 'CHECKPOINT.json')).write_text(json.dumps({'cases':len(rows),'assertions':checks}),encoding='utf-8')

occupation=0
for sizes in [(2,2,2),(1,2,3)]:
    offsets=[sum(sizes[:j]) for j in range(3)]
    for mask in range(1,64):
        counts=[((mask>>o)&((1<<s)-1)).bit_count() for s,o in zip(sizes,offsets)]
        active=sum(a>0 for a in counts)
        ck(mask.bit_count()-1==sum(a-1 for a in counts if a)+(active-1))
        if active>=2:ck(3*sum(a>=2 for a in counts)<=6*(active-1))
        occupation+=1

# Explicit actual AND4: reference is uniform on 9 mixed sets, not Boolean.
andtab=table(4,lambda x:1 if all(x) else -1)
andsp=transform(andtab,[Q(1,2)]*4);am=mix_data(andsp,2,2)
ck(am['qa']==[Q(0),Q(1,3),Q(1,3),Q(1,3)])
ck(tuple(am['qa']) not in catalog[2,Q(1,2)])
ck(set(am['Qprod'].values())=={Q(1,9)})
ck(all((x*Q(256)).denominator!=1 for x in am['Qprod'].values()))

# Coupled signs realize a joint product law although both marginals are non-Boolean.
phase=table(4,lambda x:(2*x[0]-1)*(2*x[2]-1)*(-1 if x[1]*x[3] else 1))
phase_sp=transform(phase,[Q(1,2)]*4);pm=mix_data(phase_sp,2,2)
ck(pm['M']==1);ck(pm['qa']==[Q(0),Q(1,2),Q(0),Q(1,2)])
ck(tuple(pm['qa']) not in catalog[2,Q(1,2)])
ck(all(phase_sp[1][k]==a for k,a in pm['Qprod'].items()))
ck(all(pm['M']*p==pm['a'][u]*pm['b'][t] for k,u,t,p in pm['mixed']))
# Signed coefficient matrix has a nonzero 2x2 determinant, so signs are not separable.
sub=[phase_sp[0][u|(t<<2)] for u,t in [(1,1),(1,3),(3,1),(3,3)]]
ck(sub[0]*sub[3]-sub[1]*sub[2]!=0)

conjunction=[]
for m in [1,2,3,4]:
    P=Q(4)**(1-2*m);M=(2**m-1)**2*P
    Dm=2*m*2**(m-1)*(2**m-1)*P-M
    ck(Dm/M==Q(2*m*2**(m-1),2**m-1)-1)
    conjunction.append({'m':m,'M':str(M),'Delta_mixed':str(Dm),'E_mixed_over_M':'2(2m-1)ln2'})

# Polynomial endpoint extension is compared to the properly contracted actual cube.
endpoint_cases=0
for i,b,t in itertools.product([0,2],[0,1],[3,5]):
    tab=table(4,lambda x:1 if 2*(x[0]+x[1])+x[2]+x[3]>=t else -1)
    ps=[Q(1,4),Q(1,2),Q(3,4),Q(1,2)];ps[i]=Q(b)
    extended=transform(tab,ps)[1];other=[j for j in range(4) if j!=i]
    contracted=[tab[(b<<i)+sum(((x>>k)&1)<<j for k,j in enumerate(other))] for x in range(8)]
    actual=transform(contracted,[ps[j] for j in other])[1]
    for U,pv in enumerate(actual):
        mask=sum(((U>>k)&1)<<j for k,j in enumerate(other))
        ck(extended[mask]==pv);ck(extended[mask|(1<<i)]==0)
    endpoint_cases+=1

out={'status':'PASS','pilot':PILOT,'assertions':checks,'threshold_cases':len(rows),'catalog_truth_tables':catalog_cases,'catalog_distinct_laws':[{'n':n,'p':str(p),'laws':len(v)} for (n,p),v in catalog.items()],'nonzero_mixed_cases':all_mixed,'cases_with_not_both_marginals_Boolean':nonadmitted,'scalar_cases':scalar,'physical_coefficient_Jensen_checks':physical_jensen,'occupation_patterns':occupation,'endpoint_cases':endpoint_cases,'first_nonadmitted_example':one_example,'different_degree_KL_example':degree_difference,'AND4_reference':{'marginals':['0','1/3','1/3','1/3'],'reference_mass_per_mixed_set':'1/9','Boolean_realizable_joint':'NO_DYADIC_MASS_OBSTRUCTION'},'coupled_phase_reference':{'truth_table':phase,'marginals':['0','1/2','0','1/2'],'joint_Boolean_realizable':True,'separable_Boolean_phase_possible':False,'coefficient_submatrix':[str(x) for x in sub]},'conjunction_checks':conjunction,'runtime_seconds':time.perf_counter()-START}
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK_OUTPUT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','pilot','assertions','threshold_cases','catalog_truth_tables','nonzero_mixed_cases','cases_with_not_both_marginals_Boolean','physical_coefficient_Jensen_checks','runtime_seconds','first_nonadmitted_example','different_degree_KL_example']},indent=2))
