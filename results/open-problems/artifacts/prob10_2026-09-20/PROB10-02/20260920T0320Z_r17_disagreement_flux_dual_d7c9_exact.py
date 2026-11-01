from itertools import product
from fractions import Fraction
from collections import deque

UVS=((0,0),(0,1),(1,0),(1,1))

def step(state, uv):
    x,g=state
    u,v=uv
    m=len(x)
    d=[0]*(m+1)
    for i in range(1,m+1):
        d[i]=(1-g[i-1])*int(bool(d[i-1] or (x[i-1]==v)))
    gp=[0]*m
    for i in range(m-1):
        gp[i]=g[i+1]+d[i+2]-d[i+1]
    gp[m-1]=(1-d[m])*int(u==v)
    return (x[1:]+(u,), tuple(gp)), tuple(d)

def reachable(m):
    S={((0,)*m,(0,)*m),((1,)*m,(0,)*m)}
    frontier=list(S)
    while frontier:
        s=frontier.pop()
        for uv in UVS:
            sp,_=step(s,uv)
            if sp not in S:
                S.add(sp); frontier.append(sp)
    return S

def comparable_pairs_same_x(S):
    byx={}
    for x,g in S:
        byx.setdefault(x,[]).append(g)
    for x,gs in byx.items():
        for g in gs:
            for h in gs:
                if g!=h and all(a<=b for a,b in zip(g,h)):
                    yield x,g,h

def verify_flux(m):
    S=reachable(m)
    n=0
    worst=Fraction(0)
    worst_arg=None
    for x,g,h in comparable_pairs_same_x(S):
        D=sum(b-a for a,b in zip(g,h))
        for u,v in UVS:
            (xp,gg),dg=step((x,g),(u,v))
            (xp2,hh),dh=step((x,h),(u,v))
            assert xp==xp2
            assert all(a<=b for a,b in zip(gg,hh))
            dd=[a-b for a,b in zip(dg,dh)]
            assert all(z>=0 for z in dd)
            Dp=sum(b-a for a,b in zip(gg,hh))
            rhs=D-(h[0]-g[0])*int(x[0]!=v)-dd[m]*int(u!=v)
            assert Dp==rhs
            assert Dp<=D
            n+=1
        e=Fraction(0)
        for uv in UVS:
            (_,gg),_=step((x,g),uv);(_,hh),_=step((x,h),uv)
            e += Fraction(sum(b-a for a,b in zip(gg,hh)),4)
        if e/D>worst:
            worst=e/D; worst_arg=(x,g,h,D,e)
    return len(S),n,worst,worst_arg

def weighted(g,h,a):
    return sum((a**i)*(b-c) for i,(c,b) in enumerate(zip(g,h)))

def geometric_counterexample():
    m=4; a=Fraction(6,5); S=reachable(m)
    best=Fraction(0); arg=None
    for x,g,h in comparable_pairs_same_x(S):
        F=weighted(g,h,a)
        e=Fraction(0); vals=[]
        for uv in UVS:
            (_,gg),_=step((x,g),uv);(_,hh),_=step((x,h),uv)
            val=weighted(gg,hh,a); vals.append(val); e+=val/4
        if F and e/F>best:
            best=e/F;arg=(x,g,h,F,e,tuple(vals))
    assert best==Fraction(11,10)
    return a,best,arg

def apply_word(s,word):
    for uv in word:
        s,_=step(s,uv)
    return s

def formal_reset_check(m):
    for a in (0,1):
        word=((a,1-a),)*m
        target=((a,)*m,(0,)*m)
        for x in product((0,1),repeat=m):
            for g in product((0,1),repeat=m):
                assert apply_word((x,g),word)==target

def sync_census(m):
    S=tuple(reachable(m))
    good=[]
    for word in product(UVS,repeat=m):
        target=None; ok=True
        for s in S:
            out=apply_word(s,word)
            if target is None: target=out
            elif out!=target:
                ok=False;break
        if ok: good.append(word)
    expected=[tuple([(0,1)]*m),tuple([(1,0)]*m)]
    assert good==expected
    return len(S),len(good),good

def joint_graph_extreme(m):
    starts=[(x,(0,)*m,(1,)*m) for x in product((0,1),repeat=m)]
    seen=set(starts); dq=deque(starts)
    while dq:
        x,g,h=dq.popleft()
        for uv in UVS:
            (xp,gg),_=step((x,g),uv);(xp2,hh),_=step((x,h),uv)
            assert xp==xp2 and all(a<=b for a,b in zip(gg,hh))
            if gg==hh: continue
            q=(xp,gg,hh)
            if q not in seen:
                seen.add(q);dq.append(q)
    states=list(seen); idx={s:i for i,s in enumerate(states)}
    succ=[]
    for x,g,h in states:
        row=[]
        for uv in UVS:
            (xp,gg),_=step((x,g),uv);(_,hh),_=step((x,h),uv)
            row.append(-1 if gg==hh else idx[(xp,gg,hh)])
        succ.append(tuple(row))
    return states,succ,[idx[s] for s in starts]

def bellman_coalescence_certificate(m,T,ceiling):
    states,succ,starts=joint_graph_extreme(m)
    nums=[2*(4**m-1)]*len(states); den=3
    for _ in range(T):
        newden=4*den
        nums=[newden+sum(nums[j] for j in row if j>=0) for row in succ]
        den=newden
    slacks=[]
    for i,row in enumerate(succ):
        slack=4*nums[i]-(4*den+sum(nums[j] for j in row if j>=0))
        assert slack>=0
        slacks.append(slack)
    mx=max(nums[i] for i in starts)
    assert mx*ceiling.denominator < ceiling.numerator*den
    return len(states),Fraction(mx,den),min(slacks),max(slacks)

print('R17 PROB10-02 disagreement-flux exact checker')
for m in range(1,5):
    ns,npairs,worst,arg=verify_flux(m)
    print(f'm={m} reachable={ns} checked_pair_inputs={npairs} worst_one_step_D_ratio={worst}')
    if m==3:
        assert worst==1
        print('m=3 strict-contraction obstruction=',arg)
print('EXACT_DISAGREEMENT_FLUX_IDENTITY_PASS')
print('EXACT_PATHWISE_HAMMING_MONOVARIANT_PASS')

a,best,arg=geometric_counterexample()
print(f'geometric_alpha={a} worst_ratio_m4={best}')
print('geometric_counterexample=',arg)
print('EXACT_GEOMETRIC_WEIGHT_CONTRACTION_COUNTEREXAMPLE_PASS')

for m in range(1,7):
    formal_reset_check(m)
print('EXACT_FORMAL_MISMATCH_RESET_M1_TO_M6_PASS')

for m in (2,4,6):
    ns,ng,good=sync_census(m)
    print(f'sync_length={m} reachable={ns} universal_words={ng}')
    print('universal_words=',good)
print('EXACT_SHORTEST_SYNCHRONIZER_CENSUS_W1_W2_W3_PASS')

certs=((2,12,Fraction(3122,1000)),(4,24,Fraction(7787,1000)),(6,90,Fraction(13139,1000)))
for m,T,ceil in certs:
    nj,q,mn,mx=bellman_coalescence_certificate(m,T,ceil)
    reset=Fraction(2*(4**m-1),3)
    total=Fraction(m,1)+q
    print(f'joint_m={m} states={nj} bellman_iter={T}')
    print(f'K_ext_upper_exact={q} K_ext_upper_decimal={float(q):.12f} ceiling={ceil}')
    print(f'arbitrary_start_stationary_reward_error_upper={total} decimal={float(total):.12f}')
    print(f'old_overlapping_reset_mean={reset}')
    print(f'bellman_slack_num_min={mn} max={mx}')
print('EXACT_JOINT_COALESCENCE_BELLMAN_DUAL_PASS')
print('ALL_EXACT_CHECKS_PASS')
