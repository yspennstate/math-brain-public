import sys,json,time,itertools
from pathlib import Path
from functools import lru_cache
from exact import *
ROOT=Path(__file__).resolve().parents[1]
delta=Q(1,64); U=Q(2,64); checks=0
def eq(a,b):
    global checks
    checks+=1; assert plus(a,mul(b,-1))=={},(a,b)
def positive(a):
    global checks
    checks+=1; assert bounds(a)[0]>=0,a
def G(a):
    s=Q(sum(a),len(a)); r=1-delta+delta*s*s
    return plus(phi(r),mul(phi(s*s),-delta),const(6*delta*(1-s*s)))
def J(a,d):
    s=Q(sum(a),len(a)); r=1-delta+delta*s*s
    return plus(G(a),mul(lg(r),1-Q(1,2**d)))
@lru_cache(None)
def qdata(d,x):
    ans=[Q(1)]
    for b in range(2):
        j=min(3,max(0,d-3*b)); u=(x>>(3*b))&((1<<j)-1)
        if j==0: q=[Q(9,16)]+[Q(1,16)]*7
        elif j==1: q=[Q(1,4)]*4 if u==0 else [Q(13,16)]+[Q(1,16)]*3
        elif j==2: fav=1 if u==0 else 0; q=[Q(15,16) if i==fav else Q(1,16) for i in range(2)]
        else: q=[Q(1)]
        ans=[p*r for r in q for p in ans]
    return tuple(ans)
@lru_cache(None)
def state(v,d,x,a):
    nd=2**(6-d); f=[]
    for z in range(len(a)):
        for y in range(nd):
            xx=x+(y<<d); b=g(xx&7)*g(xx>>3)
            f.append(b*(a[z] if xx==v else 1))
    P=spectrum(tuple(f)); pa=spectrum(a); R=[delta*p for p in pa]; R[0]+=1-delta
    q=qdata(d,x); refs=[u*r for r in R for u in q]
    C=ce(P,refs); H=entropy(P)
    I=sum(inf(f,i) for i in range(6-d))
    # Independent physical-edge enumeration is used by inf, not Fourier degree.
    return C,H,I,entropy(pa), tuple(f)
def cut(v,d,leaves):
    C=H=L={}; I=Q(0); weight=Q(0)
    for x,a,p in leaves:
        w=Q(1,2**d)*p; c,h,i,ha,f=state(v,d,x,a)
        C=plus(C,mul(c,w)); H=plus(H,mul(h,w)); I+=w*i; weight+=w
        if x==(v&((1<<d)-1)): L=plus(L,mul(ha,delta*p))
    assert weight==1
    B=plus(const(4*I-U),L,mul(C,-1)); D=plus(C,mul(H,-1))
    return B,D,H,L
def run(v,a,policy):
    leaves=[(0,a,Q(1))]; gamma={}; E={}; K={}
    base0=cut(v,0,leaves); invariant=plus(base0[0],base0[1]); L0=base0[3]
    for d in range(6):
        pure=[(x,a,Q(1)) for x in range(2**d)]
        baseline=cut(v,d,pure)
        now=cut(v,d,leaves)
        eq(now[0],plus(baseline[0],gamma)); eq(plus(now[0],now[1],E),invariant)
        eq(plus(now[3],K),L0); positive(plus(now[0],const(-Q(26,576))))
        # One full active split; second split stops on one actual control outcome.
        when=(d==1 if policy==0 else d==2)
        second=(d==3 if policy==0 else d==4)
        if when or second:
            updated=[]
            for x,aa,p in leaves:
                active=x==(v&((1<<d)-1))
                selected=active and ((when and len(aa)==4) or (second and len(aa)==2 and p==Q(1,2) and aa is chosen))
                # Preserve the chosen physical child by tuple identity even when
                # the two restricted truth tables happen to have equal values.
                if second and selected and already: selected=False
                if not selected: updated.append((x,aa,p)); continue
                if second: already=True
                i=(0 if policy==0 else 1) if when else 0
                kids=[tuple(restrict(aa,i,b)) for b in (0,1)]
                if when: chosen=kids[policy]; already=False
                old=state(v,d,x,aa); new=[state(v,d,x,k) for k in kids]
                gap=plus(J(aa,d),mul(plus(*(J(k,d) for k in kids)),-Q(1,2)))
                positive(gap); gamma=plus(gamma,mul(gap,p))
                dh=plus(old[1],mul(plus(*(s[1] for s in new)),-Q(1,2)))
                dha=plus(old[3],mul(plus(*(s[3] for s in new)),-Q(1,2)))
                K=plus(K,mul(dha,delta*p)); E=plus(E,mul(dha,delta*p),mul(dh,-Q(1,2**d)*p))
                updated.extend((x,k,p/2) for k in kids)
            leaves=updated; now=cut(v,d,leaves)
            eq(now[0],plus(baseline[0],gamma)); eq(plus(now[0],now[1],E),invariant); eq(plus(now[3],K),L0)
        if d==5: break
        old=cut(v,d,leaves); newleaves=[]; em={}
        for x,aa,p in leaves:
            c,h,i,ha,f=state(v,d,x,aa); kids=[state(v,d+1,x+(b<<d),aa) for b in (0,1)]
            dh=plus(h,mul(plus(*(s[1] for s in kids)),-Q(1,2)))
            em=plus(em,mul(plus(const(4*inf(f,0)),mul(dh,-1)),Q(1,2**d)*p))
            newleaves.extend((x+(b<<d),aa,p) for b in (0,1))
        leaves=newleaves; new=cut(v,d+1,leaves); E=plus(E,em)
        bp=cut(v,d+1,[(x,a,Q(1)) for x in range(2**(d+1))])
        eq(plus(new[0],mul(old[0],-1)),plus(bp[0],mul(baseline[0],-1)))
        eq(new[0],plus(bp[0],gamma)); eq(plus(new[0],new[1],E),invariant)
    return len(leaves)
def main():
    start=time.monotonic(); pilot='--pilot' in sys.argv
    cases=[(v,tuple(1 if (mask>>z)&1 else -1 for z in range(4)),p) for v in [0,1,7,63] for mask in range(16) for p in (0,1)]
    if pilot: cases=[cases[i] for i in [0,19,84,127]]
    for v,a,p in cases:
        run(v,a,p)
        assert time.monotonic()-start<(60 if pilot else 240)
    out={'status':'PASS','cases':len(cases),'assertions':checks,'elapsed_seconds':time.monotonic()-start,'peak_memory':'unmeasured','arithmetic':'Fraction/prime-log exact; outward rational bounds','helper':'exact.py stage8 copy'}
    (ROOT/'out'/('pilot.json' if pilot else 'main.json')).write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__': main()
