"""New fourth-observable quadrature; reuse pinned own second-observable results."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
from time import monotonic
import json
from flint import arb,ctx
from t067_piecewise_gaussian_own import GaussianQuadrature,ar

ctx.prec=192
start=monotonic(); engine=GaussianQuadrature()
gpath=Path('checks/t067_piecewise_endpoints_own.json')
graw=json.loads(gpath.read_text());assert graw['complete'] and len(graw['checked'])==86
gupper={F(r['signal']):F(r['g_upper']) for r in graw['checked']}
parameters=json.loads(Path('checks/t067_compensated_constants_own.json').read_text())
assert parameters['complete']
outpath=Path('checks/t067_compensated_gaussian_own.json')
rows=[]
for i in range(86):
    signal=F(10,100-i);s=ar(signal)
    drift=(-9*s/2).exp();alpha=3*(3*s).sqrt()/2;beta=3*s.sqrt()/2
    columns=[(w,(beta*m).cosh(),(2*beta*m).cosh()) for w,m,_ in engine.bins]
    total=arb(0)
    for wi,mi,_ in engine.bins:
        eplus=drift*(-alpha*mi).exp();eminus=drift*(alpha*mi).exp()
        subtotal=arb(0)
        for wj,b,b2 in columns:
            qplus=9*(1+2*eplus*eplus*b2)/(1+2*eplus*b)**2-3
            qminus=9*(1+2*eminus*eminus*b2)/(1+2*eminus*b)**2-3
            subtotal+=wj*(qplus*qplus+qminus*qminus)
        total+=2*wi*subtotal
    error=90*s*engine.P*engine.D
    upper=F(str((total+error+36*(1-engine.P*engine.P)).upper().fmpq()))
    lower=F(str((total-error).lower().fmpq()))
    rows.append({'signal':str(signal),'U_upper':str(upper),'U_lower':str(lower),'g_upper':str(gupper[signal])})
    receipt={'at':datetime.now().astimezone().isoformat(),'complete':False,'precision_bits':192,'signed_bins_per_axis':192,'own_g_receipt_sha256':sha256(gpath.read_bytes()).hexdigest(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'endpoints':rows,'seconds':monotonic()-start}
    outpath.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
gates=[]
for r in parameters['rows']:
    alpha=F(r['alpha']);B=F(r['B']);C=F(r['curvature'])
    assert alpha>0 and B>0 and C>0
    lower=[alpha*(F(e['signal'])-F(e['g_upper']))-B*F(e['signal'])**2-F(e['U_upper']) for e in rows]
    margins=[min(lower[i],lower[i+1])-C*(F(rows[i+1]['signal'])-F(rows[i]['signal']))**2/8 for i in range(85)]
    threshold=F(3,200) if r['degree']==91 else F(0)
    assert min(margins)>threshold,(r['degree'],str(min(margins)))
    assert min(margins)-1<threshold,'inflated fourth-observable negative control must fail'
    gates.append({'degree':r['degree'],'threshold':str(threshold),'minimum_interval_margin':str(min(margins)),'minimum_endpoint_margin':str(min(lower)),'intervals':[str(q) for q in margins],'unit_inflation_control_rejected':True})
assert len(rows)==86 and F(rows[0]['signal'])==F(1,10) and F(rows[-1]['signal'])==F(2,3)
receipt.update(complete=True,gates=gates,seconds=monotonic()-start)
outpath.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'complete':True,'endpoints':86,'gates':[{'degree':r['degree'],'minimum_margin_display':float(F(r['minimum_interval_margin']))} for r in gates],'seconds':receipt['seconds']}))
