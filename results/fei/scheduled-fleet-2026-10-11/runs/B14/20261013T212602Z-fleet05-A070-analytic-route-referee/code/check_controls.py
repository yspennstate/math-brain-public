from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,time
run=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(v):
    global checks
    assert v
    checks+=1
    if time.monotonic()-start>55: raise RuntimeError('frozen runtime guard')
def chars(values):
    return [sum(t*(-1 if (s&x).bit_count()%2 else 1) for x,t in enumerate(values)) for s in range(len(values))]
def influence(values):
    n=(len(values)-1).bit_length()
    return [Q(sum(values[x]!=values[x^(1<<i)] for x in range(len(values))),len(values)) for i in range(n)]
def cells(coords):
    if len(coords)==1:return []
    k=len(coords)//2
    return [sum(1<<i for i in coords)]+cells(coords[:k])+cells(coords[k:])
def lengths(N,cs):return [1+2*sum(bool(s&c) for c in cs) for s in range(1<<N)]
def energy(a,L):return Q(sum(t*t*l for t,l in zip(a,L)),len(a)**2)
def embedded(x,indices):return sum(((x>>j)&1)<<i for j,i in enumerate(indices))
neutral_cases=0; boundary=[]
for n in range(4):
    for mask in range(1<<(1<<n)):
        seed=[1-2*((mask>>x)&1) for x in range(1<<n)]; b=chars(seed); Ib=influence(seed)
        for N in [n+1,n+2]:
            M=1<<N; g=[seed[x&((1<<n)-1)] for x in range(M)]; g[0]*=-1
            a=chars(g); ii=influence(g); p=[Q(t*t,M*M) for t in a]
            ck(all(a[s]==(b[s]*(1<<(N-n)) if s<1<<n else 0)-2*seed[0] for s in range(M)))
            ck(sum(p)==1)
            for i in range(N):ck(abs(ii[i]-(Ib[i] if i<n else 0))<=Q(2,M))
            l1=sum(abs(p[s]-(Q(b[s]*b[s],1<<(2*n)) if s<1<<n else 0)) for s in range(M))
            # Squaring removes the only sqrt(2^n) in the claimed total variation bound.
            ck((max(Q(0),l1*Q(M,4)-1))**2<=1<<n)
            if n==0 and N==1:
                ck(a[0]==0 and a[1]!=0)
                boundary.append({'seed_sign':seed[0],'n':n,'N':N,'truth_table':g,'Walsh_numerators':a,'bad_anchor':1,'anchored_top_coefficient':'0'})
            else:
                ck(all(a)); I=sum(ii); V=1-p[0]
                U=sum(p[s]*(N-s.bit_count()) for s in range(1,M))
                ck(U==N*V-I)
            neutral_cases+=1
address_cases=0; address_bases=[]
for a in [1,2]:
    n=a+(1<<a)
    for N in [n,n+2]:
        selector=list(range(a)); data=list(range(a,n)); pad=list(range(n,N))
        cs=[(1<<n)-1]+cells(selector)+cells(data)
        if pad:cs=[(1<<N)-1]+cs+cells(pad)
        L=lengths(N,cs); M=1<<N
        base=[1-2*((x>>(a+(x&((1<<a)-1))))&1) for x in range(M)]
        b=chars(base); I=1+Q(a,2); Gamma=energy(b,L)
        def R(k):return Q(0) if k==1 else 1-Q(1,1<<k)+R(k//2)+R((k+1)//2)
        ck(Gamma==3+2*a+2*R(a)+2*bool(pad)); ck(Gamma<=8*I-5);ck(max(L)==2*N-1)
        # Kraft evaluated exactly over every subset; prefix proof is separate.
        ck(sum(Q(1,1<<l) for l in L)<=1)
        address_bases.append({'a':a,'N':N,'I':str(I),'Gamma':str(Gamma)})
        for x0 in range(M):
            g=base[:];g[x0]*=-1; aa=chars(g); Ii=influence(g); E=energy(aa,L)
            ck(all(aa[s]==b[s]-2*base[x0]*(-1 if (s&x0).bit_count()%2 else 1) for s in range(M)))
            ck(E<=16*sum(Ii)-10+Q(48*N-8,M));ck(E<=25*sum(Ii))
            if N>=6:ck(E<=16*sum(Ii))
            address_cases+=1
subcube_cases=0
for mask in range(256):
    g=[1-2*((mask>>x)&1) for x in range(8)]; a=chars(g); Ig=influence(g)
    for Zmask in range(1,7):
        Z=[i for i in range(3) if Zmask>>i&1];Y=[i for i in range(3) if not Zmask>>i&1]
        cz=cells(Z);cy=cells(Y);L=lengths(3,[7]+cz+cy)
        r=len(Z);rho=Q(1,1<<r);Wz=[2*sum(bool(s&c) for c in cz) for s in range(8)];Wy=[2*sum(bool(s&c) for c in cy) for s in range(8)]
        Uz=sum(2*(1-Q(1,1<<c.bit_count())) for c in cz)
        sourceY=Q(sum(t*t*w for t,w in zip(a,Wy)),64)
        averagedY=Q(0)
        for z in range(1<<r):
            zb=embedded(z,Z);h=[g[zb|embedded(y,Y)] for y in range(1<<len(Y))];bh=chars(h)
            EY=sum(Q(t*t,len(h)**2)*Wy[embedded(s,Y)] for s,t in enumerate(bh))
            averagedY+=rho*EY
            f=[-t if x&Zmask==zb else t for x,t in enumerate(g)];bf=chars(f);dd=[v-u for u,v in zip(a,bf)]
            E=energy(dd,L);mh=Q(bh[0],len(h))
            ck(E==4*rho*(1+2*(1-rho*mh*mh)+Uz+EY))
            for s in range(8):
                # Normalize both independent direct character sums.
                yfreq=sum(((s>>i)&1)<<j for j,i in enumerate(Y))
                ck(Q(dd[s],8)==-2*rho*(-1 if (s&zb).bit_count()%2 else 1)*Q(bh[yfreq],len(h)))
            ck(rho*EY<=sourceY);ck(E<=4*sourceY+4*rho*(2*r+1))
            If=influence(f)
            for i in Y:ck(If[i]==Ig[i])
            ck(sum(If[i]+Ig[i] for i in Z)>=2*r*rho)
            subcube_cases+=1
        ck(averagedY==sourceY)
pair_cases=0; witnesses=[]
for N in [2,3]:
    M=1<<N;cs=cells(list(range(N)));L=lengths(N,cs)
    for mask in range(1<<M):
        g=[1-2*((mask>>x)&1) for x in range(M)];b=chars(g)
        for x,y in combinations(range(M),2):
            u=[-2*g[x]*(-1 if (s&x).bit_count()%2 else 1) for s in range(M)]
            v=[-2*g[y]*(-1 if (s&y).bit_count()%2 else 1) for s in range(M)]
            cross=Q(sum(t*w*l for t,w,l in zip(u,v,L)),M*M)
            K=-sum(2*(1<<(N-c.bit_count())) for c in cs if (x^y)&~c==0)
            ck(cross==Q(4*g[x]*g[y]*K,M*M))
            f=g[:];f[x]*=-1;f[y]*=-1;af=chars(f)
            ck(all(af[s]-b[s]==u[s]+v[s] for s in range(M)))
            Etot=energy([t-w for t,w in zip(af,b)],L)
            ck(Etot==energy(u,L)+energy(v,L)+2*cross)
            if N==2 and g==[1,-1,1,-1] and x==0 and y==1:
                ck(cross==Q(1,2));ck(Etot==6)
                witnesses.append({'N':N,'base_truth_table':g,'edited_truth_table':f,'points':[x,y],'physical_overlap_density':'0','cross_energy':str(cross),'single_energies':[str(energy(u,L)),str(energy(v,L))],'combined_energy':str(Etot),'lengths':L})
            pair_cases+=1
ck([neutral_cases,address_cases,subcube_cases,pair_cases]==[556,360,4608,7264])
output={'status':'PASS','helper_version':'A070-stage2-independent-v1','arithmetic':'integer direct character sums and Fraction; no floating entropy or author implementation imported','counts':{'neutralization':neutral_cases,'addressing':address_cases,'subcube':subcube_cases,'double_point':pair_cases},'exact_assertions':checks,'seconds':time.monotonic()-start,'boundary_counterexamples':boundary,'addressing_bases':address_bases,'positive_disjoint_cross_witnesses':witnesses}
(run/'out').mkdir(exist_ok=True)
(run/'out/CONTROL_CHECK.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in output.items() if k not in ['boundary_counterexamples','addressing_bases','positive_disjoint_cross_witnesses']}))
