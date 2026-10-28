"""A003 original Boolean canonical reset: independent A092 implementation.

No producer helper imports. Direct characters/edges for fixed literal members;
five row classes for other declared members. The query refund is NEW here.
"""
from arithmetic import F,lg,add,sub,mul,ent,ce,h2,spectrum,edges,pretty,ROOT
from pathlib import Path
from collections import defaultdict
import json,sys,time,hashlib

checks=0
def ck(b):
    global checks
    checks+=1
    assert b,checks
def weighted_logs(terms):
    # Aggregate identical exact rational ratios before evaluating logs.
    masses=defaultdict(F)
    for w,q in terms:
        if w:masses[q]+=w
    ans=(F(0),F(0))
    for q,w in masses.items():ans=add(ans,mul(w,lg(q)))
    return ans
def close(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))

def parameters(m):
    s=F(1,2**m);e=s*s;k=1-s;mu=1-2*s;v=4*s*(1-s)
    Rj=v*(1-e-e**3)+4*s**8
    beta=2*(1-2*s)/(s*s*(1-s+s**4*(1-2*s)))
    qj=s*s*(4-3*s);u=k*Rj+s**3
    p0=(1-4*s+2*s*s)**2
    A=(1-2*s+s*s)**2;B=(2*s-s*s)**2
    o0=A+u*B/qj
    weights=[p0,(1/s-1)*4*s**4,(1/(2*s)-1)*4*qj,4*s**3,(1/(2*s)-1)*4*s**3]
    ratios=[o0/p0,(1+u/qj)/4,
            (k*8*s**8+2*s**3)/(k*beta*8*s**8+4*s**3),
            (k*v*s*s+2*s**3)/(k*beta*v*s*s+4*s**3),F(1,2)]
    ck(sum(weights)==1);ck(all(w>0 for w in weights));ck(all(q>0 for q in ratios))
    Z=mul(F(1,2),weighted_logs(zip(weights,ratios)))
    # Root vacuum-frequency fiber conditional KL, NOT a physical conditioning.
    # Q(empty,Uempty)=A, Q({j},Uempty)=u B/qj, P masses A and B.
    rho0=weighted_logs([(A+B,o0/(A+B)),(B,qj/u)])
    ck(rho0[0]>0);ck(Z[0]>0)
    netupper=sub(Z,rho0)
    ck(netupper[1]<0)
    Ig=2*m*s;If=Ig+s*s;dj=2*s-s*s
    ck(If>0 and dj>0);ck(Rj>=s)
    # Source CE, explicitly including vacuum and every occupied active atom.
    c=weighted_logs([(mu*mu,1/(mu*mu)),(4*s*s,1/Rj),((1/s-2)*4*s*s,1/(4*s**8))])
    ck(c[1]<17*Ig)
    analytic_source_upper=6*s+4*m*s*s+4*s*(8*m-2)
    ck(analytic_source_upper<=17*Ig)
    ck(1-e-e**3>F(3,4));ck(1-s+s**4*(1-2*s)>0)
    return dict(m=m,s=s,e=e,k=k,mu=mu,v=v,Rj=Rj,beta=beta,qj=qj,u=u,p0=p0,A=A,B=B,o0=o0,
                weights=weights,ratios=ratios,Z=Z,rho0=rho0,netupper=netupper,c=c,Ig=Ig,If=If,dj=dj)

def complete_floor(a,b,r,R):
    s=F(1,2**a);t=F(1,2**(a+b));e=F(1,2**(a+b+r-1));mu=1-2*s;k=1-e/s
    D=2**(a+b);L=2**r
    q=[];p=[];data=[]
    for T in range(D):
        base=mu if T==0 else (-2*s if T<2**a else F(0))
        probs=[(base+e)**2]+[e*e]*(L-1)
        mass=sum(probs)
        rp=k*R[T]+(e/s)*mu*(T==0)+2*e*t
        ck(mass>0 and rp>0)
        data.append(rp)
        p.extend(probs);q.extend([rp*x/mass for x in probs])
    ck(sum(data)==1);ck(sum(p)==sum(q)==1);ck(all(q))
    return p,q

def literal(m,par):
    s,e=par['s'],par['e'];D=2**(m+1);L=2**m
    R=[F(0)]*D;R[0]=par['mu']**2
    for T in range(1,2**m):R[T]=4*s**8
    R[1]+=par['v']*(1-e-e**3);R[2**m]+=par['v']*e
    ck(sum(R)==1);ck(R[0]==par['mu']**2);ck(R[1]==par['Rj'])
    V=[R[2*T]+R[2*T+1] for T in range(D//2)]
    beta=(1-(1-4*s)**2)/(1-V[0]);ck(beta==par['beta'])
    Rc=[(1-4*s)**2]+[beta*x for x in V[1:]]
    ck(sum(Rc)==1)
    proot,Q=complete_floor(m,1,m,R)
    pchild,Qnew=complete_floor(m-1,1,m,Rc)
    # complete_floor indexes (data T, control U); actual characters use
    # data as low physical bits, so reorder only for comparison with characters.
    n=2*m+1;N=2**n
    vals=[1-2*(u%(2**m)==0)+2*(u==0) for u in range(N)]
    w=spectrum(vals);rawp=[z*z for z in w]
    for T in range(D):
        for U in range(L):ck(proot[T*L+U]==rawp[T+(U<<(m+1))])
    inf=edges(vals);ck(sum(inf)==par['If']);ck(inf[0]==par['dj'])
    childvals=vals[0::2];other=vals[1::2];ck(set(other)=={1});ck(len(set(childvals))==2)
    wc=spectrum(childvals);pcraw=[z*z for z in wc]
    for T in range(D//2):
        for U in range(L):ck(pchild[T*L+U]==pcraw[T+(U<<m)])
    Qold=[];pavg=[]
    for T in range(D//2):
        for U in range(L):
            z=Q[(2*T)*L+U]+Q[(2*T+1)*L+U]
            q=proot[(2*T)*L+U]+proot[(2*T+1)*L+U]
            Qold.append(z);pavg.append(q)
    ck(sum(Qold)==1);ck(all(Qold))
    for i in range(len(Qold)):ck(pavg[i]==(pchild[i]+int(i==0))/2)
    Z=mul(F(1,2),weighted_logs((p,a/b) for p,a,b in zip(pchild,Qold,Qnew)))
    close(Z,par['Z'])
    # Full conditional KL direct in each root frequency fiber; all terms
    # are retained before summation, including ghosts in the denominators.
    terms=[];erasure_terms=[]
    for T in range(D//2):
        for U in range(L):
            ia=2*T*L+U;ib=(2*T+1)*L+U
            x,y=proot[ia],proot[ib];q0,q1=Q[ia],Q[ib]
            for p0,q0a in [(x,q0),(y,q1)]:terms.append((p0,p0*(q0+q1)/(q0a*(x+y))))
            erasure_terms.extend([(x,(x+y)/x),(y,(x+y)/y)])
    rho=weighted_logs(terms);B=weighted_logs(erasure_terms)
    ck(rho[0]>par['rho0'][1])
    oldcost=mul(F(1,2),add(ce(pchild,Qold),mul(-1,lg(Qold[0]))))
    newcost=mul(F(1,2),add(ce(pchild,Qnew),mul(-1,lg(Qold[0]))))
    rootcost=ce(proot,Q)
    close(rootcost,add(B,add(oldcost,rho)))
    close(sub(newcost,oldcost),Z)
    net=sub(Z,rho)
    close(net,sub(add(B,newcost),rootcost))
    ck(net[1]<0)
    # Original K44 quota is used once, with full off-child inherited CE.
    ck(add(B,newcost)[1]<rootcost[0]);ck(rootcost[1]<44*par['If'])
    return dict(m=m,root_dimension=n,root_CE=pretty(rootcost),erasure=pretty(B),
                full_query_refund=pretty(rho),signed_reset=pretty(Z),signed_net=pretty(net),
                unchanged_off_child_CE=pretty(mul(-1,lg(Qold[0]))),
                complete_new_bill=pretty(add(B,newcost)),source_CE=pretty(par['c']))

def old_debit():
    vals=[-1,1,1,1];p=[z*z for z in spectrum(vals)]
    ck(p==[F(1,4)]*4);ck(sum(edges(vals))==1)
    ck(ent(p)==(F(2),F(2)) or ent(p)[0]<=2<=ent(p)[1])
    # Every conditional spectral pair is fair; erasure exactly one bit.
    ck(p[0]==p[1] and p[2]==p[3]);ck(sum(p)==1)
    for c in [vals[0::2],vals[1::2]]:
        pc=[z*z for z in spectrum(c)];CE=ce(pc,[F(1,2)]*2);ck(CE[0]<=1<=CE[1])
    return {'booked_erasure':1,'retained_complete_tensor_CE':1,'original_tensor_cost':2,'donation_to_core':0}

def main():
    tic=time.perf_counter();pilot='--pilot' in sys.argv
    cases=[];literal_cases=[]
    for m in ([4] if pilot else [4,5,6,8,16,32]):
        a=parameters(m)
        cases.append(dict(m=m,s=str(a['s']),edit_mass=str(a['e']),query_influence=str(a['dj']),
                          source_CE=pretty(a['c']),source_price=17,signed_reset=pretty(a['Z']),
                          vacuum_fiber_refund=pretty(a['rho0']),net_upper_bound=pretty(a['netupper'])))
        if m in (4,5):literal_cases.append(literal(m,a))
    debit=old_debit()
    output=dict(status='PASS',cases=cases,literal_cases=literal_cases,prior_tensor_history=debit,
                assertions=checks,runtime_seconds=time.perf_counter()-tic,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                rung='Exact finite certificates; analytic all-m result proved separately; no Lean claim')
    file='PILOT.json' if pilot else 'VALIDATION.json'
    (ROOT/'out'/file).write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k not in ['cases','literal_cases']}))
if __name__=='__main__':main()
