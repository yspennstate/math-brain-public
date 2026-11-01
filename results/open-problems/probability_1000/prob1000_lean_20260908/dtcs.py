import random, math, sys
sys.setrecursionlimit(100000)
# DTCS(n): critical beta-splitting. q(m,i) = (1/a_m) * 1/(i(m-i)), a_m = (2/m) H_{m-1}
# sample i from that law efficiently via inverse cdf on 1/(i(m-i)) = (1/m)(1/i + 1/(m-i))
def sample_split(m, rng):
    # weight_i propto 1/i + 1/(m-i), i=1..m-1 ; equivalently pick one of the two terms
    # total = 2*H_{m-1}. Sample: with prob 1/2 use 1/i branch, else 1/(m-i) (symmetric)
    # 1/i branch: P(i) propto 1/i on 1..m-1  -> inverse cdf via harmonic numbers
    # use rejection-free: sample u in (0, H_{m-1}), find i with H_i > u  (i ~ exp of u)
    H = math.log(m-1) + 0.5772156649015329 + 1.0/(2*(m-1)) if m > 2 else 1.0
    while True:
        u = rng.random()*H
        i = int(round(math.exp(u - 0.5772156649015329)))
        if 1 <= i <= m-1: break
    if rng.random() < 0.5: i = m - i
    return max(1, min(m-1, i))

def dtcs_stats(n, rng):
    # iterative post-order over sizes; returns (drawn_length, height, sum_subtree_heights, sum_leaf_depths, n_internal)
    stack=[(n,0,'go')]; res=[]
    L=0.0; SH=0.0; SLD=0.0; nint=0
    # explicit stack: (size, depth, state)
    st=[(n,0)]
    vals=[]  # returned heights
    work=[(n,0,0)]  # size, depth, phase
    out=[]
    # do recursion manually
    stack=[('go',n,0)]
    heights=[]
    while stack:
        tag=stack.pop()
        if tag[0]=='go':
            _,m,d=tag
            if m==1:
                heights.append(0); SLD+=d; continue
            i=sample_split(m,rng); nint+=1
            stack.append(('done',m,d))
            stack.append(('go',m-i,d+1))
            stack.append(('go',i,d+1))
        else:
            _,m,d=tag
            hb=heights.pop(); ha=heights.pop()
            L += 2 + abs(hb-ha)
            h = 1+max(ha,hb)
            SH += h
            heights.append(h)
    return L, heights[0], SH, SLD, nint

rng=random.Random(20260908)
print(f"{'n':>9} {'reps':>4} {'L/n':>9} {'log^4 n':>10} {'L/(n log^4 n)':>14} {'sumH/n':>8} {'sumLeafD/n':>11} {'height':>7} {'L<=sumLeafD':>12}")
for n in [1000, 5000, 20000, 100000, 400000]:
    reps = 8 if n<=20000 else 3
    Ls=[];SHs=[];SLDs=[];Hs=[];ok=True
    for _ in range(reps):
        L,h,SH,SLD,ni = dtcs_stats(n,rng)
        Ls.append(L);SHs.append(SH);SLDs.append(SLD);Hs.append(h)
        if L> SLD+1e-9: ok=False
    L=sum(Ls)/reps; SH=sum(SHs)/reps; SLD=sum(SLDs)/reps; H=sum(Hs)/reps
    l4=math.log(n)**4
    print(f"{n:>9} {reps:>4} {L/n:>9.3f} {l4:>10.1f} {L/(n*l4):>14.6f} {SH/n:>8.3f} {SLD/n:>11.3f} {H:>7.1f} {str(ok):>12}")
