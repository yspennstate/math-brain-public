"""Exact checks of two UNPROVED potentials proposed by the scheduled FEI worker.
The 66-variable witness is checked by proved disjoint-product formulas; it is
not a 2**66 truth-table enumeration. No full FEI refutation is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import prior_exact_entropy as E
from verify_quadratic_coupling import spectral

def quantities(f):
    n=len(f);b=spectral(f)
    children=[spectral(tuple(f[x]*f[x^z] for x in range(n))) for z in range(n)]
    delta=2*b['M']-sum(c['M'] for c in children)/n
    D=2*b['H']-sum((c['H'] for c in children),E.LogExpr())/n
    v=1-F(max(b['m']),b['den'])
    return b['M'],v,delta,D

def main():
    w3=tuple(-1 if x==0 else 1 for x in range(8))
    w5=tuple(-1 if x==0 else 1 for x in range(32))
    M,v,delta,D=quantities(w5)
    assert (M,v,delta)==(F(5,16),F(31,256),F(9,64))
    gap=M-v-delta
    assert gap==F(13,256)>0
    M3,v3,delta3,D3=quantities(w3)
    assert (M3,v3,delta3)==(F(3,4),F(7,16),F(5,8))
    formula=(25-9*E.log_rat(3))/4
    assert (D3-formula).is_zero()
    # Independently instantiate and check a two-block product before using
    # the all-q analytical tensorization identity.
    product=tuple(w3[x&7]*w3[x>>3] for x in range(64))
    M2,v2,delta2,D2=quantities(product)
    assert M2==2*M3 and delta2==2*delta3
    assert (D2-2*D3).is_zero() and v2==1-F(9,16)**2
    q=22
    gap66=q*D3-4*(1-F(9,16)**q+q*delta3)
    equivalent=(157-99*E.log_rat(3))/2+4*F(9,16)**22
    assert (gap66-equivalent).is_zero()
    assert gap66.interval()[0]>F(44,1000)
    # The additive resource drift by itself needs a constant larger than four.
    Kseed=D3/delta3
    assert Kseed.interval()[0]>F(429,100)
    out={'status':'ALL_CHECKS_PASS','full_FEI_refuted':False,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'resource_potential':{'dimension':5,'function':'one-point defect w_5',
             'M':str(M),'v':str(v),'delta_M':str(delta),'violation':str(gap)},
         'entropy_potential_constant_4':{'dimension':66,'function':'w_3 tensor power 22',
             'seed_M':str(M3),'seed_delta_M':str(delta3),'seed_D':E.show(D3),
             'violation':E.show(gap66),'necessary_constant_from_seed':E.show(Kseed),
             'scope':'Exact seed enumeration, exact two-block tensor check, analytical 22-block formula; no 2**66 enumeration'},
         'independent_audit':False,'lean_used':False}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_name('scheduled_potential_checks.json').write_text(text)
    print(text)

if __name__=='__main__':main()
