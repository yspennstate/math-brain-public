"""Independent literal-graph audit of the all-port adjacent theorem.

All original graph vertices are retained in the connectivity DP; no terminal
transfer helper or component contraction is used for marked coefficients.
The apex polynomial is separately constructed at every degree, including
its derivatives at s=0. Exact integer/Fraction arithmetic only.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

def merge(p,u,v):
    a,b=p[u],p[v]
    if a==b:return None
    a,b=min(a,b),max(a,b)
    return tuple(a if x==b else x for x in p)

def dp(n,edges,apex=False):
    # Edge: (u,v,weight,state,tag), tag -1 for ordinary edges; otherwise a
    # mutual-edge indicator bit, or one increment of apex degree.
    states={(tuple(range(n)),0):Q(1)}
    for u,v,w,required,tag in edges:
        out=defaultdict(Q)
        for (p,mark),mass in states.items():
            if required!='present':out[p,mark]+=mass
            if required!='absent' and w:
                joined=merge(p,u,v)
                if joined is not None:
                    nextmark=mark if tag<0 else mark+1 if apex else mark|(1<<tag)
                    out[joined,nextmark]+=mass*w
        states={key:value for key,value in out.items() if value}
    return states

def powers_at(coeff,s,derivative):
    total=Q(0)
    for k,c in enumerate(coeff):
        if k<derivative:continue
        factor=1
        for d in range(derivative):factor*=k-d
        total+=c*factor*s**(k-derivative)
    return total

def check(case):
    n,H,beta,columns,rho=[case[k] for k in ('n','H','beta','columns','rho')]
    a,b,c=columns;s=a+b+c
    # Actual backbone partition states, aggregated only after literal edge
    # cycle tests. Component-dependent quantities depend just on that state.
    base=dp(n,H);assert base
    D=EU=EG=EU2=Q(0)
    for (part,mark),mass in base.items():
        assert mark==0
        x=defaultdict(Q)
        for i,v in enumerate(beta):x[part[i]]+=v
        value=mass
        for row in x.values():value*=1+s*row
        U=sum((row**2/(1+s*row) for row in x.values()),Q(0))
        G=sum((row**3/(1+s*row)**2 for row in x.values()),Q(0))
        D+=value;EU+=value*U;EG+=value*G;EU2+=value*U*U
    U=EU/D;Gamma=EG/D+s*(EU2/D-U*U)
    assert U>=0 and Gamma>=0
    assert bool(U)==bool(sum(beta))
    # Independent entire apex polynomial. Its weights are beta, not s beta;
    # the selected-apex-spoke count records the exponent of the scalar s.
    ap=dp(n+1,H+[(n,i,v,'free',0) for i,v in enumerate(beta)],apex=True)
    ac=[Q(0)]*(n+1)
    for (part,k),mass in ap.items():ac[k]+=mass
    D0,Dp,Dpp=[powers_at(ac,s,d) for d in range(3)]
    assert D0==D
    log2=Dpp/D-(Dp/D)**2
    assert log2<=0
    if s:assert U/s-Gamma==-log2/s>=0
    # The entire uncontracted H + three added vertices + mutual triangle.
    spokes=[(n+k,i,v*x,'free',-1) for k,v in enumerate(columns) for i,x in enumerate(beta) if v*x]
    triangle=[(n,n+1,Q(1),'free',0),(n+1,n+2,Q(1),'free',1),(n,n+2,Q(1),'free',2)]
    literal=dp(n+3,H+spokes+triangle)
    full=[Q(0)]*8
    for (part,mask),mass in literal.items():full[mask]+=mass
    assert full[7]==0
    # Incorporate the fixed outer activity only after all eight literal
    # indicator coefficients have been evaluated independently.
    coeff=[full[k]+rho*full[k|4] for k in range(4)]
    l=a*b+a*c+b*c;j=a*b*c
    expected=[D*(1+rho+(l+rho*b*(a+c))*U+j*Gamma+s*j*U*U),
              D*(1+rho+c*(a+b)*U),D*(1+rho+a*(b+c)*U),D]
    assert coeff==expected
    A,E,F,C=coeff;R=E*F-A*C
    assert R==D**2*(rho*(1+rho)+a*c*((1+2*rho)*U+a*c*U*U-b*Gamma))
    lower=D**2*(rho*(1+rho)+a*c*((((a+c)/s) if s else Q(0))+2*rho)*U+a*a*c*c*U*U)
    assert R>=lower>=0
    strict=bool(rho or (a*c and sum(beta)))
    assert bool(R)==strict
    # Explicit covariance at different positive marked activities, using
    # the literal four-mass law rather than a derivative implementation.
    for we,wf in ((Q(1),Q(1)),(Q(2,3),Q(5,7)),(Q(11),Q(13))):
        Z=A+E*we+F*wf+C*we*wf
        pe=(E*we+C*we*wf)/Z;pf=(F*wf+C*we*wf)/Z;pef=C*we*wf/Z
        covariance=pef-pe*pf
        assert covariance==-we*wf*R/Z**2<=0
    return {'name':case['name'],'backbone_vertices':n,'nonzero_profiles':sum(bool(x) for x in beta),
            'backbone_edges':len(H),'profile':beta,'columns':columns,'outer_activity':rho,
            'whole_literal_triangle_coefficients':full,'four_marked_coefficients':coeff,
            'apex_polynomial_coefficients':ac,'D_Dprime_Dsecond':(D,Dp,Dpp),
            'U_Gamma_logsecond':(U,Gamma,log2),'Rayleigh':R,'lower_bound':lower,
            'strict':strict,'status':'PASS'}

def graph(n,weights,state=None):
    return [(u,v,Q(w),state.get((u,v),'free') if state else 'free',-1) for u,v,w in weights]

def main():
    cases=[]
    def add(name,n,H,beta,col,rho):cases.append({'name':name,'n':n,'H':H,'beta':list(map(Q,beta)),
                                              'columns':list(map(Q,col)),'rho':Q(rho)})
    H4=graph(4,[(0,1,2),(0,2,3),(0,3,5),(1,2,7),(1,3,11),(2,3,13)])
    add('four common ports: nonuniform K4 backbone, rho below one',4,H4,[1,2,3,5],[2,3,7],Q(2,5))
    H5=graph(5,[(0,1,2),(1,2,3),(2,3,5),(3,4,7),(0,4,11),(0,2,13)])
    add('five common ports: cyclic backbone, rho zero',5,H5,[1,3,2,4,5],[1,2,3],0)
    H6=graph(6,[(i,i+1,i+2) for i in range(5)])
    add('six common ports: zero middle column',6,H6,[1,2,3,4,5,6],[2,0,3],Q(1,7))
    add('six common ports: all columns positive',6,H6,[1,2,3,4,5,6],[1,2,3],0)
    conditioned=graph(5,[(0,1,2),(1,2,3),(2,3,5),(3,4,7),(0,4,11),(0,2,13)],
                      {(0,1):'present',(1,2):'present',(0,4):'absent'})
    add('backbone conditioning merges common-neighbor vertices',5,conditioned,[1,3,2,4,5],[2,5,3],Q(1,3))
    add('all columns zero: exact apex derivatives at scalar zero',4,H4,[1,2,3,5],[0,0,0],7)
    add('all profiles zero: equality without outer edge',5,H5,[0]*5,[2,3,5],0)
    add('outer column zero: bridge equality',4,H4,[1,2,3,5],[0,2,3],0)
    Hextra=graph(6,[(0,5,2),(1,5,3),(2,5,5),(3,5,7),(4,5,11),(0,2,13),(1,3,17)])
    add('five common ports plus a non-neighbor backbone vertex',6,Hextra,[1,2,3,4,5,0],[2,3,5],Q(1,3))
    rational=graph(4,[(0,1,Q(2,3)),(0,2,Q(3,5)),(0,3,Q(5,7)),
                      (1,2,Q(7,11)),(1,3,Q(11,13)),(2,3,Q(13,17))])
    add('rational fields on every edge and profile',4,rational,[Q(1,2),Q(2,3),Q(3,5),Q(5,7)],
        [Q(2,5),Q(3,7),Q(5,11)],Q(7,13))
    zero=graph(4,[(0,1,0),(0,2,3),(0,3,5),(1,2,7),(1,3,11),(2,3,13)])
    add('zero-activity backbone field',4,zero,[1,2,3,5],[2,3,7],Q(2,5))
    results=[]
    for case in cases:
        results.append(check(case));print(case['name'],'PASS',flush=True)
    out={'status':'PASS independent literal original-graph all-port adjacent audit',
         'arithmetic':'exact Fraction; full connectivity state retained',
         'cases':results,'case_count':len(results)}
    Path(__file__).with_name('forest_all_ports_adjacent_k_independent_results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
    print('All independent literal checks PASS.',flush=True)

if __name__=='__main__':main()
