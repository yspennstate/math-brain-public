#!/usr/bin/env python3
"""Derive the Bernstein certificate via exact interpolation, not UV expansion."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
from math import comb
import ast
import json

HERE=Path(__file__).resolve().parent
BASE=32
def add(*ps):
    out=defaultdict(F)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(*ps):
    out={0:F(1)}
    for p in ps:
        new=defaultdict(F)
        for a,v in out.items():
            for b,w in p.items():new[a+b]+=v*w
        out={k:v for k,v in new.items() if v}
    return out
def power(p,k):return mul(*([p]*k))
def decode(k):return tuple((k//BASE**j)%BASE for j in range(3))
one={0:F(1)}
x,y,z=({BASE**j:F(1)} for j in range(3))
s,t=add(x,z),mul(x,z)

def cluster(rows,u,v):
    M,J=u/2,u*v/18
    ds=[add(one,a) for a in rows]
    out=mul(*ds)
    for i,a in enumerate(rows):
        rest=[d for j,d in enumerate(ds) if i!=j]
        out=add(out,scale(mul(a,a,*rest),M),scale(mul(a,a,a,*rest),J))
        for j in range(i):
            rest=[d for k,d in enumerate(ds) if k not in (i,j)]
            out=add(out,scale(mul(a,a,rows[j],rows[j],*rest),2*J))
    return out

def rayleigh(u,v):
    A=cluster([x,y,z],u,v)
    E=cluster([add(x,y),z],u,v)
    FF=cluster([x,add(y,z)],u,v)
    EF=cluster([add(x,y,z)],u,v)
    out=add(mul(E,FF),scale(mul(A,EF),-1))
    assert all(decode(k)[0]>=1 and decode(k)[2]>=1 for k in out)
    return {k-1-BASE**2:c for k,c in out.items()}

def symmetric_coordinates(p):
    # A unique expansion in s=x+z, t=xz, y. Eliminate largest x power.
    assert {((k//BASE**2)%BASE)+BASE*((k//BASE)%BASE)+BASE**2*(k%BASE):v
            for k,v in p.items()} == p
    out={}
    rest=dict(p)
    while rest:
        key=max(rest,key=lambda k:(decode(k)[1],decode(k)[0],decode(k)[2]))
        a,b,c=decode(key)
        assert a>=c
        coeff=rest[key]
        out[(a-c,c,b)]=coeff
        rest=add(rest,scale(mul(power(s,a-c),power(t,c),power(y,b)),-coeff))
    return out

def main():
    grid=(F(0),F(1,2),F(1))
    values=[[rayleigh(u,v) for v in grid] for u in grid]
    # Bernstein degree2: b0=f(0), b2=f(1), b1=2f(.5)-(f(0)+f(1))/2.
    along_u=[values[0], [add(scale(values[1][j],2),scale(values[0][j],F(-1,2)),
                           scale(values[2][j],F(-1,2))) for j in range(3)],values[2]]
    result={}
    for i,row in enumerate(along_u):
        cols=[row[0],add(scale(row[1],2),scale(row[0],F(-1,2)),scale(row[2],F(-1,2))),row[2]]
        for j,q in enumerate(cols):result[str(i)+str(j)]=symmetric_coordinates(q)
    # Read only declared comparison data; do not import or execute author code.
    tree=ast.parse((HERE/'forest_adjacent_terminal_core3_bernstein_exact.py').read_text())
    node=next(n for n in tree.body if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id=='NUMERATORS' for t in n.targets))
    author=ast.literal_eval(node.value)
    report={'route':'nine exact grid evaluations, Bernstein interpolation, symmetric elimination',
            'polynomials':{}}
    for label,q in result.items():
        compare='00' if label in ('01','02') else label
        den,nums=author[compare]
        assert q == {k:F(v,den) for k,v in nums.items()}
        assert all(c>0 for c in q.values())
        report['polynomials'][label]={'positive_terms':len(q),'coefficients':{
            ','.join(map(str,k)):str(v) for k,v in sorted(q.items())},
            'all_explicit_author_terms_match':True}
    assert result['00']==result['01']==result['02']
    # M=J=0 endpoint follows directly, including arbitrary middle row.
    assert result['00']=={(0,0,0):F(1),(1,0,0):F(1),(0,1,0):F(1)}
    report['status']='PASS: all seven positive polynomials independently derived exactly'
    path=HERE/'adjacent_bernstein_ant_independent_checks.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'])
    print({k:v['positive_terms'] for k,v in report['polynomials'].items()})

if __name__=='__main__':main()
