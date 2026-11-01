from fractions import Fraction
from itertools import combinations

def forest_eval(n, edges, weights, marks=(), terminals=None):
    m=len(edges)
    Z=Fraction(0)
    d1={i:Fraction(0) for i in marks}
    d2={}
    for i,j in combinations(sorted(marks),2):
        d2[(i,j)]=Fraction(0)
    D=C=Fraction(0)
    DC1={i:[Fraction(0),Fraction(0)] for i in marks}  # [D_i,C_i]
    for mask in range(1<<m):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        ok=True
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    ok=False
                    break
                parent[ru]=rv
        if not ok:
            continue
        wt=Fraction(1)
        for i,w in enumerate(weights):
            if (mask>>i)&1:
                wt*=w
        Z+=wt
        conn=None
        if terminals is not None:
            conn=(find(terminals[0])==find(terminals[1]))
            if conn: C+=wt
            else: D+=wt
        for i in marks:
            if (mask>>i)&1:
                der=wt/weights[i]
                d1[i]+=der
                if terminals is not None:
                    DC1[i][1 if conn else 0]+=der
        for i,j in combinations(sorted(marks),2):
            if (mask>>i)&1 and (mask>>j)&1:
                d2[(i,j)]+=wt/(weights[i]*weights[j])
    return Z,d1,d2,D,C,DC1

def delta(n, edges, weights, i, j):
    Z,d1,d2,_,_,_=forest_eval(n,edges,weights,(i,j))
    return d1[i]*d1[j]-Z*d2[(min(i,j),max(i,j))]

def theta_formula(k,L):
    d=2**L-1
    D=d**k
    C=k*d**(k-1)
    S=(2**(L-1))*d**(2*k-2)
    return Fraction(D),Fraction(C),Fraction(S)

def build_theta_substitution(base_n, base_edges, specs):
    edges=[]
    marks=[]
    nextv=base_n
    locals_=[]
    for (u,v),(k,L) in zip(base_edges,specs):
        first=None
        for p in range(k):
            prev=u
            for s in range(L-1):
                w=nextv
                nextv+=1
                edges.append((prev,w))
                if first is None:
                    first=len(edges)-1
                prev=w
            edges.append((prev,v))
            if first is None:
                first=len(edges)-1
        marks.append(first)
        locals_.append(theta_formula(k,L))
    return nextv,edges,marks,locals_

# A. Exact theta formulas against enumeration for four small networks.
for k,L in [(1,2),(2,2),(1,3),(2,3)]:
    edges=[]
    nextv=2
    mark=None
    for p in range(k):
        prev=0
        for s in range(L-1):
            w=nextv; nextv+=1
            edges.append((prev,w))
            if mark is None: mark=len(edges)-1
            prev=w
        edges.append((prev,1))
    Z,d1,d2,D,C,DC1=forest_eval(nextv,edges,[Fraction(1)]*len(edges),(mark,),terminals=(0,1))
    De,Ce=DC1[mark]
    S=D*Ce-C*De
    assert (D,C,S)==theta_formula(k,L)
print("PASS theta_response_formula cases=4")

# B. Simultaneous substitution factorization on a base triangle.
base_edges=[(0,1),(1,2),(0,2)]
specs=[(2,2),(1,3),(2,3)]
N,H_edges,marks,local=build_theta_substitution(3,base_edges,specs)
ratios=[C/D for D,C,S in local]
base_delta=delta(3,base_edges,ratios,0,1)
lhs=delta(N,H_edges,[Fraction(1)]*len(H_edges),marks[0],marks[1])
K=Fraction(1)
for D,C,S in local:
    K*=D
rhs=K*K*(local[0][2]/local[0][0]**2)*(local[1][2]/local[1][0]**2)*base_delta
assert ratios==[Fraction(2,3),Fraction(1,7),Fraction(2,7)]
assert base_delta==Fraction(18,49)
assert lhs==rhs==Fraction(63504)
print("PASS simultaneous_substitution_factorization delta=63504 base_delta=18/49")

# C. Weighted two-separator gluing, including a singleton uv edge.
n=5
edges=[(0,2),(2,1),(0,3),(3,4),(4,1),(0,1)]
weights=[Fraction(2),Fraction(3),Fraction(5,2),Fraction(7,3),Fraction(4),Fraction(3,2)]
# state sums for three bridges
def bridge(indices, mark_local=None):
    es=[edges[i] for i in indices]
    ws=[weights[i] for i in indices]
    marks=() if mark_local is None else (mark_local,)
    return forest_eval(n,es,ws,marks,terminals=(0,1))
b1=bridge([0,1],0)
b2=bridge([2,3,4],0)
b3=bridge([5],0)
D1,C1=b1[3],b1[4]
D2,C2=b2[3],b2[4]
D3,C3=b3[3],b3[4]
assert (D1,C1,D2,C2,D3,C3)==(6,6,35,Fraction(70,3),1,Fraction(3,2))

# same-bridge marks original edges 2 and 3
lam=C1/D1+C3/D3
aug_edges=[edges[i] for i in [2,3,4]]+[(0,1)]
aug_weights=[weights[i] for i in [2,3,4]]+[lam]
lhs_same=delta(n,edges,weights,2,3)
delta_aug=delta(n,aug_edges,aug_weights,0,1)
rhs_same=(D1*D3)**2*delta_aug
assert lam==Fraction(5,2)
assert (lhs_same,delta_aug,rhs_same)==(6300,175,6300)
print("PASS two_cut_same_bridge lambda=5/2 delta=6300")

# cross-bridge marks original edges 0 and 2
De1,Ce1=b1[5][0]
De2,Ce2=b2[5][0]
R1=D1*Ce1-C1*De1
R2=D2*Ce2-C2*De2
lhs_cross=delta(n,edges,weights,0,2)
rhs_cross=D3**2*R1*R2
assert (R1,R2)==(12,Fraction(1400,9))
assert lhs_cross==rhs_cross==Fraction(5600,3)
print("PASS two_cut_cross_bridge R1=12 R2=1400/9 delta=5600/3")
print("ALL_EXACT_CHECKS_PASS")
