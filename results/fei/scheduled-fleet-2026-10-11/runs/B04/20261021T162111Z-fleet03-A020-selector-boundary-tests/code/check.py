from pathlib import Path
from fractions import Fraction as Q
import importlib.util, sys, json, time, argparse
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T062539Z-fleet05-A020-selector-boundary-tests/code/check.py'
sp=importlib.util.spec_from_file_location('old',old); a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
def plus(*terms):
    z={}
    for f,c in terms:a.formadd(z,f,c)
    return z
def const(c):return {2:Q(c)} if c else {}
def positive(f):
    lo,_=a.interval(f);ck(lo>0)
def less(f,c):positive(plus((const(c),1),(f,-1)))
def equal(f,g):ck(plus((f,1),(g,-1))=={})
def marginal(p,i):
    m=1<<i
    return [p[(t&(m-1))|((t>>i)<<(i+1))]+p[(t&(m-1))|((t>>i)<<(i+1))|m] for t in range(len(p)//2)]
def restrict(f,i,b):
    m=1<<i
    return [f[(t&(m-1))|((t>>i)<<(i+1))|(b<<i)] for t in range(len(f)//2)]
def full(core):
    N=len(core);s=[-1,1,1,1]
    return [1 if not(t&1) else core[(t>>1)%N]*s[(t>>1)//N] for t in range(8*N)]
def core_child(k,q,t,active):
    # Remaining core coordinates are u, then k-t unqueried v bits.
    return [(-1)**q if active and (y>>1)==0 else (-1)**(y&1) for y in range(1<<(k-t+1))]
def node_ref_formula(k,t):
    d=Q(1,1<<k);r=k-t;z=(1<<t)*d*d
    cq=[Q(0)]*(1<<(r+1))
    for T in range(len(cq)):
        cq[T]=((1-2*d+z) if T==1 else (1+z) if T==0 else z)/2
    ck(sum(cq)==1)
    return [
        (cq[T%len(cq)]/4+int(T==0))/4 for T in range(4*len(cq)) for e in range(2)]
def case(k):
    d=Q(1,1<<k)
    h=[(-1)**(z&1) if (z>>2)==0 else (-1)**((z>>1)&1) for z in range(1<<(k+2))]
    ph=a.law(h);qh=[(p+int(i==1))/2 for i,p in enumerate(ph)]
    root=a.activation(h,qh);Qroot=root['QF'];froot=root['F'];Croot=root['CE']
    ck(sum(Qroot)==1);ck(a.a.energy(froot)==(3+k*d)/2)
    # Root reference is explicitly uniform at both gate frequencies.
    ck(all(Qroot[2*T]==Qroot[2*T+1] for T in range(len(Qroot)//2)))
    ref=marginal(Qroot,1);costs=[];energies=[];posdef=[];depths=[]
    for t in range(k+1):
        ck(ref==node_ref_formula(k,t));ck(sum(ref)==1)
        C={};I=Q(0);D={};Ncredit={};lawavg=[Q(0)]*len(ref)
        for q in [0,1]:
            for active,w in [(True,Q(1,2*(1<<t))),(False,(1-Q(1,1<<t))/2)]:
                if not w:continue
                core=core_child(k,q,t,active);f=full(core);p=a.law(f);ce=a.ce(p,ref);inf=a.a.energy(f)
                ck(sum(p)==1);ck(all(not x or y>0 for x,y in zip(p,ref)))
                a.formadd(C,ce,w);I+=w*inf
                for i,x in enumerate(p):lawavg[i]+=w*x
                deficit=plus((ce,1),(const(4*inf),-1))
                lo,hi=a.interval(deficit)
                if lo>0:a.formadd(D,deficit,w)
                elif hi<0:a.formadd(Ncredit,deficit,-w)
                else:ck(deficit=={})
        er=a.law(froot)
        er=marginal(er,1)
        for j in range(t):er=marginal(er,2)
        ck(lawavg==er)
        equal(C,a.ce(er,ref))
        ck(I==Q(3,2)+(k-t-1)*d/2)
        totalL=plus((Croot,1),(C,-1));slack=plus((const(4*I),1),(C,-1))
        removed=(t+1)*d/2
        equal(slack,plus((const(4*a.a.energy(froot)),1),(Croot,-1),(const(-4*removed),1),(totalL,1)))
        positive(plus((slack,1),(const(Q(-5,4)),1)))
        equal(plus((Ncredit,1),(D,-1)),slack)
        costs.append(C);energies.append(I);posdef.append(D)
        depths.append({'t':t,'average_CE_prime_log':a.jsonform(C),'average_influence':str(I),'signed_slack_prime_log':a.jsonform(slack),'positive_terminal_deficit_prime_log':a.jsonform(D),'negative_terminal_credit_prime_log':a.jsonform(Ncredit)})
        if t<k:
            newref=marginal(ref,2)
            # Direct full-code identity at BOTH active children, keeping both outcomes.
            for q in [0,1]:
                parent=full(core_child(k,q,t,True));cp=a.ce(a.law(parent),ref)
                c0=a.ce(a.law(restrict(parent,2,0)),newref);c1=a.ce(a.law(restrict(parent,2,1)),newref)
                L={}
                for T,p in enumerate(a.law(parent)):
                    if p:
                        U=(T&3)|((T>>3)<<2)
                        a.formadd(L,a.logterm(newref[U]/ref[T],p))
                equal(cp,plus((c0,Q(1,2)),(c1,Q(1,2)),(L,1)))
            ref=newref
    # Closed terminal formulas, independent of the spectrum grouping above.
    Cpar=plus((const(5),1),(a.logterm((9+d)*(1-d),Q(-1,2)),1))
    Ccon=plus((const(5),1),(a.logterm(9+d,Q(-5,8)),1),(a.logterm(1+d,Q(-3,8)),1))
    Cend=plus((Cpar,1-d),(Ccon,d));equal(Cend,costs[-1])
    near=full(core_child(k,0,k-1,True))
    nearcost=a.ce(a.law(near),node_ref_formula(k,k-1))
    nearformula=plus((const(6+Q(k,4)),1),(a.logterm(18+d,Q(-17,32)),1),(a.logterm(2+d,Q(-3,32)),1),(a.logterm(2-3*d,Q(-1,8)),1))
    equal(nearcost,nearformula);ck(a.a.energy(near)==Q(11,8))
    if k>=8:positive(plus((nearcost,1),(const(Q(-11,2)),1)))
    less(Ccon,Q(25,8));positive(plus((Cend,1),(const(Q(-53,16)),1)))
    if k>=6:positive(plus((Ccon,1),(const(-3),1)));positive(posdef[-1])
    else:less(Ccon,3)
    # The signed (positive-only) terminal shortfall is kept, not canceled silently.
    if k>=6:less(posdef[-1],d/16)
    # Preserve original half-core reserve and exact first insertion + conversion.
    child=core_child(k,0,0,True);pc=a.law(child);qc=[(p+int(i==0))/2 for i,p in enumerate(pc)]
    cc=a.ce(pc,qc);S=plus((const(2*a.a.energy(child)),1),(cc,Q(-1,2)))
    fresh0=a.activation(child,qc);fresh1=a.activation(core_child(k,1,0,True),qc)
    freshavg=plus((fresh0['CE'],Q(1,2)),(fresh1['CE'],Q(1,2)))
    E=plus((costs[0],1),(freshavg,-1));less(E,d*d)
    J=plus((Croot,1),(freshavg,-1));less(J,Q(5,8))
    afterq=plus((costs[0],1),(costs[-1],-1))
    total_debit=plus((J,1),(afterq,1))
    equal(total_debit,plus((Croot,1),(Cend,-1),(E,1)))
    remain=plus((S,1),(total_debit,-1));positive(plus((remain,1),(const(Q(-5,128)),1)))
    positive(plus((remain,1),(posdef[-1],-1),(const(Q(-1,32)),1)))
    ck(9**5<2**16);ck(9**4<2**13);ck((Q(73,8)**4)<2**13);ck(Q(9,8)**4<2)
    return {'k':k,'depths':depths,'original_half_core_bank':a.jsonform(S),'booked_first_debit':a.jsonform(J),'conversion':a.jsonform(E),'all_remaining_queries_debit':a.jsonform(afterq),'remaining_bank':a.jsonform(remain),'final_constant_cost':a.jsonform(Ccon),'nonconstant_penultimate_CE':a.jsonform(nearcost),'status':'PASS'}
def main(pilot):
    start=time.perf_counter();rows=[]
    for k in ([3] if pilot else range(3,9)):
        rows.append(case(k));ck(time.perf_counter()-start<60)
        (R/'out').mkdir(exist_ok=True)
        (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps({'status':'PASS','cases':len(rows),'assertions':COUNT,'rows':rows,'runtime_seconds':time.perf_counter()-start},indent=2),encoding='utf-8')
    print(json.dumps({'status':'PASS','cases':len(rows),'assertions':COUNT,'runtime_seconds':time.perf_counter()-start}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');main(p.parse_args().pilot)
