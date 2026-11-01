#!/usr/bin/env python3
from fractions import Fraction

# Exact arithmetic checker for the P26 all-fixed-distance theorem on the
# p=2 Eisenstein (9,3)-biregular parameters K=8,k=2.


def padd(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c


def pscale(a,c):
    return [c*x for x in a]


def pshift_x_minus_c(a,c):
    return padd([0]+a, pscale(a,-c))


def peval(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y


def degree(m):
    return 18*16**(m-1)


# f_m(B) is adjacency at exact bigraph distance 2m on the left side.
f={1:[-9,1], 2:[72,-19,1]}
for m in range(2,9):
    f[m+1]=padd(pshift_x_minus_c(f[m],10), pscale(f[m-1],-16))

for m in range(1,9):
    assert peval(f[m],27)==degree(m)
    assert Fraction(peval(f[m],0),degree(m))==Fraction((-1)**m,2**m)

assert f[4]==[4608,-2732,520,-39,1]
assert Fraction(5*4-7,4**4)==Fraction(13,256)
assert Fraction(13,256)<Fraction(1,16)
for m in range(4,30):
    assert 5*m-7 <= 2**m


def radial_counts(m):
    # s is the number of initial ancestor edges followed toward the root.
    # Delta=m-s.  For K=8,k=2 the exact multiplicities are as below.
    out={m:16**m, -m:1}
    for a in range(0,m):
        s=2*a+1
        delta=m-s
        out[delta]=out.get(delta,0)+16**(m-a-1)
    for a in range(1,m):
        s=2*a
        delta=m-s
        out[delta]=out.get(delta,0)+14*16**(m-a-1)
    return dict(sorted(out.items()))

for m in range(1,9):
    c=radial_counts(m)
    D=degree(m)
    assert sum(c.values())==D
    v=sum(Fraction(delta*cnt,D) for delta,cnt in c.items())
    M2=sum(Fraction(delta*delta*cnt,D) for delta,cnt in c.items())
    v_formula=Fraction(m,1)-Fraction(8,45)*(1-Fraction(1,16**m))
    M2_formula=(Fraction(675*m*m-240*m+232,675)
                -Fraction(240*m+232,675*16**m))
    assert v==v_formula
    assert M2==M2_formula

m=4
c4=radial_counts(m)
v4=Fraction(m,1)-Fraction(8,45)*(1-Fraction(1,16**m))
M24=(Fraction(675*m*m-240*m+232,675)
     -Fraction(240*m+232,675*16**m))
tau2=M24/(v4**3)

assert c4=={-4:1,-3:1,-2:14,-1:16,0:224,1:256,2:3584,3:4096,4:65536}
assert v4==Fraction(93935,24576)
assert M24==Fraction(1100129,73728)
assert tau2==Fraction(221485222330368,828862171175375)
assert Fraction(1,1)/v4==Fraction(24576,93935)
assert 16**4 < degree(4)-1

print('P26 T08 exact-distance-8 / all-m checker')
print('f4_coeff_low_to_high=', f[4], sep='')
print('D4=', degree(4), sep='')
print('q4(27)=', Fraction(peval(f[4],27),degree(4)), sep='')
print('q4(0)=', Fraction(peval(f[4],0),degree(4)), sep='')
print('bulk_chebyshev_bound=', Fraction(13,256), sep='')
print('zero_mode_bound=', Fraction(1,16), sep='')
print('radial_counts_m4=', c4, sep='')
print('v4=', v4, sep='')
print('M2_4=', M24, sep='')
print('tau2_4=', tau2, sep='')
print('center_coefficient_1_over_v4=', Fraction(1,1)/v4, sep='')
print('branching=', 16**4, ' output_D_minus_1=', degree(4)-1, sep='')
print('general_v_formula=m-8/45*(1-16^-m)')
print('general_M2_formula=(675m^2-240m+232)/675-(240m+232)/(675*16^m)')
print('ALL_CHECKS_PASS')
