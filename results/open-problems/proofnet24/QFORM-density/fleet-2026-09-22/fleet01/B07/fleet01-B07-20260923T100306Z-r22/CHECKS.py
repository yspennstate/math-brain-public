import itertools
import math
import numpy as np

D = 12824703626379264
C_shadow = 13*math.e*math.sqrt(5/6)*(5/3)**(-3/26)*(5/2)**(-1/13)
print('C_shadow=', repr(C_shadow))
print('r29_shadow_cap=', repr(C_shadow*D**(5/26)))
print('r29_partner_cap=', repr(3*math.sqrt(math.e)*(6*D)**(1/6)))
print('double_pair_denominator=', 5*D)

rng = np.random.default_rng(2209231003)
max_ratio = 0.0
count = 0
for m,n in [(4,4),(5,6),(7,8),(9,7)]:
    for _ in range(25):
        M = rng.normal(size=(m,n))
        i=a=0
        R2 = float(np.dot(M[i],M[i]))
        for K in itertools.combinations(range(1,m),2):
            g=0.0
            rows=(i,)+K
            for L in itertools.combinations(range(1,n),2):
                cols=(a,)+L
                d=float(np.linalg.det(M[np.ix_(rows,cols)]))
                g += d*d
            W=0.0
            for T in itertools.combinations(range(n),2):
                d=float(np.linalg.det(M[np.ix_(K,T)]))
                W += d*d
            if g>1e-12:
                ratio=g/(R2*W)
                max_ratio=max(max_ratio,ratio)
                assert ratio <= 1+1e-9
                count += 1
print('shadow_pairs_checked=', count)
print('max_g_over_R2W=', repr(max_ratio))
assert abs(C_shadow-28.34252305879395) < 1e-12
assert 5*D == 64123518131896320
print('STATUS=QFORM_ANCHORED_E3_EXACT_E2_SHADOW_CHECK_PASS')
