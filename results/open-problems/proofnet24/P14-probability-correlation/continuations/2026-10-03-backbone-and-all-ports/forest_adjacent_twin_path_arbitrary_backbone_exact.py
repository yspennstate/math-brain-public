"""Exact uncontracted-graph checks for the arbitrary-backbone theorem.

The four marked coefficients are collected from actual edge subsets and
union-find cycle checks, not from contractions, scalar cones or transfer
formulas. Every positive-probability partial backbone conditioning is
then compared with the independent five-port-partition computation.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json

STATES=((0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0))
def canonical(labels):
    names={}
    return tuple(names.setdefault(value,len(names))for value in labels)
def prod(values):
    answer=F(1)
    for value in values:answer*=value
    return answer


def full_original_graph_table(n,backbone,rows,columns):
    k=len(backbone)
    edges=list(backbone)+[(n+j,i,rows[j]*columns[i])for j in range(3)for i in range(3)if rows[j]*columns[i]]
    table=[[F(0)]*4 for _ in range(1<<k)];forest_count=0
    for mask in range(1<<len(edges)):
        parent=list(range(n+3));weight=F(1)
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for index,(a,b,w) in enumerate(edges):
            if mask>>index&1:
                a,b=root(a),root(b)
                if a==b:break
                parent[a]=b;weight*=w
        else:
            if not weight:continue
            forest_count+=1
            masses=table[mask&((1<<k)-1)]
            masses[0]+=weight
            a,b,c=(root(n+j)for j in range(3))
            if a!=b:masses[1]+=weight
            if b!=c:masses[2]+=weight
            if len({a,b,c})==3:masses[3]+=weight
    return table,forest_count,len(edges)


def independent_backbone_partition_table(n,backbone):
    table=[]
    for mask in range(1<<len(backbone)):
        parent=list(range(n));weight=F(1)
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for k,(a,b,w)in enumerate(backbone):
            if mask>>k&1:
                a,b=root(a),root(b)
                if a==b:break
                parent[a]=b;weight*=w
        else:
            row=[F(0)]*5;row[STATES.index(canonical([root(i)for i in range(3)]))]=weight
            table.append(row);continue
        table.append([F(0)]*5)
    return table


def scalar_coefficients(row,rows,columns):
    B=sum(columns,F(0));J0=prod(columns)
    F0=sum(row,F(0))
    M=sum((weight*sum((columns[i]*columns[j]for i,j in combinations(range(3),2)if state[i]!=state[j]),F(0))
           for state,weight in zip(STATES,row)),F(0))
    J=row[0]*J0
    e2=sum((columns[i]*columns[j]for i,j in combinations(range(3),2)),F(0))
    assert 0<=M<=e2*F0<=B*B*F0/3
    assert B*M>=9*J
    def C(groups):
        ds=[1+B*x for x in groups]
        answer=F0*prod(ds)
        for i,x in enumerate(groups):
            rest=prod(ds[j]for j in range(len(ds))if j!=i)
            answer+=(M*x*x+J*x**3)*rest
            for j in range(i):answer+=2*B*J*x*x*groups[j]*groups[j]*prod(ds[l]for l in range(len(ds))if l not in(i,j))
        return answer
    a,b,c=rows
    return [C([a,b,c]),C([a+b,c]),C([a,b+c]),C([a+b+c])],(F0,M,J)


def all_backbone_conditionings(n,backbone,rows,columns):
    original,forest_count,edge_count=full_original_graph_table(n,backbone,rows,columns)
    partitions=independent_backbone_partition_table(n,backbone)
    verified=0;examples=[]
    for condition in product((-1,0,1),repeat=len(backbone)):
        masks=[mask for mask in range(1<<len(backbone))
               if all(value==-1 or ((mask>>j)&1)==value for j,value in enumerate(condition))]
        actual=[sum((original[mask][i]for mask in masks),F(0))for i in range(4)]
        if not actual[0]:continue
        row=[sum((partitions[mask][i]for mask in masks),F(0))for i in range(5)]
        scalar,parameters=scalar_coefficients(row,rows,columns)
        assert actual==scalar
        rayleigh=actual[1]*actual[2]-actual[0]*actual[3]
        if rows[0]*rows[2]*sum(columns):assert rayleigh>0
        else:assert rayleigh==0
        verified+=1
        if condition==(-1,)*len(backbone)or row[0]==0 and len(examples)<5:
            examples.append({'backbone_condition':condition,'port_partition_weights':list(map(str,row)),
                             'F_M_J':list(map(str,parameters)),'A_Be_Bf_C':list(map(str,actual)),
                             'rayleigh':str(rayleigh)})
    return {'backbone_vertices':n,'backbone_edges':[[a,b,str(w)]for a,b,w in backbone],
            'rows':list(map(str,rows)),'columns':list(map(str,columns)),
            'full_uncontracted_unmarked_edges':edge_count,'enumerated_full_graph_forests':forest_count,
            'all_valid_partial_backbone_conditionings':verified,'representative_exact_results':examples}


def main():
    cases=[
        (5,[(0,3,2),(3,1,5),(1,4,3),(4,2,7),(0,2,11),(3,4,13),(0,1,17)], [1,2,3],[2,3,5]),
        (4,[(0,3,F(1,2)),(3,1,F(2,3)),(1,2,F(3,5)),(2,0,F(5,7)),(3,2,F(7,11))], [1,0,2],[1,2,0]),
        (3,[(0,1,F(2)),(1,2,F(3)),(0,2,F(5))],[F(1,2),F(2,3),F(3,4)],[1,0,0]),
        (3,[(0,1,F(2)),(1,2,F(3)),(0,2,F(5))],[0,2,3],[1,2,4]),
    ]
    results={'arithmetic':'exact Fraction; literal uncontracted original-graph subset enumeration','cases':[]}
    for n,edges,rows,columns in cases:
        edges=[(a,b,F(w))for a,b,w in edges];rows=list(map(F,rows));columns=list(map(F,columns))
        result=all_backbone_conditionings(n,edges,rows,columns)
        results['cases'].append(result)
        print('Original arbitrary-backbone graph and every conditioning PASS:',n,'vertices,',len(edges),'backbone edges.',flush=True)
    Path(__file__).with_name('forest_adjacent_twin_path_arbitrary_backbone_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
