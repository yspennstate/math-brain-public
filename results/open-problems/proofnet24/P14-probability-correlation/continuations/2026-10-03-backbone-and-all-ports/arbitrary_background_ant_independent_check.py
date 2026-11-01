#!/usr/bin/env python3
"""Independent original-star enumeration of the arbitrary-H matching extension."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def forest(n,edges,mask):
    parent=list(range(n));weight=F(1)
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for k,(i,j,w) in enumerate(edges):
        if mask>>k&1:
            i,j=find(i),find(j)
            if i==j:return None
            parent[i]=j;weight*=w
    return weight,tuple(find(i) for i in range(n))

def canonical(labels):
    names={};return tuple(names.setdefault(i,len(names)) for i in labels)

@lru_cache(None)
def star(state,row,cols):
    out=defaultdict(F)
    for chosen in range(8):
        parent=list(range(4));weight=F(1)
        def find(i):
            while parent[i]!=i:i=parent[i]
            return i
        for i in range(3):
            for j in range(i):
                if state[i]==state[j]:parent[find(i)]=find(j)
        for i,b in enumerate(cols):
            if chosen>>i&1:
                u,v=find(i),find(3)
                if u==v:break
                parent[u]=v;weight*=row*b
        else:out[canonical(tuple(find(i) for i in range(3)))]+=weight
    return dict(out)

def apply_star(law,row,cols):
    out=defaultdict(F)
    for state,w in law.items():
        for nxt,c in star(state,row,tuple(cols)).items():out[nxt]+=w*c
    return dict(out)

def initial_core(weights):
    edges=[(0,1,weights[0]),(0,2,weights[1]),(1,2,weights[2])]
    law=defaultdict(F)
    for mask in range(8):
        item=forest(3,edges,mask)
        if item:
            w,labels=item;law[canonical(labels)]+=w
    return dict(law)

def bg_clusters(rows,edges,mask):
    item=forest(len(rows),edges,mask)
    if item is None:return None
    weight,labels=item;sums=defaultdict(F)
    for label,a in zip(labels,rows):sums[label]+=a
    return weight,list(sums.values())

def background(rows,edges,B):
    Z=Z1=Z2=EU=EG=EU2=F(0)
    for mask in range(1<<len(edges)):
        item=bg_clusters(rows,edges,mask)
        if item is None:continue
        w,clusters=item;d=F(1)
        for a in clusters:d*=1+B*a
        W=sum(a/(1+B*a) for a in clusters)
        minus=sum(a*a/(1+B*a)**2 for a in clusters)
        U=sum(a*a/(1+B*a) for a in clusters)
        G=sum(a**3/(1+B*a)**2 for a in clusters)
        Z+=w*d;Z1+=w*d*W;Z2+=w*d*(W*W-minus)
        EU+=w*d*U;EG+=w*d*G;EU2+=w*d*U*U
    U=EU/Z;Gamma=EG/Z+B*(EU2/Z-U*U)
    apex=list(edges)+[(len(rows),i,B*a) for i,a in enumerate(rows)]
    direct=[F(0)]*3
    for mask in range(1<<len(apex)):
        item=forest(len(rows)+1,apex,mask)
        if item:
            w,_=item;k=(mask>>len(edges)).bit_count()
            direct[0]+=w;direct[1]+=w*k/B;direct[2]+=w*k*(k-1)/(B*B)
    assert direct==[Z,Z1,Z2]
    logsecond=Z2/Z-(Z1/Z)**2
    assert U/B-Gamma==-logsecond/B>=0
    return Z,U,Gamma,logsecond

def joint(rows,bgrows,cols,core,activities,bgedges):
    k=len(activities);out=[F(0)]*(1<<(k+len(bgedges)))
    for hm in range(1<<len(bgedges)):
        item=bg_clusters(bgrows,bgedges,hm)
        if item is None:continue
        weight,clusters=item;start=initial_core(core)
        for a in clusters:start=apply_star(start,a,cols)
        for mm in range(1<<k):
            law=start;factor=weight
            for i,w in enumerate(activities):
                a,b=rows[2*i:2*i+2]
                if mm>>i&1:
                    law=apply_star(law,a+b,cols);factor*=w
                else:law=apply_star(apply_star(law,a,cols),b,cols)
            out[mm+(hm<<k)]=factor*sum(law.values())
    return out

def forced_or(rows,cols,core,activities,U,Gamma):
    B=sum(cols);J=cols[0]*cols[1]*cols[2];b0,b1,b2=cols;p,q,r=core
    S=1+p+q+r+p*q+p*r+q*r
    L=b0*b1+b0*b2+b1*b2+p*b2*(b0+b1)+q*b1*(b0+b2)+r*b0*(b1+b2)
    d=lambda x:1+B*x;alpha=lambda x:x*x/d(x);gamma=lambda x:x**3/d(x)**2
    U+=sum(map(alpha,rows));Gamma+=sum(map(gamma,rows))
    A=S+L*U+J*Gamma+B*J*U*U;M=L+2*B*J*U;K=2*B*J
    theta=[];t=[];h=[]
    for i,w in enumerate(activities):
        a,b=rows[2*i:2*i+2]
        delta=alpha(a+b)-alpha(a)-alpha(b)
        epsilon=gamma(a+b)-gamma(a)-gamma(b)
        c=d(a+b)/(d(a)*d(b))
        theta.append(c*w/(1+c*w));t.append(delta*theta[-1])
        h.append(M+J*epsilon/delta+B*J*delta)
    assert min(h)**2>K*A and 2*min(h)>max(h)
    k=len(theta);Y={0:A}
    for i in range(k):Y[1<<i]=h[i]*t[i]
    for i,j in combinations(range(k),2):Y[(1<<i)+(1<<j)]=K*t[i]*t[j]
    Ysum=sum(Y.values());out=[F(0)]*(1<<k)
    for forced,w in Y.items():
        for noise in range(1<<k):
            p=F(1)
            for i,tt in enumerate(theta):p*=tt if noise>>i&1 else 1-tt
            out[forced|noise]+=w*p/Ysum
    return out

@lru_cache(None)
def events(block,k):
    positions=[i for i in range(k) if block>>i&1]
    r=len(positions);proper=[]
    for selected in range(1, (1<<(1<<r))-1):
        good=True
        for i in range(1<<r):
            if selected>>i&1:
                for j in range(r):
                    if not (selected>>(i|(1<<j)))&1:good=False;break
            if not good:break
        if good:
            proper.append(sum(1<<x for x in range(1<<k)
                if selected>>sum(((x>>pos)&1)<<j for j,pos in enumerate(positions))&1))
    return tuple(proper)

def condition_checks(law,k,h):
    matching_laws=checks=bg_laws=0
    for hs in product((-1,0,1),repeat=h):
        base=[F(0)]*(1<<k)
        for x,w in enumerate(law):
            if all(v==-1 or ((x>>(k+j))&1)==v for j,v in enumerate(hs)):
                base[x&((1<<k)-1)]+=w
        if not sum(base):continue
        bg_laws+=1
        for ms in product((-1,0,1),repeat=k):
            weights=[w if all(v==-1 or ((x>>i)&1)==v for i,v in enumerate(ms)) else F(0)
                     for x,w in enumerate(base)]
            total=sum(weights)
            if not total:continue
            matching_laws+=1
            free=sum(1<<i for i,v in enumerate(ms) if v==-1)
            for left in range(1,1<<k):
                if left&free!=left:continue
                for right in range(left+1,1<<k):
                    if right&free!=right or left&right:continue
                    for e in events(left,k):
                        E=sum(w for x,w in enumerate(weights) if e>>x&1)
                        for f in events(right,k):
                            FF=sum(w for x,w in enumerate(weights) if f>>x&1)
                            both=sum(w for x,w in enumerate(weights) if (e&f)>>x&1)
                            assert total*both<=E*FF
                            checks+=1
    return bg_laws,matching_laws,checks

def main():
    cases=[
      ([F(i+1,i+2)for i in range(6)],[F(1,3),F(5,4),F(7,5)],
       [F(2,3),F(3,4),F(5,7)],[F(1,3),F(2,5),F(3,7)],[F(2,3),F(4,5),F(6,7)],
       [(0,1,F(1,2)),(1,2,F(2,3)),(0,2,F(3,4))]),
      ([F(i+2,3)for i in range(6)],[F(1),F(2),F(3),F(4)],
       [F(1),F(2),F(4)],[F(0),F(3),F(2)],[F(1,3),F(2),F(7)],
       [(i,j,F(i+j+1,3))for i,j in combinations(range(4),2)])]
    report={'route':'no author imports; all original8-choice stars and exact monotone events', 'cases':[]}
    for rows,bgrows,cols,core,acts,edges in cases:
        B=sum(cols);Z,U,Gamma,logsecond=background(bgrows,edges,B)
        law=joint(rows,bgrows,cols,core,acts,edges);k=len(acts)
        marginal=[sum(law[x] for x in range(len(law)) if x&((1<<k)-1)==m) for m in range(1<<k)]
        represented=forced_or(rows,cols,core,acts,U,Gamma)
        assert [w/sum(marginal)for w in marginal]==represented
        bglaws,mlaws,checks=condition_checks(law,k,len(edges))
        report['cases'].append({'matching_edges':k,'background_vertices':len(bgrows),
            'background_edges':len(edges),'apex_partition':str(Z),'U':str(U),'Gamma':str(Gamma),
            'logZ_second':str(logsecond),'forced_OR_configuration_identity':True,
            'valid_H_partial_conditionings':bglaws,'matching_conditional_laws':mlaws,
            'all_disjoint_increasing_event_inequalities':checks})
        print('PASS:',k,'matching edges;',len(edges),'background edges;',checks,'inequalities',flush=True)
    report['status']='PASS: exact apex, derivative, OR law and conditional NA checks'
    (HERE/'arbitrary_background_ant_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
