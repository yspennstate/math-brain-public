"""Independent full-forest check of proposed global H2 boundary Gram formula.

Uses no Grassmann algebra. Forest coefficients come from acyclic full-edge
subsets and marked-edge insertion tests. Formula uses separately solved exact
Laplacian, harmonic exit rows and boundary projected cycle-flow matrices.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from four_twins_full_graph_audit_heat import mul,inv_det


def mm(A,B):
    return [[sum((A[i][k]*B[k][j]for k in range(len(B))),F(0))
             for j in range(len(B[0]))]for i in range(len(A))]


def forest_R(n,edges,e,f):
    parent=list(range(n));size=[1]*n;polys=[{}for _ in range(4)]
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    def visit(i,k,weight):
        if i==len(edges):
            a,b,c,d=map(root,e+f);ee=a!=b;ff=c!=d
            for p,ok in zip(polys,[True,ee,ff,ee and ff and {a,b}!={c,d}]):
                if ok:p[k]=p.get(k,F(0))+weight
            return
        visit(i+1,k,weight)
        x,y,w=edges[i];rx,ry=root(x),root(y)
        if rx==ry:return
        if size[rx]<size[ry]:rx,ry=ry,rx
        old=size[rx];size[rx]+=size[ry];parent[ry]=rx
        visit(i+1,k+1,weight*w)
        size[rx]=old;parent[ry]=ry
    visit(0,0,F(1));A,B,C,D=polys;R=mul(B,C)
    for k,v in mul(A,D).items():R[k]=R.get(k,F(0))-v
    return {k:v for k,v in sorted(R.items())if v}


def global_formula(n,unmarked,e,f,root,marked_weights=(F(1),F(1))):
    edges=unmarked+[(e[0],e[1],marked_weights[0]),(f[0],f[1],marked_weights[1])]
    L=[[F(0)for _ in range(n)]for _ in range(n)]
    for x,y,w in edges:
        L[x][x]+=w;L[y][y]+=w;L[x][y]-=w;L[y][x]-=w
    nonroot=[x for x in range(n)if x!=root]
    Gsmall,tau=inv_det([[L[x][y]for y in nonroot]for x in nonroot])
    G=[[F(0)for _ in range(n)]for _ in range(n)]
    for i,x in enumerate(nonroot):
        for j,y in enumerate(nonroot):G[x][y]=Gsmall[i][j]
    v=[G[x][e[0]]-G[x][e[1]]for x in range(n)]
    w=[G[x][f[0]]-G[x][f[1]]for x in range(n)]
    assert v[f[0]]==v[f[1]]==w[e[0]]==w[e[1]]==0
    assert all(not(v[x]and w[x])for x in range(n))
    assert all(v[x]*w[y]==v[y]*w[x]for x,y,c in edges)
    S=[x for x in range(n)if v[x]==w[x]==0];assert root in S
    boundary=[x for x in S if x!=root];interior=[x for x in range(n)if x not in S]
    if not boundary:return F(0),tau,{'boundary':S,'active_e':[x for x in range(n)if v[x]],'active_f':[x for x in range(n)if w[x]]}
    K=[[L[x][y]for y in interior]for x in interior];Kinv,_=inv_det(K)
    p=[[F(0)for _ in boundary]for _ in range(n)]
    for j,x in enumerate(boundary):p[x][j]=1
    inside=mm(Kinv,[[-L[x][y]for y in boundary]for x in interior])
    for i,x in enumerate(interior):p[x]=inside[i]
    def B(current,pair):
        pi=p[pair[0]];assert pi==p[pair[1]]
        out=[[F(0)for _ in boundary]for _ in boundary]
        for x,y,c in edges:
            eta=[current[x]*p[y][i]-current[y]*p[x][i]-(current[x]-current[y])*pi[i]for i in range(len(boundary))]
            for i in range(len(boundary)):
                for j in range(len(boundary)):out[i][j]+=c*eta[i]*eta[j]
        return out
    Be=B(v,e);Bf=B(w,f);T=[[G[x][y]for y in boundary]for x in boundary]
    C=mm(mm(mm(T,Be),T),Bf);value=tau*tau*sum((C[i][i]for i in range(len(boundary))),F(0))
    return value,tau,{'boundary':S,'active_e':[x for x in range(n)if v[x]],'active_f':[x for x in range(n)if w[x]],'Be':[[str(c)for c in row]for row in Be],'Bf':[[str(c)for c in row]for row in Bf]}


def main():
    cases=[]
    # Four-node mirrored branches on side e; plain pair twins on side f.
    edges=[(2,4,2),(3,5,2),(4,0,1),(4,1,2),(5,0,1),(5,1,2),
           (6,0,1),(6,1,3),(7,0,1),(7,1,3),(0,1,4)]
    cases.append(('mirror_path_two_boundary',8,edges,(2,3),(6,7)))
    cases.append(('mirror_path_with_rung',8,edges+[(4,5,9)],(2,3),(6,7)))
    # One side attaches to only one interface point; should have H2=0.
    cases.append(('one_point_attachment',8,[x for x in edges if x[:2]not in[(4,1),(5,1)]],(2,3),(6,7)))
    # Two separate four-node mirrored branches and three boundary vertices.
    edges2=[(3,5,2),(4,6,2),(5,0,1),(5,1,2),(5,2,3),(6,0,1),(6,1,2),(6,2,3),
            (7,9,4),(8,10,4),(9,0,3),(9,1,1),(10,0,3),(10,1,1),(0,1,5),(1,2,2)]
    cases.append(('two_mirror_paths_three_boundary',11,edges2,(3,4),(7,8)))
    # Active e side has six vertices; different positive side branches use
    # disjoint boundary neighborhoods, so exit rows need not coincide inside.
    edges3=[(2,4,2),(2,6,5),(3,5,2),(3,7,5),(4,0,3),(5,0,3),(6,1,7),(7,1,7),
            (8,0,1),(8,1,4),(9,0,1),(9,1,4),(0,1,2)]
    cases.append(('unequal_mirror_branches_zero_spokes',10,edges3,(2,3),(8,9)))
    # An endpoint may itself lie in S. Its whole side then exits through that
    # boundary point, and the cycle-flow boundary Gram matrix is zero.
    cases.append(('one_endpoint_in_S',6,
                  [(0,3,2),(3,2,3),(4,0,1),(4,1,3),(5,0,1),(5,1,3),(0,1,4)],
                  (0,2),(4,5)))
    # Adjacent marked edges also satisfy the formula in the independence
    # equality geometry; the common vertex is the entire boundary.
    cases.append(('shared_marked_endpoint',5,
                  [(0,2,2),(2,1,3),(0,4,5),(4,3,7)],(0,1),(0,3)))
    out=[]
    for name,n,raw,e,f in cases:
        unmarked=[(x,y,F(c))for x,y,c in raw]
        R=forest_R(n,unmarked,e,f);value,tau,structure=global_formula(n,unmarked,e,f,0)
        assert R.get(2*n-4,F(0))==R.get(2*n-5,F(0))==0
        assert R.get(2*n-6,F(0))==value,(name,R.get(2*n-6),value)
        for weight in [(F(2),F(3)),(F(1,2),F(7,5))]:
            again,_,_=global_formula(n,unmarked,e,f,0,weight);assert again==value
        for root in structure['boundary']:
            again,_,_=global_formula(n,unmarked,e,f,root);assert again==value
        out.append({'name':name,'n':n,'unmarked_edges':[(x,y,str(c))for x,y,c in unmarked],
                    'e':e,'f':f,'H2':str(value),'tau_at_marked_weights_one':str(tau),
                    'R_coefficients':{str(k):str(c)for k,c in R.items()},'structure':structure,
                    'all_roots_and_marked_weights_agree':True,'passed':True})
        print('global non-twin passed',name,'H2',value,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'arithmetic':'Fraction exact','all_passed':True,'cases':out},indent=2))


if __name__=='__main__':main()
