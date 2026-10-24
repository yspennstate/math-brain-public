from fractions import Fraction as R
import json
from pathlib import Path
ROOT=Path(__file__).parent
p=[R(281,400),R(19,400),R(99,400),R(1,400)]
v=[R(-83,100),R(3,100),R(63,100),R(17,100)]
pe=[R(17368,25000),R(-3633,25000),R(-13603,25000),R(-132,25000)]
w=[R(-32493,25000),R(12493,25000),R(27493,25000),R(-7493,25000)]
delta=R(1,1000)
r=[delta*vi/pi for vi,pi in zip(v,p)]
F=sum(vi*vi/pi for vi,pi in zip(v,p))
S=sum(2*vi*wi/pi-vi*vi*pei/(pi*pi) for vi,wi,pi,pei in zip(v,w,p,pe))

def atanh_interval(x,m=5):
 center=sum(x**(2*k+1)/R(2*k+1) for k in range(m))
 tail=abs(x)**(2*m+1)/(R(2*m+1)*(1-x*x))
 return center-tail,center+tail

lo=hi=R(0)
for vi,wi,pi,pei,ri in zip(v,w,p,pe,r):
 l,h=atanh_interval(ri)
 coeff=delta*wi
 if coeff<0:l,h=h,l
 rational=delta*vi*(delta*wi-ri*pei)/(pi*(1-ri*ri))
 lo+=coeff*l+rational;hi+=coeff*h+rational
assert hi<R(-4,10**6)
assert lo>R(-5,10**6)

# Same data certify that the actual measured mutual information increases.
# I_s' = 1/2 sum p_s' log(1-r^2)+delta sum w atanh(r).
def log1m_interval(x,m=8):
 assert 0<=x<1
 center=-sum(x**k/R(k) for k in range(1,m+1))
 tail=x**(m+1)/(R(m+1)*(1-x))
 return center-tail,center
mi_lo=mi_hi=R(0)
for wi,pei,ri in zip(w,pe,r):
 for coeff,interval in [(pei/2,log1m_interval(ri*ri)),(delta*wi,atanh_interval(ri))]:
  l,h=interval
  if coeff<0:l,h=h,l
  mi_lo+=coeff*l;mi_hi+=coeff*h
assert mi_lo>R(-223,10**8) and mi_hi<R(-221,10**8)

out={
 'A':[['1/20','1/10'],['1/10','1/4']],
 'B':[['1003/5000','1996/5000'],['1996/5000','3997/5000']],
 'Q':[['1/5','-2/5'],['-2/5','4/5']],
 'delta':'1/1000',
 'p':[str(x) for x in p], 'v':[str(x) for x in v], 'p_derivative':[str(x) for x in pe], 'w':[str(x) for x in w], 'r':[str(x) for x in r],
 'fisher':str(F),'fisher_scaled_derivative':str(S),'fisher_scaled_derivative_float':float(S),
 'cross_dissipation_exact_lower':str(lo),'cross_dissipation_exact_upper':str(hi),'cross_dissipation_decimal_interval':[float(lo),float(hi)],
 'mutual_information_derivative_exact_lower':str(mi_lo),'mutual_information_derivative_exact_upper':str(mi_hi),'mutual_information_derivative_decimal_interval':[float(mi_lo),float(mi_hi)],
 'rational_certificate':'-5/10^6 < cross dissipation < -4/10^6',
 'proof_method':'Fraction arithmetic, five terms of atanh and geometric rational tails; eight terms for log(1-x).'
}
(ROOT/'exact_obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if 'exact_' not in k},indent=2))
