from fractions import Fraction

L = Fraction(99083249,125000000)
RHO_THRESHOLD = Fraction(99083249,150916751)

def leading_run_len(x,ell):
    h=(x>>(ell-1))&1
    r=1
    while r<ell and ((x>>(ell-1-r))&1)==h:
        r+=1
    return r


def bellman_sym(ell, steps, include_paired=True):
    S=1<<ell
    mask=S-1
    nstates=5*S*S
    H=[0]*nstates
    def idx(st,a,b): return (st*S+a)*S+b
    sh=[[((a<<1)&mask)|u for u in (0,1)] for a in range(S)]
    head=[(a>>(ell-1))&1 for a in range(S)]
    D=1
    hist=[]
    for t in range(steps):
        N=[0]*nstates
        reward=4*D
        for a in range(S):
            a0,a1=sh[a]
            ha=head[a]
            for b in range(S):
                b0,b1=sh[b]
                hb=head[b]
                if ha==hb:
                    val=reward + H[idx(0,a0,b0)]+H[idx(0,a0,b1)]+H[idx(0,a1,b0)]+H[idx(0,a1,b1)]
                else:
                    A0=2*(H[idx(0,a0,b)]+H[idx(0,a1,b)])
                    B0=2*(H[idx(0,a,b0)]+H[idx(0,a,b1)])
                    PA=max(2*H[idx(0,a0,b)], H[idx(1,a,b0)]+H[idx(1,a,b1)]) + max(2*H[idx(0,a1,b)], H[idx(2,a,b0)]+H[idx(2,a,b1)])
                    PB=max(H[idx(3,a0,b)]+H[idx(3,a1,b)], 2*H[idx(0,a,b0)]) + max(H[idx(4,a0,b)]+H[idx(4,a1,b)], 2*H[idx(0,a,b1)])
                    vals=[A0,B0,PA,PB]
                    if include_paired:
                        PAB=(max(H[idx(3,a0,b)],H[idx(1,a,b0)])+
                             max(H[idx(4,a0,b)],H[idx(1,a,b1)])+
                             max(H[idx(3,a1,b)],H[idx(2,a,b0)])+
                             max(H[idx(4,a1,b)],H[idx(2,a,b1)]))
                        vals.append(PAB)
                    val=max(vals)
                N[idx(0,a,b)]=val
                for u in (0,1):
                    st=1+u
                    au=sh[a][u]
                    if ha==hb:
                        val=reward + 2*(H[idx(0,au,b0)]+H[idx(0,au,b1)])
                    else:
                        skipx=4*H[idx(0,au,b)]
                        skipy=2*(H[idx(st,a,b0)]+H[idx(st,a,b1)])
                        cross=2*(max(H[idx(3,au,b)],H[idx(st,a,b0)])+
                                 max(H[idx(4,au,b)],H[idx(st,a,b1)]))
                        val=max(skipx,skipy,cross)
                    N[idx(st,a,b)]=val
                for v in (0,1):
                    st=3+v
                    bv=sh[b][v]
                    if ha==hb:
                        val=reward + 2*(H[idx(0,a0,bv)]+H[idx(0,a1,bv)])
                    else:
                        skipy=4*H[idx(0,a,bv)]
                        skipx=2*(H[idx(st,a0,b)]+H[idx(st,a1,b)])
                        cross=2*(max(H[idx(st,a0,b)],H[idx(1,a,bv)])+
                                 max(H[idx(st,a1,b)],H[idx(2,a,bv)]))
                        val=max(skipy,skipx,cross)
                    N[idx(st,a,b)]=val
        newD=D*4
        diffs=[N[i]-4*H[i] for i in range(nstates)]
        hist.append((min(diffs),newD,max(diffs)))
        H=N; D=newD
    return H,D,hist


def macro_bellman_int(ell,steps):
    S=1<<ell; mask=S-1
    Q=1<<(ell+1)
    heads=[(x>>(ell-1))&1 for x in range(S)]
    runs=[leading_run_len(x,ell) for x in range(S)]
    H=[0]*(S*S)
    D=1
    hist=[]
    def idx(a,b): return a*S+b
    for t in range(steps):
        N=[0]*(S*S)
        for a in range(S):
            ha=heads[a]; rA=runs[a]
            ash=[((a<<1)&mask)|u for u in (0,1)]
            for b in range(S):
                hb=heads[b]; rB=runs[b]
                bsh=[((b<<1)&mask)|v for v in (0,1)]
                if ha==hb:
                    sm=sum(H[idx(aa,bb)] for aa in ash for bb in bsh)
                    val=2*Q*D + (Q//4)*sm
                else:
                    if rA<ell:
                        k=rA+1; base=(a<<k)&mask; sm=0
                        for z in range(1<<k):
                            aa=base|z
                            sm += H[idx(aa,bsh[0])] + H[idx(aa,bsh[1])]
                        ex=(rA+2)*Q*D + (Q>>(k+1))*sm
                    else:
                        sm=0
                        for aa in range(S):
                            sm += H[idx(aa,bsh[0])]+H[idx(aa,bsh[1])]
                        ex=(ell+3)*Q*D + sm
                    if rB<ell:
                        k=rB+1; base=(b<<k)&mask; sm=0
                        for z in range(1<<k):
                            bb=base|z
                            sm += H[idx(ash[0],bb)] + H[idx(ash[1],bb)]
                        ey=(rB+2)*Q*D + (Q>>(k+1))*sm
                    else:
                        sm=0
                        for bb in range(S):
                            sm += H[idx(ash[0],bb)]+H[idx(ash[1],bb)]
                        ey=(ell+3)*Q*D + sm
                    val=min(ex,ey)
                N[idx(a,b)]=val
        newD=Q*D
        diffs=[N[i]-Q*H[i] for i in range(S*S)]
        hist.append((min(diffs),newD,max(diffs)))
        H=N; D=newD
    return H,D,hist


def fmt(fr):
    return f"{float(fr):.15f}"

print('PROB10-02 R17 exact symmetric single-debt / run-macro checker')
print('source lower L =',L,'=',fmt(L))
print('rho threshold =',RHO_THRESHOLD,'=',fmt(RHO_THRESHOLD))

sym_results={}
for ell,steps in [(1,25),(2,25),(3,30),(4,30),(5,35),(6,50),(7,55),(8,50)]:
    H,D,hist=bellman_sym(ell,steps,True)
    mn,den,mx=hist[-1]
    rho=Fraction(mn,den)
    rho_hi=Fraction(mx,den)
    gamma=2*rho/(1+rho)
    sym_results[ell]=(H,D,hist,rho,rho_hi,gamma)
    print(f'SYM ell={ell} steps={steps} rho_lo={rho} rho_lo_dec={fmt(rho)} rho_hi_dec={fmt(rho_hi)} gamma_transfer={fmt(gamma)} source_beats_L={gamma>L}')
    assert mn <= mx

H8,D8,h8,rho8,rho_hi8,gamma8=sym_results[8]
mn8,den8,mx8=h8[-1]
old=Fraction(6293309,10000000)
old_gamma=2*old/(1+old)
assert rho8 > old
assert gamma8 > old_gamma
assert gamma8 < L
print('SYM8 exact rho numerator =',mn8)
print('SYM8 exact rho denominator =',den8)
print('SYM8 exact transferred numerator =',2*mn8)
print('SYM8 exact transferred denominator =',den8+mn8)
print('SYM8 improvement over prior transferred =',float(gamma8-old_gamma))

for ell,steps in [(1,20),(2,20),(3,20),(4,25),(5,25)]:
    H,D,hist=macro_bellman_int(ell,steps)
    mn,den,mx=hist[-1]
    c_lo=Fraction(mn,den); c_hi=Fraction(mx,den)
    g=Fraction(2,1)/c_hi
    print(f'MACRO ell={ell} steps={steps} c_lo_dec={fmt(c_lo)} c_hi={c_hi} c_hi_dec={fmt(c_hi)} gamma_transfer={fmt(g)} source_beats_L={g>L}')
    assert mn <= mx
    assert c_hi > 0

H,D,hist=macro_bellman_int(4,2)
S=16
a=0; b1=9; b2=10
v1=H[a*S+b1]; v2=H[a*S+b2]
assert ((a>>3)&1, (b1>>3)&1, leading_run_len(a,4), leading_run_len(b1,4)) == ((a>>3)&1, (b2>>3)&1, leading_run_len(a,4), leading_run_len(b2,4))
assert v1 != v2
print('RUN_QUOTIENT_COUNTEREXAMPLE a=0000 b1=1001 b2=1010 scale=',D,'values=',v1,v2,'dec=',float(Fraction(v1,D)),float(Fraction(v2,D)))
print('ALL_EXACT_CHECKS_PASS')
print('RETURN_CODE=0')
