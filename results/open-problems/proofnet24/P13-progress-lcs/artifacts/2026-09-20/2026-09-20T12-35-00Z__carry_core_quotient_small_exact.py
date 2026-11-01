from itertools import product

def bits(z,n):
    return [(z>>i)&1 for i in range(n)]

def full_step(x,g,u,v,W):
    M=2*W
    d=[0]*(M+1)
    for i in range(1,M+1):
        d[i]=(1-g[i-1]) * (d[i-1] or (x[i-1]==v))
    gp=[0]*M
    for i in range(1,M):
        gp[i-1]=g[i]+d[i+1]-d[i]
    gp[M-1]=(1-d[M])*(u==v)
    xp=x[1:]+[u]
    rho=g[W]+d[W+1]
    assert all(z in (0,1) for z in gp)
    return xp,gp,int(rho)

def context_from_full(x,g):
    M=len(x)
    xb=x[1:M-1]
    gb=g[1:M-1]
    c=((1-g[0])*(x[0]==0),(1-g[0])*(x[0]==1))
    assert c in ((0,0),(1,0),(0,1))
    right=(x[M-1],g[M-1])
    return xb,gb,c,right

def quotient_step(xb,gb,c,right,u,v,w):
    m=2*w
    e=[0]*(m+2)
    e[0]=c[v]
    for j in range(1,m+1):
        e[j]=(1-gb[j-1])*(e[j-1] or (xb[j-1]==v))
    xr,gr=right
    e[m+1]=(1-gr)*(e[m] or (xr==v))
    rho=gb[w]+e[w+1]
    xbp=xb[1:]+[xr]
    gbp=[0]*m
    for j in range(1,m):
        gbp[j-1]=gb[j]+e[j+1]-e[j]
    gbp[m-1]=gr+e[m+1]-e[m]
    xleftp=xb[0]
    gleftp=gb[0]+e[1]-e[0]
    cp=((1-gleftp)*(xleftp==0),(1-gleftp)*(xleftp==1))
    rightp=(u,(1-e[m+1])*(u==v))
    assert all(z in (0,1) for z in gbp)
    assert gleftp in (0,1)
    assert cp in ((0,0),(1,0),(0,1))
    return xbp,gbp,cp,rightp,int(rho)

def check(w):
    W=w+1; M=2*W; nstates=1<<(2*M); checks=0
    contexts=set()
    for state in range(nstates):
        x=bits(state & ((1<<M)-1),M)
        g=bits(state>>M,M)
        ctx=context_from_full(x,g)
        contexts.add((tuple(ctx[0]),tuple(ctx[1]),ctx[2],ctx[3]))
        for u,v in product((0,1), repeat=2):
            xp,gp,r=full_step(x,g,u,v,W)
            q=quotient_step(*ctx,u,v,w)
            tgt=context_from_full(xp,gp)
            assert q[4]==r
            assert tuple(q[0])==tuple(tgt[0])
            assert tuple(q[1])==tuple(tgt[1])
            assert q[2]==tgt[2]
            assert q[3]==tgt[3]
            checks+=1
    expected_contexts=(1<<(4*w))*12
    assert len(contexts)==expected_contexts,(len(contexts),expected_contexts)
    print(f'core_w={w} full_w={W} M={M} formal_states={nstates} transition_checks={checks} quotient_contexts={len(contexts)} expected={expected_contexts} PASS')

for w in (1,2,3): check(w)
print('ALL_EXACT_CHECKS_PASS')
