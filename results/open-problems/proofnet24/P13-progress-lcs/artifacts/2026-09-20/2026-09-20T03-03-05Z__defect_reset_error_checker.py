from fractions import Fraction
from itertools import product

UV=((0,0),(0,1),(1,0),(1,1))
A=1  # source pair (0,1)
B=2  # source pair (1,0)


def trans_state(state,a):
    u,v=UV[a]
    x,g=state
    m=len(x)
    d=[0]
    for xi,gi in zip(x,g):
        d.append((1-gi)*int(bool(d[-1] or xi==v)))
    gp=tuple([g[i]+d[i+1]-d[i] for i in range(1,m)] +
             [(1-d[m])*int(u==v)])
    assert all(z in (0,1) for z in gp)
    return (x[1:]+(u,),gp)


def apply_word(state,word):
    for a in word:
        state=trans_state(state,a)
    return state


def reset_patterns(m):
    pats=[(A,)*m,(B,)*m]
    for z in range(4):
        if z!=A:
            pats.append((A,)*(m-1)+(z,A))
        if z!=B:
            pats.append((B,)*(m-1)+(z,B))
    return tuple(pats)


def exact_wait_via_prefix_automaton(m):
    pats=reset_patterns(m)
    pref={()}
    for p in pats:
        for k in range(1,len(p)):
            pref.add(p[:k])
    states=sorted(pref,key=lambda s:(len(s),s))
    idx={s:i for i,s in enumerate(states)}

    def is_hit(w):
        return any(len(w)>=len(p) and w[-len(p):]==p for p in pats)

    def nxt(s,a):
        w=s+(a,)
        if is_hit(w):
            return None
        for k in range(min(len(w),m),-1,-1):
            suf=w[-k:] if k else ()
            if suf in idx:
                return suf
        raise AssertionError

    n=len(states)
    M=[[Fraction(0) for _ in range(n+1)] for __ in range(n)]
    for i,s in enumerate(states):
        M[i][i]=Fraction(1)
        M[i][-1]=Fraction(1)
        for a in range(4):
            ns=nxt(s,a)
            if ns is not None:
                M[i][idx[ns]]-=Fraction(1,4)

    # Exact Gauss-Jordan elimination for expected absorption times.
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                q=M[r][c]
                M[r]=[M[r][j]-q*M[c][j] for j in range(n+1)]
    return M[idx[()]][-1],len(states)


# Exhaustively verify the new reset family on every formal bit state.
# This is stronger than checking only reachable strip states.
for m in range(2,8):
    formal=[(tuple(x),tuple(g))
            for x in product((0,1),repeat=m)
            for g in product((0,1),repeat=m)]
    for base in (A,B):
        for z in range(4):
            word=(base,)*(m-1)+(z,base)
            outs={apply_word(s,word) for s in formal}
            assert len(outs)==1, (m,base,z,len(outs))
    print('DEFECT_RESET_FORMAL_PASS', 'm='+str(m), 'states='+str(len(formal)))

# Independently solve the finite prefix automaton and verify the closed form
# E tau_m^dagger = (8*4^m+10)/21 for m>=3.
for m in range(2,11):
    E,nstates=exact_wait_via_prefix_automaton(m)
    if m>=3:
        closed=Fraction(8*4**m+10,21)
        assert E==closed,(m,E,closed)
    print('WAIT_EXACT','m='+str(m),'automaton_states='+str(nstates),'E='+str(E))

# Compare against the preceding overlapping-run constant 2(4^m-1)/3.
for w in range(1,6):
    m=2*w
    old=Fraction(2*(4**m-1),3)
    new,_=exact_wait_via_prefix_automaton(m)
    assert new<old
    print('WIDTH','w='+str(w),'m='+str(m),'old_C='+str(old),'new_C='+str(new),
          'gain='+str(old-new),'ratio=%.15f'%float(new/old))

print('ALL_EXACT_CHECKS_PASS')
