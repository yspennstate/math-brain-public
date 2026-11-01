"""Exact audit of the exceptional four-twin arbitrary-core H2 formula.

Core forests are directly enumerated. Their components are then processed by
an independently implemented, four-terminal, full-partition transfer over
polynomials in lambda. Matrix-forest moments are evaluated by the same core
subset enumeration, not numerical eigenvalues.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json


def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,Q(0))+v
        if not r[k]:del r[k]
    return r

def times(p,q):
    r={}
    for k,v in p.items():
        for j,w in q.items():r[k+j]=r.get(k+j,Q(0))+v*w
    return {k:v for k,v in r.items() if v}

def canonical(p):
    lookup={};result=[]
    for x in p:
        if x not in lookup:lookup[x]=len(lookup)
        result.append(lookup[x])
    return tuple(result)

def star_polynomial(cs,initial):
    row={initial:{0:Q(1)}}
    for c in cs:
        out={}
        for state,poly in row.items():
            for mask in range(16):
                selected=[state[i] for i in range(4) if mask>>i&1]
                if len(set(selected))!=len(selected):continue
                if selected:
                    new=canonical([selected[0] if b in selected else b for b in state])
                else:new=state
                k=len(selected);mon={k:c**k}
                out[new]=add(out.get(new,{}),times(poly,mon))
        row=out
    result={}
    for poly in row.values():result=add(result,poly)
    return result

def determinant(matrix):
    matrix=[row[:] for row in matrix];n=len(matrix);value=Q(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if matrix[j][i]),None)
        if pivot is None:return Q(0)
        if pivot!=i:matrix[i],matrix[pivot]=matrix[pivot],matrix[i];value=-value
        x=matrix[i][i];value*=x
        for j in range(i+1,n):
            factor=matrix[j][i]/x
            for k in range(i+1,n):matrix[j][k]-=factor*matrix[i][k]
    return value

def adjugate_sos(a,edges):
    s=len(a);M=[[Q(0)for _ in a]for _ in a]
    for i,x in enumerate(a):M[i][i]=4*x
    for u,v,w in edges:
        M[u][u]+=w;M[v][v]+=w;M[u][v]-=w;M[v][u]-=w
    W=determinant(M);d=sum(a,Q(0));result=Q(0)
    for i in range(s):
        for j in range(s):
            # adj(M)_{ij} is cofactor(j,i), not cofactor(i,j).
            minor=[[M[u][v] for v in range(s)if v!=i]for u in range(s)if u!=j]
            adj=(-1)**(i+j)*determinant(minor)
            result+=a[i]*a[j]*(4*d*adj-W)**2/64
    return W,result

def audit(a,edges):
    s=len(a);groups={};moment=[Q(0)]*3;Wpoly={}
    for mask in range(1<<len(edges)):
        parent=list(range(s));wf=Q(1)
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        cyclic=False
        for k,(u,v,w) in enumerate(edges):
            if mask>>k&1:
                ru,rv=root(u),root(v)
                if ru==rv:cyclic=True;break
                parent[ru]=rv;wf*=w
        if cyclic:continue
        blocks={}
        for i in range(s):blocks[root(i)]=blocks.get(root(i),Q(0))+a[i]
        cs=tuple(sorted(blocks.values()));r=len(cs)
        groups[cs]=groups.get(cs,Q(0))+wf
        weight=wf*4**r
        for c in cs:weight*=c
        for j in range(3):moment[j]+=r**j*weight
        Wpoly[r]=Wpoly.get(r,Q(0))+weight
    polys=[]
    for initial in [(0,1,2,3),(0,0,1,2),(0,0,1,1)]:
        poly={}
        for cs,wf in groups.items():
            p=star_polynomial(cs,initial)
            shift=s-len(cs)
            poly=add(poly,{k+shift:wf*v for k,v in p.items()})
        polys.append(poly)
    A,B,D=polys;R=add(times(B,B),{k:-v for k,v in times(A,D).items()})
    H0=R.get(2*s+4,Q(0));H1=R.get(2*s+3,Q(0));H2=R.get(2*s+2,Q(0))
    W=moment[0];mean=moment[1]/W;var=moment[2]/W-mean**2
    d=sum(a,Q(0));predicted=d**2*W**2*(mean-1-var)/64
    assert H0==0 and H1==0,(H0,H1)
    assert H2==predicted,(H2,predicted)
    matrix_W,sos=adjugate_sos(a,edges)
    assert W==matrix_W,(W,matrix_W)
    assert H2==sos,(H2,sos)
    assert H2>0 if s>=2 else H2==0
    return {'s':s,'hub_spoke_weights':list(map(str,a)),
            'core_edges':[[u,v,str(w)] for u,v,w in edges],
            'rooted_core_polynomial':{str(k):str(v) for k,v in sorted(Wpoly.items())},
            'mean_components':str(mean),'variance_components':str(var),
            'H0':str(H0),'H1':str(H1),'H2':str(H2),'predicted_H2':str(predicted),'adjugate_sos_H2':str(sos),
            'R_coefficients':{str(k):str(v)for k,v in sorted(R.items())},
            'all_R_power_coefficients_nonnegative':all(v>=0 for v in R.values()),'passed':True}

def main():
    cases=[]
    for s in range(1,7):
        a=[Q(1)]*s
        cases.append((a,[]))
        if s>=2:cases.append((a,[(i,i+1,Q(1))for i in range(s-1)]))
        if s>=3:cases.append((a,[(u,v,Q(1))for u,v in combinations(range(s),2)]))
    cases += [([Q(1,2),Q(2,3),Q(3,4)],[(0,1,Q(5,7)),(1,2,Q(7,5))]),
              ([Q(1),Q(2),Q(3),Q(4)],[(0,1,Q(2)),(2,3,Q(3))]),
              ([Q(1),Q(2),Q(3),Q(4),Q(5)],[(u,v,Q(1+(u+v)%3))for u,v in combinations(range(5),2)])]
    reports=[]
    for a,edges in cases:
        result=audit(a,edges);reports.append(result)
        print('passed',len(a),len(edges),'H2',result['H2'],'all-coeff+',result['all_R_power_coefficients_nonnegative'],flush=True)
    Path(__file__).with_name('twin_core_high_fugacity_audit_results.json').write_text(json.dumps({'cases':reports,'all_passed':True},indent=2))
if __name__=='__main__':main()
