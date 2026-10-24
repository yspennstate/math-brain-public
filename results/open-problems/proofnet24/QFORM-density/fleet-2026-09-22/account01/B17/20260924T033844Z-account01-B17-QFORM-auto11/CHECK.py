import sympy as sp
import mpmath as mp

# Exact algebra.
B = sp.Matrix([[sp.Rational(1,3), -sp.Rational(2,3), -sp.Rational(2,3)],
               [-sp.Rational(2,3), sp.Rational(1,3), -sp.Rational(2,3)],
               [-sp.Rational(2,3), -sp.Rational(2,3), sp.Rational(1,3)]])
assert B*B == sp.eye(3)
R = sp.zeros(6,3)
for j in range(3):
    R[2*j,j] = sp.sqrt(2)/2
    R[2*j+1,j] = sp.sqrt(2)/2
assert R.T*R == sp.eye(3)
A = sp.simplify(R*B*R.T)
expected = sp.Matrix([
 [sp.Rational(1,6),sp.Rational(1,6),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3)],
 [sp.Rational(1,6),sp.Rational(1,6),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3)],
 [-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,6),-sp.Rational(1,3),-sp.Rational(1,3)],
 [-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,6),-sp.Rational(1,3),-sp.Rational(1,3)],
 [-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,6)],
 [-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,6)]])
assert A == expected
assert all(x != 0 for x in A)
assert A.eigenvals() == {-1:1, 0:3, 1:2}

# Certified midpoint enclosure of the exact cone-tip integral.
# G(theta)=sqrt(2)*P(|omega(theta)|), integral p_Q(0)=int_0^(2*pi) G(theta)dtheta.
# Global Lipschitz constant L=3*sqrt(3)/2, hence midpoint error <= L(2*pi)^2/(4N).
iv = mp.iv
N = 50000
pi = iv.pi
sqrt = iv.sqrt
rt2, rt3, rt6 = sqrt(2), sqrt(3), sqrt(6)
h = 2*pi/N
total = iv.mpf([0,0])
ambiguous_max = 0
for k in range(N):
    th = (iv.mpf(k)+iv.mpf('0.5'))*h
    c, s = iv.cos(th), iv.sin(th)
    w = [1/rt6+c/2+s/(2*rt3),
         1/rt6-c/2+s/(2*rt3),
         1/rt6-s/rt3]
    aa = [abs(x) for x in w]
    lows = [float(x.a) for x in aa]
    ups = [float(x.b) for x in aa]
    idx = None
    for i in range(3):
        if all(i == j or lows[i] > ups[j] for j in range(3)):
            idx = i
            break
    s1 = aa[0]+aa[1]+aa[2]
    s2 = aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2]
    s3 = aa[0]*aa[1]*aa[2]
    if idx is None:
        ambiguous_max += 1
        candidates = []
        for m in aa:
            candidates.append(1/m-s1/(2*m**2)+s2/(3*m**3)-s3/(4*m**4))
        lo = min(float(x.a) for x in candidates)
        hi = max(float(x.b) for x in candidates)
        P = iv.mpf([lo,hi])
    else:
        m = aa[idx]
        P = 1/m-s1/(2*m**2)+s2/(3*m**3)-s3/(4*m**4)
    total += rt2*P
mid = h*total
L = 3*sqrt(3)/2
err = L*(2*pi)**2/(4*N)
cert_lo = float(mid.a)-float(err.b)
cert_hi = float(mid.b)+float(err.b)
assert ambiguous_max == 0
assert cert_lo > 4.0625
print('QFORM_B17_SYMMETRIC_HOUSEHOLDER_CHECK_PASS')
print('spectrum =', A.eigenvals())
print('all_36_entries_nonzero =', all(x != 0 for x in A))
print('N =', N)
print('midpoint_interval =', mid)
print('lipschitz_error_interval =', err)
print('certified_integral_interval = [%.15f, %.15f]' % (cert_lo, cert_hi))
print('certified_lower_gt_4.0625 =', cert_lo > 4.0625)
