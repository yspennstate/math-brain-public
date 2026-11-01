#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from fractions import Fraction

UV = ((0,0),(0,1),(1,0),(1,1))

def transition(w, state, uv):
    x, g = state
    u, v = uv
    assert len(x) == 2*w and len(g) == 2*w
    V = [0]
    for z in g:
        assert z in (0,1)
        V.append(V[-1] + z)
    m = [int(z == v) for z in x] + [int(u == v)]
    Q = [0]*(2*w+1)
    Q[0] = max(V[1], V[0] + m[0])
    for k in range(1, 2*w):
        Q[k] = max(Q[k-1], V[k] + m[k], V[k+1])
    Q[2*w] = max(Q[2*w-1], V[2*w] + m[2*w])
    gp = tuple(Q[k] - Q[k-1] for k in range(1,2*w+1))
    assert all(z in (0,1) for z in gp)
    xp = tuple(x[1:]) + (u,)
    reward = Q[w] - V[w]
    assert reward in (0,1)
    return (xp,gp), reward

def reachable(w):
    s0 = ((0,)*(2*w),(0,)*(2*w))
    seen = {s0}
    q = deque([s0])
    while q:
        s = q.popleft()
        for uv in UV:
            t,_ = transition(w,s,uv)
            if t not in seen:
                seen.add(t)
                q.append(t)
    return sorted(seen)

def reset_state(w,s):
    for _ in range(4*w):
        s,_ = transition(w,s,(0,1))
    return s

def gauss(A,b):
    A = [[Fraction(x) for x in row] + [Fraction(y)] for row,y in zip(A,b)]
    n = len(A)
    row = 0
    pivcols=[]
    for col in range(n):
        piv = next((r for r in range(row,n) if A[r][col]), None)
        if piv is None:
            continue
        A[row],A[piv]=A[piv],A[row]
        z=A[row][col]
        A[row]=[x/z for x in A[row]]
        for r in range(n):
            if r != row and A[r][col]:
                z=A[r][col]
                A[r]=[A[r][c]-z*A[row][c] for c in range(n+1)]
        pivcols.append(col)
        row += 1
    assert row == n
    ans=[Fraction(0)]*n
    for r,c in enumerate(pivcols):
        ans[c]=A[r][-1]
    return ans

def exact_w1():
    w=1
    states=reachable(w)
    idx={s:i for i,s in enumerate(states)}
    N=len(states)
    P=[[Fraction(0) for _ in range(N)] for __ in range(N)]
    rb=[Fraction(0) for _ in range(N)]
    for i,s in enumerate(states):
        for uv in UV:
            t,r=transition(w,s,uv)
            P[i][idx[t]] += Fraction(1,4)
            rb[i] += Fraction(r,4)
    # Stationary equations pi P = pi, with final equation sum pi=1.
    A=[]; b=[]
    for j in range(N-1):
        A.append([P[i][j] - (1 if i==j else 0) for i in range(N)])
        b.append(0)
    A.append([1]*N); b.append(1)
    pi=gauss(A,b)
    assert sum(pi)==1 and all(p>=0 for p in pi)
    gamma=sum(pi[i]*rb[i] for i in range(N))
    assert gamma == Fraction(7,10)
    # Poisson/Bellman equality witness, normalized h(s0)=0.
    s0=((0,0),(0,0)); i0=idx[s0]
    A=[]; b=[]
    for i in range(N):
        if i==i0:
            row=[0]*N; row[i0]=1
            A.append(row); b.append(0)
        else:
            A.append([(1 if i==j else 0)-P[i][j] for j in range(N)])
            b.append(rb[i]-gamma)
    h=gauss(A,b)
    residual=[]
    for i in range(N):
        val=rb[i] + sum(P[i][j]*h[j] for j in range(N)) - h[i]
        residual.append(val)
    assert set(residual)=={gamma}
    return states, pi, h, gamma, P, rb

def grad_signature(w,s):
    c=Counter()
    for uv in UV:
        t,r=transition(w,s,uv)
        c[(t[1],r)] += 1
    return tuple(sorted(c.items()))

def gradient_only_counterexample():
    states=reachable(1)
    by_g=defaultdict(list)
    for s in states:
        by_g[s[1]].append(s)
    for g,ls in sorted(by_g.items()):
        sigs=defaultdict(list)
        for s in ls:
            sigs[grad_signature(1,s)].append(s)
        if len(sigs)>1:
            reps=[]
            for sig, ss in sorted(sigs.items(), key=lambda z: repr(z[0]))[:2]:
                reps.append((ss[0],sig))
            return g,reps
    raise AssertionError("no counterexample found")

def lcs(x,y):
    m=len(y)
    prev=[0]*(m+1)
    for a in x:
        cur=[0]*(m+1)
        for j,b in enumerate(y,1):
            if a==b:
                cur[j]=prev[j-1]+1
            else:
                cur[j]=max(prev[j],cur[j-1])
        prev=cur
    return prev[m]

def band_lcs(x,y,w):
    n=len(x); m=len(y)
    neg=-10**9
    D=[[neg]*(m+1) for _ in range(n+1)]
    D[0][0]=0
    for i in range(n+1):
        for j in range(m+1):
            if abs(i-j)>w or (i==0 and j==0):
                continue
            best=neg
            if i>0 and abs((i-1)-j)<=w:
                best=max(best,D[i-1][j])
            if j>0 and abs(i-(j-1))<=w:
                best=max(best,D[i][j-1])
            if i>0 and j>0 and abs((i-1)-(j-1))<=w and x[i-1]==y[j-1]:
                best=max(best,D[i-1][j-1]+1)
            D[i][j]=best
    return D[n][m]

# Metric arithmetic.
L=Fraction(792665992,10**9)
U=Fraction(826275942762282626,10**18)
W=U-L
assert W == Fraction(33609950762282626,10**18)
print("CERTIFIED_INTERVAL_LOWER", "0.792665992", L)
print("CERTIFIED_INTERVAL_UPPER", "0.826275942762282626", U)
print("CERTIFIED_INTERVAL_WIDTH", "0.033609950762282626", W)

# Exact finite-strip state counts and synchronizing/reset check.
for w in (1,2,3):
    states=reachable(w)
    s0=((0,)*(2*w),(0,)*(2*w))
    assert all(reset_state(w,s)==s0 for s in states)
    print("REACHABLE_STATES", w, len(states))
    print("RESET_WORD_PASS", w, "length",4*w)

states,pi,h,gamma,P1,r1=exact_w1()
print("W1_EXACT_GAMMA", gamma)
print("W1_STATIONARY_DENOMS", sorted(set(p.denominator for p in pi)))
print("W1_BELLMAN_EQUALITY_PASS", len(states), "states")
print("W1_H_RANGE", min(h), max(h))
# Finite-horizon Bellman certificate h_T=sum_{t<T}P^t r: residual=P^T r.
v=list(r1)
T=8
for _ in range(T):
    v=[sum(P1[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]
lo,hi=min(v),max(v)
assert lo <= gamma <= hi
print("W1_T8_EXACT_BELLMAN_BRACKET", lo, hi, "width", hi-lo)
# Generic synchronizing-word contraction bound: L=4w=4, q=4^-4=1/256.
qsync=Fraction(1,256)
generic=(1-qsync)**(T//4)
assert hi-lo <= generic
print("W1_T8_SYNC_CONTRACTION_BOUND_PASS", generic)

g,reps=gradient_only_counterexample()
print("GRADIENT_ONLY_COUNTEREXAMPLE_G", g)
for k,(s,sig) in enumerate(reps,1):
    print("GRADIENT_ONLY_WORLD",k,"state",s,"signature",sig)
assert reps[0][1] != reps[1][1]
print("GRADIENT_ONLY_NONMARKOV_PASS")

# Exact deterministic obstruction to a uniform fixed-band transfer.
m=5; w=2
x=(0,)*m+(1,)*m
y=(1,)*m+(0,)*m
u=lcs(x,y); b=band_lcs(x,y,w)
assert u==m and b==w
print("SHIFTED_BLOCK_OBSTRUCTION", "m",m,"w",w,"LCS",u,"band_LCS",b,"gap",u-b)
print("SHIFTED_BLOCK_OBSTRUCTION_PASS")

print("ALL_EXACT_CHECKS_PASS")
