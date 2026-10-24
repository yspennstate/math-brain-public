from fractions import Fraction
import mpmath as mp

mp.iv.dps = 50
iv = mp.iv

def lo_iv(x):
    return mp.mpf(x._mpi_[0])

def hi_iv(x):
    return mp.mpf(x._mpi_[1])

# Exact rational matrices.
R_num = [
    [1,1,1],
    [1,-1,1],
    [1,1,-1],
    [1,-1,-1],
]
B = [
    [Fraction(2,27), Fraction(-25,27), Fraction(-10,27)],
    [Fraction(-25,27), Fraction(2,27), Fraction(-10,27)],
    [Fraction(-10,27), Fraction(-10,27), Fraction(23,27)],
]
A_expected = [
    [Fraction(-7,12), Fraction(1,36), Fraction(-23,36), Fraction(-1,36)],
    [Fraction(1,36), Fraction(77,108), Fraction(-43,108), Fraction(31,108)],
    [Fraction(-23,36), Fraction(-43,108), Fraction(17,108), Fraction(43,108)],
    [Fraction(-1,36), Fraction(31,108), Fraction(43,108), Fraction(77,108)],
]

def matmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]

R = [[Fraction(v,2) for v in row] for row in R_num]
Rt = list(map(list, zip(*R)))
assert matmul(Rt,R) == [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]
A = matmul(matmul(R,B),Rt)
assert A == A_expected
I3 = [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]
assert matmul(B,B) == I3
assert sum(B[i][i] for i in range(3)) == Fraction(1,1)  # spectrum 1,1,-1

# Cone-tip integral certificate for n=(5,5,2)/sqrt(54).
# Unit cone ray:
# omega=(n + cos(theta)e1 + sin(theta)e2)/sqrt(2),
# e1=(1,-1,0)/sqrt(2), e2=(1,1,-5)/(3sqrt(3)).
# Therefore
# w1=5/(6sqrt3)+cos/2+sin/(3sqrt6)
# w2=5/(6sqrt3)-cos/2+sin/(3sqrt6)
# w3=1/(3sqrt3)-5 sin/(3sqrt6).
# H=sum of the two largest absolute coordinates.
# H is 1-Lipschitz in theta:
# x -> top2(|x|) is sqrt(2)-Lipschitz and |omega'|=1/sqrt(2).

def certified_tip_interval(N=20000):
    pi_iv = iv.pi
    delta_iv = 2*pi_iv/N
    dl, du = lo_iv(delta_iv), hi_iv(delta_iv)
    sqrt3, sqrt6 = iv.sqrt(3), iv.sqrt(6)
    c0, cs = 5/(6*sqrt3), 1/(3*sqrt6)
    z0, zs = 1/(3*sqrt3), 5/(3*sqrt6)
    low_sum = mp.mpf('0')
    up_sum = mp.mpf('0')
    for k in range(N):
        th = (2*k+1)*pi_iv/N
        s, c = iv.sin(th), iv.cos(th)
        ws = [c0+c/2+cs*s, c0-c/2+cs*s, z0-zs*s]
        a = [abs(w) for w in ws]
        upper = [hi_iv(x) for x in a]
        lower = [lo_iv(x) for x in a]
        hu = max(upper[0]+upper[1], upper[0]+upper[2], upper[1]+upper[2])
        hl = max(lower[0]+lower[1], lower[0]+lower[2], lower[1]+lower[2])
        # H(theta) <= H(mid)+delta/2 and >= H(mid)-delta/2.
        low_sum += dl/(hu+du/2)
        denom = hl-du/2
        assert denom > 0
        up_sum += du/denom
    invsqrt2 = 1/iv.sqrt(2)
    return lo_iv(invsqrt2)*low_sum, hi_iv(invsqrt2)*up_sum

lb, ub = certified_tip_interval()
old = 4*iv.log(1+iv.sqrt(2))
old_lb, old_ub = lo_iv(old), hi_iv(old)
three_sqrt2 = 3*iv.sqrt(2)
thr_lb, thr_ub = lo_iv(three_sqrt2), hi_iv(three_sqrt2)
bank = (iv.pi*iv.sqrt(2)/3)*(1+4/iv.sqrt(5))
bank_lb, bank_ub = lo_iv(bank), hi_iv(bank)

assert lb > mp.mpf(89)/25
assert lb > old_ub
assert ub < thr_lb
assert bank_ub < thr_lb

print("QFORM_B17_TETRA_OUTOFPLANE_CHECK_PASS")
print("tip_interval=[%s, %s]" % (mp.nstr(lb,30), mp.nstr(ub,30)))
print("rational_lower=89/25 =", mp.nstr(mp.mpf(89)/25,30))
print("old_45_interval=[%s, %s]" % (mp.nstr(old_lb,30), mp.nstr(old_ub,30)))
print("partner_bank_interval=[%s, %s]" % (mp.nstr(bank_lb,30), mp.nstr(bank_ub,30)))
print("3sqrt2_interval=[%s, %s]" % (mp.nstr(thr_lb,30), mp.nstr(thr_ub,30)))
