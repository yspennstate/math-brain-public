import math

C_COL = 16*math.sqrt(2)/(3**(3/4))
C_TIME = math.sqrt(2*math.pi)*C_COL
assert C_COL < 9.927
assert C_TIME < 24.882

# Indefinite adversary R^-_eta.  Matrix eigenvalues are 1/eta and -1.
for eta in [1/256, 1e-4, 1e-8, 1e-12]:
    a = (1-eta)/(2*eta)
    b = (1+eta)/(2*eta)
    c = a
    tr = a+c
    det = a*c-b*b
    disc = math.sqrt(tr*tr-4*det)
    eig1=(tr+disc)/2
    eig2=(tr-disc)/2
    assert abs(eig1-1/eta) <= 1e-10*max(1,1/eta)
    assert abs(eig2+1) <= 1e-10*max(1,1/eta)
    D=abs(det)
    assert abs(D-1/eta) <= 1e-10*max(1,1/eta)
    m=abs(a)
    lower = math.sqrt(2*eta)/8 * math.log(1/(8*math.sqrt(eta)))
    scaled = lower*math.sqrt(m)
    theorem = 8/math.sqrt(m)*(3+2*max(0,math.log(2*math.sqrt(2)*m/math.sqrt(D))))
    collision = C_COL/math.sqrt(m)
    print(f'eta={eta:g} m={m:.12g} D={D:.12g} lowerH={lower:.12g} lowerHsqrtm={scaled:.12g} theorem={theorem:.12g} collision<={collision:.12g}')

print('C_col', C_COL)
print('weighted_time_constant', C_TIME)
print('QFORM_B03_PAIR_LOG_BRIDGE_PASS')
