"""Replay the original width1/8 Gaussian gate with our own Arb quadrature."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=192
def ar(q):
    q=F(q);return arb(q.numerator)/q.denominator
def dyad(pair):return F(int(pair[0]))*F(2)**int(pair[1])
bins=[];sqrt2=arb(2).sqrt();norm=(2*arb.pi()).sqrt()
for j in range(48):
    a=arb(j)/8;b=arb(j+1)/8
    fa=(-a*a/2).exp()/norm;fb=(-b*b/2).exp()/norm
    w=((b/sqrt2).erf()-(a/sqrt2).erf())/2
    m=(fa-fb)/w;v=w+a*fa-b*fb-(fa-fb)**2/w
    assert w>0 and v>0;bins.append((w,m,v))
P=2*sum((v[0] for v in bins),arb(0));D=2*sum((v[2] for v in bins),arb(0))
folder=Path('~/brain_workers/w682/checks/gaussian_fourth_gate_v1')
raw=json.loads((folder/'report.json').read_text());assert raw['completed']==86
constants=json.loads(Path('checks/t067_compensated_constants_own.json').read_text())['rows'][0]
alpha=F(constants['alpha']);B=F(constants['B']);C=F(constants['curvature'])
assert alpha==F(raw['alpha']) and B==F(raw['B']) and C==F(raw['curvature_upper'])
results=[]
for i in range(86):
    s0=F(10,100-i);s=ar(s0);drift=(-9*s/2).exp();a=3*(3*s).sqrt()/2;b=3*s.sqrt()/2
    cols=[(w,(b*m).cosh(),(2*b*m).cosh()) for w,m,_ in bins]
    Fsum=arb(0);Qsum=arb(0)
    for wi,mi,_ in bins:
        ep=drift*(-a*mi).exp();em=drift*(a*mi).exp()
        ff=arb(0);qq=arb(0)
        for wj,ch,ch2 in cols:
            dp=1+2*ep*ch;dm=1+2*em*ch
            ff+=wj*(1/dp+1/dm)
            qp=9*(1+2*ep*ep*ch2)/(dp*dp)-3
            qm=9*(1+2*em*em*ch2)/(dm*dm)-3
            qq+=wj*(qp*qp+qm*qm)
        Fsum+=2*wi*ff;Qsum+=2*wi*qq
    file=folder/f'endpoint_{i:03}.json';e=json.loads(file.read_text())
    assert e['index']==i and F(e['s'])==s0
    assert sha256(file.read_bytes()).hexdigest()==raw['endpoints'][i]['sha256']
    for name,own in [('F_quadrature',Fsum),('Q_quadrature',Qsum)]:
        assert dyad(e[name]['lower'])<=F(str(own.lower().fmpq()))<=F(str(own.upper().fmpq()))<=dyad(e[name]['upper']),(i,name)
    gupper=F(str((Fsum+(9*s/10)*P*D+1-P*P-ar(F(1,3))).upper().fmpq()))
    uupper=F(str((Qsum+90*s*P*D+36*(1-P*P)).upper().fmpq()))
    gate=alpha*(s0-gupper)-B*s0*s0-uupper
    assert gate>0
    results.append({'s':str(s0),'lower':str(gate),'source_sha256':sha256(file.read_bytes()).hexdigest()})
lower=[F(r['lower']) for r in results]
margins=[min(lower[i],lower[i+1])-C*(F(results[i+1]['s'])-F(results[i]['s']))**2/8 for i in range(85)]
assert min(margins)>0
assert min(margins)-1<0
out={'complete':True,'precision_bits':192,'bin_width':'1/8','endpoints':results,'intervals':[str(m) for m in margins],'minimum_margin':str(min(margins)),'all86_raw_quadrature_enclosures_contain_own_replay':True,'unit_fourth_observable_inflation_rejected':True}
Path('checks/t067_gaussian_gate96_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'complete':True,'endpoints':86,'intervals':85,'minimum_margin_display':float(min(margins))}))
