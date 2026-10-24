from fractions import Fraction as Q
from itertools import combinations
import hashlib, json

TERMS=(0,1,2)

def forest_state(n, edges, mask):
    parent=list(range(n)); rank=[0]*n
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            if not union(u,v): return None
    r=[find(t) for t in TERMS]
    if len(set(r))==3: return 0       # D: all terminals separate
    if r[0]==r[1]==r[2]: return 4    # T: all terminals connected
    if r[0]==r[1]: return 1
    if r[0]==r[2]: return 2
    return 3

def state_counts(n, edges):
    m=len(edges)
    total=[0]*5
    one=[[0]*5 for _ in range(m)]
    two={}
    for mask in range(1<<m):
        s=forest_state(n,edges,mask)
        if s is None: continue
        total[s]+=1
        inc=[i for i in range(m) if (mask>>i)&1]
        for i in inc: one[i][s]+=1
        for i,j in combinations(inc,2):
            two.setdefault((i,j),[0]*5)[s]+=1
    return total,one,two

def connected_after_delete(n,edges,dels):
    rem=[v for v in range(n) if v not in dels]
    if len(rem)<=1: return True
    adj={v:[] for v in rem}
    for u,v in edges:
        if u in adj and v in adj:
            adj[u].append(v); adj[v].append(u)
    seen={rem[0]}; stack=[rem[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==len(rem)

def is_3connected(n,edges):
    if n<4: return False
    for k in (0,1,2):
        for ds in combinations(range(n),k):
            if not connected_after_delete(n,edges,set(ds)): return False
    return True

def F(s):
    d,a,b,c,t=s
    return Q(31*d+24*(a+b+c)+16*t,16)

def data(total,se,sf,sef):
    d,de,df,def_=total[0],se[0],sf[0],sef[0]
    assert d>0
    z,ze,zf,zef=F(total),F(se),F(sf),F(sef)
    q0=ze*zf-z*zef
    q1=ze*df+de*zf-z*def_-d*zef
    q2=de*df-d*def_
    c=q0/(z*z)
    cp=Q(q2,d*d)
    deltae=ze/z-Q(de,d)
    deltaf=zf/z-Q(df,d)
    r=Q(d,16)/z
    N1=q0+Q(1,16)*q1+Q(1,256)*q2
    B=None if 32*c+cp==0 else deltae*deltaf/(32*c+cp)
    R=None if (1+r)*(c+r*cp)==0 else r*deltae*deltaf/((1+r)*(c+r*cp))
    return dict(F=z,Fe=ze,Ff=zf,Fef=zef,q0=q0,q1=q1,q2=q2,c=c,cp=cp,
                deltae=deltae,deltaf=deltaf,r=r,N1=N1,B=B,R=R)

def qstr(x): return f"{x.numerator}/{x.denominator}" if x.denominator!=1 else str(x.numerator)

# A. Explicit 7-vertex route-kill for the proposed uniform 32-barrier.
A=[(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
e=(0,3); f=(1,2)
G=A+[(6,0),(6,1),(6,2)]
assert is_3connected(7,G)
tot,one,two=state_counts(6,A)
se=one[A.index(e)]; sf=one[A.index(f)]; sef=two.get(tuple(sorted((A.index(e),A.index(f)))),[0]*5)
assert tot==[110,54,68,178,248]
assert se==[22,31,39,27,143]
assert sf==[0,0,0,110,122]
assert sef==[0,0,0,22,70]
dat=data(tot,se,sf,sef)
assert dat['F']==Q(7289,8) and dat['Fe']==Q(2649,8) and dat['Ff']==287 and dat['Fef']==103
assert (dat['q0'],dat['q1'],dat['q2'])==(Q(1187),Q(-5016),Q(0))
assert dat['N1']==Q(1747,2)
assert dat['r']==Q(55,7289)
assert dat['c']==Q(75968,53129521) and dat['cp']==0
assert dat['deltae']==Q(5956,36445) and dat['deltaf']==Q(2296,7289)
assert dat['B']==Q(427343,379840) and dat['B']>1
assert dat['R']==Q(4700773,17434656) and dat['R']<1
barrier_excess=dat['deltae']*dat['deltaf']-(32*dat['c']+dat['cp'])
assert barrier_excess==Q(1520096,265647605)>0

# Direct unit-forest check on G.
def pair_counts(n,edges,e,f):
    ei=edges.index(e); fi=edges.index(f)
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(edges)):
        if forest_state(n,edges,mask) is None: continue
        Z+=1; xe=(mask>>ei)&1; xf=(mask>>fi)&1
        Ze+=xe; Zf+=xf; Zef+=xe*xf
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef
Gcnt=pair_counts(7,G,e,f)
assert Gcnt==(3672,1330,1148,412,13976)
assert Gcnt[-1]==16*dat['N1']

# B. Complete small extremal census: every labeled A on 5 vertices whose unit 3-spoke apex extension is 3-connected.
allA=list(combinations(range(5),2))
num_A=0; num_pairs=0; neg_physical=0
bestB=(Q(-10),None); bestR=(Q(-10),None)
for mask in range(1<<len(allA)):
    E=[uv for i,uv in enumerate(allA) if (mask>>i)&1]
    GG=E+[(5,0),(5,1),(5,2)]
    if not is_3connected(6,GG): continue
    num_A+=1
    total,ones,twos=state_counts(5,E)
    for i,j in combinations(range(len(E)),2):
        num_pairs+=1
        dd=data(total,ones[i],ones[j],twos.get((i,j),[0]*5))
        if dd['N1']<0: neg_physical+=1
        if dd['B'] is not None and dd['B']>bestB[0]: bestB=(dd['B'],(tuple(E),i,j,dd))
        if dd['R'] is not None and dd['R']>bestR[0]: bestR=(dd['R'],(tuple(E),i,j,dd))
assert (num_A,num_pairs,neg_physical)==(82,2064,0)
assert bestB[0]==Q(49803,50416)
assert bestR[0]==Q(49803,197828)
assert bestB[1][0]==((0,1),(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(3,4))
assert (bestB[1][0][bestB[1][1]],bestB[1][0][bestB[1][2]])==((0,1),(2,3))

manifest={
  'claim':'P14-STAR-TILT-32-BARRIER-COUNTEREXAMPLE-59',
  'explicit_candidate':{
    'A_vertices':6,'A_edges':A,'apex':6,'apex_neighbors':[0,1,2],'tested_pair':[e,f],
    'state_total':tot,'state_e':se,'state_f':sf,'state_ef':sef,
    'F':qstr(dat['F']),'Fe':qstr(dat['Fe']),'Ff':qstr(dat['Ff']),'Fef':qstr(dat['Fef']),
    'q0':qstr(dat['q0']),'q1':qstr(dat['q1']),'q2':qstr(dat['q2']),
    'r':qstr(dat['r']),'c':qstr(dat['c']),'cprime':qstr(dat['cp']),
    'delta_e':qstr(dat['deltae']),'delta_f':qstr(dat['deltaf']),
    'barrier_ratio':qstr(dat['B']),'barrier_excess':qstr(barrier_excess),
    'physical_ratio':qstr(dat['R']),'physical_N1':qstr(dat['N1']),
    'G_counts':Gcnt,
  },
  'complete_nA5_star_apex_census':{
    'labeled_A_graphs_with_3connected_apex_extension':num_A,
    'present_edge_pairs':num_pairs,
    'negative_physical_gaps':neg_physical,
    'max_barrier_ratio':qstr(bestB[0]),
    'max_physical_ratio':qstr(bestR[0]),
    'maximizer_A_edges':bestB[1][0],
    'maximizer_pair':[bestB[1][0][bestB[1][1]],bestB[1][0][bestB[1][2]]],
  },
  'scope':'Route-kill plus restricted exact small census only; NOT a counterexample to Grimmett 4.2 and NOT complete n=10 coverage.'
}
canon=json.dumps(manifest,sort_keys=True,separators=(',',':'))
print(json.dumps(manifest,indent=2,sort_keys=True))
print('MANIFEST_SHA256',hashlib.sha256(canon.encode()).hexdigest())
print('ALL_EXACT_CHECKS_PASSED')
