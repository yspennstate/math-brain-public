"""Exact checks of the ordinary-forest log-concavity background extension.

Computes literal terminal-forest configurations, actual spoke subsets,
independent apex forests and derivatives, forced-OR matching laws, and
every matching increasing-event inequality under partial conditioning of
both matching indicators and background terminal edges.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from forest_matching_negative_association_exact import (
    STATES,terminal,clear_denominators,conditional_na_check,forced_bernoulli_table)


def forest_components(rows,edges,mask):
    parent=list(range(len(rows)));weight=F(1)
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for k,(u,v,w) in enumerate(edges):
        if mask>>k&1:
            u,v=root(u),root(v)
            if u==v:return None
            parent[u]=v;weight*=w
    sums=defaultdict(F)
    for i,row in enumerate(rows):sums[root(i)]+=row
    return weight,list(sums.values())


def background_parameters(rows,edges,B):
    Z=Zp=Zpp=EU=EG=EU2=F(0)
    for mask in range(1<<len(edges)):
        item=forest_components(rows,edges,mask)
        if item is None:continue
        weight,sums=item
        ds=[1+B*x for x in sums]
        d=F(1)
        for value in ds:d*=value
        W=sum((x/(1+B*x)for x in sums),F(0))
        Wp=-sum((x*x/(1+B*x)**2 for x in sums),F(0))
        U=sum((x*x/(1+B*x)for x in sums),F(0))
        G=sum((x**3/(1+B*x)**2 for x in sums),F(0))
        value=weight*d
        Z+=value;Zp+=value*W;Zpp+=value*(Wp+W*W)
        EU+=value*U;EG+=value*G;EU2+=value*U*U
    U=EU/Z;Gamma=EG/Z+B*(EU2/Z-U*U)
    logsecond=Zpp/Z-(Zp/Z)**2
    assert U/B-Gamma==-logsecond/B>=0
    assert U>=0 and Gamma>=0
    return Z,Zp,Zpp,U,Gamma,logsecond


def apex_partition_derivatives(rows,edges,B):
    """Independent original-graph forest enumeration; no cluster factors."""
    n=len(rows);all_edges=list(edges)+[(n,j,B*a)for j,a in enumerate(rows)]
    Z=Zp=Zpp=F(0)
    for mask in range(1<<len(all_edges)):
        parent=list(range(n+1));weight=F(1);star_count=0
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for k,(u,v,w) in enumerate(all_edges):
            if mask>>k&1:
                u,v=root(u),root(v)
                if u==v:break
                parent[u]=v;weight*=w
                if k>=len(edges):star_count+=1
        else:
            Z+=weight
            Zp+=weight*star_count/B
            Zpp+=weight*star_count*(star_count-1)/(B*B)
    return Z,Zp,Zpp


def joint_matching_background_table(matching_rows,bg_rows,columns,core,activities,edges):
    k=len(activities);weights=[F(0)]*(1<<(k+len(edges)))
    p,q,r=core
    initial=dict(zip(STATES,(F(1),p,q,r,p*q+p*r+q*r)))
    for bgmask in range(1<<len(edges)):
        item=forest_components(bg_rows,edges,bgmask)
        if item is None:continue
        bgweight,sums=item
        background=initial
        for row in sums:background=terminal(background,row,columns)
        for matchmask in range(1<<k):
            frontier=background;factor=bgweight
            for i,w in enumerate(activities):
                a,b=matching_rows[2*i:2*i+2]
                if matchmask>>i&1:frontier=terminal(frontier,a+b,columns);factor*=w
                else:frontier=terminal(terminal(frontier,a,columns),b,columns)
            weights[matchmask+(bgmask<<k)]=factor*sum(frontier.values(),F(0))
    return weights


def forced_parameters(matching_rows,columns,core,activities,U,G):
    B=sum(columns,F(0));J=columns[0]*columns[1]*columns[2]
    p,q,r=core;b0,b1,b2=columns
    S=1+p+q+r+p*q+p*r+q*r
    L=b0*b1+b0*b2+b1*b2+p*b2*(b0+b1)+q*b1*(b0+b2)+r*b0*(b1+b2)
    d=lambda x:1+B*x
    alpha=lambda x:x*x/d(x)
    gamma=lambda x:x**3/d(x)**2
    U+=sum(map(alpha,matching_rows),F(0));G+=sum(map(gamma,matching_rows),F(0))
    assert 0<=G<=U/B
    A=S+L*U+J*G+B*J*U*U;M=L+2*B*J*U;K=2*B*J
    theta=[];ts=[];hs=[]
    for i,w in enumerate(activities):
        a,b=matching_rows[2*i:2*i+2]
        delta=alpha(a+b)-alpha(a)-alpha(b)
        epsilon=gamma(a+b)-gamma(a)-gamma(b)
        c=d(a+b)/(d(a)*d(b))
        theta.append(c*w/(1+c*w));ts.append(delta*theta[-1])
        hs.append(M+J*epsilon/delta+B*J*delta)
    assert min(hs)**2>K*A and max(hs)<2*min(hs)
    return A,K,theta,ts,hs


def every_background_conditioning_na(joint,k,h):
    integers=clear_denominators(joint);laws=events=bg_laws=0
    for status in product((-1,0,1),repeat=h):
        matching=[0]*(1<<k)
        for outcome,weight in enumerate(integers):
            bgmask=outcome>>k
            if any(value!=-1 and ((bgmask>>j)&1)!=value for j,value in enumerate(status)):continue
            matching[outcome&((1<<k)-1)]+=weight
        if not sum(matching):continue
        count,tested=conditional_na_check(matching)
        bg_laws+=1;laws+=count;events+=tested
    return bg_laws,laws,events


def main():
    cases=[
        ([1,2,3,4,5,6],[1,2,3],[2,3,5],[2,3,5],[F(1,2),2,F(3,5)],
         [(0,1,F(2)),(1,2,F(3)),(0,2,F(5))]),
        ([F(i+1,i+2)for i in range(8)],[F(1,3),F(3,2),F(5,4)],
         [F(2,3),F(3,4),F(5,7)],[F(1,3),0,F(2,5)],[F(2,3),F(4,5),F(6,7),F(8,9)],
         [(0,1,F(1,2)),(1,2,F(2,3)),(0,2,F(3,4))]),
        ([1,2,1,3,2,4],[1,2,3,4],[1,2,4],[1,3,2],[F(1,3),2,7],
         [(i,j,F(i+j+1,3))for i in range(4)for j in range(i+1,4)]),
    ]
    results={'arithmetic':'exact Fraction / denominator-cleared integers','cases':[]}
    for matching_rows,bg_rows,columns,core,activities,edges in cases:
        matching_rows,bg_rows,columns,core,activities=[list(map(F,values))for values in(matching_rows,bg_rows,columns,core,activities)]
        edges=[(i,j,F(w))for i,j,w in edges];B=sum(columns,F(0))
        Z,Zp,Zpp,U,G,logsecond=background_parameters(bg_rows,edges,B)
        assert (Z,Zp,Zpp)==apex_partition_derivatives(bg_rows,edges,B)
        joint=joint_matching_background_table(matching_rows,bg_rows,columns,core,activities,edges)
        k=len(activities);actual=[sum((joint[mask+(bgmask<<k)]for bgmask in range(1<<len(edges))),F(0))for mask in range(1<<k)]
        represented,_=forced_bernoulli_table(*forced_parameters(matching_rows,columns,core,activities,U,G))
        assert represented==[value/sum(actual)for value in actual]
        bg_laws,conditional_laws,event_checks=every_background_conditioning_na(joint,k,len(edges))
        results['cases'].append({'matching_edges':k,'background_vertices':len(bg_rows),'background_edges':[[i,j,str(w)]for i,j,w in edges],
             'Z_Zprime_Zsecond':list(map(str,(Z,Zp,Zpp))),'U_Gamma':list(map(str,(U,G))),
             'logZ_second':str(logsecond),'exact_gap_UoverB_minus_Gamma':str(U/B-G),
             'apex_original_graph_identity':True,'forced_OR_law_exact':True,
             'valid_background_partial_conditionings':bg_laws,'total_matching_conditional_laws':conditional_laws,
             'all_disjoint_matching_increasing_event_checks':event_checks})
        print('Exact arbitrary-background extension check passed for',k,'matching edges and',len(edges),'background edges.',flush=True)
    Path(__file__).with_name('forest_matching_arbitrary_background_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
    print('All ordinary-forest derivative, closure, forced-law and conditioning checks PASS.',flush=True)
if __name__=='__main__':main()
