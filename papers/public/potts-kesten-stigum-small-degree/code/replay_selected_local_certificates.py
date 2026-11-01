"""Rebuild two new local certificates from the unsummed rational ledger.

Imports no symbolic producer. Source derives polynomial independently from the
prefix sums, and was separately checked against the original symbolic source.
"""
import hashlib,json,pathlib,time
from fractions import Fraction as F
import uniform_local_fast_independent_check as ledger
ROOT=pathlib.Path(__file__).resolve().parent
def replay(name):
    start=time.monotonic();raw,meta=ledger.load(name,'raw');current=raw;scales=[]
    for axis in (0,1):
        nxt,_=ledger.load(name,f'bern{axis+1}')
        scales.append(ledger.axis_check(current,nxt,axis,meta['degrees'][axis]));current=nxt
    assert all(v>0 for v in current.values())
    m=F(meta['M_radius']);margin=F(meta['retained_drift_fraction']);L=F(meta['lambda_upper'])
    poly=ledger.expected_numerator(m,margin)
    expected={key:v*F(meta['denominator_positive_content'])*L**key[0] for key,v in poly.items()}
    restored=ledger.scale(raw,F(meta['raw_content_divided_out'])/F(meta['raw_common_multiplier']))
    assert restored==expected
    checks=[]
    for d in (9,16,25,49,100,225,400):
        l=F(1,int(d**0.5));assert l*l==F(1,d)
        if l>L:continue
        for k in sorted({2,3,d//2,d}):
            A,B,g=ledger.direct_recursion(d,k);r=F(k-2,d-2)
            gap=(1-margin)*g-m*A-m*m*B
            assert gap>=0 and ledger.evaluate(poly,l,r)==(1-l*l)**3*gap
            checks.append({'d':d,'k':k,'gap':str(gap)})
    receipt={'status':'PASS separate rational reconstruction',
        'name':name,'M_radius':str(m),'x_radius':str(m/9),'lambda_upper':str(L),
        'full_polynomial_identity':True,'positive_coefficients':len(current),'implicit_zero_coefficients':126-len(current),
        'axis_scales':scales,'unsummed_checks':checks,'seconds':time.monotonic()-start,
        'sha256':{f'uniform_local_{name}_{phase}.json':hashlib.sha256((ROOT/f'uniform_local_{name}_{phase}.json').read_bytes()).hexdigest() for phase in ('raw','bern1','bern2','report')}}
    for source in ('uniform_local_fast_independent_check.py','replay_selected_local_certificates.py'):
        receipt['sha256'][source]=hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
    target=ROOT/f'uniform_local_{name}_replay.json';assert not target.exists()
    target.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:receipt[k] for k in ('status','name','x_radius','positive_coefficients','seconds')}),flush=True)
if __name__=='__main__':
    for name in ('radius_d5_048','radius_d89_10over83'):replay(name)
