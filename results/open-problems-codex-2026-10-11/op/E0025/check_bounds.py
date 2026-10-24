"""Short supplementary numerical checks; the proof does not rely on quadrature."""
import mpmath as mp, json, pathlib
mp.mp.dps=100
m=mp.mpf(4)/3*(1-mp.power(2,-mp.mpf(3)/4))
l=4*(mp.power(2,mp.mpf(1)/4)-1)
q=mp.mpf(4)/5*(mp.power(2,mp.mpf(5)/4)-1)
c0=(1-mp.cos(1))*4*(1-mp.power(2,-mp.mpf(1)/4))
C0=mp.mpf(28)/3
data=[]
for n in range(1,6):
 r=mp.power(2,-16**n); z=1/mp.sqrt(r); theta=mp.sqrt(r)
 # Rescale the own block to [1,2]; this phase is small, never oscillatory.
 ownI=r**(-mp.mpf(1)/4)*mp.quad(lambda u: (mp.sin(theta*u)/theta)*u**(-mp.mpf(7)/4),[1,2])
 ownR=r**(mp.mpf(1)/4)*mp.quad(lambda u: 2*(mp.sin(theta*u/2)/theta)**2*u**(-mp.mpf(7)/4),[1,2])
 coarse=sum(m*mp.power(2,mp.mpf(3)/4*16**k) for k in range(1,n))
 # Full stable base is 4 Gamma(3/4) (-iz)^(1/4); truncation error <=8.
 stableR=4*mp.gamma(mp.mpf(3)/4)*mp.cos(mp.pi/8)*z**mp.mpf('.25')
 stableI=4*mp.gamma(mp.mpf(3)/4)*mp.sin(mp.pi/8)*z**mp.mpf('.25')
 realLo=max(c0*z**mp.mpf('.25'),stableR-8)+ownR
 realHi=stableR+8+ownR+2*coarse+q*r**19
 imagLo=ownI+stableI-8-coarse
 imagHi=ownI+stableI+8+coarse+2*l*r**mp.mpf('3.5')
 ratioLo=imagLo/(1+realHi); ratioHi=imagHi/(1+realLo)
 entry={'n':n,'log10_ratio_lower':mp.nstr(mp.log10(ratioLo),18),
        'log10_ratio_upper':mp.nstr(mp.log10(ratioHi),18),
        'normalized_own_I':mp.nstr(ownI*r**mp.mpf('.25'),18),
        'normalized_own_R':mp.nstr(ownR/r**mp.mpf('.25'),18)}
 # Supplementary tests of the analytic good-band comparison for q in [4,5].
 entries=[]
 for exponent in ['4','4.25','4.5','4.75','5']:
  e=mp.mpf(exponent); frequency=r**(-e)
  bound=(C0*frequency**mp.mpf('.25')+4*m*r**(-mp.mpf('.75'))+2*l*frequency*r**4)
  entries.append({'exponent':exponent,'upper_B_over_A':mp.nstr((1+bound)/(c0*frequency**mp.mpf('.25')),16)})
 entry['good_band_bounds']=entries
 data.append(entry)
 print(json.dumps(entry),flush=True)
pathlib.Path('numerical_checks.json').write_text(json.dumps({'precision_digits':100,'data':data},indent=2),encoding='utf8')
