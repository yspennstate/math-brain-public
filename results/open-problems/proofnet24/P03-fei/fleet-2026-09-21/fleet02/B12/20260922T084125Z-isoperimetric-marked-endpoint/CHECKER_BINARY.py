from fractions import Fraction
import math

K_BIN = Fraction(5706,2021)
C = Fraction(3260925607,500000000)
LN2_LOWER = 2*(Fraction(1,3)+Fraction(1,81)+Fraction(1,1215))
DELTA_STAR = 47*(3-math.sqrt(3))/3456

def fwht(vals):
    a=list(vals); h=1
    while h < len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def source_stats(vals,n,i=0):
    N=1<<n
    W=fwht(vals)
    p=[(w/N)**2 for w in W]
    H=-sum(x*math.log2(x) for x in p if x>0)
    I=sum(s.bit_count()*p[s] for s in range(N))
    atom=p[1<<i]
    eps=1-atom
    pg=[p[s^(1<<i)] for s in range(N)]
    Ig=sum(s.bit_count()*pg[s] for s in range(N))
    bi=sum(pg[s] for s in range(N) if s&(1<<i))
    condH=0.0
    if eps>0:
        for s in range(1,N):
            if pg[s]>0:
                q=pg[s]/eps
                condH-=q*math.log2(q)
    M=Ig/eps if eps else 0.0
    beta=bi/eps if eps else 0.0
    return I-1,H,eps,Ig,bi,condH,M,beta

assert 3**12 > 2**19
assert LN2_LOWER > Fraction(9,13)
assert K_BIN < C

print("PASS")
print("K_binary",K_BIN,f"{float(K_BIN):.15f}")
print("C_minus_K_binary",C-K_BIN,f"{float(C-K_BIN):.15f}")
print("ln2_lower",LN2_LOWER,f"{float(LN2_LOWER):.15f}")
print("delta_star",f"{DELTA_STAR:.15f}")

for n in range(12,16):
    N=1<<n
    vals=[1 if (x&1)==0 else -1 for x in range(N)]
    for x in (0,7):
        vals[x]*=-1
    delta,H,eps,Ig,bi,condH,M,beta=source_stats(vals,n,0)
    flag=0.0 if eps in (0.0,1.0) else -eps*math.log2(eps)-(1-eps)*math.log2(1-eps)
    identity=eps*(M-2*beta)
    print("sparse",n,
          "delta",f"{delta:.15f}",
          "flag_over_delta",f"{flag/delta:.15f}",
          "conditional_ratio",f"{condH/(M-2*beta):.15f}",
          "identity_error",f"{abs(delta-identity):.3e}",
          "binary_ok",flag <= float(K_BIN)*delta+1e-12)
