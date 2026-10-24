"""Exact four-core/tree-apex checks; no numerical roots or eigenvalues.

Uses a rational matrix similar to the Gaussian tree covariance, literal
independent percolation, direct four-spoke cycle transitions, and original
graph enumeration. None of the disjoint Rayleigh signs is assumed.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from forest_adjacent_rank_one_attachment_all_ports_exact import forest_records, conditioned


def determinant(matrix):
    if not matrix:return F(1)
    matrix=[row[:]for row in matrix];value=F(1);n=len(matrix)
    for i in range(n):
        pivot=next((j for j in range(i,n)if matrix[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:matrix[i],matrix[pivot]=matrix[pivot],matrix[i];value=-value
        v=matrix[i][i];value*=v
        for j in range(i+1,n):
            factor=matrix[j][i]/v
            for k in range(i+1,n):matrix[j][k]-=factor*matrix[i][k]
    return value


def canonical(row):
    names={};return tuple(names.setdefault(x,len(names))for x in row)


def terminal(frontier,x,columns):
    out=defaultdict(F);n=len(columns)
    for state,mass in frontier.items():
        for mask in range(1<<n):
            selected=[i for i in range(n)if mask>>i&1]
            labels=[state[i]for i in selected]
            if len(set(labels))!=len(labels):continue
            touched=set(labels)
            target=canonical(tuple(labels[0]if k in touched else k for k in state))if labels else state
            value=mass
            for i in selected:value*=x*columns[i]
            out[target]+=value
    return dict(out)


def direct_four_coefficients(records,columns):
    result=[F(0)]*4
    for _,weight,rows in records:
        for marked in range(4):
            state=list(range(4))
            if marked&1:state[1]=state[0]
            if marked&2:state[3]=state[2]
            frontier={canonical(state):weight}
            for x in rows:frontier=terminal(frontier,x,columns)
            result[marked]+=sum(frontier.values(),F(0))
    return result


def parameters(records,s):
    D=DU=DG=DH=DU2=DUG=DU3=Dp=Dpp=Dppp=F(0)
    for _,weight,rows in records:
        mass=weight
        for x in rows:mass*=1+s*x
        U=sum((x*x/(1+s*x)for x in rows),F(0))
        G=sum((x**3/(1+s*x)**2 for x in rows),F(0))
        H=sum((x**4/(1+s*x)**3 for x in rows),F(0))
        W=sum((x/(1+s*x)for x in rows),F(0))
        Y=sum((x*x/(1+s*x)**2 for x in rows),F(0))
        V=sum((x**3/(1+s*x)**3 for x in rows),F(0))
        D+=mass;DU+=mass*U;DG+=mass*G;DH+=mass*H
        DU2+=mass*U*U;DUG+=mass*U*G;DU3+=mass*U**3
        Dp+=mass*W;Dpp+=mass*(W*W-Y);Dppp+=mass*(W**3-3*W*Y+2*V)
    U=DU/D;EG=DG/D;variance=DU2/D-U*U;covariance=DUG/D-U*EG
    cumulant=DU3/D-3*U*DU2/D+2*U**3
    Gamma=EG+s*variance
    Omega=DH/D-variance/2+3*s*covariance/2+s*s*cumulant/2
    T=U-s*Gamma
    logsecond=Dpp/D-(Dp/D)**2
    logthird=Dppp/D-3*Dp*Dpp/(D*D)+2*(Dp/D)**3
    assert T==-logsecond>=0
    assert Omega==Gamma/s-logthird/(2*s)
    return D,U,Gamma,Omega,T,Dp,Dpp,Dppp


def scalar_coefficients(p,columns):
    D,U,G,O,T,*_=p;a,b,c,d=columns;s=a+b+c+d
    pp=a+b;qq=c+d;u=a*b;v=c*d;H3=G+s*U*U;H4=2*O-U*U+3*s*U*G+s*s*U**3
    return [D*(1+(pp*qq+u+v)*U+(u*qq+v*pp)*H3+u*v*H4),
            D*(1+(pp*qq+v)*U+v*pp*H3),D*(1+(pp*qq+u)*U+u*qq*H3),D*(1+pp*qq*U)]


def covariance_similar_kernel(n,edges):
    adjacency=[[]for _ in range(n)]
    for u,v,w in edges:
        p=w/(1+w);adjacency[u].append((v,p));adjacency[v].append((u,p))
    paths=[None]*n;parent_probability={}
    for root in range(n):
        if paths[root]is not None:continue
        paths[root]=[root];stack=[root]
        while stack:
            u=stack.pop()
            for v,p in adjacency[u]:
                if paths[v]is None:
                    paths[v]=paths[u]+[v];parent_probability[v]=p;stack.append(v)
    K=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if paths[i][0]!=paths[j][0]:continue
            common=0
            while common<min(len(paths[i]),len(paths[j]))and paths[i][common]==paths[j][common]:common+=1
            value=F(1)
            for v in paths[j][common:]:value*=parent_probability[v]
            K[i][j]=value
    return K


def verify_covariance_identity(n,edges,profile):
    K=covariance_similar_kernel(n,edges);probabilities=[w/(1+w)for _,_,w in edges]
    events=[]
    for mask in range(1<<len(edges)):
        parent=list(range(n));prob=F(1)
        def root(u):
            while parent[u]!=u:u=parent[u]
            return u
        for i,(u,v,w)in enumerate(edges):
            prob*=probabilities[i]if mask>>i&1 else 1-probabilities[i]
            if mask>>i&1:parent[root(u)]=root(v)
        events.append((prob,[root(i)for i in range(n)]))
    coeff=[F(0)]*(n+1)
    for mask in range(1<<n):
        selected=[i for i in range(n)if mask>>i&1]
        minor=determinant([[K[i][j]for j in selected]for i in selected])
        probability=sum((prob for prob,state in events if len(set(state[i]for i in selected))==len(selected)),F(0))
        assert minor==probability>=0
        value=minor
        for i in selected:value*=profile[i]
        coeff[len(selected)]+=value
    ZH=F(1)
    for _,_,w in edges:ZH*=1+w
    actual=[F(0)]*(n+1)
    for _,weight,rows in forest_records(n,edges,profile):
        poly=[F(1)]
        for x in rows:
            following=[F(0)]*(len(poly)+1)
            for i,value in enumerate(poly):following[i]+=value;following[i+1]+=x*value
            poly=following
        for i,value in enumerate(poly):actual[i]+=weight*value
    assert actual==[ZH*x for x in coeff]
    return actual


def contract_condition(n,edges,profile,status):
    parent=list(range(n))
    def root(u):
        while parent[u]!=u:u=parent[u]
        return u
    for value,(u,v,w)in zip(status,edges):
        if value==1:parent[root(u)]=root(v)
    labels={};rows=[]
    for i,x in enumerate(profile):
        r=root(i)
        if r not in labels:labels[r]=len(rows);rows.append(F(0))
        rows[labels[r]]+=x
    return sum(bool(x)for x in rows)


def literal_original_graph(n,edges,profile,columns):
    unmarked=edges+[(n+i,j,a*x)for i,a in enumerate(columns)for j,x in enumerate(profile)if a*x]
    coeff=[F(0)]*4;counts=[0]*4
    def root(parent,u):
        while parent[u]!=u:u=parent[u]
        return u
    def visit(index,parent,mass):
        if index<len(unmarked):
            visit(index+1,parent,mass)
            u,v,w=unmarked[index];u,v=root(parent,u),root(parent,v)
            if u!=v:
                copy=parent.copy();copy[u]=v;visit(index+1,copy,mass*w)
            return
        for marked in range(4):
            copy=parent.copy()
            for i,(u,v)in enumerate(((n,n+1),(n+2,n+3))):
                if marked>>i&1:
                    u,v=root(copy,u),root(copy,v)
                    if u==v:break
                    copy[u]=v
            else:coeff[marked]+=mass;counts[marked]+=1
    visit(0,list(range(n+4)),F(1));return coeff,counts


def main():
    cases=[
        {'name':'four_profile_path','n':4,'edges':[(0,1,F(2)),(1,2,F(3)),(2,3,F(5))],
         'profile':[F(1),F(2),F(3),F(4)],'columns':[F(1),F(2),F(3),F(4)],'literal':True},
        {'name':'six_profile_branching_tree_rational','n':6,
         'edges':[(0,1,F(2,3)),(0,2,F(3,4)),(2,3,F(5,7)),(2,4,F(7,11)),(4,5,F(11,13))],
         'profile':[F(i+1,i+2)for i in range(6)],'columns':[F(1,3),F(2,5),F(3,7),F(4,9)]},
        {'name':'disconnected_zero_profile_vertex','n':5,
         'edges':[(0,1,F(2)),(2,3,F(3))],
         'profile':[F(1),F(2),F(3),F(4),F(0)],'columns':[F(2),F(3),F(5),F(7)]},
        {'name':'one_positive_profile_equality','n':4,
         'edges':[(0,1,F(2)),(1,2,F(0)),(2,3,F(5))],
         'profile':[F(0),F(3),F(0),F(0)],'columns':[F(2),F(3),F(5),F(7)]},
        {'name':'zero_endpoint_equality','n':4,
         'edges':[(0,1,F(2)),(0,2,F(3)),(0,3,F(5))],
         'profile':[F(1),F(2),F(3),F(4)],'columns':[F(0),F(3),F(5),F(7)],'literal':True},
    ]
    report={'arithmetic':'exact Fraction; no numerical roots/eigenvalues','cases':[]}
    for case in cases:
        n,edges,profile,columns=[case[key]for key in('n','edges','profile','columns')];s=sum(columns)
        apex=verify_covariance_identity(n,edges,profile);records=forest_records(n,edges,profile)
        unconditional=direct_four_coefficients(records,columns);counts=None
        if case.get('literal'):
            literal,counts=literal_original_graph(n,edges,profile,columns);assert literal==unconditional
        conditionings=strictcases=0;minimum=None
        for status in product((-1,0,1),repeat=len(edges)):
            selected=conditioned(records,status)
            if not sum((r[1]for r in selected),F(0)):continue
            p=parameters(selected,s);actual=direct_four_coefficients(selected,columns);assert actual==scalar_coefficients(p,columns)
            D,U,G,O,T,*_=p;A,E,Ff,C=actual;R=E*Ff-A*C
            first=U*T-O;second=G*G+U*U*T-2*U*O
            assert first>=0 and second>=0
            a,b,c,d=columns;assert R==D*D*a*b*c*d*(2*first+(a+b)*(c+d)*second)>=0
            strict=bool(a*b*c*d and contract_condition(n,edges,profile,status)>=2)
            assert (R>0)==strict;strictcases+=strict;conditionings+=1
            minimum=R if minimum is None else min(minimum,R)
        report['cases'].append({'name':case['name'],'vertices':n,'positive_profile_vertices':sum(bool(x)for x in profile),
            'tree_covariance_all_principal_minors_equal_disconnect_probabilities':True,
            'exact_apex_polynomial_coefficients_ascending':list(map(str,apex)),
            'unconditional_four_coefficients':list(map(str,unconditional)),
            'positive_backbone_partial_conditionings':conditionings,'strict_conditionings':strictcases,
            'smallest_exact_Rayleigh':str(minimum),'literal_original_graph_match':counts is not None,
            'literal_forest_counts_by_marked_subset':counts})
        print(case['name'],'PASS;',conditionings,'positive backbone conditions.',flush=True)
    Path(__file__).with_name('forest_disjoint_rank_one_attachment_forest_backbone_exact_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('All tree covariance, four-core identity and disjoint pair checks PASS.',flush=True)


if __name__=='__main__':main()
