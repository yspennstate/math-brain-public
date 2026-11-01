"""Exact C038 certificates. Standard library only; no optimizer required."""
from fractions import Fraction as F
from itertools import combinations
from collections import deque
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
E = tuple(range(6))
PAIRS = list(combinations(E, 2))
TRIPLES = list(combinations(E, 3))
EDGES = [(a,b) for a in PAIRS for b in PAIRS if not set(a)&set(b)]
MATCHING = ((0,1),(2,3),(4,5))

def det(a):
    a = [[F(z) for z in row] for row in a]
    result = F(1)
    for j in range(len(a)):
        k = next((k for k in range(j,len(a)) if a[k][j]), None)
        if k is None: return F(0)
        if k != j: a[j],a[k]=a[k],a[j];result=-result
        pivot=a[j][j];result*=pivot
        for k in range(j+1,len(a)):
            factor=a[k][j]/pivot
            for l in range(j+1,len(a)):a[k][l]-=factor*a[j][l]
    return result

def rank(a):
    a = [[F(z) for z in row] for row in a]
    i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        pivot=a[i][j]
        for k in range(i+1,len(a)):
            if not a[k][j]:continue
            factor=a[k][j]/pivot
            for l in range(j,len(a[0])):a[k][l]-=factor*a[i][l]
        i+=1
        if i==len(a):break
    return i

def cube(m, matching=MATCHING):
    if any(len(set(m)&set(p))!=1 for p in matching):return 0
    result=1
    for a,b in matching:result*=1 if a in m else -1
    return result

def edge_parts(a,b):
    j=tuple(i for i in E if i not in a and i not in b)
    return j, [tuple(sorted(a+(i,))) for i in j]

def laws_from_x(x):
    a={p:F(0) for p in PAIRS};h=dict(a);c=dict(a)
    g={m:F(0) for m in TRIPLES}
    for (aa,bb),v in x.items():
        jj,mm=edge_parts(aa,bb)
        a[aa]+=v;h[jj]+=v;c[bb]+=v
        for m in mm:g[m]+=v
    return a,h,c,g

def mass_table(d):
    return [{"set":list(k),"mass":str(v)} for k,v in sorted(d.items())]

def flow_table(d):
    return [{"left":list(a),"right":list(b),"mass":str(v)}
            for (a,b),v in sorted(d.items()) if v]

def check_flow(x,left,right,allowed):
    assert all(v>=0 and allowed(a,b) for (a,b),v in x.items())
    assert {a:sum(v for (aa,b),v in x.items() if aa==a) for a in left}==left
    assert {b:sum(v for (a,bb),v in x.items() if bb==b) for b in right}==right

def inclusion_flow(left,right):
    # Exact Edmonds--Karp on source/left/right/sink graph.
    ls=list(left);rs=list(right);n=2+len(ls)+len(rs);sink=n-1
    cap=[[F(0) for _ in range(n)] for _ in range(n)]
    adj=[[] for _ in range(n)]
    def arc(i,j,c):
        cap[i][j]=c;adj[i].append(j);adj[j].append(i)
    for i,a in enumerate(ls):arc(0,1+i,left[a])
    for j,b in enumerate(rs):arc(1+len(ls)+j,sink,right[b])
    for i,a in enumerate(ls):
        for j,b in enumerate(rs):
            if set(a)<=set(b):arc(1+i,1+len(ls)+j,F(2))
    sent=F(0)
    while True:
        prev=[None]*n;prev[0]=0;todo=deque([0])
        while todo and prev[sink] is None:
            i=todo.popleft()
            for j in adj[i]:
                if prev[j] is None and cap[i][j]>0:prev[j]=i;todo.append(j)
        if prev[sink] is None:break
        amount=F(2);j=sink
        while j:amount=min(amount,cap[prev[j]][j]);j=prev[j]
        j=sink
        while j:i=prev[j];cap[i][j]-=amount;cap[j][i]+=amount;j=i
        sent+=amount
    assert sent==sum(left.values())==sum(right.values())
    ans={(a,b):cap[1+len(ls)+j][1+i] for i,a in enumerate(ls) for j,b in enumerate(rs) if set(a)<=set(b)}
    check_flow(ans,left,right,lambda a,b:set(a)<=set(b))
    return ans

def projection_law(q,columns,sites=E):
    return {a:det([[q[i][j] for j in columns] for i in a])**2
            for a in combinations(sites,len(columns))}

# Exact dimensions and a unimodular harmonic basis.
P=[[0]*90 for _ in range(45)]
G=[[0]*90 for _ in range(20)]
D=[[0]*90 for _ in range(50)]
for k,(a,b) in enumerate(EDGES):
    j,ms=edge_parts(a,b)
    P[PAIRS.index(a)][k]=P[15+PAIRS.index(j)][k]=P[30+PAIRS.index(b)][k]=1
    D[PAIRS.index(a)][k]=D[35+PAIRS.index(b)][k]=1
    for m in ms:G[TRIPLES.index(m)][k]=D[15+TRIPLES.index(m)][k]=1
L=[[int(set(p)<=set(m)) for m in TRIPLES] for p in PAIRS]
bases=[((0,1),(2,3),(4,5)),((0,1),(2,4),(3,5)),
       ((0,2),(1,3),(4,5)),((0,2),(1,4),(3,5)),
       ((0,3),(1,4),(2,5))]
H=[[cube(m,b) for b in bases] for m in TRIPLES]
assert all(sum(L[i][k]*H[k][j] for k in range(20))==0 for i in range(15) for j in range(5))
minor_rows=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4)]
hminor=det([H[TRIPLES.index(m)] for m in minor_rows])
assert hminor==1
# Eight-atom trades give an integer right inverse for every harmonic cube.
for matching in bases:
    trade={edge:0 for edge in EDGES}
    aa,bb,cc=matching
    for s in range(2):
        for t in range(2):
            for v in range(2):
                bottom=tuple(sorted((aa[s],bb[t])))
                comp=tuple(sorted((aa[1-s],cc[v])))
                trade[bottom,comp]=-(-1)**(s+t+v)
    ta,th,tc,tg=laws_from_x(trade)
    assert all(z==0 for d in (ta,th,tc) for z in d.values())
    assert all(tg[m]==cube(m,matching) for m in TRIPLES)
ranks={"pair_color":rank(P),"full_diamond":rank(D),"pair_triple_inclusion":rank(L)}
assert ranks=={"pair_color":38,"full_diamond":43,"pair_triple_inclusion":15}
# Sharp cube inequality has all 90 pointwise costs in the asserted range.
for a,b in EDGES:
    j,ms=edge_parts(a,b);cost=sum(cube(m) for m in ms)
    assert cost==0 if j in MATCHING else abs(cost)<=1
assert sum(cube(m) for m in edge_parts((0,2),(3,5))[1])==1

# Counterexample family g_t: same pair-color marginals for every t.
a={p:F(1,15) for p in PAIRS};c=dict(a)
h={p:F(1,3) if p in MATCHING else F(0) for p in PAIRS}
x0={}
for aa,bb in EDGES:
    j,ms=edge_parts(aa,bb)
    x0[aa,bb]=F(0) if j not in MATCHING else F(1,30) if aa in MATCHING else F(1,15)
a0,h0,c0,g0=laws_from_x(x0)
assert (a0,h0,c0)==(a,h,c)
assert all(g0[m]==(F(1,5) if cube(m) else F(1,30)) for m in TRIPLES)
covers={}
for sign in (-1,1):
    t=F(sign,5);g={m:g0[m]+t*cube(m) for m in TRIPLES};nu={m:v/2 for m,v in g.items()}
    # Lower covers at the two extreme signs; intermediate ones are their mixtures.
    lower={}
    for aa in PAIRS:
        for m in TRIPLES:
            if not set(aa)<=set(m):continue
            v=F(1,60) if aa in MATCHING else F(1,15) if cube(m)==sign else F(0)
            if v:lower[aa,m]=v
    check_flow(lower,a,nu,lambda aa,m:set(aa)<=set(m))
    # Upper cover comes from complementing the opposite lower cover.
    upper={}
    for bb in PAIRS:
        for mc in TRIPLES:
            if not set(bb)<=set(mc):continue
            v=F(1,60) if bb in MATCHING else F(1,15) if cube(mc)==-sign else F(0)
            if v:
                m=tuple(i for i in E if i not in mc);tt=tuple(i for i in E if i not in bb)
                upper[m,tt]=v
    top={tuple(i for i in E if i not in bb):v for bb,v in c.items()}
    check_flow(upper,nu,top,lambda m,tt:set(m)<=set(tt))
    # Every claimed moment, the forced added-pair law, and strict dual failure.
    assert sum(g.values())==2
    for i in E:assert sum(v for m,v in g.items() if i in m)==1
    for p in PAIRS:
        assert a[p]+sum(v for bb,v in c.items() if not set(bb)&set(p))-sum(v for m,v in g.items() if set(p)<=set(m))==h[p]
    assert sum(cube(m)*g[m] for m in TRIPLES)==8*t
    covers[str(sign)]={"g":mass_table(g),"lower":flow_table(lower),"upper":flow_table(upper),"cube_moment":str(8*t)}

# An explicit full-support endpoint flag in the new missing-color boundary class.
nums=[
[3135,0,0,0,4180,0],[-960,3075,600,-3510,720,-1930],
[2480,1200,3675,1230,-1860,-1110],[-240,-3150,150,-355,180,-4140],
[780,2400,-3100,2460,-585,-2220],[3120,-850,-1950,-2700,-2340,525]]
Q=[[F(z,5225) for z in row] for row in nums]
assert all(sum(Q[k][i]*Q[k][j] for k in E)==int(i==j) for i in E for j in E)
assert Q[0][2]==Q[0][3]==0
sites=tuple(range(1,6));out={edge:F(0) for edge in EDGES}
rankone_certs=[]
for wcol,prob,included in [(1,F(9,25),True),(5,F(16,25),False)]:
    h5=projection_law(Q,(2,3),sites);top5=projection_law(Q,(wcol,2,3),sites)
    flow=inclusion_flow(h5,top5)
    for (j,t),v in flow.items():
        center=tuple(i for i in t if i not in j)
        if included:
            aa=tuple(sorted((0,)+center));bb=tuple(i for i in sites if i not in t)
        else:
            aa=tuple(i for i in sites if i not in t);bb=tuple(sorted((0,)+center))
        out[aa,bb]+=prob*v
    rankone_certs.append({"bottom_column":wcol,"probability":str(prob),"site_zero_in_bottom":included,"pair_to_triple_flow":flow_table(flow)})
aQ=projection_law(Q,(0,1));hQ=projection_law(Q,(2,3));cQ=projection_law(Q,(4,5))
gu=projection_law(Q,(0,1,2));gv=projection_law(Q,(0,1,3));gQ={m:gu[m]+gv[m] for m in TRIPLES}
assert laws_from_x(out)==(aQ,hQ,cQ,gQ)
assert sum(out.values())==1 and all(v>=0 for v in out.values())
assert all(v>0 for v in aQ.values()) and all(v>0 for v in cQ.values())
cert={"ranks":ranks,"harmonic_basis":bases,"harmonic_minor_rows":minor_rows,"harmonic_minor":str(hminor),
      "counterexample":{"matching":MATCHING,"a":mass_table(a),"h":mass_table(h),"c":mass_table(c),"g_zero":mass_table(g0),"three_pair_coupling":flow_table(x0),"endpoint_covers":covers},
      "boundary_flag":{"frame_denominator":5225,"frame_numerators":nums,"two_rankone_flows":rankone_certs,"diamond_weights":flow_table(out),"bottom":mass_table(aQ),"added_pair":mass_table(hQ),"complement_top":mass_table(cQ),"middle_sum":mass_table(gQ)}}
(HERE/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
summary={"status":"all_exact_checks_passed","ranks":ranks,"harmonic_basis_minor":str(hminor),"cube_edge_inequalities_checked":90,"counterexample_endpoint_cover_checks":4,"counterexample_dual_moments":["-8/5","8/5"],"boundary_flag_orthogonal":True,"boundary_diamond_positive_atoms":sum(v>0 for v in out.values()),"boundary_marginal_equations":50,"boundary_endpoint_supports":[15,15],"boundary_minimum_positive_weight":str(min(v for v in out.values() if v))}
(HERE/'verified_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
