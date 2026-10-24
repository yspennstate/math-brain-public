"""Literal exact checks for the three-port ordinary-forest Hessian lemma.

This checks every unweighted simple backbone on at most six vertices using
a subset zeta transform, and weighted/conditioned multigraphs by a separate
connectivity DP.  No transfer operator, matroid theorem, or assumed Rayleigh
inequality is used to calculate the forest partition coefficients.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import random

PARTS=((0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0))
BS=((1,1,1),(1,2,3),(7,2,11),(1,1,0),(0,1,0),(1,0,3))

def merge(p,u,v):
    a,b=p[u],p[v]
    if a==b:return None
    a,b=min(a,b),max(a,b)
    return tuple(a if x==b else x for x in p)

def portpart(p):
    seen={};out=[]
    for i in range(3):
        if p[i] not in seen:seen[p[i]]=len(seen)
        out.append(seen[p[i]])
    return tuple(out)

def psd(c):
    # For a real symmetric 3x3 matrix, all principal minors >=0 are equivalent
    # to PSD. All calculations here are exact Python integers/rationals.
    assert all(c[i][i]>=0 for i in range(3))
    assert all(c[i][i]*c[j][j]-c[i][j]**2>=0 for i,j in combinations(range(3),2))
    a,b,d=c[0][0],c[1][1],c[2][2]
    x,y,z=c[0][1],c[0][2],c[1][2]
    determinant=a*b*d+2*x*y*z-a*z*z-b*y*y-d*x*x
    assert determinant>=0
    return determinant

def verify_row(v,N):
    r,p12,p13,p23,c=v
    F=sum(v)
    assert F>0 and N>=3
    A=(r+p13+p23,r+p12+p23,r+p12+p13)
    weak=[[A[i]*A[j]-(r*F if i!=j else 0) for j in range(3)] for i in range(3)]
    strong=[[(N-1)*A[i]*A[j]-(N*r*F if i!=j else 0) for j in range(3)] for i in range(3)]
    psd(weak);psd(strong)
    for b1,b2,b3 in BS:
        B=b1+b2+b3
        M=A[0]*b1*b2+A[1]*b1*b3+A[2]*b2*b3
        J=r*b1*b2*b3
        D=M*M-2*B*J*F
        assert N*D>=M*M
        assert D>=0 and (M==0 or D>0)
        assert B*M>=9*J
    return F,A

def all_simple_graphs(n):
    edges=list(combinations(range(n),2));m=len(edges);size=1<<m
    v=[[0]*size for _ in range(5)]
    forest_count=0
    for mask in range(size):
        p=tuple(range(n));z=mask;valid=True
        while z:
            bit=z&-z;i=bit.bit_length()-1;z-=bit
            p=merge(p,*edges[i])
            if p is None:valid=False;break
        if valid:
            v[PARTS.index(portpart(p))][mask]=1;forest_count+=1
    # Every graph G receives exactly its contained acyclic edge subsets.
    for bit in range(m):
        step=1<<bit
        for a in v:
            for start in range(0,size,2*step):
                for j in range(start+step,start+2*step):a[j]+=a[j-step]
    for mask in range(size):verify_row(tuple(a[mask] for a in v),mask.bit_count()+3)
    return {'vertices':n,'simple_backbones':size,'complete_graph_forest_count':forest_count,
            'all_weak_and_degree_sharpened_matrix_checks':'PASS'}

def forest_dp(n,edges):
    # edges: (u,v,activity,required-state,mark), mark -1 for backbone.
    states={(tuple(range(n)),0):1}
    for u,v,w,required,mark in edges:
        nxt=defaultdict(int)
        for (p,mask),value in states.items():
            if required!='present':nxt[p,mask]+=value
            if required!='absent':
                q=merge(p,u,v)
                if q is not None:nxt[q,mask if mark<0 else mask|(1<<mark)]+=value*w
        states=dict(nxt)
    return states

def literal_case(n,edges,name):
    base=forest_dp(n,edges)
    v=[0]*5
    for (p,mask),w in base.items():assert mask==0;v[PARTS.index(portpart(p))]+=w
    # Contract/delete conditioned backbone edges when counting homogeneous
    # ground-set degree. Loops may remain and do not affect validity.
    required=sum(e[3]=='present' for e in edges)
    absent=sum(e[3]=='absent' for e in edges)
    N=len(edges)-required-absent+3
    F,A=verify_row(v,N)
    augmented=forest_dp(n,edges+[(0,1,1,'free',0),(0,2,1,'free',1),(1,2,1,'free',2)])
    coefficients=[0]*8
    for (p,mask),w in augmented.items():coefficients[mask]+=w
    expected=[F,A[0],A[1],v[0],A[2],v[0],v[0],0]
    assert coefficients==expected
    return {'name':name,'vertices':n,'backbone_edges':len(edges),'port_partition_weights':v,
            'augmented_triangle_coefficients':coefficients,'homogeneous_degree':N,'status':'PASS'}

def weighted_cases():
    out=[]
    out.append(literal_case(3,[],'empty backbone'))
    out.append(literal_case(4,[(0,3,2,'free',-1),(1,3,3,'free',-1),(2,3,5,'free',-1)],'weighted hidden Steiner star'))
    out.append(literal_case(4,[(0,1,7,'free',-1),(0,1,11,'free',-1),(1,3,3,'free',-1),
                               (2,3,5,'free',-1),(0,2,13,'free',-1),(3,3,17,'free',-1)],'parallel edges and loop'))
    out.append(literal_case(4,[(0,1,2,'present',-1),(1,3,3,'free',-1),(2,3,5,'free',-1),
                               (0,2,7,'absent',-1),(1,2,11,'free',-1)],'conditioning identifies two ports'))
    out.append(literal_case(5,[(0,3,2,'present',-1),(1,3,3,'present',-1),(2,3,5,'present',-1),
                               (3,4,7,'free',-1),(0,4,11,'free',-1)],'conditioning identifies all ports'))
    rng=random.Random(261002031)
    for trial in range(100):
        n=rng.randrange(3,8);all_edges=list(combinations(range(n),2));rng.shuffle(all_edges)
        chosen=all_edges[:rng.randrange(min(len(all_edges),12)+1)]
        edges=[];required_state=tuple(range(n))
        for u,v in chosen:
            required='free'
            draw=rng.randrange(8)
            if draw==0:
                q=merge(required_state,u,v)
                if q is not None:required='present';required_state=q
            elif draw==1:required='absent'
            edges.append((u,v,rng.randrange(1,12),required,-1))
        out.append(literal_case(n,edges,f'weighted conditioned random multigraph {trial}'))
    # Include rational fields, independently of the integer test family.
    out.append(literal_case(5,[(0,1,Fraction(2,3),'free',-1),(0,3,Fraction(3,7),'free',-1),
                               (1,3,Fraction(5,11),'free',-1),(2,3,Fraction(7,13),'free',-1),
                               (2,4,Fraction(11,17),'free',-1),(3,4,Fraction(13,19),'free',-1)],'rational fields'))
    return out

def main():
    simple=[all_simple_graphs(n) for n in range(3,7)]
    weighted=weighted_cases()
    # A formal nonnegative frontier row which cannot arise from the weighted
    # forest model: this demonstrates why arbitrary-row positivity is false.
    formal=(1,0,0,0,1);F=sum(formal);B=3;M=3;J=1
    assert M*M-2*B*J*F==-3
    c=[[1-(2 if i!=j else 0) for j in range(3)] for i in range(3)]
    assert sum(sum(row) for row in c)==-3
    out={'status':'PASS exact literal-backbone Hessian verification',
         'simple_graph_sweeps':simple,'total_unweighted_simple_backbones':sum(x['simple_backbones'] for x in simple),
         'column_profiles':BS,'weighted_conditioned_cases':weighted,
         'formal_row_obstruction':{'row':formal,'F':F,'B':B,'M':M,'J':J,'cone_gap':-3,
                                    'matrix_all_ones_quadratic_form':-3}}
    path=Path(__file__).with_name('forest_three_port_hessian_lemma_k_exact_results.json')
    path.write_text(json.dumps(out,indent=2,default=str)+'\n')
    print(json.dumps({'status':out['status'],'unweighted_backbones':out['total_unweighted_simple_backbones'],
                      'weighted_conditioned_cases':len(weighted),'formal_row_gap':-3},indent=2))

if __name__=='__main__':main()
