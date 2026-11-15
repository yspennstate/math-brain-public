"""Independent degree>=5 local-radius polynomial and Bernstein certificate.
Own prior audited algebra, new parameters; no author producer imported.
"""
from pathlib import Path
import sympy as S
import json,time,hashlib,math,itertools
OUT=Path(__file__).resolve().parent
ROOT=Path('~/brain_workers/w682')
def run():
    started=time.time();l,r,z=S.symbols('l r z');d,k=S.symbols('d k',positive=True)
    Z=k*(k-1)/2+d*(d-k);Cu=5*Z/(d*(d-1));Ct=Cu*(1+l)/3
    te=l*Ct/d;ve=Cu/d**2;K=1/(9*(1-l));Kpre=d/(9*(d-1))
    A2=Kpre*Cu/d**3
    B2=Kpre*(3*Ct**2/d**3+l*Cu*Ct/d**3+Cu**2/(12*d**4))
    S1=k*(k-1)/2-1;S2=k*(k-1)*(k-2)/3
    su=(Cu*S1+S.Rational(5,2)*S2)/d**2
    st=l*Ct*S1/d+S.Rational(5,6)*S2/d**2
    Ak=A2+S2/(72*d**3)+K*(Cu*S1+S.Rational(5,4)*S2)/d**3
    Bk=B2+K*((3*te+ve/2)*st+(te/2+ve/12)*su)
    g=k*(k-1)/(12*d**2);M=S.Rational(217,500);delta=S.Rational(1,1000);L=S.Rational(559017,1250000)
    gap=(1-delta)*g-M*Ak-M*M*Bk
    G=gap.subs(k,2+r*(d-2)).subs(d,1/l**2)
    exact=S.cancel(8640000*(1-l)**3*(1+l)**3*G)
    assert S.denom(exact)==1 or S.denom(exact).is_Integer
    P=S.Poly(exact.subs(l,L*z),z,r);assert P.degree_list()==(17,6)
    # Freeze independently computed polynomial BEFORE reading saved author coefficients.
    own=dict(degrees=list(P.degree_list()),poly=[[list(e),str(c)] for e,c in P.terms()])
    (OUT/'degree6_local_independent_polynomial.json').write_text(json.dumps(own,indent=2),encoding='utf-8')
    n,m=P.degree_list();coeff=dict(P.terms());bern=[]
    for i,j in itertools.product(range(n+1),range(m+1)):
        b=sum(c*S.Rational(math.comb(i,e),math.comb(n,e))*S.Rational(math.comb(j,f),math.comb(m,f)) for (e,f),c in coeff.items() if e<=i and f<=j)
        assert b>=0,(i,j,b);bern.append([i,j,str(b)])
    positive=sum(1 for i,j,b in bern if S.Rational(b)>0);zero=sum(1 for i,j,b in bern if S.Rational(b)==0)
    assert (positive,zero)==(120,6)
    controls=0
    for q in [3,4,5,6,8,10,15,20]:
        dd=q*q;ll=S.Rational(1,q)
        for kk in sorted(set([2,3,dd//2,dd-1,dd])):
            sub={d:dd,k:kk,l:ll};cu=Cu.subs(sub);ct=Ct.subs(sub);aa=A2.subs(sub);bb=B2.subs(sub)
            for j in range(2,kk):
                uj=(j*cu+S.Rational(5,2)*j*(j-1))/dd**2
                tj=j*ll*ct/dd+S.Rational(5,6)*j*(j-1)/dd**2
                aa+=S.Rational(j*(j-1),72*dd**3)+(uj/(2*dd)+S.Rational(j,2*dd**3)*cu)/(9*(1-ll))
                bb+=(3*tj*ll*ct/dd+(uj*ll*ct/dd+tj*cu/dd**2)/2+uj*cu/(12*dd**2))/(9*(1-ll))
            assert aa==Ak.subs(sub) and bb==Bk.subs(sub) and gap.subs(sub)>=0;controls+=1
    assert 5*L**2>1 and L<S.Rational(2887,5000)
    rawpath=ROOT/'checks/uniform_local_radius_d5_048_raw.json';raw=json.loads(rawpath.read_text(encoding='utf-8'))
    saved={tuple(e):S.Rational(c)*S.Rational(raw['raw_content_divided_out'])/S.Rational(raw['raw_common_multiplier']) for e,c in raw['poly']}
    assert dict(P.terms())==saved
    result=dict(status='PASS local rectangle arithmetic; inherited moment and prefix proof premises separately reviewed',radius='217/4500',Mstar=str(M),delta=str(delta),lambda_max=str(L),degrees=[n,m],positive=positive,zero=zero,coefficients=bern,unsummed_controls=controls,raw_sha256=hashlib.sha256(rawpath.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.time()-started)
    (OUT/'degree6_local_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='coefficients'}),flush=True)
if __name__=='__main__':run()
