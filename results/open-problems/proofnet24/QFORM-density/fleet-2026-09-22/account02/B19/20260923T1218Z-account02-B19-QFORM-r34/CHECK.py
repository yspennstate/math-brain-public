import math

d0=377/1344
rho0=math.sqrt(29/3072)
Cbase=3*4**(2/3)
rho_min=math.sqrt(15/16)/(4*math.sqrt(2))
H_univ=Cbase*(256/105)**(1/3)
assert (7/8)**2 > d0
assert rho_min > rho0
assert H_univ < 10.175

tau=0.01
r=1/256
eps=math.sqrt(r)
a=10.0
h=1/(16*a*a)
Nu=1000
Nw=51
d=(1-eps)**2
rho=math.sqrt(1-h)/(4*math.sqrt(2))
rhop=eps*math.sqrt(1-eps*h)/(4*math.sqrt(2))
ratio=rhop/(rho*math.sqrt(r))
maxdiag=max(a*(1-h)/Nu,(1-eps)/(16*a),eps/(16*a))
maxpair=1/(2*Nw)
H=Cbase*(a*(1-h)*(1-eps)/2)**(-1/3)
assert d>d0 and r<1/64 and rho>rho0
assert maxdiag<tau and maxpair<tau
assert ratio>1 and ratio<1.001
print('d0',d0)
print('rho0',rho0)
print('rho_min',rho_min)
print('H_universal',H_univ)
print('example detK',d)
print('example rT',r)
print('example rho',rho)
print('example rho_prime',rhop)
print('example transfer_ratio',ratio)
print('example maxdiag',maxdiag)
print('example maxpair',maxpair)
print('example H_bound',H)
print('QFORM_B19_R34_PAIRCOLOOP_CHECK_PASS')
