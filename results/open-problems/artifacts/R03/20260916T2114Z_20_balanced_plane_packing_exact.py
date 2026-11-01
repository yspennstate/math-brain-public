from itertools import product, combinations
from math import comb
from fractions import Fraction

def falling(a,m):
    if a < m: return 0
    z=1
    for j in range(m): z*=a-j
    return z

def L(s):
    h=s//2
    return comb(s,h) if s%2 else comb(s,h)//2

def bal(s):
    h=s//2
    plus=h+1 if s%2 else h
    return [1]*plus+[-1]*(s-plus)

def canonical_vectors(m,s,t):
    v=[0]*m; w=[0]*m
    for i,a in enumerate(bal(s)): v[i]=a
    for j,a in enumerate(bal(t),start=s): w[j]=a
    return tuple(v),tuple(w)

def support(v,p):
    return sum((x%p)!=0 for x in v)

def projective_supports(v,w,p):
    sig=set()
    for a in range(p):
        for b in range(p):
            if a==0 and b==0: continue
            x=tuple((a*v[i]+b*w[i])%p for i in range(len(v)))
            j=next(i for i,z in enumerate(x) if z)
            inv=pow(x[j],-1,p)
            y=tuple((z*inv)%p for z in x)
            sig.add(y)
    assert len(sig)==p+1
    return sorted(support(x,p) for x in sig)

def canonical_S(m,s,t,p):
    v,w=canonical_vectors(m,s,t)
    S=[]
    for x in product((0,1),repeat=m):
        if not any(x): continue
        if sum(v[i]*x[i] for i in range(m))%p==0 and sum(w[i]*x[i] for i in range(m))%p==0:
            S.append(x)
    return S

def g_value(m,s,t,p):
    S=canonical_S(m,s,t,p)
    bad=[]
    for i in range(m):
        bad.append(sum(x[i]==0 for x in S))
    for i,j in combinations(range(m),2):
        bad.append(sum(x[i]==x[j] for x in S))
    g=falling(len(S),m)-sum(falling(c,m) for c in bad)
    return len(S),g,tuple(sorted(set(bad)))

def Nplanes(m,s,t):
    if s>t: s,t=t,s
    z=comb(m,s)*comb(m-s,t)*L(s)*L(t)
    if s==t: z//=2
    return z

def new_pairs(m):
    return [(s,t) for s in range(3,m+1) for t in range(s,m+1)
            if s+t<=m and max(s,t)>=5]

expected_core={
 (9,7):{
  (3,5):(59,3916648128677760,15120,59219719705607731200),
  (3,6):(59,3932565242981760,2520,9910064412314035200),
  (4,5):(59,3932565242981760,3780,14865096618471052800)},
 (10,11):{
  (3,5):(119,341195024766866054400,75600,25794343872375073712640000),
  (3,6):(119,342228359682822412800,25200,8624154664007124802560000),
  (3,7):(104,84769310307474777600,12600,1068093309874182197760000),
  (4,5):(119,342228359682822412800,37800,12936231996010687203840000),
  (4,6):(119,342228359682822412800,6300,2156038666001781200640000),
  (5,5):(99,51574291322435481600,12600,649836070662687068160000)}
}

print("R03 run20 balanced sparse plane packing exact checker")
totals={}
for (m,p),E in expected_core.items():
    assert new_pairs(m)==list(E)
    total=0
    for (s,t),exp in E.items():
        v,w=canonical_vectors(m,s,t)
        sups=projective_supports(v,w,p)
        small=[x for x in sups if x<s+t]
        assert small==sorted([s,t])
        assert sum(x<=4 for x in sups)<=1
        Ssz,g,bad=g_value(m,s,t,p)
        N=Nplanes(m,s,t)
        add=N*max(g,0)
        assert (Ssz,g,N,add)==exp, ((m,p,s,t),(Ssz,g,N,add),exp)
        total+=add
        print("case",m,p,(s,t),"S",Ssz,"g",g,"bad_sizes",bad,
              "N",N,"add",add,"support_spectrum",sups)
    totals[(m,p)]=total
    print("total_new_M2",m,p,total)

assert totals[(9,7)]==83994880736392819200
assert totals[(10,11)]==51228698578931536185600000

cases=[
(9,7,651685823418402269683200,2942127020232812160000,totals[(9,7)],
 Fraction(159002423250871502925,576460752303423488)),
(10,11,325043331888785398807391827200,807305539038902680414176000,totals[(10,11)],
 Fraction(4089622106045106025499398988925,7787900129957441143457185792))
]
for m,p,M1,M2,add,old in cases:
    D=m-5
    c=Fraction(p*(p*p-1),p**D-1)
    scale=Fraction(2**(m+1),2**(m*m))
    new=scale*(M1-c*(M2+add))
    assert new<old
    print(f'metric {m} {p} D {D} c {c}')
    print("new_r",new,"decimal",float(new))
    print("improvement",old-new,"decimal",float(old-new))

for s in range(3,13):
    c=bal(s)
    cnt=sum(1 for x in product((0,1),repeat=s)
            if sum(a*b for a,b in zip(c,x))==0)
    assert cnt==comb(s,s//2)
print("balanced_density_identity_s3_to12 PASS")
print("SELF-CHECK PASS")
