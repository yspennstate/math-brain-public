#!/usr/bin/env python3
"""Literal uncontracted graph check of the arbitrary-backbone adjacent result."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import json

HERE=Path(__file__).resolve().parent

def evaluate_forest(n,edges,mask):
    par=list(range(n));weight=F(1)
    def root(i):
        while par[i]!=i:i=par[i]
        return i
    for j,(a,b,w) in enumerate(edges):
        if mask>>j&1:
            a,b=root(a),root(b)
            if a==b:return None
            par[a]=b;weight*=w
    return weight,tuple(root(i) for i in range(n))

def allowed(mask,condition):
    return all(((mask>>i)&1)==s for i,s in condition.items())

def parameters(n,edges,ports,columns,condition):
    partitions=defaultdict(F)
    for mask in range(1<<len(edges)):
        if not allowed(mask,condition):continue
        item=evaluate_forest(n,edges,mask)
        if item:
            weight,labels=item
            names={};key=tuple(names.setdefault(labels[p],len(names)) for p in ports)
            partitions[key]+=weight
    B=sum(columns);J0=columns[0]*columns[1]*columns[2]
    total=sum(partitions.values());M=F(0)
    for part,w in partitions.items():
        M+=w*sum(columns[i]*columns[j]for i,j in combinations(range(3),2)if part[i]!=part[j])
    J=partitions.get((0,1,2),F(0))*J0
    e2=sum(columns[i]*columns[j]for i,j in combinations(range(3),2))
    assert 0<=M<=e2*total<=B*B*total/3
    assert B*M>=9*J
    return total,M,J,partitions

def C(groups,total,M,J,B):
    ds=[1+B*x for x in groups]
    out=total*prod(ds)
    for i,x in enumerate(groups):
        out+=(M*x*x+J*x**3)*prod(d for j,d in enumerate(ds)if i!=j)
        for j in range(i):
            out+=2*B*J*x*x*groups[j]**2*prod(d for k,d in enumerate(ds)if k not in(i,j))
    return out

def prod(xs):
    out=F(1)
    for x in xs:out*=x
    return out

def literal_coefficients(n,backbone,ports,rows,cols,condition):
    stars=[(n+j,p,row*col)for j,row in enumerate(rows)for p,col in zip(ports,cols)if row*col]
    unmarked=list(backbone)+stars
    marked=[(n,n+1,F(1)),(n+1,n+2,F(1))]
    coefficients=[F(0)]*4;counts=[0]*4
    for mask in range(1<<len(unmarked)):
        if not allowed(mask,condition):continue
        # Rejecting cycles before adding marked edges saves four repeated cycle tests.
        if evaluate_forest(n+3,unmarked,mask) is None:continue
        for chosen in range(4):
            item=evaluate_forest(n+3,unmarked+marked,mask+(chosen<<len(unmarked)))
            if item:
                coefficients[chosen]+=item[0];counts[chosen]+=1
    return coefficients,counts,len(unmarked)+2

def main():
    backbone=[(i,j,F(w))for(i,j),w in zip(combinations(range(4),2),(2,3,5,7,11,13))]
    cases=[
      ([F(1,2),F(2,3),F(3,5)],[F(2),F(3),F(5)],{}),
      ([F(1),F(0),F(2)],[F(0),F(2),F(3)],{0:1,3:1}),
      ([F(1),F(2),F(3)],[F(1),F(2),F(3)],{0:1,1:1,4:0}),
      ([F(0),F(2),F(3)],[F(1),F(2),F(3)],{}),
      ([F(1),F(2),F(3)],[F(0),F(0),F(0)],{})]
    report={'route':'literal UNCONTRACTED whole graph forest enumeration; no author imports','cases':[]}
    for rows,cols,condition in cases:
        ports=(0,1,2);B=sum(cols)
        total,M,J,parts=parameters(4,backbone,ports,cols,condition)
        a,b,c=rows
        expected=[C([a,b,c],total,M,J,B),C([a+b,c],total,M,J,B),
                  C([a,b+c],total,M,J,B),C([a+b+c],total,M,J,B)]
        actual,counts,nedges=literal_coefficients(4,backbone,ports,rows,cols,condition)
        assert actual==expected
        rayleigh=actual[1]*actual[2]-actual[0]*actual[3]
        assert rayleigh>=0
        if a and c and B:assert rayleigh>0
        else:assert rayleigh==0
        report['cases'].append({'rows':list(map(str,rows)),'columns':list(map(str,cols)),
            'required_backbone_bits':condition,'full_graph_edges':nedges,
            'port_partition_weights':{str(k):str(w)for k,w in parts.items()},
            'F_M_J':list(map(str,(total,M,J))),'exact_coefficients':list(map(str,actual)),
            'literal_forest_counts':counts,'rayleigh_difference':str(rayleigh),
            'all_four_formula_coefficients_match':True})
        print('PASS',list(map(str,rows)),list(map(str,cols)),condition,flush=True)
    report['status']='PASS: arbitrary-backbone coefficient identities, scalar bounds and endpoints'
    (HERE/'arbitrary_backbone_adjacent_ant_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
