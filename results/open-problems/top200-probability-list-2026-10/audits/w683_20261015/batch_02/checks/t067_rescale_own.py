from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

EPS=F(1,100)
mu=[tuple((1+(2*EPS if i==j else -EPS))/3 for i in range(3)) for j in range(3)]

def fusion(points,r):
    law={}; mass=F(0)
    for a,b in product(points,repeat=2):
        likelihood=[(1-r+3*r*a[i])*(1-r+3*r*b[i]) for i in range(3)]
        total=sum(likelihood); p=tuple(x/total for x in likelihood)
        weight=total/27
        law[p]=law.get(p,F(0))+weight; mass+=weight
    assert mass==1
    return law

def moments(law):
    M=F(0); U=F(0)
    for p,w in law.items():
        A=sum((3*x-1)**2 for x in p); M+=w*A; U+=w*A*A
    return M,U

def main():
    original={p:F(1,3) for p in mu}; M,U=moments(original)
    assert M==6*EPS**2 and U==36*EPS**4
    lam=F(4,5); eta=F(9,10); c=lam/eta
    scaled=[tuple(F(1,3)+c*(x-F(1,3)) for x in p) for p in mu]
    assert fusion(mu,lam)==fusion(scaled,eta)
    lam=eta=F(9,10)
    lhs=moments(fusion(mu,lam))[1]
    rhs=2*lam**4*U+F(3,5)*(lam/eta)**4*M*M
    assert lhs>rhs
    eta0=F(2887,5000); lam0=F(1,2)
    good_lhs=moments(fusion(mu,lam0))[1]
    good_rhs=2*lam0**4*U+F(3,5)*(lam0/eta0)**4*M*M
    assert good_lhs<=good_rhs
    proof=Path('~/brain_workers/w682/proofs/T067-RESCALE-001_v1.md')
    result={'proof_sha256':sha256(proof.read_bytes()).hexdigest(),'identity_test':'exact posterior-law equality at lambda=4/5, eta=9/10','epsilon':str(EPS),'M':str(M),'U':str(U),'lambda':str(lam),'eta':str(eta),'unrestricted_corollary_lhs':str(lhs),'unrestricted_corollary_rhs':str(rhs),'strict_difference':str(lhs-rhs),'restricted_reference_check':'PASS at eta=2887/5000, lambda=1/2','verdict':'FIX: specify the cited eta regime for the moment corollary; identity unchanged'}
    Path('checks/t067_rescale_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
