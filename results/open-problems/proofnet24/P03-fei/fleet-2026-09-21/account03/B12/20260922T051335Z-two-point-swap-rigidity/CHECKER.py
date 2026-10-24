from __future__ import annotations
import hashlib
from fractions import Fraction
import numpy as np

EXPECTED_SHA="f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP="fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT="fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES=[
(TOP,BOT),
(TOP,"fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
(TOP,"fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00","fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
(TOP,"fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
(TOP,"fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00",BOT),
("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00",BOT),
("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00",BOT),
("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00",BOT),
]
M=10**12

def fwht_i64(a):
    a=np.array(a,dtype=np.int64,copy=True); h=1
    while h<len(a):
        v=a.reshape(-1,2*h); x=v[:,:h].copy(); y=v[:,h:].copy()
        v[:,:h]=x+y; v[:,h:]=x-y; h*=2
    return a

def make_table():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(r),16)^base for r in SLICES[1:]]
    hosts=[]; seen=base
    for m in masks:
        assert not (seen&m) and m.bit_count()==2
        seen|=m; hosts.append([x for x in range(512) if (m>>x)&1])
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    out=np.tile(core,(1<<9,1))
    for j,cells in enumerate(hosts):
        mask=(np.arange(1<<9)&(1<<j))!=0
        out[np.ix_(mask,np.array(cells))]=-1
    return out.ravel()

def ln_bounds(m,r=50):
    assert Fraction(1)<=m<=Fraction(2)
    if m==1: return Fraction(0),Fraction(0)
    t=(m-1)/(m+1); t2=t*t
    s=sum((t**(2*j+1)/Fraction(2*j+1) for j in range(r)),Fraction())
    lo=2*s
    rem=2*t**(2*r+1)/(Fraction(2*r+1)*(1-t2))
    return lo,lo+rem

LN2_LO,LN2_HI=ln_bounds(Fraction(2))

def pow2(e): return Fraction(1<<e) if e>=0 else Fraction(1,1<<(-e))
def floor_log2(q):
    e=q.numerator.bit_length()-q.denominator.bit_length()
    if pow2(e)>q: e-=1
    while pow2(e+1)<=q: e+=1
    return e

def h_bounds(z,N):
    z=abs(int(z))
    if z==0: return Fraction(0),Fraction(0)
    q=Fraction(N,z); e=floor_log2(q); m=q/pow2(e)
    lm0,lm1=ln_bounds(m)
    fac=Fraction(2*z*z,N*N)
    return fac*(Fraction(e)+lm0/LN2_HI), fac*(Fraction(e)+lm1/LN2_LO)

def ceilq(q): return -((-q.numerator)//q.denominator)
def floorq(q): return q.numerator//q.denominator

def main():
    f=make_table(); N=len(f); N2=N*N
    digest=hashlib.sha256(",".join(map(str,f)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and int(f.sum())==0
    A=fwht_i64(f)
    wt=np.fromiter((s.bit_count() for s in range(N)),dtype=np.int16,count=N)
    Inum=sum(int(a)*int(a)*int(k) for a,k in zip(A,wt))
    assert Fraction(Inum,N2)==Fraction(261,128)

    vals=sorted(set(abs(int(a)) for a in A)|set(abs(int(a)-4) for a in A)|set(abs(int(a)+4) for a in A))
    hb={z:h_bounds(z,N) for z in vals}
    Hlo=sum((hb[abs(int(a))][0] for a in A),Fraction())
    Hhi=sum((hb[abs(int(a))][1] for a in A),Fraction())
    L0=floorq(Hlo*M)

    up=np.empty(N,np.int64); um=np.empty(N,np.int64)
    for s,a0 in enumerate(A):
        a=int(a0); old=hb[abs(a)][0]
        up[s]=ceilq((hb[abs(a-4)][1]-old)*M)
        um[s]=ceilq((hb[abs(a+4)][1]-old)*M)
    CH=up+um; BH=up-um
    CHh=fwht_i64(CH); BHh=fwht_i64(BH)
    CJ=32*wt.astype(np.int64); BJ=-16*wt.astype(np.int64)*A
    CJh=fwht_i64(CJ); BJh=fwht_i64(BJ)
    CtH=int(CH.sum()); CtJ=int(CJ.sum())

    maxD=max(133*N2*(CtH-int(CHh[d]))-128*L0*(CtJ-int(CJh[d])) for d in range(1,N))
    U=[133*N2*int(BHh[x])-128*L0*int(BJh[x]) for x in range(N)]
    max_pos=max(U[x] for x in range(N) if f[x]==1)
    min_neg=min(U[x] for x in range(N) if f[x]==-1)
    score=maxD+max_pos-min_neg
    assert score==-9660085769520308813824
    score_q=Fraction(score,512*M*N2)
    assert score_q==Fraction(-2249163987469,8192000000000000) and score<0

    min_d=min(CtJ-int(CJh[d]) for d in range(1,N))
    min_pos=min(int(BJh[x]) for x in range(N) if f[x]==1)
    max_neg=max(int(BJh[x]) for x in range(N) if f[x]==-1)
    infl_lower=Fraction(min_d+min_pos-max_neg,4*N2)
    assert infl_lower==Fraction(1,8192)

    print("PASS")
    print("truth_table_sha256",digest)
    print("N",N)
    print("balanced_swaps",(N//2)*(N//2))
    print("I_exact",Fraction(Inum,N2))
    print("nonzero_walsh",int(np.count_nonzero(A)))
    print("distinct_entropy_magnitudes",len(vals))
    print("H_interval_width_lt",float(Hhi-Hlo))
    print("H_lower_fixed",f"{L0}/{M}")
    print("DeltaI_global_lower",infl_lower)
    print("score_scaled_integer",score)
    print("T_global_upper",score_q,float(score_q))

if __name__=="__main__": main()
