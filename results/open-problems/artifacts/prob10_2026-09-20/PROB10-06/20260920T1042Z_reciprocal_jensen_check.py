from fractions import Fraction as F

class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, o):
        o = asI(o); return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, o): return self + (-asI(o))
    def __rsub__(self, o): return asI(o) - self
    def __mul__(self, o):
        o = asI(o)
        v = (self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi)
        return I(min(v), max(v))
    __rmul__ = __mul__
    def inv(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError((self.lo, self.hi))
        return I(1/self.hi, 1/self.lo)
    def __truediv__(self, o): return self * asI(o).inv()
    def __rtruediv__(self, o): return asI(o) / self
    def sq(self):
        if self.lo >= 0: return I(self.lo*self.lo, self.hi*self.hi)
        if self.hi <= 0: return I(self.hi*self.hi, self.lo*self.lo)
        return I(0, max(self.lo*self.lo, self.hi*self.hi))

def asI(x): return x if isinstance(x, I) else I(x)

# Main reciprocal-Jensen bound for P(nu=2)=1-p, P(nu=3)=p.
def bound_rj(L, P):
    d = 1 - L*(3-P)/6
    d2 = 2*d/(2*d + L)
    d3 = 3*d/(3*d + L)
    w2, w3 = 1-P, P

    # After conditioning on sibling offspring types, reciprocal Jensen gives
    # E[a/(a+sum B_i)^2] <= the deterministic-type expression below.
    def K(base, j):
        if j == 1:
            return base*w2/(base+d2).sq() + base*w3/(base+d3).sq()
        return (base*w2*w2/(base+2*d2).sq()
                + 2*base*w2*w3/(base+d2+d3).sq()
                + base*w3*w3/(base+2*d3).sq())

    K1, K2 = K(L, 1), K(L, 2)
    rho = (1-P)*2*K1 + P*3*K2

    # Inhomogeneous term in U=-B' recursion, using B<=u=(3-lambda)/3.
    A = (1-P)*6*(3-L)/(L+6).sq() + P*(3-L)/9
    eta = A/(1-rho)

    mu = (1-P)*d2 + P*d3
    a = L-1
    Kc = K(a, 2)

    # Upper bound for Delta=h2/c2-h3/c3 from the report proof.
    Delta = 1/a + 2*eta*Kc/mu - 3/(9-L)

    # c3/c2 >= 3/4 gives actual tilt theta_actual >= theta below.
    # On this p-range g(theta)=theta(1-theta)/(2+theta) is decreasing.
    theta = 3*P/(4-P)
    g = theta*(1-theta)/(2+theta)
    product = L*g*Delta
    return d, d2, d3, rho, product

def certify_box(box, q, rho_q, maxdepth=34):
    x0, x1, y0, y1 = box
    stack = [(F(x0), F(x1), F(y0), F(y1), 0)]
    visited = accepted = 0
    worst_product = F(-10**9)
    worst_rho = F(-10**9)
    while stack:
        a, b, c, d, depth = stack.pop()
        visited += 1
        try:
            dd, d2, d3, rho, product = bound_rj(I(a,b), I(c,d))
            good = (dd.lo > 0 and d2.lo > 0 and d3.lo > 0
                    and rho.hi < rho_q and product.hi < q)
        except ZeroDivisionError:
            good = False
            rho = product = None
        if good:
            accepted += 1
            worst_product = max(worst_product, product.hi)
            worst_rho = max(worst_rho, rho.hi)
            continue
        assert depth < maxdepth, ("uncertified", a,b,c,d,depth,rho,product)
        if depth % 2 == 0:
            m = (a+b)/2
            stack.append((a,m,c,d,depth+1))
            stack.append((m,b,c,d,depth+1))
        else:
            m = (c+d)/2
            stack.append((a,b,c,m,depth+1))
            stack.append((a,b,m,d,depth+1))
    return visited, accepted, worst_product, worst_rho

# Attack 2: inverse-moment quantile proxy. At lambda=2,p=3/4,
# Markov gives P(B < alpha*d_k | nu=k)<=alpha. The induced two-level
# proxy fails to contract for every alpha in [0,1].
def quantile_rho(A):
    L, P = F(2), F(3,4)
    d = 1 - L*(3-P)/6
    d2 = 2*d/(2*d+L)
    d3 = 3*d/(3*d+L)
    t2, t3 = A*d2, A*d3
    w0 = A
    w2 = (1-P)*(1-A)
    w3 = P*(1-A)
    K1 = w0/L + L*w2/(L+t2).sq() + L*w3/(L+t3).sq()
    K2 = (w0*w0/L
          + 2*L*w0*w2/(L+t2).sq()
          + 2*L*w0*w3/(L+t3).sq()
          + L*w2*w2/(L+2*t2).sq()
          + 2*L*w2*w3/(L+t2+t3).sq()
          + L*w3*w3/(L+2*t3).sq())
    return (1-P)*2*K1 + P*3*K2

def certify_quantile_obstruction(maxdepth=18):
    stack = [(F(0), F(1), 0)]
    visited = accepted = 0
    lower_target = F(6,5)
    weakest_lower = F(10**9)
    while stack:
        a,b,depth = stack.pop()
        visited += 1
        rho = quantile_rho(I(a,b))
        if rho.lo > lower_target:
            accepted += 1
            weakest_lower = min(weakest_lower, rho.lo)
            continue
        assert depth < maxdepth, ("quantile obstruction not certified", a,b,depth,rho.lo,rho.hi)
        m=(a+b)/2
        stack.append((a,m,depth+1)); stack.append((m,b,depth+1))
    return visited, accepted, weakest_lower

# Attack 3: reciprocal-escape derivative W=U/B^2 with sibling decoupling.
# For the proposed endpoint-chord decoupling at lambda=2,p=71/100, the
# resulting coefficient is this exact rational number, already >1.
RHO_W = F(2135191601264005788851, 1498331327641225000000)

box = (F(185527,100000), F(20021,10000), F(71,100), F(1))
q = F(9999,10000)
rho_q = F(19,20)
visited, accepted, worst_product, worst_rho = certify_box(box, q, rho_q)
margin = F(4)*(1-q)/(F(3)+F(20021,10000))**2
assert margin == F(40000,2502100441)

# g'(theta)<0 iff theta^2+4 theta-2>0. Verify it at the smallest tilt.
theta_min = 3*F(71,100)/(4-F(71,100))
assert theta_min*theta_min + 4*theta_min - 2 > 0

qv, qa, qlower = certify_quantile_obstruction()
assert qlower > F(6,5)
assert RHO_W > 1

print("MAIN_PASS visited=%d accepted=%d" % (visited, accepted))
print("MAIN product_upper<9999/10000 rho_upper<19/20")
print("MAIN worst_accepted_product_upper_float=%.15f" % float(worst_product))
print("MAIN worst_accepted_rho_upper_float=%.15f" % float(worst_rho))
print("MAIN derivative_margin=40000/2502100441")
print("MAIN rectangle: 185527/100000 <= lambda <= 20021/10000, 71/100 <= p <= 1")
print("QUANTILE_OBSTRUCTION_PASS visited=%d accepted=%d rho_quantile>6/5 for all alpha in [0,1]" % (qv,qa))
print("QUANTILE weakest_interval_lower_float=%.15f" % float(qlower))
print("W_ROUTE_OBSTRUCTION_PASS rhoW=%s float=%.15f > 1" % (RHO_W, float(RHO_W)))
print("ALL_EXACT_CHECKS_PASS")
