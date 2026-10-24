"""Finite exact polynomial certificate for adjacent terminal forest edges.

This is a symbolic identity and sign certificate, not evaluation on a grid.
No third-party algebra package is used. Variables, in order:
a,b,c,b1,b2,b3,p,q,r,U,Gamma. The complete polynomial has positive integer
coefficients. See the separate derivation for the reduction to this one
finite polynomial for arbitrary background terminal graphs.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

N=11
NAMES=('a','b','c','b1','b2','b3','p','q','r','U','Gamma')
def constant(v): return {(0,)*N:v} if v else {}
def variable(i):
    key=[0]*N;key[i]=1
    return {tuple(key):1}
def add(*polys):
    result=defaultdict(int)
    for poly in polys:
        for key,value in poly.items(): result[key]+=value
    return {key:value for key,value in result.items() if value}
def scale(poly,c): return {key:value*c for key,value in poly.items() if value*c}
def multiply(*polys):
    result=constant(1)
    for poly in polys:
        following=defaultdict(int)
        for key,value in result.items():
            for other,coefficient in poly.items():
                following[tuple(x+y for x,y in zip(key,other))]+=value*coefficient
        result={key:value for key,value in following.items() if value}
    return result
def power(poly,n): return multiply(*([poly]*n))
def evaluate(poly,values):
    return sum((coefficient*product(values[i]**k for i,k in enumerate(key))
                for key,coefficient in poly.items()),F(0))
def product(values):
    result=F(1)
    for value in values: result*=value
    return result


def certificate():
    a,b,c,b1,b2,b3,p,q,r,U,G=map(variable,range(N))
    one=constant(1)
    B=add(b1,b2,b3);J=multiply(b1,b2,b3)
    S=add(one,p,q,r,multiply(p,q),multiply(p,r),multiply(q,r))
    L=add(multiply(b1,b2),multiply(b1,b3),multiply(b2,b3),
          multiply(p,b3,add(b1,b2)),multiply(q,b2,add(b1,b3)),
          multiply(r,b1,add(b2,b3)))
    H=add(S,multiply(L,U),multiply(J,G),multiply(B,J,U,U))
    M=add(L,scale(multiply(B,J,U),2))

    def clusters(groups):
        ds=[add(one,multiply(B,x)) for x in groups]
        ans=multiply(H,*ds)
        for i,x in enumerate(groups):
            rest=[ds[j] for j in range(len(groups)) if j!=i]
            ans=add(ans,multiply(M,x,x,*rest),multiply(J,x,x,x,*rest))
            for j in range(i):
                rest=[ds[k] for k in range(len(groups)) if k not in (i,j)]
                ans=add(ans,scale(multiply(B,J,x,x,groups[j],groups[j],*rest),2))
        return ans

    A=clusters([a,b,c])
    E=clusters([add(a,b),c])
    Ff=clusters([a,add(b,c)])
    EF=clusters([add(a,b,c)])
    R=add(multiply(E,Ff),scale(multiply(A,EF),-1))
    assert len(R)==11063 and all(value>0 for value in R.values())
    assert all(key[0]>=1 and key[2]>=1 for key in R)
    # A fixed strictly positive coefficient independent of the middle row,
    # core activities, and background establishes strictness when a,c>0.
    strict_key=(1,0,1,2,0,0,0,0,0,0,0)
    assert R[strict_key]==1
    summary={}
    for key,value in R.items():
        label=','.join(map(str,key[-2:]))
        row=summary.setdefault(label,{'terms':0,'minimum_coefficient':value})
        row['terms']+=1;row['minimum_coefficient']=min(row['minimum_coefficient'],value)
    return (A,E,Ff,EF),R,summary


STATES=((0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0))
def canonical(state):
    names={}
    return tuple(names.setdefault(value,len(names)) for value in state)
def star(frontier,row,columns):
    out=defaultdict(F)
    for state,weight in frontier.items():
        for mask in range(8):
            selected=[i for i in range(3) if mask>>i&1]
            blocks=[state[i] for i in selected]
            if len(blocks)!=len(set(blocks)): continue
            target=canonical([blocks[0] if value in blocks else value for value in state]) if blocks else state
            out[target]+=weight*product(row*columns[i] for i in selected)
    return dict(out)
def background_data(rows,columns,edges):
    """Literal forest subsets on other terminals, before adding core spokes."""
    B=sum(columns,F(0));D=EU=EG=EU2=F(0)
    for mask in range(1<<len(edges)):
        parent=list(range(len(rows)))
        def root(v):
            while parent[v]!=v: v=parent[v]
            return v
        weight=F(1)
        for k,(u,v,w) in enumerate(edges):
            if mask>>k&1:
                u,v=root(u),root(v)
                if u==v: break
                parent[u]=v;weight*=F(w)
        else:
            sums=defaultdict(F)
            for i,row in enumerate(rows): sums[root(i)]+=row
            cluster=list(sums.values())
            d=product(1+B*x for x in cluster)
            u=sum((x*x/(1+B*x) for x in cluster),F(0))
            g=sum((x**3/(1+B*x)**2 for x in cluster),F(0))
            term=weight*d;D+=term;EU+=term*u;EG+=term*g;EU2+=term*u*u
    U=EU/D;G=EG/D+B*(EU2/D-U*U)
    assert D>0 and U>=0 and G>=0
    return D,U,G
def literal_coefficients(rows,columns,core,edges):
    p,q,r=core
    start=dict(zip(STATES,(F(1),p,q,r,p*q+p*r+q*r)))
    out=[]
    for ee,ff in ((0,0),(1,0),(0,1),(1,1)):
        total=F(0)
        for mask in range(1<<len(edges)):
            parent=list(range(len(rows)))
            def root(v):
                while parent[v]!=v:v=parent[v]
                return v
            weight=F(1)
            chosen=[(0,1,F(1))] if ee else []
            chosen+=([(1,2,F(1))] if ff else [])
            chosen += [edge for k,edge in enumerate(edges) if mask>>k&1]
            for u,v,w in chosen:
                u,v=root(u),root(v)
                if u==v:break
                parent[u]=v;weight*=w
            else:
                sums=defaultdict(F)
                for i,row in enumerate(rows):sums[root(i)]+=row
                state=start
                for row in sums.values():state=star(state,row,columns)
                total+=weight*sum(state.values(),F(0))
        out.append(total)
    return out


def main():
    coeffs,R,summary=certificate()
    results={'arithmetic':'exact sparse integer polynomials and Fraction evaluations',
             'variables':NAMES,'positive_monomials':len(R),'coefficient_slices_U_Gamma':summary,
             'literal_background_graph_checks':[]}
    cases=[
        ([1,2,3,4,5,6],[2,3,5],[2,3,5],[(3,4,F(2)),(4,5,F(3)),(3,5,F(5))]),
        ([F(1,2),0,F(3,4),F(4,5),F(5,6)],[F(2,3),F(3,4),F(5,7)],[F(1,3),0,F(2,5)],[(3,4,F(7,3))]),
        ([1,2,3]+[F(i+1,i+2) for i in range(7)],[1,2,4],[1,3,2],[(i,i+1,F(i+1,3)) for i in range(3,9)]+[(3,6,F(5)),(5,9,F(7))]),
        ([F(1,100)]*8,[1,1,1],[0,0,0],[(3,4,F(1)),(4,5,F(2)),(5,6,F(3)),(6,7,F(4)),(3,7,F(5))]),
    ]
    for rows,columns,core,edges in cases:
        rows,columns,core=[list(map(F,values)) for values in (rows,columns,core)]
        D,U,G=background_data(rows[3:],columns,[(i-3,j-3,w) for i,j,w in edges])
        values=rows[:3]+columns+core+[U,G]
        scalar=[D*evaluate(poly,values) for poly in coeffs]
        literal=literal_coefficients(rows,columns,core,edges)
        assert scalar==literal
        rayleigh=literal[1]*literal[2]-literal[0]*literal[3]
        assert rayleigh==D*D*evaluate(R,values)>0
        results['literal_background_graph_checks'].append({'terminals':len(rows),'rows':list(map(str,rows)),
            'columns':list(map(str,columns)),'core':list(map(str,core)),'background_edges':[[i,j,str(w)]for i,j,w in edges],
            'D_U_Gamma':list(map(str,(D,U,G))),'A_Be_Bf_C':list(map(str,literal)),'rayleigh':str(rayleigh)})
    here=Path(__file__).parent
    (here/'forest_adjacent_terminal_core3_coefficient_certificate.json').write_text(json.dumps({
        'variables':NAMES,'coefficients':[{'exponents':key,'coefficient':value}for key,value in sorted(R.items())]},separators=(',',':'))+'\n')
    (here/'forest_adjacent_terminal_core3_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
    print('Exact adjacent-pair coefficient certificate and all background-graph checks pass.',flush=True)
if __name__=='__main__':main()
