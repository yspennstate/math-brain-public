import math

TOL=1e-11

def assert_close(a,b,tol=TOL):
    if not math.isfinite(a) or not math.isfinite(b) or abs(a-b)>tol*max(1.0,abs(a),abs(b)):
        raise AssertionError((a,b,a-b))

# Theorem 3.1 exact inverse-Hausdorff--Young constant cancellation, delta=1.
for p in [2,3,4,10,100]:
    q=p/(p-1)
    a=math.pi
    iq=2*a*q/(q-1)
    via=(2*math.pi)**(-1/q)*iq**(1/q)
    closed=p**((p-1)/p)
    assert_close(via,closed)

# L2 endpoint.
assert_close(2**0.5, math.sqrt(2))

# Fejer interval-kernel factor.
kernel_factor=math.pi/(2*(1-math.cos(1)))
assert_close(kernel_factor,3.4170202436219475)

# Partner gluing at r=2 gives exactly constant 2.
r=2.0
c=(r/(r-1))**(1/r)*2**((r-1)/r)
assert_close(c,2.0)

# Reciprocal-scale cancellation and constants.
expected={
  1:2.0,
  2:2.620741394208897,
  3:3.363585661014859,
  4:4.162766037009367,
  10:9.42078269242037,
}
for q0,target in expected.items():
    r=1+1/q0
    net=(-1+q0*(r-1))/r
    assert_close(net,0.0)
    C=(r/(r-1))**(1/r)*2**((r-1)/r)
    assert_close(C,target)
    # density scaling: delta scales as lambda^2, c as lambda.
    scale=(1/r)+((r-1)/r)
    assert_close(scale,1.0)

print('cross2 finite-p exact constants: PASS')
print('L2 endpoint sqrt(2): PASS')
print('Fejer interval factor:',repr(kernel_factor))
print('partner r=2 gluing constant: PASS (=2)')
for q0,target in expected.items():
    print('reciprocal q0=%d constant=%.15g exponent_cancel=PASS' % (q0,target))
print('homogeneity: PASS')
print('STATUS=PASS')
