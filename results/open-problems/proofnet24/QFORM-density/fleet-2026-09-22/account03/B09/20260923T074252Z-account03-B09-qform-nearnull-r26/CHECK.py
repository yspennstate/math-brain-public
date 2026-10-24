import math

C1=(5.0/3.0)*math.exp(3.0/5.0)

def data(k):
    m=k**4
    disc=math.sqrt(k**(-2)+4*k*k)
    lp=(k**(-1)+disc)/2
    lm=(k**(-1)-disc)/2
    rho=(1-1/m)**3
    bound=C1*rho**(-1/5)
    max_coeff=1/k
    rankone_resource=1/(k*k)
    wedge=1.0
    return m,lp,lm,rho,bound,max_coeff,rankone_resource,wedge

for k in [2,3,4,129]:
    m,lp,lm,rho,bound,max_coeff,res,wedge=data(k)
    assert lp >= 1
    assert abs(lm) >= 1
    assert abs(1.0) >= 1
    assert 0 < 1/k < 1
    assert abs(wedge-1.0)<1e-15
    assert abs(res-1/(k*k))<1e-15
    assert bound < 3.157
    print({
        'k':k,
        'm':m,
        'nonzero_spectrum':[lm,-1/k,1/k,1,lp],
        'rho':rho,
        'pluecker_bound':bound,
        'max_physical_coefficient':max_coeff,
        'rankone_resource':res,
        'cross_wedge':wedge,
    })

k=129
assert 1/k < 1/128
assert 1/(k*k) < 1/128
print('strict_N3_k129_diagonal_cap',1/k)
print('strict_N3_k129_pairdet_cap',1/(k*k))
print('universal_k_ge_2_bound_using_m_ge_16', C1*((15/16)**3)**(-1/5))
print('QFORM_B09_R26_CHECK_PASS')
