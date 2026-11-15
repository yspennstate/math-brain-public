from fractions import Fraction as F
import json

def bounds(x,M=30):
 y=(x-1)/(x+1)
 lo=2*sum(y**(2*j+1)/(2*j+1) for j in range(M))
 hi=lo+2*y**(2*M+1)/((2*M+1)*(1-y*y))
 return lo,hi
assert sum(F(1,__import__('math').factorial(k)) for k in range(7))>F(279,200)**3
ln2lo,ln2hi=bounds(F(2));ln5lo,ln5hi=bounds(F(5));lnplo,lnphi=bounds(F(15,4))
assert F(693,1000)<ln2lo<ln2hi<F(694,1000)
assert F(8,5)<ln5lo<ln5hi<F(161,100)
assert F(2643,2000)<lnplo<lnphi<F(661,500)
# A coarse but wholly rational bound on D/(2I) for 25<=n<=39.
Dupper=F(3,2)+(-F(33,100)/F(1233,200)+F(1,76)-F(386,1000)/39)/(2*F(694,1000))
assert F(1233,200)**2>38
assert Dupper<F(183,125) # 1.464
# Maximum correction at rho=4/15 in that block, bounded at n=25.
gupper=F(3,20)*(1+F(161,100)-F(3,2)*F(2643,2000))/F(693,1000)
assert gupper<F(17,125) # .136
# Large-n envelope, bounded at n=40.
assert F(1169,100)**3<40**2
assert F(253,40)**2>40
G40=F(3,2)+(F(100,93)/F(1169,100)-F(33,100)/(2*F(253,40))+F(57,1000)/40+F(1,4*40*39))/F(693,1000)
assert G40<F(8,5)
# High-rho branch on the small block is even smaller.
highrho=F(1,2)+F(661,500)/(2*F(693,1000))+F(17,125)
assert highrho<F(8,5)
print(json.dumps({'small_block_D_half_upper':str(Dupper),'small_block_correction_upper':str(gupper),'small_block_sum_decimal':float(Dupper+gupper),'large_n_Gamma_upper':str(G40),'large_n_Gamma_upper_decimal':float(G40),'high_rho_upper_decimal':float(highrho),'Gamma_bound':'8/5','all_rational_checks_pass':True},indent=2))
