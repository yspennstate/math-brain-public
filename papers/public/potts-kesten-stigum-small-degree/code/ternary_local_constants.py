"""Exact constants for the local exclusion at d >= 3."""
from fractions import Fraction as F
import json,pathlib
def main():
    eta=F(2887,5000);kappa=2*eta**4;assert 3*eta*eta>1
    denom=1-kappa-F(1,9);assert denom>0
    Cu0=F(341,100);Ct0=F(44,25);assert F(34,15)/denom<Cu0;assert F(20,27)/(1-eta)<Ct0
    Mmax=F(333,2000);radius=F(37,2000);assert 9*radius==Mmax
    a0=2*eta*Ct0/27+Cu0/162;b0=Ct0**2/54+eta*Cu0*Ct0/162+Cu0**2/5832
    assert a0*Mmax+b0*Mmax*Mmax<F(1,54)
    Cu=F(257,100);Ct=F(33,25);assert F(77,45)/denom<Cu;assert F(5,9)/(1-eta)<Ct
    Cu2=F(59,50);Ct2=F(7,10);assert kappa*Cu+F(3,5)<Cu2;assert 2*eta*Ct/3+F(5,27)<Ct2
    Ve=Cu/9;Te=eta*Ct/3;K=1/(9*(1-eta))
    Apre=2*eta*Ct/27+Cu/162;Bpre=Ct*Ct/54+eta*Cu*Ct/162+Cu*Cu/5832
    Athird=(Ct2+2*Te)/9;AR=K*(Cu2/6+Cu/27)
    BR=K*(3*Ct2*Te+(Cu2*Te+Ct2*Ve)/2+Cu2*Ve/12)
    A=F(1,972)+Apre+Athird+AR;B=Bpre+BR
    assert Mmax<18 and A*Mmax+B*Mmax*Mmax<F(1,18)
    out={'status':'PASS exact rational algebra, conditional on the new moment inequalities','assumed_cubic_C':'5/3','assumed_fourth_prefix_C':'3/5','assumed_fourth_merge_C':'5','eta':str(eta),'kappa_prefix':str(kappa),'root_M_radius':str(Mmax),'posterior_x_radius':str(radius),'bootstrap_error':str(a0*Mmax+b0*Mmax*Mmax),'bootstrap_limit':'1/54','final_drift_error':str(A*Mmax+B*Mmax*Mmax),'final_drift_limit':'1/18','A':str(A),'B':str(B),'scope':'no unconditional ternary theorem until cubic certificate, written identities, and finite entry bound are validated'}
    pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
