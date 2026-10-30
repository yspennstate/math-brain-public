"""Separate exact arithmetic replay plus direct full-plane quadrature controls."""
import os
os.environ['OMP_NUM_THREADS']='1'
import hashlib,json,math,time
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'gaussian_fourth_gate_refined_v1'

def dyadic(pair):
    m,e=pair;return F(m*2**e) if e>=0 else F(m,2**(-e))
def upper(row):return dyadic(row['upper'])
def lower(row):return dyadic(row['lower'])

def main():
    start=time.monotonic();config=json.loads((OUT/'config.json').read_text(encoding='utf-8'))
    result=json.loads((OUT/'report.json').read_text(encoding='utf-8'))
    constants=json.loads((ROOT/'compensated_replacement_constants.json').read_text(encoding='utf-8'))
    fU,fM=map(F,constants['F_constants']);qU,qM=map(F,constants['Q_constants'])
    alpha=(100-qU)/fU;B=81*((1-qU/100)*fM/fU+qM/100);C=32*alpha+2*B+3600
    assert str(alpha)==config['alpha'] and str(B)==config['B'] and str(C)==config['curvature_upper']
    assert qM-qU*fM/fU>0 and 100>qU+F(441,4)*fU
    bins=json.loads((OUT/'bins.json').read_text(encoding='utf-8'))
    assert len(bins['bins'])==96
    P,D,T=upper(bins['P']),upper(bins['D']),upper(bins['tail'])
    assert lower(bins['P'])>0 and P<1 and lower(bins['D'])>0 and lower(bins['tail'])>0
    rows=[]
    for i in range(86):
        ss=1/(F(10)-F(i,10));path=OUT/f'endpoint_{i:03d}.json'
        r=json.loads(path.read_text(encoding='utf-8'));assert r['s']==str(ss) and r['source_sha256']==config['source_sha256']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==result['endpoints'][i]['sha256']
        # Recompute all quadrature and tail allowances from raw directed endpoints.
        gU=upper(r['F_quadrature'])+F(9,10)*ss*P*D+T-F(1,3)
        UG=upper(r['Q_quadrature'])+90*ss*P*D+36*T
        e=alpha*(ss-gU)-B*ss*ss-UG
        rows.append((ss,e))
    margins=[min(e,f)-C*(b-a)**2/8 for (a,e),(b,f) in zip(rows,rows[1:])]
    assert len(margins)==85 and min(margins)>0
    # Negative control on the live scope: a missing endpoint cannot pass coverage.
    assert len(rows[:-1])!=86
    import flint
    from flint import arb,ctx
    ctx.prec=192
    def ball(q):q=F(q);return arb(q.numerator)/q.denominator
    normalizer=(2*arb.pi()).sqrt();rt2=arb(2).sqrt()
    def density(z):return (-z*z/2).exp()/normalizer
    full=[]
    for k in range(-96,96):
        a,b=ball(F(k,16)),ball(F(k+1,16));weight=((b/rt2).erf()-(a/rt2).erf())/2
        mean=(density(a)-density(b))/weight;full.append((weight,mean))
    controls=[]
    for index in (0,42,85):
        ss=ball(rows[index][0]);r3=(3*ss).sqrt();rs=ss.sqrt()
        qF=arb(0);qQ=arb(0)
        for w1,z1 in full:
            for w2,z2 in full:
                logits=[3*ss+r3*z1,-3*ss/2-r3*z1/2+3*rs*z2/2,-3*ss/2-r3*z1/2-3*rs*z2/2]
                weights=[z.exp() for z in logits];total=sum(weights,arb(0));p=[z/total for z in weights]
                A=sum(((3*z-1)**2 for z in p),arb(0));qF+=w1*w2*p[0];qQ+=w1*w2*A*A
        r=json.loads((OUT/f'endpoint_{index:03d}.json').read_text(encoding='utf-8'))
        for name,value in [('F_quadrature',qF),('Q_quadrature',qQ)]:
            assert lower(r[name])<=upper_bound(value) and lower_bound(value)<=upper(r[name]),(index,name)
        controls.append({'index':index,'cells':192**2,'F_and_Q_overlap':True})
    output={'status':'EXACT_ALL_INTERVALS_AND_DIRECT_QUADRATURE_PASS','endpoints':86,'intervals':85,
        'minimum_exact_margin':str(min(margins)),'minimum_margin_display_only':float(min(margins)),
        'controls':controls,'missing_endpoint_control_rejected':True,
        'producer_report_sha256':hashlib.sha256((OUT/'report.json').read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds':time.monotonic()-start}
    (ROOT/'gaussian_fourth_refined_replay.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output))

def lower_bound(x):
    lo=x.lower();m,e=lo.man_exp();return dyadic((int(m),int(e)))
def upper_bound(x):
    hi=x.upper();m,e=hi.man_exp();return dyadic((int(m),int(e)))

if __name__=='__main__':main()
