"""Exact rational algebra and Gaussian dependence diagnostic; not an LQG simulation."""
from fractions import Fraction as F
from math import erfc, sqrt, log, exp
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
out=[]
# gamma=sqrt(8/3), d_gamma=4 gives xi*Q=5/6, xi^2=1/6.
a,b=F(5,6),F(1,6)
q=1-a+b
for eps in [F(1,10),F(1,2),F(1)]:
    s=1+eps
    gap=q+a*s-b*s*s-1
    assert gap==eps*(a-2*b-b*eps) and gap>0
    out.append({'case':'Brownian parameters, conditional only','s':str(s),'qcrit':str(q),'summability_gap':str(gap)})
# For H~N(0,2L), event A={H>=cL}, tilting by e^(tH) gives
# P_t(A)=Gaussian tail((c-2t)*sqrt(L/2)). No independence.
tail=lambda z: erfc(z/sqrt(2))/2
c,t=1.0,0.5
for n in [8,32,128]:
    L=n*log(2)
    p=tail(c*sqrt(L/2))
    pt=tail((c-2*t)*sqrt(L/2))
    out.append({'case':'correlated Gaussian event','dyadic_n':n,'ordinary_event_probability':p,'tilted_event_probability':pt,'ratio_to_independent_prediction':pt/p})
out.append({'case':'Holder marginal probability threshold, conditional only','a':'5/6','b':'1/6','qcrit':'1/3','critical_p_exact':'1/2+sqrt(2)/3','critical_p':0.5+sqrt(2)/3,'optimizing_t_exact':'1+sqrt(2)','optimizing_t':1+sqrt(2)})
(ROOT/'exponent_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
