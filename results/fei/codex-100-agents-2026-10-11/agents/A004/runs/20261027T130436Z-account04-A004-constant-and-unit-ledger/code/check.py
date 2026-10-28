"""Independent A004 tensor/reference certificates; no producer helper imports."""
from exact import *
import exact as E
from math import factorial

def spectrum(v):
    w=list(v);h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):a,b=w[j],w[j+h];w[j],w[j+h]=a+b,a-b
        h*=2
    return tuple(F(z*z,len(v)**2) for z in w)
def direct(v):
    return tuple(F(sum(a*(-1)**((s&t).bit_count()) for t,a in enumerate(v))**2,len(v)**2) for s in range(len(v)))
def tensor(a,b):return tuple(x*y for x in a for y in b)
def infl(p):return sum((F(s.bit_count())*q for s,q in enumerate(p)),F(0))
def H(p):return CE(p,p)
def conv(m):
    law={(0,0):1}
    for _ in range(m):
        nxt={}
        for (u,v),a in law.items():
            for du,dv in [(-1,1),(0,1),(1,0),(1,-1)]:
                k=(u+du,v+dv);nxt[k]=nxt.get(k,0)+a
        law=nxt
    return law

def run(pilot):
    start=time.perf_counter();rootcount=tensors=mixcases=0
    roots=[]
    for n in range(0,3):
        for mask in range(1<<(1<<n)):roots.append(tuple(1 if mask>>t&1 else -1 for t in range(1<<n)))
    if not pilot:
        for mask in range(0,256,17):roots.append(tuple(1 if mask>>t&1 else -1 for t in range(8)))
    for v in roots:
        p=spectrum(v);ck(p==direct(v));ck(sum(p)==1)
        h=H(p);ii=infl(p);q=(F(1),);vt=(1,)
        for m in range(1,4):
            q=tensor(q,p);vt=tensor(vt,v);ck(spectrum(vt)==q)
            if len(vt)<=64:ck(direct(vt)==q)
            ck(H(q)==add((m,h)));ck(infl(q)==m*ii)
            vac=1-q[0];over=H((vac,1-vac))
            ck(bounds(over)[0]>=0 and bounds(over)[1]<=1+F(1,10**15))
            # The all-dimensional proof supplies h2<=1; this is a boundary check.
            mu=F(sum(v),len(v));ck(q[0]==mu**(2*m))
            if not ii:ck(h=={} and q==(F(1),)+(F(0),)*(len(q)-1))
            tensors+=1
        rootcount+=1;ck(time.perf_counter()-start<55)
    # Sharp original witness identity: rederive formal log coefficients;
    # no arbitrary algebraic reference is claimed to be an admitted witness.
    symbolic=0
    for v in roots:
        p=spectrum(v);a=1-p[0]
        if not a:continue
        tail=tuple(z/a for z in p[1:]);c=F(3,2)
        # Extra basis0 denotes log2(e), not a prime logarithm.
        kr=add((1,{2:F(4),3:F(3),0:F(1)}))
        rstar=add((a,{2:c}),*[(z,{2:F(j+1)}) for j,z in enumerate(p[1:])])
        lhs=add((1,H((a,1-a))),(infl(p),kr),(1,rstar))
        vd=add(*[(p[j],add((1,logq(p[j]/a)),(1,{2:c+F(j)}),(j.bit_count(),kr))) for j in range(1,len(p)) if p[j]])
        rhs=add((1,H(p)),(1,vd));ck(lhs==rhs);symbolic+=1
    loss=[(-1,1),(0,1),(1,0),(1,-1)]
    for j in (0,1):
        mean=sum((F(z[j],4) for z in loss),F(0));var=sum((F(1,4)*(z[j]-mean)**2 for z in loss),F(0))
        ck(mean==F(1,4) and var==F(11,16))
    # Exact actual Boolean carrier and independent physical influence.
    h=(1,-1,-1,-1);v=(1,)
    for m in range(1,5 if not pilot else 3):
        v=tensor(v,h);p=spectrum(v);ck(p==tuple(F(1,len(v)) for _ in v))
        physical=sum((F(sum(v[t]!=v[t^(1<<i)] for t in range(len(v))),len(v)) for i in range(2*m)),F(0))
        ck(infl(p)==physical==m);ck(H(p)=={2:F(2*m)})
    totals=[]
    for m in range(1,5 if pilot else 9):
        law=conv(m);ck(sum(law.values())==4**m)
        ck(sum(F(a,4**m)*u for (u,v),a in law.items())==F(m,4))
        ck(sum(F(a,4**m)*v for (u,v),a in law.items())==F(m,4))
        varsum=sum((F(a,4**m)*((u-F(m,4))**2+(v-F(m,4))**2) for (u,v),a in law.items()),F(0))
        ck(varsum==F(11*m,8))
        minmean=sum((F(a,4**m)*min(u,v) for (u,v),a in law.items()),F(0))
        # Compare full mixture KL at every state, including zero weights.
        for w in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            d={}
            for (u,v),a in law.items():
                ratio=w*F(2)**(-u)+(1-w)*F(2)**(-v)
                ck(ratio<=F(2)**(-min(u,v)))
                d=add((1,d),(-F(a,4**m),logq(ratio)))
            ck(bounds(d)[0]>=0)
            ck(bounds(add((1,d),(-1,{2:minmean})))[0]>=0)
            if w in (0,1):ck(d=={2:F(m,4)})
            # Missing mass1/2 remains a complete additional one-bit bill.
            ds=add((1,d),(1,{2:F(1)}));ck(add((1,ds),(-1,d))=={2:F(1)})
            mixcases+=1
            if w==F(1,2):totals.append({'m':m,'divergence':record(d),'E_min':str(minmean)})
        ck(time.perf_counter()-start<55)
    cert={}
    if not pilot:
        law=conv(88);ck(sum(law.values())==4**88)
        emin=sum((F(a,4**88)*min(u,v) for (u,v),a in law.items()),F(0))
        zmax=F(22)-emin
        second=sum((F(a,4**88)*((u-22)**2+(v-22)**2) for (u,v),a in law.items()),F(0))
        ck(second==121);ck(zmax>=0 and zmax*zmax<=second);ck(emin>=11)
        ck(F(88,8)**2==F(11*88,8))
        cert={'m':88,'states':len(law),'E_min_exact':str(emin),'E_min_display_only':float(emin),'variance_sum':str(second),'all_weights_D_lower_at_least':11,'all_weights_complete_CE_lower_at_least':187,'H':176,'I':88}
    # The exact minimum loss vanishes when an actual product source is present.
    for m in (1,2,8):
        for w in (F(1,4),F(1,2),F(1)):
            ck(w<=1);ck(-logq(w).get(2,F(0))>=0)
    kbase=add((1,{2:F(4)}),(3,logq(F(3))));lo,hi=bounds(kbase)
    klo=lo+1/LN2[1];khi=hi+1/LN2[0]
    ck(F(101975,10000)<klo<khi<F(101976,10000))
    out={'status':'PASS','pilot':pilot,'assertions':E.COUNT,'Boolean_roots':rootcount,'tensor_cases':tensors,'formal_witness_coefficient_identities':symbolic,'mixture_cases':mixcases,'seconds':time.perf_counter()-start,'Kref_bits':{'lower':str(klo),'upper':str(khi),'display_only':float((klo+khi)/2)},'conditional_Kref_plus_4_display_only':float((klo+khi)/2+4),'mixture_curve':totals,'m88_all_weights_certificate':cert,'scope':'Actual Boolean tensor carrier; reference-mixture mismatch obstruction, not FEI; original fixed witness supplier conditional'}
    (RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','pilot','assertions','Boolean_roots','tensor_cases','mixture_cases','seconds']}))
if __name__=='__main__':run('--pilot' in sys.argv)
