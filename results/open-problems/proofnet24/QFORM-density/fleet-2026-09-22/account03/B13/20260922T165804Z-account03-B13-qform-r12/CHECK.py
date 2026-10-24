import math

phi=(1+math.sqrt(5))/2
assert 4*math.log(phi) < 2

def psi(u):
    a=abs(u)
    if a==0:
        return math.inf
    if a<=1:
        return 1+math.log(1/a)
    return a**(-0.25)

def prod_env(u):
    a=abs(u)
    return 4*math.asinh(1/(2*math.sqrt(a)))

mx=0.0
arg=None
for k in range(-1200,1201):
    u=10**(k/100)
    ratio=prod_env(u)/(2*psi(u))
    if ratio>mx:
        mx=ratio; arg=u
assert mx < 1

Klocal=2**(5/4)*math.sqrt(15)
Kagg=Klocal*math.e**0.25
delta=0.25
xminus=(1-math.sqrt(1-delta))/(1+math.sqrt(1-delta))
bmin=math.sqrt(delta*xminus)
Cheavy=Kagg*(delta*bmin)**(-0.25)
assert abs(xminus-(7-4*math.sqrt(3))) < 1e-14
assert abs(bmin-(2-math.sqrt(3))/2) < 1e-14
assert Cheavy < 27.649

for alpha in (1.0, 1.5, 3.0, 10.0):
    for beta in (0.02, 0.1, 0.7, 2.0, 8.0):
        t=0.7/math.sqrt(alpha+beta)
        s=0.6/math.sqrt(alpha+beta)
        c=t*t*(alpha+beta)
        h=s*s*(alpha+beta)
        D=4*t*t*s*s*alpha*beta
        b=2*t*s*alpha*beta
        assert c<=1 and h<=1
        assert abs(b*b-D*alpha*beta) < 1e-10*max(1,b*b)
        rho=D/(c*h)
        assert rho+1e-14 >= D
        xm=(1-math.sqrt(max(0.0,1-D)))/(1+math.sqrt(max(0.0,1-D)))
        assert alpha*beta + 1e-14 >= xm

print('QFORM_NULLPAIR_PRODUCT_CHECK_PASS')
print(f'4log(phi)={4*math.log(phi):.15f}<2')
print(f'max_grid_product_envelope_over_2Psi={mx:.15f} at u={arg:.3e}')
print(f'local_constant={Klocal:.15f}')
print(f'aggregate_prefactor={Kagg:.15f}')
print(f'xminus_1_4={xminus:.15f}')
print(f'bmin_1_4={bmin:.15f}')
print(f'heavy_Delta_ge_1_4_constant={Cheavy:.15f}')
