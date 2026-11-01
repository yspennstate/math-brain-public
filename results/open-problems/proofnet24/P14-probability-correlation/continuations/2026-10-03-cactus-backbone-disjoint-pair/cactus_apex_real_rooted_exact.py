"""Exact author checks for the unicyclic apex determinant-lift theorem.

Uses a rational square-weight version of the lift, literal forest sums, exact
polynomial determinants, and square-free Sturm layers.  Finite verification
is corroboration, not proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations,product
from math import gcd,isqrt
from pathlib import Path
from random import Random
import json

HERE=Path(__file__).resolve().parent

def merge(p,u,v):
    a,b=p[u],p[v]
    if a==b:return None
    return tuple(a if x==b else x for x in p)

def forests(n,edges):
    state={tuple(range(n)):F(1)}
    for u,v,w in edges:
        out=defaultdict(F)
        for p,z in state.items():
            out[p]+=z
            q=merge(p,u,v)
            if q is not None:out[q]+=w*z
        state=out
    return state

def apex(n,edges,beta):
    ans=[F(0)]*(sum(x>0 for x in beta)+1)
    for p,z in forests(n,edges).items():
        mass=defaultdict(F)
        for i,b in enumerate(beta):mass[p[i]]+=b
        P=[F(1)]
        for b in mass.values():
            if not b:continue
            Q=[F(0)]*(len(P)+1)
            for j,x in enumerate(P):Q[j]+=x;Q[j+1]+=b*x
            P=Q
        for j,x in enumerate(P):ans[j]+=z*x
    while len(ans)>1 and not ans[-1]:ans.pop()
    return ans

def apex_pointed(n,edges,beta,u):
    """Return (D,E_u), where E_u deletes the u-component spoke factor."""
    D=[F(0)]*(sum(x>0 for x in beta)+1);E=[F(0)]*max(1,sum(x>0 for x in beta))
    for p,z in forests(n,edges).items():
        mass=defaultdict(F)
        for i,b in enumerate(beta):mass[p[i]]+=b
        P=[F(1)];umass=mass[p[u]]
        for label,b in mass.items():
            if label==p[u] or not b:continue
            Q=[F(0)]*(len(P)+1)
            for j,x in enumerate(P):Q[j]+=x;Q[j+1]+=b*x
            P=Q
        Q=P+[F(0)]
        for j,x in enumerate(P):Q[j+1]+=umass*x
        for j,x in enumerate(Q):D[j]+=z*x
        for j,x in enumerate(P):E[j]+=z*x
    return trim(D),trim(E)

def padd(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def psub(a,b):
    return padd(a,[-x for x in b])

def det_poly(M):
    n=len(M);out=[F(0)]
    # Small matrices only; permutation expansion is deliberately independent.
    for perm in __import__('itertools').permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[F(-1 if inv%2 else 1)]
        for i,j in enumerate(perm):term=pmul(term,M[i][j])
        out=padd(out,term)
    while len(out)>1 and not out[-1]:out.pop()
    return out

def outer(q):return [[q[i]*q[j] for j in range(len(q))] for i in range(len(q))]

def lift(K,qs,u,w):
    # Checks use w=r^2 so sqrt(w/(1+w)) is rational after choosing
    # w=a^2/(b^2-a^2).  Test instances below use w=3/1 -> sqrt(3/4) not
    # rational, so represent vectors in Q(sqrt(3)) would be needless.  Scale
    # the last coordinate instead: congruence-equivalent rational lift
    # K'=diag(K,(1+w)^2), q_v=(sqrt(w(1+w))q_u,sqrt(1+w)).
    # We choose w=k^2/(1-k^2) with rational k in the generated cases.
    k2=w/(1+w);num=isqrt(k2.numerator);den=isqrt(k2.denominator)
    assert num*num==k2.numerator and den*den==k2.denominator
    k=F(num,den);d=len(K)
    K2=[row+[F(0)] for row in K]+[[F(0)]*d+[1+w]]
    qs2=[q+[F(0)] for q in qs]
    qs2.append([k*x for x in qs[u]]+[F(1)])
    return K2,qs2

def determinant_from_DR(K,qs,beta):
    d=len(K);B=[[F(0) for _ in range(d)] for _ in range(d)]
    for b,q in zip(beta,qs):
        for i in range(d):
            for j in range(d):B[i][j]+=b*q[i]*q[j]
    M=[[[K[i][j],B[i][j]] for j in range(d)] for i in range(d)]
    return det_poly(M)

def trim(p):
    p=p[:]
    while len(p)>1 and not p[-1]:p.pop()
    return p

def rem(a,b):
    a=list(map(F,a));b=list(map(F,b))
    while len(a)>=len(b) and any(a):
        z=a[-1]/b[-1];d=len(a)-len(b)
        for i,x in enumerate(b):a[d+i]-=z*x
        a=trim(a)
    return a

def primitive(p):
    den=1
    for x in p:den=den*x.denominator//gcd(den,x.denominator)
    z=[x.numerator*(den//x.denominator) for x in p];g=0
    for x in z:g=gcd(g,abs(x))
    if not g:return [F(0)]
    z=[F(x//g) for x in z]
    if z[-1]<0:z=[-x for x in z]
    return z

def real_roots_multiplicity(poly):
    p=list(map(F,poly));total=0
    while len(p)>1:
        seq=[p,[i*p[i] for i in range(1,len(p))]]
        while len(seq[-1])>1:
            r=primitive([-x for x in rem(seq[-2],seq[-1])])
            if not any(r):break
            seq.append(r)
        pos=[1 if x[-1]>0 else -1 for x in seq]
        neg=[z*(-1 if (len(x)-1)%2 else 1) for x,z in zip(seq,pos)]
        ch=lambda z:sum(x!=y for x,y in zip(z,z[1:]))
        total+=ch(neg)-ch(pos)
        if len(seq[-1])==1:break
        p=seq[-1]
    return total

def marked(n,edges,beta,rows,cond=None):
    cond=cond or {};N=n+4;state={(tuple(range(N)),0,0):F(1)}
    all_edges=[]
    for j,(u,v,w) in enumerate(edges):
        if cond.get(j)==0:continue
        all_edges.append((u,v,w,None,cond.get(j)==1))
    for r,a in enumerate(rows):
        for i,b in enumerate(beta):
            if a*b:all_edges.append((n+r,i,a*b,None,False))
    all_edges += [(n,n+1,F(1),0,False),(n+2,n+3,F(1),1,False)]
    for u,v,w,tag,forced in all_edges:
        out=defaultdict(F)
        for (p,a,b),z in state.items():
            if not forced:out[p,a,b]+=z
            q=merge(p,u,v)
            if q is None:continue
            aa,bb=a,b
            if tag==0:aa=1
            if tag==1:bb=1
            out[q,aa,bb]+=z*w
        state=out
    ans={(0,0):F(0),(1,0):F(0),(0,1):F(0),(1,1):F(0)}
    for (_,a,b),z in state.items():ans[a,b]+=z
    return ans

def main():
    # Start from an isolated vertex DR: D=1+s beta.
    allowed=[F(1,3),F(3,5),F(4,5)] # w=k^2/(1-k^2): 1/8,9/16,16/9
    allowed=[k*k/(1-k*k) for k in allowed]
    rng=Random(310032027);records=[]
    for trial in range(24):
        # Build a tree solely by leaf lifts; this directly audits the lemma.
        n=1;edges=[];K=[[F(1)]];qs=[[F(1)]]
        for _ in range(rng.randrange(1,6)):
            u=rng.randrange(n);w=rng.choice(allowed)
            edges.append((u,n,w));K,qs=lift(K,qs,u,w);n+=1
        beta=[F(rng.choice([1,2,3,5]),rng.choice([1,2,3])) for _ in range(n)]
        literal=apex(n,edges,beta);determinant=determinant_from_DR(K,qs,beta)
        # Every leaf lift multiplies c by no factor: K' contains 1+w and
        # determinant formula already matches (1+w) in the recurrence.
        assert literal==determinant,(edges,beta,literal,determinant)
        count=real_roots_multiplicity(literal);assert count==len(literal)-1
        records.append({'kind':'tree-lift','vertices':n,'edges':[(u,v,str(w)) for u,v,w in edges],
          'profile':list(map(str,beta)),'coefficients':list(map(str,literal)),'root_count':count})

    # Literal unicyclic stress cases audit the theorem independently of a
    # cycle-K construction: exact Sturm counts plus full marked graphs.
    unicyclic=[];marked_records=[]
    for ncycle in range(3,7):
        for trial in range(6):
            n=ncycle;edges=[(i,(i+1)%ncycle,F(rng.randrange(1,6),rng.randrange(1,4))) for i in range(ncycle)]
            for _ in range(trial%4):
                u=rng.randrange(n);edges.append((u,n,rng.choice(allowed)));n+=1
            beta=[F(rng.choice([0,1,1,2,3]),rng.choice([1,2])) for _ in range(n)]
            if not any(beta):beta[0]=F(1)
            P=apex(n,edges,beta);count=real_roots_multiplicity(P)
            assert count==len(P)-1,(edges,beta,P,count)
            unicyclic.append({'cycle':ncycle,'vertices':n,'degree':len(P)-1,'root_count':count,
              'edges':[(u,v,str(w)) for u,v,w in edges],'profile':list(map(str,beta)),
              'coefficients':list(map(str,P))})
            if trial<2:
                rows=(F(1),F(2),F(3),F(4));A=marked(n,edges,beta,rows)
                delta=A[1,0]*A[0,1]-A[0,0]*A[1,1]
                strict=sum(x>0 for x in beta)>=2;assert (delta>0)==strict
                marked_records.append({'cycle':ncycle,'vertices':n,'EF_minus_AC':str(delta),'strict':strict})

    # Disconnected pseudoforests with two cyclic components: factorization
    # and exact roots.  One sparse-profile case also gets a literal marked
    # graph check.
    pseudoforest=[]
    for trial in range(8):
        edges=[(0,1,F(1+trial%3)),(1,2,F(2)),(2,0,F(3)),
               (3,4,F(2)),(4,5,F(3+trial%2)),(5,3,F(1))]
        if trial%2:edges.append((trial%3,6,F(4,3)))
        n=7 if trial%2 else 6
        beta=[F(rng.choice([0,1,2,3])) for _ in range(n)]
        if not any(beta):beta[0]=F(1)
        P=apex(n,edges,beta);count=real_roots_multiplicity(P)
        assert count==len(P)-1,(edges,beta,P,count)
        pseudoforest.append({'vertices':n,'degree':len(P)-1,'root_count':count,
          'profile':list(map(str,beta)),'coefficients':list(map(str,P))})
    sparse=[F(1),F(0),F(0),F(2),F(0),F(0)]
    two_cycles=[(0,1,F(1)),(1,2,F(2)),(2,0,F(3)),
                (3,4,F(2)),(4,5,F(3)),(5,3,F(1))]
    A=marked(6,two_cycles,sparse,(F(1),F(2),F(3),F(4)))
    delta=A[1,0]*A[0,1]-A[0,0]*A[1,1]
    assert delta>0
    marked_records.append({'kind':'two-cycle-pseudoforest','vertices':6,
                           'EF_minus_AC':str(delta),'strict':True})

    # Exact one-vertex-sum component formula on independently enumerated
    # sides, including a nontrivial profile split at the articulation.
    gluing=[]
    for trial in range(12):
        e1=[(0,1,F(1+trial%3)),(1,2,F(2)),(2,0,F(3))]
        e2=[(0,1,F(2)),(1,2,F(1+trial%2)),(2,0,F(4))]
        b1=[F(1+trial%2),F(2),F(3)];b2=[F(2),F(1),F(2+trial%3)]
        D1,E1=apex_pointed(3,e1,b1,0);D2,E2=apex_pointed(3,e2,b2,0)
        joined=e1+[(0,3,w) if (u,v)==(0,1) else
                   (3,4,w) if (u,v)==(1,2) else (4,0,w)
                   for u,v,w in e2]
        beta=[b1[0]+b2[0],b1[1],b1[2],b2[1],b2[2]]
        literal=apex(5,joined,beta)
        formula=psub(padd(pmul(D1,E2),pmul(E1,D2)),pmul(E1,E2))
        assert literal==formula,(trial,literal,formula)
        gluing.append({'trial':trial,'literal_coefficients':list(map(str,literal)),
                       'formula_coefficients':list(map(str,formula))})

    # Genuine connected cacti with multiple cycles sharing articulation
    # vertices. These are beyond the pseudoforest checkpoint.
    cactus=[]
    cactus_graphs=[
      (5,[(0,1,F(1)),(1,2,F(2)),(2,0,F(3)),
          (0,3,F(2)),(3,4,F(1)),(4,0,F(4))]),
      (7,[(0,1,F(2)),(1,2,F(1)),(2,0,F(3)),(2,3,F(5,2)),
          (3,4,F(1)),(4,5,F(2)),(5,3,F(3)),(5,6,F(4,3))]),
      (8,[(0,1,F(1)),(1,2,F(2)),(2,0,F(1)),(0,3,F(3)),
          (3,4,F(2)),(4,5,F(1)),(5,3,F(2)),
          (4,6,F(1)),(6,7,F(3)),(7,4,F(2))]),
    ]
    for n,edges in cactus_graphs:
        for trial in range(4):
            beta=[F(rng.choice([0,1,1,2,3]),rng.choice([1,2])) for _ in range(n)]
            if not any(beta):beta[0]=F(1)
            P=apex(n,edges,beta);count=real_roots_multiplicity(P)
            assert count==len(P)-1,(edges,beta,P,count)
            cactus.append({'vertices':n,'degree':len(P)-1,'root_count':count,
              'profile':list(map(str,beta)),'coefficients':list(map(str,P))})
    sparse=[F(1),F(0),F(0),F(2),F(0)]
    A=marked(5,cactus_graphs[0][1],sparse,(F(1),F(2),F(3),F(4)))
    delta=A[1,0]*A[0,1]-A[0,0]*A[1,1]
    assert delta>0
    marked_records.append({'kind':'figure-eight-cactus','vertices':5,
                           'EF_minus_AC':str(delta),'strict':True})

    # Exhaust all 3^4 conditionings of a triangle with one leaf.
    edges=[(0,1,F(2)),(1,2,F(3)),(2,0,F(5)),(1,3,F(7,9))]
    beta=[F(1),F(2),F(3),F(4)];rows=(F(1),F(2),F(3),F(4));conditioned=0;zero_conditionings=0
    for code in range(3**4):
        z=code;cond={}
        for j in range(4):
            d=z%3;z//=3
            if d<2:cond[j]=d
        A=marked(4,edges,beta,rows,cond)
        if not sum(A.values()):
            zero_conditionings+=1
            continue
        delta=A[1,0]*A[0,1]-A[0,0]*A[1,1]
        assert delta>=0,(code,cond,delta);conditioned+=1
    out={'status':'PASS determinant leaf lifts, exact one-vertex gluing, literal cactus Sturm counts, full marked graphs, exhaustive conditioning',
      'tree_lift_cases':len(records),'unicyclic_cases':len(unicyclic),
      'pseudoforest_cases':len(pseudoforest),'cactus_cases':len(cactus),
      'one_vertex_gluing_cases':len(gluing),
      'marked_cases':len(marked_records),
      'positive_probability_conditioned_cases':conditioned,
      'zero_probability_conditionings_skipped':zero_conditionings,
      'tree_lift_records':records,'unicyclic_records':unicyclic,
      'pseudoforest_records':pseudoforest,'cactus_records':cactus,
      'one_vertex_gluing_records':gluing,'marked_records':marked_records}
    (HERE/'unicyclic_apex_real_rooted_exact_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if not k.endswith('records')})

if __name__=='__main__':main()
