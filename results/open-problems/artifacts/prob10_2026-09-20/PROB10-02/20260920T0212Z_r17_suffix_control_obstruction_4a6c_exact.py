from itertools import product
from collections import defaultdict


def T(z,k,v,c,u):
    x=z[:k]; g=z[k:]
    d=[0]*(k+1); d[0]=c
    for j in range(1,k+1):
        d[j]=(1-g[j-1])*int(bool(d[j-1] or (x[j-1]==v)))
    gp=[]
    for j in range(1,k):
        val=g[j]+d[j+1]-d[j]
        assert val in (0,1)
        gp.append(val)
    gp.append((1-d[k])*int(u==v))
    return tuple(x[1:]+(u,)+tuple(gp)), tuple(d)


def check_c_domination(kmax=7):
    for k in range(1,kmax+1):
        n=0
        for z in product((0,1), repeat=2*k):
            z=tuple(z)
            for v,u in product((0,1), repeat=2):
                z0,d0=T(z,k,v,0,u)
                z1,d1=T(z,k,v,1,u)
                assert z0[:k]==z1[:k]
                assert all(a<=b for a,b in zip(z1[k:],z0[k:]))
                delta=[d1[i]-d0[i] for i in range(k+1)]
                assert delta[0]==1
                assert all(delta[i]>=delta[i+1] for i in range(k))
                n+=1
        print(f'C_DOMINATION_PASS k={k} cases={n}')


def check_g_monotonicity(kmax=7):
    for k in range(1,kmax+1):
        n=0
        for x in product((0,1), repeat=k):
            for g in product((0,1), repeat=k):
                zero=[i for i,a in enumerate(g) if a==0]
                for flips in product((0,1), repeat=len(zero)):
                    h=list(g)
                    for b,i in zip(flips,zero):
                        if b: h[i]=1
                    h=tuple(h)
                    for v,u in product((0,1), repeat=2):
                        zg,_=T(tuple(x+g),k,v,0,u)
                        zh,_=T(tuple(x+h),k,v,0,u)
                        assert zg[:k]==zh[:k]
                        assert all(a<=b for a,b in zip(zg[k:],zh[k:]))
                        n+=1
        print(f'G_MONOTONICITY_PASS k={k} ordered_cases={n}')


def apply_word(z,k,steps):
    for u,v in steps:
        z,_=T(z,k,v,0,u)
    return z


def check_reset(kmax=7):
    for k in range(1,kmax+1):
        target=(0,)*(2*k)
        steps=[(0,1)]*(2*k)
        n=0
        for z in product((0,1), repeat=2*k):
            out=apply_word(tuple(z),k,steps)
            assert out==target,(k,z,out)
            n+=1
        print(f'ZERO_CONTROL_RESET_PASS k={k} states={n} length={2*k}')


def carry_map(x,g,v):
    outs=[]
    k=len(x)
    for c in (0,1):
        z=tuple(x+g)
        _,d=T(z,k,v,c,0)
        outs.append(d[k])
    return tuple(outs)


def summary(x,g):
    return (carry_map(x,g,0),carry_map(x,g,1))


def prefix_update(x,g,bx,bg,v):
    r=len(x)
    z=tuple(x+(bx,)+g+(bg,))
    zn,_=T(z,r+1,v,0,0)
    return tuple(zn[:r]), tuple(zn[r+1:r+1+r])


def check_pair_summary_counterexample():
    xA=(0,0); gA=(0,1)
    xB=(1,0); gB=(0,1)
    assert summary(xA,gA)==summary(xB,gB)==((0,0),(0,0))
    inp=(0,0,1)
    A=prefix_update(xA,gA,*inp)
    B=prefix_update(xB,gB,*inp)
    assert A!=B
    assert summary(*A)!=summary(*B)
    print('PAIR_TRANSDUCER_NONMARKOV_PASS')
    print(' old_summary=',summary(xA,gA),' input=',inp)
    print(' A_next=',A,' A_summary=',summary(*A))
    print(' B_next=',B,' B_summary=',summary(*B))


def canon_state(state):
    x,g=state
    t=0
    while t<len(g) and g[t]==1:
        t+=1
    xc=list(x)
    for i in range(t):
        xc[i]=0
    return (tuple(xc),tuple(g))


def check_canonical_congruence(rmax=7):
    inputs=list(product((0,1), repeat=3))
    for r in range(1,rmax+1):
        bits=list(product((0,1), repeat=r))
        states=[(tuple(x),tuple(g)) for x in bits for g in bits]
        groups=defaultdict(list)
        for st in states:
            groups[canon_state(st)].append(st)
        expected=(2*(4**r)+1)//3
        assert len(groups)==expected
        for _,lst in groups.items():
            o=summary(*lst[0])
            for st in lst:
                assert summary(*st)==o
            for a in inputs:
                nxt=canon_state(prefix_update(*lst[0],*a))
                for st in lst:
                    assert canon_state(prefix_update(*st,*a))==nxt
        print(f'CANONICAL_CONGRUENCE_PASS r={r} raw={4**r} quotient={len(groups)} formula={expected}')


def minimize_prefix_machine(r):
    bits=list(product((0,1), repeat=r))
    states=[(tuple(x),tuple(g)) for x in bits for g in bits]
    idx={s:i for i,s in enumerate(states)}
    inputs=list(product((0,1), repeat=3))
    outs=[summary(*s) for s in states]
    trans=[]
    for s in states:
        row=[]
        for a in inputs:
            row.append(idx[prefix_update(*s,*a)])
        trans.append(row)
    labels={}
    cls=[]
    for o in outs:
        if o not in labels: labels[o]=len(labels)
        cls.append(labels[o])
    refinements=[len(labels)]
    while True:
        sig_to_class={}
        new=[]
        for i in range(len(states)):
            sig=(outs[i],tuple(cls[j] for j in trans[i]))
            if sig not in sig_to_class:
                sig_to_class[sig]=len(sig_to_class)
            new.append(sig_to_class[sig])
        refinements.append(len(sig_to_class))
        if len(sig_to_class)==len(set(cls)):
            cls=new
            break
        cls=new
    sizes=defaultdict(int)
    for c in cls:sizes[c]+=1
    dist=defaultdict(int)
    for s in sizes.values():dist[s]+=1
    return len(sizes),dict(sorted(dist.items())),refinements


def check_minimization(rmax=6):
    for r in range(1,rmax+1):
        n,dist,refs=minimize_prefix_machine(r)
        formula=(2*(4**r)+1)//3
        assert n==formula,(r,n,formula)
        expected={}
        for j in range(r):
            expected[2**j]=2*(4**(r-j-1))
        expected[2**r]=1
        assert dist==expected,(r,dist,expected)
        print(f'MOORE_MIN_PASS r={r} raw={4**r} classes={n} formula={formula} dist={dist} refinements={refs}')


if __name__=='__main__':
    check_c_domination()
    check_g_monotonicity()
    check_reset()
    check_pair_summary_counterexample()
    check_canonical_congruence()
    check_minimization()
    print('ALL_EXACT_CHECKS_PASS')
