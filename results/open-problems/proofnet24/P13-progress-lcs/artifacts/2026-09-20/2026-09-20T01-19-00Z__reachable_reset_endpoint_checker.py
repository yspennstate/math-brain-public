from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product
from collections import deque

getcontext().prec=180
COUNTS={1:14,2:224,3:3098,4:39774}

# ---------- exact inherited C045 endpoint compilation ----------
LOW=F(99083249,125000000)
P02_BEFORE=F(8262759427622826251,10**19)
x=F(256717,800000)
A=4*x*x
LAM=F(
10114875937111444750637950885399422919832438289108176982868202874026753,
29591135160849999997918500618240000000000000000000000000000000000000000)

def neglog_bounds(z,n):
    y=(1-z)/(1+z)
    s=F(0); p=y
    for k in range(n):
        s += p/F(2*k+1)
        p *= y*y
    lo=2*s
    hi=lo + 2*p/F(2*n+1)/(1-y*y)
    return lo,hi

def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

a_lo,a_hi=neglog_bounds(A,500)
l_lo,l_hi=neglog_bounds(LAM,700)
alpha_lo=a_lo/l_hi
alpha_hi=a_hi/l_lo
SCALE=10**30
P13_AFTER=F((alpha_hi.numerator*SCALE)//alpha_hi.denominator+1,SCALE)
assert alpha_lo<=alpha_hi<P13_AFTER<P02_BEFORE
print("UPPER_BEFORE",dec(P02_BEFORE))
print("UPPER_AFTER",dec(P13_AFTER))
print("WIDTH_BEFORE",dec(P02_BEFORE-LOW))
print("WIDTH_AFTER",dec(P13_AFTER-LOW))
print("STRICT_DECREASE",dec(P02_BEFORE-P13_AFTER))
print("ENDPOINT_PASS")

# ---------- true correlated strip carry recursion ----------
def carries(x,g,v,left=0):
    d=[left]
    for xi,gi in zip(x,g):
        d.append((1-gi)*int(bool(d[-1] or (xi==v))))
    return d

def trans(state,u,v):
    x,g=state; n=len(x)
    d=carries(x,g,v,0)
    gp=tuple([g[i]+d[i+1]-d[i] for i in range(1,n)] +
             [(1-d[n])*int(u==v)])
    assert all(z in (0,1) for z in gp)
    return (x[1:]+(u,),gp)

def reward(state,v):
    x,g=state; w=len(x)//2
    d=carries(x,g,v,0)
    return g[w]+d[w+1]

def h0(state):
    x,g=state; w=len(x)//2
    return sum(g[w:-1],F(0))+F(2,3)*g[-1]

def boundary_event(state):
    x,g=state
    d0=carries(x,g,0,0)[-1]
    d1=carries(x,g,1,0)[-1]
    return int(g[-1]==0 and d0==1 and d1==1)

def residual_h0(state):
    z=F(0)
    for u in (0,1):
        for v in (0,1):
            z += F(1,4)*(F(reward(state,v))+h0(trans(state,u,v))-h0(state))
    return z

def reachable(w):
    n=2*w; z=((0,)*n,(0,)*n)
    S={z}; q=deque([z])
    while q:
        s=q.popleft()
        for u in (0,1):
            for v in (0,1):
                t=trans(s,u,v)
                if t not in S:
                    S.add(t); q.append(t)
    return S

# Boundary carry extinction identity: a left carry discrepancy survives k sites iff
# every gradient is zero and every raw X bit is opposite the same column bit v.
for k in range(1,9):
    survive=0; total=0
    for xx in product((0,1),repeat=k):
        for v in (0,1):
            total+=1
            g=(0,)*k
            c0=carries(xx,g,v,0)
            c1=carries(xx,g,v,1)
            delta=[b-a for a,b in zip(c0[1:],c1[1:])]
            prodv=[]
            p=1
            for xi,gi in zip(xx,g):
                p *= (1-gi)*int(xi!=v)
                prodv.append(p)
            assert delta==prodv
            survive += delta[-1]
    assert F(survive,total)==F(1,2**k)
print("CARRY_EXTINCTION_K_LE_8_PASS")

# Reachable-state theorem checks: exact state counts; h0 boundary-event identity;
# and 2w constant-mismatch reset (the older formal-state proof used 4w).
for w in (1,2,3,4):
    S=reachable(w); n=2*w
    assert len(S)==COUNTS[w]
    for s in S:
        assert residual_h0(s)==F(2,3)+F(boundary_event(s),3)
    for a in (0,1):
        b=1-a
        target=((a,)*n,(0,)*n)
        for s in S:
            t=s
            for _ in range(n):
                t=trans(t,a,b)
            assert t==target
    q=F(2,4**n)
    C=F(n,1)/q
    assert C==w*4**(2*w)
    print("REACHABLE_RESET",w,"states",len(S),"length",n,"minorization_q",q,
          "finite_to_infinite_additive_C",C)
print("REACHABLE_2W_RESET_AND_MIXING_CONSTANT_PASS")

# Exact dual obstruction for any additive one-site potential
# h(s)=sum_i phi_i(x_i,g_i). Four constant reachable phases, with weights
# 1/3,1/6,1/3,1/6, cancel the potential drift and have mean reward 2/3.
def feat(state):
    x,g=state; n=len(x)
    out=[F(0) for _ in range(4*n)]
    for i,(xi,gi) in enumerate(zip(x,g)):
        out[4*i+2*xi+gi]+=1
    return out

def exp_feat(state):
    out=[F(0) for _ in range(len(state[0])*4)]
    for u in (0,1):
        for v in (0,1):
            z=feat(trans(state,u,v))
            for i,a in enumerate(z): out[i]+=F(1,4)*a
    return out

def exp_reward(state):
    return sum((F(1,4)*reward(state,v) for u in (0,1) for v in (0,1)),F(0))

weights={(0,0):F(1,3),(0,1):F(1,6),(1,0):F(1,3),(1,1):F(1,6)}
for w in (1,2,3,4):
    n=2*w
    drift=[F(0) for _ in range(4*n)]
    rr=F(0)
    for (xv,gv),wt in weights.items():
        s=((xv,)*n,(gv,)*n)
        a=feat(s); b=exp_feat(s)
        for i in range(4*n): drift[i]+=wt*(b[i]-a[i])
        rr += wt*exp_reward(s)
    assert all(z==0 for z in drift)
    assert rr==F(2,3)
print("ONE_SITE_ADDITIVE_DUAL_OBSTRUCTION_PASS")
print("ALL_EXACT_CHECKS_PASS")
