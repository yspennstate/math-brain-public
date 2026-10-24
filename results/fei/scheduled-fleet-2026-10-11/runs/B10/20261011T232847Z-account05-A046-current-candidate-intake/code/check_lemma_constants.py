"""Rational constants for independent reviews of the lead's analytic lemmas."""
from fractions import Fraction as Q
from pathlib import Path
import runpy
import json
import math

RUN=Path(__file__).resolve().parents[1]
STAGE1=RUN.parent/'20261011T214251Z-account05-A046-current-candidate-intake'/'code'/'exact_check.py'
module=runpy.run_path(str(STAGE1),run_name='A046_prior_rational_log_kernel')
log2=module['log2']; entropy=module['entropy']; lnunit=module['ln_unit']

checks=[]
def check(label,predicate):
    assert predicate,label
    checks.append(label)

exp_lo=sum((Q(3)**j/Q(math.factorial(j)) for j in range(41)),Q(0))
nextterm=Q(3)**41/Q(math.factorial(41))
exp_hi=exp_lo+nextterm/(1-Q(3,42))
check('20 < exp(3) < 1000/49, hence 49/1000 < exp(-3) < 1/20',exp_lo>20 and exp_hi<Q(1000,49))
check('h2(49/1000)>7/25',entropy([Q(49,1000),Q(951,1000)])[0]>Q(7,25))
check('h2(321/500)>7/25',entropy([Q(321,500),Q(179,500)])[0]>Q(7,25))
p=Q(2,25)
h=entropy([p,1-p]); ell=log2((1-p)/p)
Rupper=h[1]-p*ell[0]/2
check('R(2/25)<131/500',Rupper<Q(131,500))
check('sqrt(2/25)<71/250, so sin^2(theta)<321/500',Q(71,250)**2>p)
check('sqrt(p)/2<exp(-3/2) for p<=2/25',p/4<Q(49,1000))
Llo,Lhi=lnunit(Q(2))
alpha_lo=1-1/(2*Llo)
C_hi=(Q(1,4)+Q(2,69))/Llo
check('1-1/(2ln2)>27/100',alpha_lo>Q(27,100))
check('(1/4+2/69)/ln2<41/100',C_hi<Q(41,100))
check('27/100-(41/100)(2/25)>0',Q(27,100)-Q(41,100)*p>0)
d=Q(301,1000)
check('(sin d/d)^2 >= (1-d^2/6)^2 >97/100', (1-d*d/6)**2>Q(97,100))
check('sin^2 d<=d^2<1/3<1/e',d*d<Q(1,3) and exp_hi<27)
Alo=Q(97,100)*log2(1/(Q(97,100)*d*d))[0]-2*log2(Q(2))[1]/Llo
# 2/ln2 is bounded above by 2/Llo; log2(2) is exactly one.
check('A(d)/d^2>1/2 for d<=301/1000',Alo>Q(1,2))
ell_hi=log2(Q(511,489))[1]
check('log2(511/489)<13/200',ell_hi<Q(13,200))
loss=Q(13,200)*(d-Q(489,2000))
credit=Q(1,2)*Q(489,2000)**2
check('max negative linear loss < A(d) for d>=489/2000',loss<credit)
result={'status':'PASS','check_count':len(checks),'checks':checks,
        'arithmetic':'Fraction; rational exponential tail and atanh logarithm enclosures',
        'thresholds':{'lemma_A_p_max':'2/25','lemma_B_p_min':'489/1000','lemma_B_abs_e_max':'301/1000'},
        'scope':'analytic lemma constants only; continuum box signs replayed separately'}
(RUN/'out'/'LEMMA_CONSTANT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
