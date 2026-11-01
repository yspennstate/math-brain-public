from math import sqrt, e, isclose


def diffuse_bank(m):
    assert m % 2 == 0 and m >= 2
    u = [1.0 / sqrt(m)] * m
    v = [(1.0 if k < m // 2 else -1.0) / sqrt(m) for k in range(m)]
    g11 = sum(x*x for x in u)
    g22 = sum(x*x for x in v)
    g12 = sum(x*y for x,y in zip(u,v))
    delta = g11*g22-g12*g12
    minor_sum = 0.0
    max_minor = 0.0
    for k in range(m):
        for l in range(k+1,m):
            d = abs(u[k]*v[l]-u[l]*v[k])
            minor_sum += d*d
            max_minor = max(max_minor,d)
    assert isclose(g11,1.0,rel_tol=0,abs_tol=1e-12)
    assert isclose(g22,1.0,rel_tol=0,abs_tol=1e-12)
    assert isclose(g12,0.0,rel_tol=0,abs_tol=1e-12)
    assert isclose(delta,1.0,rel_tol=0,abs_tol=1e-12)
    assert isclose(minor_sum,delta,rel_tol=1e-12,abs_tol=1e-12)
    assert isclose(max_minor,2.0/m,rel_tol=1e-12,abs_tol=1e-12)
    aggregate = 2.0*sqrt(e)*delta**(-0.25)
    single = 2.0/sqrt(max_minor)
    return delta, minor_sum, max_minor, aggregate, single

print('QFORM_ZERO_PAIR_CROSSBANK_CHECK')
print('2sqrt(e)=',2.0*sqrt(e))
for m in (10,100,1000):
    delta, minor_sum, max_minor, aggregate, single = diffuse_bank(m)
    print('m=',m,'Delta=',delta,'sum_minors_sq=',minor_sum,
          'max_minor=',max_minor,'aggregate_bound=',aggregate,
          'best_single_minor_bound=',single)
print('PASS')
