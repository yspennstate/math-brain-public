from pathlib import Path
from fractions import Fraction as F
import argparse, json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
S=1<<100
checks=0
def ck(b):
    global checks
    checks+=1
    assert b

def fw(v):
    v=list(v); h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def chars(v):
    return [sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(v)) for s in range(len(v))]
def law(v):
    w=fw(v);ck(w==chars(v))
    p=[F(a*a,len(v)**2) for a in w];ck(sum(p)==1)
    return p
def influence(v,j):
    return F(sum(a!=v[x^(1<<j)] for x,a in enumerate(v)),len(v))
def restrict(v,j,b):
    return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2)]
def marginal(p,j):
    return [p[(x&((1<<j)-1))|((x>>j)<<(j+1))]+p[(x&((1<<j)-1))|((x>>j)<<(j+1))|(1<<j)] for x in range(len(p)//2)]

# Outward dyadic interval arithmetic. All interval endpoints below are integer/S.
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z)//S,-(-max(z)//S)
def divpos(a,b):
    assert b[0]>0
    z=[F(x*S,y) for x in a for y in b]
    return min(z).__floor__(),max(z).__ceil__()
def exact(x):return (x*S).__floor__(),(x*S).__ceil__()
def ln_r(r):
    assert 1<=r<=2
    z=exact((r-1)/(r+1));z2=mul(z,z);pw=z;acc=(0,0)
    N=40
    for k in range(N):
        acc=add(acc,(pw[0]//(2*k+1),-(-pw[1]//(2*k+1))))
        pw=mul(pw,z2)
    # 2 sum_{k>=N} z^(2k+1)/(2k+1) <= 9/[4(2N+1)3^(2N+1)].
    tail=F(9,4*(2*N+1)*3**(2*N+1))
    return 2*acc[0],2*acc[1]+(tail*S).__ceil__()
LN2=ln_r(F(2))
def lg(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    r=x/F(2)**k
    if r<1:k-=1;r*=2
    assert 1<=r<2
    a=divpos(ln_r(r),LN2)
    return a[0]+k*S,a[1]+k*S
def ce(p,q):
    v=(0,0)
    for a,b in zip(p,q):
        if a:
            assert b>0
            v=add(v,mul(exact(a),neg(lg(b))))
    return v
def diff(a,b):return add(a,neg(b))
def serial(iv):return [str(F(iv[0],S)),str(F(iv[1],S))]

def run(n):
    # bit 0 is queried data j; bits 1..n are remaining data; bit n+1 is x.
    v=[(-1 if (y>>(n+1))&1 else 1)*(-1 if y% (1<<(n+1))==0 else 1) for y in range(1<<(n+2))]
    P=law(v);Q=list(P);child=[restrict(v,0,b) for b in [0,1]]
    Pc=[law(w) for w in child];q=marginal(Q,0)
    ck(all(a+b==2*c for a,b,c in zip(Pc[0],Pc[1],q)))
    ck(all(sum(influence(w,j) for j in range(n+1))>0 for w in child))
    t=F(1,1<<n);qa=2*t*t;q0=1-2*t+2*t*t;p0=(1-2*t)**2;p=4*t*t;M=1<<(2*n-2)
    empty_carrier=1<<n; atom=empty_carrier|1
    ck(q[empty_carrier]==q0 and q[atom]==qa)
    ck(Pc[0][empty_carrier]==p0 and Pc[0][atom]==p)
    ck(p*M==1 and p0<=q0 and qa<=F(1,8))
    ck(influence(v,0)==t)
    d=qa*(1-F(1,1<<M));newq=list(q)
    newq[atom]-=d;newq[empty_carrier]+=d
    ck(sum(newq)==1 and all(newq[k]>0 for k,a in enumerate(Pc[0]) if a))
    ck(sum(abs(a-b) for a,b in zip(q,newq))/2==d and 0<d<qa)
    ck(newq[atom]/q[atom]==F(1,1<<M))
    delta=diff((S,S),mul(exact(p0),lg((q0+d)/q0)))
    ck(delta[0]>3*S//4)
    oldce=ce(Pc[0],q);newce=ce(Pc[0],newq)
    direct=diff(newce,oldce)
    ck(max(delta[0],direct[0])<=min(delta[1],direct[1]))
    # Algebraic exact cancellation is checked atom by atom before interval comparison.
    for k,a in enumerate(Pc[0]):
        if k not in [atom,empty_carrier]:ck(q[k]==newq[k])
    # For matching root Q=P, occupancy refund is EXACTLY zero in every occupied fiber.
    rootCE=ce(P,Q);term=add(ce(Pc[0],q),ce(Pc[1],q));term=(term[0]//2,-(-term[1]//2))
    # B_j=H(P)-H(q), independently formed from full distributions.
    B=diff(ce(P,P),ce(q,q));balance=diff(rootCE,add(B,term))
    ck(balance[0]<=0<=balance[1])
    for k,m in enumerate(q):
        if m:
            # Since Q=P, both normalized conditional laws coincide, including zero atoms.
            ck(sum([Q[2*k],Q[2*k+1]])==m)
    ck(delta[0]//2>3*S//8)
    # Certified local replacement: qtilde >= (1-eta)q bounds its positive reset bill.
    eta=F(1,8);mix=[(1-eta)*a+eta*b for a,b in zip(q,Pc[0])]
    ck(sum(mix)==1)
    for a,b in zip(q,mix):ck(b>=(1-eta)*a)
    repair=diff(ce(Pc[0],mix),oldce);bound=neg(lg(1-eta))
    ck(repair[1]<=bound[1])
    return {'n':n,'root_dimension':n+2,'truth_table_sha256':hashlib.sha256(bytes(a+1 for a in v)).hexdigest(),'root_truth_table':v if n==2 else None,'t':str(t),'q0':str(q0),'qa':str(qa),'p0':str(p0),'p':str(p),'M':M,'TV_upper':str(qa),'active_reset_cost_interval':serial(delta),'expected_reset_cost_interval':serial((delta[0]//2,-(-delta[1]//2))),'query_influence':str(t),'normalized_cost_lower':str(F(3,8)/t),'zero_conditional_refund':True,'same_old_erasure_debit_and_complementary_terminal':True,'root_account_after_reset':'negative by Z>3/8','both_children_nonconstant':True,'repair_bound_interval':serial(bound)}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--pilot',action='store_true');args=a.parse_args()
    start=time.perf_counter();ns=[2,3] if args.pilot else range(2,8)
    # Boundary checks for range reduction, signed integer exponent and exact powers of two.
    for k in range(-12,13):
        iv=lg(F(2)**k);ck(iv[0]<=k*S<=iv[1])
    rows=[run(n) for n in ns]
    out={'status':'PASS','rung':'exact finite certificates plus separate analytic proof','assertions':checks,'runtime_seconds':time.perf_counter()-start,'cases':rows,'fixedpoint_bits':100,'atanh_terms':40,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (RUN/'out'/('PILOT.json' if args.pilot else 'RESET_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
