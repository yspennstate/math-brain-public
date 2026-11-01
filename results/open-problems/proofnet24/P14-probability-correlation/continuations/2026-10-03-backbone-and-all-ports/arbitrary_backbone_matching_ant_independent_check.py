#!/usr/bin/env python3
"""Independent actual-backbone matching check; no author modules imported."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json
from arbitrary_background_ant_independent_check import (
    forest,canonical,apply_star,condition_checks)

HERE=Path(__file__).resolve().parent

def backbone_records(n,edges):
    out=[]
    for mask in range(1<<len(edges)):
        item=forest(n,edges,mask)
        if item:
            w,labels=item;out.append((mask,canonical(labels[:3]),w))
    return out

def matching_law(row,rows,columns,activities):
    out=[]
    for mask in range(1<<len(activities)):
        law=row;weight=F(1)
        for i,w in enumerate(activities):
            a,b=rows[2*i:2*i+2]
            if mask>>i&1:law=apply_star(law,a+b,columns);weight*=w
            else:law=apply_star(apply_star(law,a,columns),b,columns)
        out.append(weight*sum(law.values()))
    return out

def parameters(row,rows,columns):
    for a in rows:row=apply_star(row,a,columns)
    A=[sum(w for state,w in row.items()if state[i]!=state[j])for i,j in ((0,1),(0,2),(1,2))]
    r=sum(w for state,w in row.items()if len(set(state))==3)
    total=sum(row.values());B=sum(columns);J=r*columns[0]*columns[1]*columns[2]
    M=sum(a*columns[i]*columns[j]for a,(i,j)in zip(A,((0,1),(0,2),(1,2))))
    H=[[A[i]*A[j]-(r*total if i!=j else 0)for j in range(3)]for i in range(3)]
    minors=[H[i][i]for i in range(3)]
    minors.extend(H[i][i]*H[j][j]-H[i][j]**2 for i,j in combinations(range(3),2))
    det=sum(H[0][i]*(H[1][(i+1)%3]*H[2][(i+2)%3]-H[1][(i+2)%3]*H[2][(i+1)%3])for i in range(3))
    minors.append(det)
    assert all(v>=0 for v in minors)
    assert M*M>=2*B*J*total and B*M>=9*J
    return total,M,J,minors,A,r

def forced(row,rows,columns,activities):
    total,M,J,minors,A,r=parameters(row,rows,columns);B=sum(columns);K=2*B*J
    theta=[];t=[];h=[]
    d=lambda x:1+B*x
    alpha=lambda x:x*x/d(x)
    gamma=lambda x:x**3/d(x)**2
    for i,w in enumerate(activities):
        a,b=rows[2*i:2*i+2];c=d(a+b)/(d(a)*d(b))
        theta.append(c*w/(1+c*w))
        delta=alpha(a+b)-alpha(a)-alpha(b)
        epsilon=gamma(a+b)-gamma(a)-gamma(b)
        if B==0 or delta==0:
            assert J==0 or delta==epsilon==0
            t.append(F(0));h.append(M)
        else:
            assert 0<delta<1/(B*B) and 0<epsilon/delta<2/B
            t.append(delta*theta[-1]);h.append(M+J*epsilon/delta+B*J*delta)
    if M:assert min(h)**2>=K*total and max(h)<2*min(h)
    else:assert J==K==0 and all(v==0 for v in h)
    k=len(activities);Y={0:total}
    Y.update({1<<i:h[i]*t[i]for i in range(k)})
    Y.update({(1<<i)+(1<<j):K*t[i]*t[j]for i,j in combinations(range(k),2)})
    denom=sum(Y.values());out=[F(0)]*(1<<k)
    for required,w in Y.items():
        for noise in range(1<<k):
            p=F(1)
            for i,tt in enumerate(theta):p*=tt if noise>>i&1 else 1-tt
            out[required|noise]+=w*p/denom
    return out,(total,M,J,minors)

def literal(n,edges,rows,columns,activities):
    k=len(activities);h=len(edges)
    unmarked=list(edges)+[(n+j,i,a*b)for j,a in enumerate(rows)for i,b in enumerate(columns)if a*b]
    marks=[(n+2*i,n+2*i+1,w)for i,w in enumerate(activities)]
    out=[F(0)]*(1<<(k+h));counts=[0]*(1<<k)
    for mask in range(1<<len(unmarked)):
        if forest(n+len(rows),unmarked,mask) is None:continue
        for mark in range(1<<k):
            item=forest(n+len(rows),unmarked+marks,mask+(mark<<len(unmarked)))
            if item:
                out[mark+((mask&((1<<h)-1))<<k)]+=item[0];counts[mark]+=1
    return out,counts

def main():
    cases=[
      (4,[(i,j,F(i+j+1))for i,j in combinations(range(4),2)],
       [F(1,2),F(2,3),F(3,4),F(4,5)],[F(1),F(2),F(3)],[F(2,3),F(3,5)],True),
      (5,[(0,3,F(2)),(1,3,F(3)),(2,4,F(5)),(3,4,F(7)),(0,2,F(11))],
       [F(i+1,i+2)for i in range(6)],[F(2,3),F(3,4),F(5,7)],[F(2),F(3),F(5)],False),
      (4,[(0,3,F(2)),(1,3,F(3)),(2,3,F(5)),(0,1,F(7))],
       [F(0),F(2),F(1),F(3),F(2),F(4)],[F(1),F(0),F(2)],[F(2),F(3),F(5)],False),
      (3,[(0,1,F(2)),(1,2,F(3))],[F(1),F(2),F(3),F(4)],
       [F(0),F(2),F(0)],[F(3),F(5)],False),
      (3,[(0,1,F(2))],[F(1),F(2),F(3),F(4)],
       [F(0),F(0),F(0)],[F(3),F(5)],False)]
    report={'route':'independent star enumeration, original flat-mask graph enumeration, all monotone events', 'cases':[]}
    for n,edges,rows,columns,activities,direct in cases:
        records=backbone_records(n,edges);k=len(activities);h=len(edges)
        law=[F(0)]*(1<<(k+h))
        for mask,state,weight in records:
            table=matching_law({state:weight},rows,columns,activities)
            for mark,w in enumerate(table):law[mark+(mask<<k)]=w
        literal_counts=None
        if direct:
            raw,literal_counts=literal(n,edges,rows,columns,activities);assert raw==law
        # Check full OR law and every Hessian minor for all partial backbone conditions.
        from itertools import product
        parameter_conditions=0;alljoined=0
        for status in product((-1,0,1),repeat=h):
            row=defaultdict(F)
            for mask,state,w in records:
                if all(s==-1 or (mask>>j&1)==s for j,s in enumerate(status)):row[state]+=w
            if not sum(row.values()):continue
            expected=matching_law(dict(row),rows,columns,activities)
            represented,params=forced(dict(row),rows,columns,activities)
            assert represented==[w/sum(expected)for w in expected]
            parameter_conditions+=1
            if set(row)=={(0,0,0)}:alljoined+=1
        bg,laws,checks=condition_checks(law,k,h)
        assert parameter_conditions==bg
        report['cases'].append({'backbone_vertices':n,'backbone_edges':h,'matching_edges':k,
            'full_literal_configuration_comparison':direct,'literal_forest_counts':literal_counts,
            'all_Hessian_principal_minors_and_OR_laws_verified':bg,
            'all_ports_already_connected_conditions':alljoined,
            'matching_conditional_laws':laws,'unordered_increasing_event_inequalities':checks})
        print('PASS:',n,'backbone vertices;',k,'matching edges;',bg,'backbone conditions',flush=True)
    report['status']='PASS: exact Hessian, law, combined conditioning and zero-boundary checks'
    (HERE/'arbitrary_backbone_matching_ant_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
