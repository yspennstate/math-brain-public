from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,factorial
import json,time
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; N=0
def ck(x):
    global N
    N+=1
    assert x,N
def fw(table):
    a=list(table); k=1
    while k<len(a):
        for i in range(0,len(a),2*k):
            for j in range(k):
                u,v=a[i+j],a[i+j+k]; a[i+j],a[i+j+k]=u+v,u-v
        k*=2
    return {s:F(v,len(a)) for s,v in enumerate(a) if v}
def influence(table):
    n=(len(table)-1).bit_length()
    return [F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table)) for j in range(n)]
def add(*xs):
    r={}
    for d in xs:
        for k,v in d.items(): r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}
def scale(d,c): return {k:v*c for k,v in d.items() if v*c}
def logq(q):
    q=F(q); ck(q>0); r={}
    for integer,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=integer:
            while integer%d==0: r[d]=r.get(d,0)+sgn; integer//=d
            d+=1
        if integer>1: r[integer]=r.get(integer,0)+sgn
    return {k:F(v) for k,v in r.items() if v}
def entropy(law):
    return add(*(scale(logq(p),-p) for p in law.values() if p))
def lnunit(q):
    z=(q-1)/(q+1); z2=z*z; power=z; s=F(0)
    for k in range(48): s+=2*power/F(2*k+1); power*=z2
    err=2*abs(power)/(97*(1-z2))
    return s-err,s+err
L2=lnunit(F(2))
def ln(q):
    q=F(q); k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    lo,hi=lnunit(q)
    return (lo+k*(L2[0] if k>=0 else L2[1]),hi+k*(L2[1] if k>=0 else L2[0]))
def ent_interval(law):
    lo=hi=F(0)
    for p in law.values():
        if p:
            a,b=ln(p); lo-=p*b; hi-=p*a
    return lo,hi

def debt():
    cases=0
    for n in range(4):
        for word in range(1<<(1<<n)):
            table=[1 if word>>x&1 else -1 for x in range(1<<n)]
            spec=fw(table); p={s:c*c for s,c in spec.items()}; v=1-p.get(0,0)
            if not v: continue
            relevant=[j for j,a in enumerate(influence(table)) if a]; d=len(relevant)
            pi=min(F(sum(x==1 for x in table),len(table)),F(sum(x==-1 for x in table),len(table)))
            I=sum(s.bit_count()*mass for s,mass in p.items()); R={}; div={}; up=F(0)
            hp=entropy(p); hsplit=entropy({0:1-v,1:v})
            for s,mass in p.items():
                if not s: continue
                ranks=[i+1 for i,j in enumerate(relevant) if s>>j&1]; k=len(ranks)
                ratio=F(1,factorial(k))
                for r in ranks: ratio*=r
                ck(1<=ratio<=comb(d,k))
                logU=add(scale(logq(F(1,432)),k),{'e':F(-k)},scale(logq(ratio),F(-6,5)))
                R=add(R,scale(logq(ratio),mass*F(6,5)))
                div=add(div,scale(add(logq(mass/v),scale(logU,-1)),mass))
                up+=F(1,432**k) # e>=1 and ratio>=1: rigorous upper mass
            ck(up<=1)
            Kref=add(logq(432),{'e':F(1)})
            ck(add(hsplit,scale(Kref,I),R)==add(hp,div))
            ck(add(logq(pi),scale(logq(pi),-1))=={})
            cases+=1
    parity=[]
    for n in range(2,9):
        d=n+1; nn=1<<n; law={0:(1-F(2,nn))**2}
        for s in range(1,1<<d):
            if s.bit_count()%2==0: law[s]=F(4,nn**2)
        ck(sum(law.values())==1)
        ck(sum(s.bit_count()*p for s,p in law.items())==F(2*d,nn))
        for s in law:
            if s: ck(all(not law.get(s^(1<<j),0) for j in range(d)))
        # Product-of-ranks ratio bounds the entire residual without logs.
        for s in law:
            if not s: continue
            k=s.bit_count(); ratio=F(1,factorial(k))
            for j in range(d):
                if s>>j&1: ratio*=j+1
            ck(1<=ratio<=comb(d,k)<=2**d)
        ck(F(6,5)*(1-law[0])*d<=F(12,5)*F(2*d,nn))
        parity.append(n)
    return {'nonconstant_tables':cases,'parity_dimensions':parity}

def root_forest(blocks,supports):
    gates=sorted(blocks); edges={(g,h) for g in gates for h in gates if g!=h and blocks[g]&supports[h]}
    reach={(g,g) for g in gates}|edges
    for k in gates: reach|={(g,h) for g in gates for h in gates if (g,k) in reach and (k,h) in reach}
    comps=[]; unseen=set(gates)
    while unseen:
        g=min(unseen); c={h for h in gates if (g,h) in reach and (h,g) in reach}; comps.append(c); unseen-=c
    roots=sorted(min(c) for c in comps if not any(h in c and g not in c for g,h in edges))
    seen=set(roots); queue=list(roots); parents=[]
    while queue:
        g=queue.pop(0)
        for h in gates:
            if (g,h) in edges and h not in seen: seen.add(h); queue.append(h); parents.append((g,h))
    ck(seen==set(gates)); ck(len(parents)+len(roots)==len(gates))
    for g,h in parents: ck(blocks[g]&supports[h]!=0)
    return roots

def roots():
    cases=0
    for w1,w2 in product(range(1,16),repeat=2):
        union=w1|w2
        if union==15: continue
        bt=[F(union>>x&1) for x in range(4)]; b=sum(bt)/4; bh=fw(bt)
        dataI=4*sum(s.bit_count()*c*c for s,c in bh.items())
        rho=[F(w1.bit_count(),4),F(w2.bit_count(),4)]
        data_sup=[sum(1<<j for j,a in enumerate(influence([w>>x&1 for x in range(4)])) if a) for w in [w1,w2]]
        for r in range(1,4):
            p=F(1,2**r); core=(1<<r)-1
            supports=[core|(s<<r) for s in data_sup]
            table=[2*int((x&core)==0)*int(union>>(x>>r)&1)-1 for x in range(1<<(r+2))]
            sp=fw(table); law={s:c*c for s,c in sp.items()}; v=4*p*b*(1-p*b); Id=p*dataI; Ic=2*r*p*b
            ck(1-law.get(0,0)==v); ck(sum(influence(table))==Id+Ic)
            counts={}; root_sets={}
            for A,mass in law.items():
                if not A: continue
                U=A&core; T=A>>r; blocks={}
                if U: blocks[0]=U
                for j in range(2):
                    if T>>j&1:
                        owner=next(g for g,s in enumerate(data_sup) if s>>j&1)
                        blocks[owner]=blocks.get(owner,0)|(1<<(r+j))
                rs=root_forest(blocks,supports)
                ck(len(rs)==1 if U else 1<=len(rs)<=T.bit_count())
                if U: ck(0 in rs)
                root_sets[A]=rs; counts[A]=len(rs)
                ck(sp[A]==2*p*bh.get(T,0))
            EK=sum(law[A]*counts[A] for A in counts)
            ck(0<=r*(EK-v)<=Id/2)
            for lam in [(F(1,3),F(2,3)),(F(1,5),F(1,5))]:
                s=sum(lam[i]*rho[i] for i in range(2)); x=[p*lam[i]*rho[i] for i in range(2)]
                D=product2(1+x[0],1+x[1])-1; a=p*s
                rootlaw={mask:product2(*[x[i] if mask>>i&1 else F(1) for i in range(2)])/D for mask in range(1,4)}
                ck(sum(rootlaw.values())==1)
                ck(D>=a); ck(ln(D/a)[1]<=a)
                left=scale(logq(D),v); base={}
                for A,rs in root_sets.items():
                    for g in rs:
                        left=add(left,scale(logq(1/(p*rho[g])),law[A]))
                        base=add(base,scale(logq(1/rho[g]),law[A]))
                right=add(scale(logq(s),v),scale(logq(D/(p*s)),v),{2:r*(EK-v)},base)
                ck(left==right); ck(v*a<=Ic); cases+=1
    petals=0
    for widths in product(range(1,3),repeat=3):
        rho=[F(1,2**w) for w in widths]; Q=F(1)
        for a in rho: Q*=1-a
        for r in range(1,4):
            n=sum(widths); table=[]
            for x in range(1<<n):
                start=0; true=False
                for w in widths:
                    true|=(x>>start)&((1<<w)-1)==0; start+=w
                table.append(int(true))
            spec=fw(table); weighted=F(0)
            for T,c in spec.items():
                if not T: continue
                start=0; K=0
                for w in widths: K+=bool((T>>start)&((1<<w)-1)); start+=w
                weighted+=(K-1)*c*c
            ck(weighted==Q*(sum(rho)-(1-Q))); petals+=1
    return {'overlap_weight_cases':cases,'petal_cases':petals}
def product2(*args):
    z=F(1)
    for x in args:z*=x
    return z

def lengths(law,return_lengths=False):
    lens={}
    for key,p in law.items():
        if not p: continue
        l=0
        while (1<<l)*p<1:l+=1
        lens[key]=l
    ck(sum(F(1,2**l) for l in lens.values())<=1)
    words={}; word=0; last=0
    for key,l in sorted(lens.items(),key=lambda kv:(kv[1],str(kv[0]))):
        word<<=l-last; ck(word<(1<<l)); words[key]=format(word,'0'+str(l)+'b') if l else ''; word+=1; last=l
    ws=list(words.values()); ck(all(not(len(a)<len(b) and b.startswith(a)) for a in ws for b in ws))
    return lens if return_lengths else sum(law[k]*l for k,l in lens.items())
def dictionary():
    nr=0; quotient=[]
    for m in range(1,6):
        raw={}; Q={}; supports={i:1|(1<<(i+1)) for i in range(m)}
        for states in product(range(4),repeat=m):
            selected=[i for i,b in enumerate(states) if b]
            if not selected:continue
            k=len(selected); prob=F(m+1,m*k*(k+1)*comb(m,k)*3**k); A=0; blocks={}
            for i in selected:
                b=[0,1,1<<(i+1),supports[i]][states[i]]; A|=b
                # Canonical ownership is first selected local subset containing j.
                own=b&~sum(blocks.values());
                if own: blocks[i]=own
            root_forest(blocks,supports)
            raw[states]=prob; Q[A]=Q.get(A,0)+prob; nr+=1
            if A==1: ck(prob<=F(1,m))
        ck(sum(raw.values())==sum(Q.values())==1)
        ck(Q[1]==sum(F(m+1,m*k*(k+1)*3**k) for k in range(1,m+1)))
        ck(Q[1]>=F(1,6))
        for A,q in Q.items():
            T=A>>1;t=T.bit_count()
            if not t:continue
            b=F(m+1,m*t*(t+1)*comb(m,t)*3**t)
            if not A&1: ck(q==b)
            else:
                expected=sum(F(comb(m-t,u)*(2**t-1 if u==0 else 2**t)*(m+1),m*(t+u)*(t+u+1)*comb(m,t+u)*3**(t+u)) for u in range(m-t+1))
                ck(q==expected and q>=b)
            ck(q>=F(1,2**(3*m+2*t)))
        v=1-F(1,4**m); full={0:1-v,**{A:v*q for A,q in Q.items()}}
        lens=lengths(full,True)
        spectral={0:1-v,1:(1-F(1,2**m))**2}
        for A in Q:
            if A!=1: spectral[A]=F(1,4**m)
        ck(sum(spectral.values())==1)
        expected=sum(spectral[A]*lens[A] for A in spectral)
        ck(expected<F(33,4)*(1+F(m-1,2**m)))
        lengths(raw); quotient.append({'m':m,'record_mass':str(sum(raw.values())),'output_mass':str(sum(Q.values())),'physical_expected_length':str(expected)})
    # A nonuniform rational table checks elementary-symmetric name normalization.
    eta=[F(1),F(2),F(3)]; kappa=[F(1,2),F(1,3),F(1,6)]; total=F(0)
    for k in range(1,4):
        Ek=sum(product2(*(eta[i] for i in c)) for c in combinations(range(3),k))
        for c in combinations(range(3),k):
            for states in product(range(3),repeat=k):
                total+=kappa[k-1]*product2(*(eta[i] for i in c))/Ek*product2(*([F(1,7),F(2,7),F(4,7)][s] for s in states))
    ck(total==1)
    return {'sunflower_records':nr,'quotient':quotient,'nonuniform_mass':str(total)}

def biased_spectrum(table,biases):
    n=len(biases); p={}; mean=F(0)
    weights=[product2(*(t if x>>j&1 else 1-t for j,t in enumerate(biases))) for x in range(1<<n)]
    for s in range(1<<n):
        num=sum(weights[x]*table[x]*product2(*(F(x>>j&1)-biases[j] for j in range(n) if s>>j&1)) for x in range(1<<n))
        q=num*num/product2(*(t*(1-t) for j,t in enumerate(biases) if s>>j&1))
        if q:p[s]=q
    ck(sum(p.values())==1)
    mean=sum(weights[x]*table[x] for x in range(1<<n))
    E=add(*(scale(logq(product2(*(4*t*(1-t) for j,t in enumerate(biases) if s>>j&1))/q),q) for s,q in p.items() if s))
    deficit=sum(s.bit_count()*q for s,q in p.items())-(1-mean*mean)
    ck(deficit>=0)
    return p,E,deficit,mean
def gate(kind,arity,x):
    if kind=='and':return 1 if x==(1<<arity)-1 else -1
    if kind=='or':return 1 if x else -1
    return (-1)**(arity-x.bit_count())
def readonce():
    universe=255; memo={0:{0,255}}
    for size in range(1,4):
        for mask in range(1,8):
            if mask.bit_count()!=size: continue
            vals={0,255}
            if size==1:
                j=(mask&-mask).bit_length()-1; v=sum(1<<x for x in range(8) if x>>j&1); vals|={v,v^255}
            sub=(mask-1)&mask
            while sub:
                other=mask^sub
                if other:
                    for a,b in product(memo[sub],memo[other]): vals|={a&b,a|b,(a^b)^255}
                sub=(sub-1)&mask
            vals|={v^255 for v in list(vals)}; memo[mask]=vals
    R=memo[7];ck(len(R)==152)
    mux=sum(1<<x for x in range(8) if (x>>1&1 if x&1 else x>>2&1)); ck(mux not in R)
    for word in R:
        for j in range(3):
            for bit in [0,1]:
                restrict=sum(1<<x for x in range(8) if word>>((x&~(1<<j))|(bit<<j))&1)
                ck(restrict in R)
    activation_cases=0
    for word in range(256):
        core=[1 if word>>x&1 else -1 for x in range(8)]; sp=fw(core); mu=F(sum(core),8)
        for r in range(1,4):
            p=F(1,2**r); mask=(1<<r)-1
            table=[core[x>>r] if not x&mask else 1 for x in range(1<<(r+3))]; actual=fw(table)
            expected={}
            for s in range(1<<(r+3)):
                U=s&mask;T=s>>r
                c=(1-p*(1-mu)) if s==0 else (-p*(1-mu) if T==0 else p*sp.get(T,0))
                if c:expected[s]=c
            ck(actual==expected)
            ck(sum(influence(table))==p*sum(influence(core))+r*p*(1-mu));activation_cases+=1
    biasgrid=[F(1,4),F(1,2),F(3,4)]; gates=0
    for n in range(1,4):
        for biases in product(biasgrid,repeat=n):
            for kind in ['and','or','parity']:
                table=[gate(kind,n,x) for x in range(1<<n)]; law,E,delta,mu=biased_spectrum(table,biases)
                lo=hi=F(0)
                for prime,c in E.items():
                    a,b=ln(prime);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
                bound=(2*L2[0]+4)*delta
                ck(hi<=bound if delta else E=={}); gates+=1
    compositions=0
    for biases in [(F(1,4),F(1,2),F(3,4),F(1,4)),(F(1,2),)*4]:
        children=[[gate(kind,2,x) for x in range(4)] for kind in ['and','parity']]
        child=[biased_spectrum(children[i],biases[2*i:2*i+2]) for i in range(2)]
        for kind in ['and','or','parity']:
            outer=[gate(kind,2,x) for x in range(4)]
            bp=[(1+c[3])/2 for c in child]; op,oe,od,om=biased_spectrum(outer,bp)
            c=[sum(q for s,q in op.items() if s>>i&1)/(1-child[i][3]**2) for i in range(2)]
            table=[outer[int(children[0][x&3]==1)|(int(children[1][x>>2]==1)<<1)] for x in range(16)]
            ap,ae,ad,am=biased_spectrum(table,biases)
            ck(ae==add(oe,*(scale(child[i][1],c[i]) for i in range(2))))
            ck(ad==od+sum(c[i]*child[i][2] for i in range(2)));compositions+=1
    for r in range(1,13):
        p=F(1,2**r); law={0:(1-p)**2}
        # Aggregate coefficient multiplicities; entropy invariant under this grouping only if stored per atom.
        Hlo,Hhi=ent_interval({0:(1-p)**2}); mass=p*p
        llo,lhi=ln(mass); Hhi-=((2**(r+1))-1)*mass*llo
        ck(Hhi<=4*r*p*L2[0]+2*p)
        J={j:F(1,2**j) for j in range(1,r+1)};J[r+1]=p
        ck(entropy(J)=={2:2*(1-p)})
        ck(F(4*(2**r-1),r+1)==F(4*(1-p),p*(r+1)))
    return {'readonce_members':len(R),'arbitrary_core_activations':activation_cases,'biased_gate_cases':gates,'composition_cases':compositions,'literal_r_max':12}

def main():
    t=time.perf_counter(); results={}
    for name,fn in [('A003',debt),('A007',roots),('A008',dictionary),('A012',readonce)]:
        results[name]=fn(); results['assertions_so_far']=N
        (OUT/'PARTIAL_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
        print(name,'PASS',N,flush=True)
    results.update(assertions=N,failures=0,seconds=time.perf_counter()-t,arithmetic='Fraction, integer Walsh, rational-log linear forms and rigorous rational natural-log intervals')
    (OUT/'EXACT_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8');print(json.dumps(results),flush=True)
if __name__=='__main__':main()
