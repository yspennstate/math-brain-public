from fractions import Fraction as Q

N = 12

def log_bounds(x: Q):
    assert x > 0
    y = x
    k = 0
    while y >= 2:
        y /= 2
        k += 1
    while y < 1:
        y *= 2
        k -= 1

    def core(v: Q):
        z = (v - 1) / (v + 1)
        if z == 0:
            return Q(0), Q(0)
        z2 = z*z
        p = z
        s = Q(0)
        for j in range(N+1):
            s += p / Q(2*j+1)
            p *= z2
        lo = 2*s
        tail = 2*p / Q(2*N+3) / (1-z2)
        return lo, lo + tail

    lo, hi = core(y)
    l2lo, l2hi = core(Q(2))
    if k >= 0:
        return lo + k*l2lo, hi + k*l2hi
    return lo + k*l2hi, hi + k*l2lo

l2lo,l2hi = log_bounds(Q(2))
l3lo,l3hi = log_bounds(Q(3))
ratio_lo = l3lo/l2hi
ratio_hi = l3hi/l2lo
A_LO = Q(5,3)-ratio_hi
A_HI = Q(5,3)-ratio_lo
D_LO = Q(1,3)+Q(4,9)*l2lo
D_HI = Q(1,3)+Q(4,9)*l2hi
C = Q(2,9)
B = Q(13,180)
SSTAR_LO = (1-A_HI)/C
SSTAR_HI = (1-A_LO)/C

# Exact source-domain reductions.
assert A_LO > Q(7,90)  # then w-s >= a-(7/9)s >0 for s<=1/10
assert SSTAR_LO > Q(413,100)
assert SSTAR_HI < Q(414,100)

def h_lower(q: Q):
    assert 0 < q < 1
    _, log_hi = log_bounds(q)
    return -q*log_hi

def k_box_lower(lo: Q, hi: Q):
    # K(s)=h(w)+h(1-w)+w log s-ds+B s^2,
    # w=a+(2/9)s. Concavity of h gives endpoint minima.
    wlo = A_LO + C*lo
    whi = A_HI + C*hi
    assert Q(0) < wlo <= whi < Q(1)
    h_w = min(h_lower(wlo), h_lower(whi))
    ulo, uhi = 1-whi, 1-wlo
    h_1w = min(h_lower(ulo), h_lower(uhi))
    log_s_lo = log_bounds(lo)[0]
    log_s_hi = log_bounds(hi)[1]
    prod = min(wlo*log_s_lo, wlo*log_s_hi,
               whi*log_s_lo, whi*log_s_hi)
    return h_w + h_1w + prod - D_HI*hi + B*lo*lo

def endpoint_box_lower(lo: Q, hi: Q):
    # E(s)=w log(s/w)-d s+B s^2 <= K(s) whenever w<=1.
    # We prove E>0 on the larger rational interval [4.13,4.14].
    wlo = A_LO + C*lo
    whi = A_HI + C*hi
    assert wlo > 0
    rlo = lo/whi
    rhi = hi/wlo
    lrlo = log_bounds(rlo)[0]
    lrhi = log_bounds(rhi)[1]
    prod = min(wlo*lrlo, wlo*lrhi, whi*lrlo, whi*lrhi)
    return prod - D_HI*hi + B*lo*lo

# Main compact interval: 1000 exact rational boxes.
start, end = Q(1,10), Q(413,100)
boxes = 1000
width = (end-start)/boxes
main_min = None
main_arg = None
for j in range(boxes):
    lo = start + j*width
    hi = lo + width
    lb = k_box_lower(lo,hi)
    assert lb > 0, (j,lo,hi,lb)
    if main_min is None or lb < main_min:
        main_min, main_arg = lb, (j,lo,hi)

# Endpoint collar: 10 exact rational boxes; no entropy near 1 is needed.
start2, end2 = Q(413,100), Q(414,100)
boxes2 = 10
width2 = (end2-start2)/boxes2
end_min = None
end_arg = None
for j in range(boxes2):
    lo = start2 + j*width2
    hi = lo + width2
    lb = endpoint_box_lower(lo,hi)
    assert lb > 0, (j,lo,hi,lb)
    if end_min is None or lb < end_min:
        end_min, end_arg = lb, (j,lo,hi)

print('R15 F0111 one-big universal scalar core')
print('log bounds terms:', N+1)
print('a > 7/90: PASS')
print('413/100 < s_* < 414/100: PASS')
print('K(s)>0 on [1/10,413/100]: PASS', boxes, 'boxes')
print('main minimum lower bound > 0: PASS')
print('main minimum box:', main_arg)
print('main lower-bound numerator/denominator digits:', len(str(main_min.numerator)), len(str(main_min.denominator)))
print('endpoint E(s)>0 on [413/100,414/100]: PASS', boxes2, 'boxes')
print('endpoint minimum lower bound > 0: PASS')
print('endpoint minimum box:', end_arg)
print('endpoint lower-bound numerator/denominator digits:', len(str(end_min.numerator)), len(str(end_min.denominator)))
print('ALL_EXACT_CHECKS_PASS')
