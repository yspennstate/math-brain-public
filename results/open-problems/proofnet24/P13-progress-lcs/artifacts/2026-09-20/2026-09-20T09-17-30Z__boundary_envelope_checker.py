from itertools import product
from fractions import Fraction
from collections import deque

PAIRS=((0,0),(0,1),(1,0),(1,1))
NEG=-10**8

def step_state(m,w,state,uv):
    x,g=state
    u,v=uv
    V=[0]
    for bit in g:
        V.append(V[-1]+bit)
    a=[int(x[i]==v) for i in range(m)] + [int(u==v)]
    Q=[0]*(m+1)
    Q[0]=max(V[1],V[0]+a[0])
    for k in range(1,m):
        Q[k]=max(Q[k-1],V[k]+a[k],V[k+1])
    Q[m]=max(Q[m-1],V[m]+a[m])
    gp=tuple(Q[k]-Q[k-1] for k in range(1,m+1))
    xp=tuple(x[1:])+(u,)
    rho=Q[w]-V[w]
    assert rho in (0,1)
    assert all(z in (0,1) for z in gp)
    return (xp,gp),rho

def reward(m,w,x,g,word):
    state=(tuple(x),tuple(g))
    total=0
    for uv in word:
        state,r=step_state(m,w,state,uv)
        total+=r
    return total

def central_score(x,word,w):
    """M_w: path starts at p_w, may move right on initial boundary for free."""
    m=2*w
    V=[NEG]*w+[0]*(m-w+1)
    xp=tuple(x)
    for u,v in word:
        a=[int(xp[i]==v) for i in range(m)] + [int(u==v)]
        Q=[NEG]*(m+1)
        Q[0]=max(V[1], V[0]+a[0] if V[0]>NEG//2 else NEG)
        for k in range(1,m):
            cand=V[k]+a[k] if V[k]>NEG//2 else NEG
            Q[k]=max(Q[k-1],cand,V[k+1])
        cand=V[m]+a[m] if V[m]>NEG//2 else NEG
        Q[m]=max(Q[m-1],cand)
        V=Q
        xp=tuple(xp[1:])+(u,)
    return V[w]

def band_lcs(a,b,w):
    n=len(a)
    assert len(b)==n
    prev=[NEG]*(n+1)
    # horizontal moves from (0,0) are legal while inside |i-j|<=w
    for j in range(0,min(n,w)+1):
        prev[j]=0
    for i in range(1,n+1):
        cur=[NEG]*(n+1)
        lo=max(0,i-w); hi=min(n,i+w)
        for j in range(lo,hi+1):
            best=prev[j]
            if j>0:
                best=max(best,cur[j-1])
                if a[i-1]==b[j-1] and prev[j-1]>NEG//2:
                    best=max(best,prev[j-1]+1)
            cur[j]=best
        prev=cur
    return prev[n]

def mapped_strings(x,word,w):
    N=len(word)
    concat=list(x)+[uv[0] for uv in word]
    A=tuple(concat[w:w+N])
    B=tuple(uv[1] for uv in word)
    assert len(A)==N
    return A,B

def exact_expectation_pm(w,N):
    m=2*w
    gminus=(1,)*w+(0,)*w
    gplus=(0,)*w+(1,)*w
    lo=hi=cnt=0
    for x in product((0,1),repeat=m):
        for word in product(PAIRS,repeat=N):
            lo+=reward(m,w,x,gminus,word)
            hi+=reward(m,w,x,gplus,word)
            cnt+=1
    return Fraction(lo,cnt),Fraction(hi,cnt)

def exact_band_expectation(w,N):
    strings=list(product((0,1),repeat=N))
    total=0
    for a in strings:
        for b in strings:
            total+=band_lcs(a,b,w)
    return Fraction(total,4**N)

def check_envelopes(w,Nmax):
    m=2*w
    gminus=(1,)*w+(0,)*w
    gplus=(0,)*w+(1,)*w
    checks=0
    for N in range(1,Nmax+1):
        for x in product((0,1),repeat=m):
            for word in product(PAIRS,repeat=N):
                rminus=reward(m,w,x,gminus,word)
                rplus=reward(m,w,x,gplus,word)
                M=central_score(x,word,w)
                assert rminus==M
                assert 0<=rplus-rminus<=w
                A,B=mapped_strings(x,word,w)
                assert M==band_lcs(A,B,w)
                for g in product((0,1),repeat=m):
                    r=reward(m,w,x,g,word)
                    assert rminus<=r<=rplus
                    checks+=1
    return checks

# Exhaustive recurrence checks.  These are finite self-checks; the all-width proof is analytic.
for w,nmax in ((1,4),(2,3),(3,2)):
    c=check_envelopes(w,nmax)
    print(f"ENVELOPE_AND_BAND_PASS w={w} Nmax={nmax} checked_state_words={c}")

# Exact finite expectations, including the first currently relevant historical width w=6.
for w,Ns in ((1,(1,2,3,4)),(2,(1,2,3,4)),(6,(1,2,3))):
    for N in Ns:
        lo,hi=exact_expectation_pm(w,N)
        assert hi-lo<=w
        b=exact_band_expectation(w,N) if N<=4 else None
        if b is not None:
            assert b==lo
        print(f"EXPECT w={w} N={N} lower={lo} upper={hi} gap={hi-lo} lower_over_N={lo/Fraction(N,1)} upper_over_N={hi/Fraction(N,1)}")

# w=1 has exact stationary gamma_1=7/10; verify the new finite bracket numerically/exactly.
gamma1=Fraction(7,10)
for N in range(1,5):
    lo,hi=exact_expectation_pm(1,N)
    assert lo <= N*gamma1 <= hi
    print(f"GAMMA1_BRACKET_PASS N={N} lower={lo} target={N*gamma1} upper={hi}")

print("ALL_EXACT_CHECKS_PASS")
