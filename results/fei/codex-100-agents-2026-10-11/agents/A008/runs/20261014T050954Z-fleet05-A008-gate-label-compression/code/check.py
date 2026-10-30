import json,itertools as it,math,time,sys
from fractions import Fraction as F
from pathlib import Path
B=Path(__file__).resolve().parents[1];checks=0
def ck(x):
    global checks
    checks+=1
    assert x
def enc(x):return [x.numerator,x.denominator]
def fwht(t):
    a=t[:];s=1
    while s<len(a):
        for k in range(0,len(a),2*s):
            for j in range(k,k+s):x,y=a[j],a[j+s];a[j],a[j+s]=x+y,x-y
        s*=2
    return a
def family(m,connected):
    n=m+3;h=0;y=m+1;z=m+2
    edges=[(h,j) for j in range(1,m+1)]+([(h,y)] if connected else [])+[(y,z)]
    t=[1 if any((x>>v&1) and (x>>w&1) for v,w in edges) else -1 for x in range(1<<n)];a=fwht(t)
    influences=[F(sum(t[x]!=t[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n)]
    I=sum(influences,F(0));P=[F(v*v,4**n) for v in a];v=1-P[0];u=F(1,2**m);q=(1+u)/2
    ck(sum(P)==1);ck(I==sum(F(mask.bit_count())*p for mask,p in enumerate(P)))
    if connected:
        expected=[F(3,4)-u/2]+[u/2]*m+[F(1,4)+u/2,F(1,4)]
        ck(influences==expected);ck(I==F(5,4)+m*u/2);ck(F(5,4)<=I<=F(3,2));ck(P[1<<z]==F(1,16))
        leafmask=sum(1<<j for j in range(1,m+1));tail=F(0)
        for mask,p in enumerate(P):
            if mask&leafmask:
                ck(p==(F(0) if mask>>z&1 else u*u/4));tail+=mask.bit_count()*p
        ck(tail==(F(m,2)+1)*u-u*u)
        lam=[F(1,2*m)]*m+[F(1,2),F(1,2)];D=math.prod(1+l/4 for l in lam)-1
        rows=[sum(l for l,e in zip(lam,edges) if j in e) for j in range(n)]
        ck(rows[0]==rows[y]==1);ck(all(0<r<=1 for r in rows));ck(D<F(25,56)<1)
        du=(1+F(1,4*(m+1)))**(m+2)-1;ck(du>F(1,4));qz=F(1,32*(m+1))/du
        ck(qz< F(1,8*(m+1)))
        # Exact core and tail bills before invoking proved logarithm inequalities.
        ck((m+7)*(F(m,2)+1)*u<=F(9,2));ck(7*I+F(9,2)<=F(53,5)*I)
        result={'m':m,'connected':True,'I':enc(I),'variance':enc(v),'tail_degree':enc(tail),'D_repaired':enc(D),'uniform_Q_singleton_z':enc(qz),'packing_rows':[enc(r) for r in rows]}
    else:
        istar=1+(m-1)*u;expectedI=F(3,4)*istar+q
        ck(I==expectedI);ck(I<=F(25,16));ck(P[1<<y]==q*q/4==P[1<<z])
        Ds=(1+F(1,4*m))**m-1;eta=3*q/4;beta=F(4,3)*Ds/((1+Ds)*(1-q))
        ck(F(1,4)<Ds<F(1,3));ck(F(8,15)<beta<F(8,9));ck(v-eta==F(9,4)*q*(1-q));ck((v-eta)*(1+Ds)*beta/4==eta*Ds)
        ck(eta/I>=F(7,25));ck((m+1)*(m+6)*u<=6);ck(F(5,4)*(1+Ds)-1<F(2,3))
        # Verify component/cross spectral formulas through the false-indicator product.
        st=[1 if (x&1) and any(x>>j&1 for j in range(1,m+1)) else -1 for x in range(1<<(m+1))];sa=fwht(st)
        for mask,p in enumerate(P):
            if not mask:continue
            sm=mask&((1<<(m+1))-1);pm=mask>>(m+1)
            if pm==0:coef=F(3,4)*F(sa[sm],1<<(m+1))
            elif sm==0:coef=q*F(-1 if pm==3 else 1,2)
            else:coef=-F(sa[sm],1<<(m+1))*F(-1 if pm==3 else 1,4)
            ck(coef*coef==p)
        result={'m':m,'connected':False,'I':enc(I),'variance':enc(v),'eta':enc(eta),'D_star':enc(Ds),'beta_slice_optimum':enc(beta)}
    return result
def root_fixture():
    p=Path('../A009/runs/20261014T024630Z-fleet05-A009-fractional-incidence-optimization/out/CHECK.json')
    cert=next(x for x in json.loads(p.read_text())['certificates'] if len(x['edges'])==2)
    n=cert['n'];edges=[tuple(e) for e in cert['edges']];base=list(map(F,cert['base_lambda']));N=len(edges)
    truth=[1 if any(all(x>>j&1 for j in e) for e in edges) else -1 for x in range(1<<n)];ft=fwht(truth);v=1-F(ft[0]**2,4**n);c=[F(0)]*N
    for mask in range(1,1<<n):
        A=[j for j in range(n) if mask>>j&1];P=F(ft[mask]**2,4**n)
        if not P:continue
        terms=[]
        for own in it.product(*[[i for i,e in enumerate(edges) if j in e] for j in A]):
            used=sorted(set(own));owned={i:{j for j,k in zip(A,own) if k==i} for i in used};pairs=[i for i in used if len(owned[i])==2];covered=set().union(*(owned[i] for i in pairs)) if pairs else set();U=set(A)-covered
            if any(set(e)<=U for e in edges):continue
            roots=[];hs={i:{j:0 for j in owned[i]} for i in pairs}
            for i in used:
                inc=[(k,j) for k in used if k!=i for j in owned[k] if j in edges[i]]
                if inc:k,j=inc[0];ck(len(inc)==1 and k in pairs);hs[k][j]+=1
                else:roots.append(i)
            mass=math.prod(base[i] for i in used)*F(1,4)**len(roots)
            for i in used:
                s=len(owned[i]);cc=sum(hs[i].values()) if i in pairs else 0
                mass*=(F(1,4) if s==1 else F(1,6))*F(1,(cc+1)*(cc+2)*math.comb(s+cc-1,cc))
                if i in pairs:mass*=math.prod(math.factorial(h) for h in hs[i].values())
            terms.append((used,mass))
        W=sum(x for _,x in terms);ck(W==F(cert['W_base'][str(mask)]))
        for i in range(N):c[i]+=P*sum(x for used,x in terms if i in used)/W
    ck(c==list(map(F,cert['c'])));C=sum(c);ck(C>v)
    lam=[F(1,4)]+[F(1,10**6)]*(N-1);D=math.prod(1+l/4 for l in lam)-1
    omega={mask:math.prod(lam[i]/4 for i in range(N) if mask>>i&1)/D for mask in range(1,1<<N)}
    sigma={1<<i:c[i]/C for i in range(N)};r=[sum(p for mask,p in omega.items() if mask>>i&1) for i in range(N)]
    needed=[(v*r[i]-c[i])/(v*r[i]-v*c[i]/C) for i in range(N) if v*r[i]>c[i]];delta=max(needed,default=F(0));ck(delta>0)
    nu={mask:(1-delta)*p+delta*sigma.get(mask,F(0)) for mask,p in omega.items()};ck(sum(nu.values())==1)
    b=[c[i]-v*sum(p for mask,p in nu.items() if mask>>i&1) for i in range(N)];ck(all(x>=0 for x in b))
    chi=sum(sigma.get(mask,F(0))**2/p for mask,p in omega.items())-1;short=sum((c[i]/C)**2*4*D/lam[i] for i in range(N))-1;ck(chi==short)
    mixed=sum((nu[mask]-p)**2/p for mask,p in omega.items());ck(mixed==delta*delta*chi)
    out={'source_fixture':cert['name'],'v':enc(v),'c':[enc(x) for x in c],'lambda_poor':[enc(x) for x in lam],'delta':enc(delta),'b':[enc(x) for x in b],'root_chi_square':enc(chi),'mixed_chi_square':enc(mixed),'scope':'root-mixture and usage subclaim independently checked; not whole 68-case A009 acceptance'}
    (B/'out/ROOT_MIXTURE_FIXTURE.json').write_text(json.dumps(out,indent=2),encoding='utf8')
def main():
    start=time.perf_counter();domain=range(2,5) if '--pilot' in sys.argv else range(2,9);out=[]
    for m in domain:
        for connected in [False,True]:
            out.append(family(m,connected));(B/'out/FAMILY_CERTIFICATES.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    root_fixture()
    result={'boolean_functions':len(out),'m_domain':list(domain),'assertions':checks,'seconds':time.perf_counter()-start,'all_exact_checks_passed':True}
    (B/'out'/('PILOT_SUMMARY.json' if '--pilot' in sys.argv else 'CHECK_SUMMARY.json')).write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
if __name__=='__main__':main()
