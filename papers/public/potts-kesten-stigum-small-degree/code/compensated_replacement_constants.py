"""Exact constants and calibrated cubic identity for the new replacement."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as R
ROOT=Path(__file__).resolve().parents[1]

def constants(L,g1,c2,c3,c31,c4):
    B4=R(25,288)+R(49,100)*L/(1-L)
    B3=R(1,6)+R(49,20)*L*B4
    B1=R(5,24)+R(49,20)*L*B3
    cu=g1*(R(1,6)+R(49,20)*L*B4)+c2/2*(R(1,24)+B3*(1/(1-L)+1+L/2)+R(1,6))
    cu+=c31/2*B1/(1-L)**2+c3/6+c4/(24*(1-L)**4)
    cm=c2/12+5*c31/24+5*c3*L*L/72+c4*(2+4*L*L+L**4)/24
    return cu,cm

def main():
    F=(R(1,8),R(1,5),R(2,5),R(1,2),R(3,5));Q=tuple(R(x) for x in (8,20,38,38,99))
    # Positive control: reproduce the already audited earlier constants.
    old=constants(R(1,16),*F)
    assert old==(R(68871759703,276480000000),R(4042249,23592960))
    L=R(1,10);beta=R(49,4);fc=constants(L,*F);qc=constants(L,*Q)
    H=tuple(qc[i]+9*beta*fc[i] for i in range(2))
    assert H[0]<57 and H[1]<38
    # Independent direct symbolic test of S_A=9 sum_i p_i ell_i^{F_i}.
    import sympy as s
    a,b=s.symbols('a b');p=(a,b,1-a-b)
    def D(f,i):return s.expand(a*(int(i==0)-p[i])*s.diff(f,a)+b*(int(i==1)-p[i])*s.diff(f,b))
    def ell(f,i):
        j,k=[v for v in range(3) if v!=i]
        second=D(D(f,j)-D(f,k),j)-D(D(f,j)-D(f,k),k)
        return s.expand((sum(D(D(D(f,r),r),r) for r in range(3))-D(f,i)-second)/4)
    A=9*sum(z*z for z in p)-3
    SA=s.expand(sum(p[i]*ell(A,i) for i in range(3)))
    SF=s.expand(sum(p[i]*ell(p[i],i) for i in range(3)))
    assert s.expand(SA-9*SF)==0
    output={'status':'EXACT_CONSTANTS_AND_CALIBRATION_IDENTITY_PASS','L':str(L),'beta':str(beta),
        'F_constants':list(map(str,fc)),'Q_constants':list(map(str,qc)),'H_constants':list(map(str,H)),
        'H_rounded_upper':['57','38'],'positive_control_old_audited_constants':True,
        'calibrated_cubic_identity':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'checks/compensated_replacement_constants.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output))

if __name__=='__main__':main()
