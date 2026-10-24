#!/usr/bin/env python3
"""
Exact/numerical falsification checks for B16 integrated phase-switch bridge.

This checker does not prove FEI. It verifies:
  (i) the finite-corridor cosine-integral primitive;
  (ii) the signed full-line logarithmic kernel after quadratic cancellation;
  (iii) a genuine n=2 nested-dual-code example, including the entropy identity;
  (iv) a synthetic endpoint-zero/window-nonzero packet showing that a full
       integral identity alone does not control an arbitrary Borel window.
"""
from itertools import product
import mpmath as mp

mp.mp.dps = 50

def tlog(c):
    c = abs(mp.mpf(c))
    return mp.mpf("0") if c == 0 else c*c*mp.log(c)

def k_full(a,b):
    a,b = mp.mpf(a),mp.mpf(b)
    return (tlog(a-b)-tlog(a+b))/4

def J(c,s):
    c,s = abs(mp.mpf(c)),mp.mpf(s)
    if c == 0:
        return -1/(2*s*s)
    return -mp.cos(c*s)/(2*s*s) + c*mp.sin(c*s)/(2*s) - (c*c/2)*mp.ci(c*s)

def k_window(a,b,A,B):
    a,b,A,B = map(mp.mpf,(a,b,A,B))
    return ((J(a-b,B)-J(a-b,A))-(J(a+b,B)-J(a+b,A)))/2

def quad_window(a,b,A,B):
    a,b,A,B = map(mp.mpf,(a,b,A,B))
    return mp.quad(lambda s: mp.sin(a*s)*mp.sin(b*s)/s**3,[A,B])

# 1. Exact finite-window primitive, three signed frequency pairs.
pairs = [(mp.mpf(".7"),mp.mpf(".2")),
         (mp.mpf(".4"),mp.mpf("-.15")),
         (mp.mpf(".55"),mp.mpf(".11"))]
A,B = mp.mpf(40),mp.mpf(150)
max_window_error = mp.mpf(0)
for a,b in pairs:
    err = abs(quad_window(a,b,A,B)-k_window(a,b,A,B))
    max_window_error=max(max_window_error,err)
assert max_window_error < mp.mpf("1e-40")

# 2. Signed full-line kernel. Choose alpha_3 so sum alpha*a*b=0.
terms=[(mp.mpf(".7"),mp.mpf(".2"),mp.mpf("1")),
       (mp.mpf(".4"),mp.mpf("-.15"),mp.mpf("-.8"))]
a3,b3=mp.mpf(".55"),mp.mpf(".11")
moment=sum(alpha*a*b for a,b,alpha in terms)
alpha3=-moment/(a3*b3)
terms.append((a3,b3,alpha3))
quad_moment=sum(alpha*a*b for a,b,alpha in terms)
assert abs(quad_moment)<mp.mpf("1e-45")
closed=sum(alpha*k_full(a,b) for a,b,alpha in terms)

def signed_integrand(s):
    return sum(alpha*mp.sin(a*s)*mp.sin(b*s) for a,b,alpha in terms)/s**3
cuts=[mp.mpf("1e-8"),mp.mpf(".01"),mp.mpf(".1"),mp.mpf(1),
      mp.mpf(5),mp.mpf(20),mp.mpf(100),mp.mpf(500),mp.mpf(2000)]
numeric=mp.mpf(0)
for x,y in zip(cuts[:-1],cuts[1:]):
    numeric += mp.quad(signed_integrand,[x,y])
full_cutoff_error=abs(numeric-closed)
assert full_cutoff_error < mp.mpf("1e-8")

# 3. Genuine n=2 retained code example.
def affine_words(n):
    N=1<<n
    ans=[]
    for c in (0,1):
        for mask in range(1<<n):
            ans.append(tuple((c+((mask & x).bit_count())) & 1 for x in range(N)))
    return ans

def mean_twist(u,r):
    N=len(u)
    return mp.fsum(mp.mpf(u[x])*(-1 if r[x] else 1) for x in range(N))/N

def psi(t):
    t=mp.mpf(t)
    return mp.mpf(0) if t == 0 else t*t*mp.log(1/(t*t))

def H_phys(u,n):
    N=1<<n
    return mp.fsum(
        psi(mp.fsum(mp.mpf(u[x])*(-1 if ((mask & x).bit_count()&1) else 1)
                    for x in range(N))/N)
        for mask in range(1<<n)
    )

def H_P(u,P):
    N=len(u)
    return (mp.mpf(N)/len(P))*mp.fsum(psi(mean_twist(u,r)) for r in P)

n=2
N=1<<n
P0=affine_words(n)                   # RM(1,2), |P0|=2N
P0set=set(P0)
P1=list(product((0,1),repeat=N))     # D={0}, so D^perp=F_2^N
f=(1,1,1,-1)
h=(1,-1,1,1)
fh=tuple(f[i]*h[i] for i in range(N))
packet=[]
for r in P1:
    ap=mp.fsum(mp.mpf(h[x])*(-1 if r[x] else 1)
               for x in range(N) if f[x]==1)/N
    am=mp.fsum(mp.mpf(h[x])*(-1 if r[x] else 1)
               for x in range(N) if f[x]==-1)/N
    alpha=(mp.mpf(1)/(2*N) if r in P0set else mp.mpf(0))-mp.mpf(1)/len(P1)
    packet.append((ap,am,alpha))
assert abs(mp.fsum(alpha*ap*am for ap,am,alpha in packet)) < mp.mpf("1e-45")
assert abs(H_P(h,P0)-H_phys(h,n)) < mp.mpf("1e-45")
assert abs(H_P(fh,P0)-H_phys(fh,n)) < mp.mpf("1e-45")

entropy_bridge=mp.mpf("0.5")*((H_P(fh,P0)-H_P(h,P0))-(H_P(fh,P1)-H_P(h,P1)))
kernel_bridge=(mp.mpf(N)/2)*mp.fsum(
    alpha*(psi(ap-am)-psi(ap+am)) for ap,am,alpha in packet)
assert abs(entropy_bridge-kernel_bridge) < mp.mpf("1e-45")
assert abs(entropy_bridge+mp.log(2)) < mp.mpf("1e-45")

# 4. Algebraic dead route: full integrated endpoint can vanish while a
#    finite Borel window remains nonzero. This packet is NOT asserted to be
#    an admissible FEI code packet.
pairs2=[(mp.mpf(".70"),mp.mpf(".20")),
        (mp.mpf(".43"),mp.mpf(".17")),
        (mp.mpf(".58"),mp.mpf("-.13"))]
m1,m2,m3=[a*b for a,b in pairs2]
q1,q2,q3=[k_full(a,b) for a,b in pairs2]
det=m2*q3-m3*q2
alpha2=(-m1*q3+m3*q1)/det
alpha3=(-m2*q1+q2*m1)/det
aa=[mp.mpf(1),alpha2,alpha3]
zero_moment=mp.fsum(aa[i]*pairs2[i][0]*pairs2[i][1] for i in range(3))
zero_full=mp.fsum(aa[i]*k_full(*pairs2[i]) for i in range(3))
window=mp.fsum(aa[i]*k_window(*pairs2[i],A,B) for i in range(3))
assert abs(zero_moment)<mp.mpf("1e-45")
assert abs(zero_full)<mp.mpf("1e-45")
assert abs(window)>mp.mpf("1e-8")

print("status=PASS")
print("finite_window_pairs=3")
print("max_finite_window_error="+mp.nstr(max_window_error,8))
print("signed_packet_quadratic_moment="+mp.nstr(quad_moment,8))
print("signed_packet_closed_full="+mp.nstr(closed,18))
print("signed_packet_cutoff_2000="+mp.nstr(numeric,18))
print("signed_packet_cutoff_error="+mp.nstr(full_cutoff_error,8))
print("n2_entropy_bridge="+mp.nstr(entropy_bridge,18))
print("n2_expected_minus_ln2="+mp.nstr(-mp.log(2),18))
print("endpoint_zero_packet_window_40_150="+mp.nstr(window,18))
print("endpoint_zero_packet_alpha2="+mp.nstr(alpha2,18))
print("endpoint_zero_packet_alpha3="+mp.nstr(alpha3,18))
