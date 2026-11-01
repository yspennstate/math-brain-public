import math

s0=1/64
tau=2**-16
eta=2/63
g=32/63
beta=(s0*math.sqrt(1-g)-tau)/math.sqrt(62)
beta_alt=1/(64*math.sqrt(126))-1/(65536*math.sqrt(62))
beta0=1/(512*math.sqrt(2))
h=1/2-1/(4*math.sqrt(2))
s_light=g*s0-tau
s_grid=h*g*s0-tau
C_R2=3.929131770449763
H=C_R2*s_grid**(-1/4)
interval=H/(2**0.25)
a0=4.2146684313588616e-8
trans=a0/(64*math.sqrt(2))

assert abs(eta/g-1/16)<1e-15
assert abs((1-g)/62-1/126)<1e-15
assert abs(beta-beta_alt)<1e-15
assert beta>beta0
assert s_light>0
assert s_grid>0
assert H<17.484826
assert interval<14.702928
assert abs(trans-4.6565947316667495e-10)<1e-24

print('eta/g',eta/g)
print('beta*',beta)
print('beta0',beta0)
print('margin',beta-beta0)
print('s_light',s_light)
print('h',h)
print('s_grid',s_grid)
print('H_1/4_bound',H)
print('interval_constant',interval)
print('partner_transverse_s2',trans)
print('QFORM_B20_R49_DEEPPEEL_GRID_CHECK_PASS')
