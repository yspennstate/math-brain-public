"""Outward-rounded joint Gaussian comparison for a candidate d=100 gate.

The analytic quadrature and interpolation estimates require a separate proof.
One CPU, <20 MB estimated working memory; saves every endpoint, bounded chunks.
"""
import argparse,ctypes,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from compensated_replacement_constants import constants
from gaussian_gap_arb import exact_ball,as_fraction,save
ROOT=Path(__file__).resolve().parent
SOURCE=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT=ROOT/'gaussian_fourth_gate_refined_v1'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=int,default=90);ap.add_argument('--count',type=int,default=86)
    args=ap.parse_args();assert 1<=args.seconds<=480 and 1<=args.count<=86
    start=time.monotonic()
    class Mem(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(n,ctypes.c_ulonglong) for n in ['total','available','page_total','page_available','virtual_total','virtual_available','extended']]
    mem=Mem();mem.length=ctypes.sizeof(mem);assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)) and mem.available>2_000_000_000
    import flint
    from flint import arb,ctx
    ctx.prec=160
    def ball(q):q=F(q);return arb(q.numerator)/q.denominator
    fc=constants(F(1,10),F(1,8),F(1,5),F(2,5),F(1,2),F(3,5))
    qc=constants(F(1,10),*(F(x) for x in (8,20,38,38,99)))
    alpha=(100-qc[0])/fc[0]
    B=81*((1-qc[0]/100)*fc[1]/fc[0]+qc[1]/100)
    assert qc[1]-qc[0]*fc[1]/fc[0]>0
    curvature=32*alpha+2*B+3600
    grid=[1/(F(10)-F(i,10)) for i in range(86)]
    config={'source_sha256':SOURCE,'constants_source_sha256':hashlib.sha256((ROOT/'compensated_replacement_constants.py').read_bytes()).hexdigest(),
        'arb_helper_sha256':hashlib.sha256((ROOT/'gaussian_gap_arb.py').read_bytes()).hexdigest(),
        'alpha':str(alpha),'B':str(B),'curvature_upper':str(curvature),'radius':'6','bin_width':'1/16',
        'precision_bits':160,'python_flint_version':flint.__version__,'cpu_workers':1,'working_memory_estimate_bytes':20_000_000}
    OUT.mkdir(exist_ok=True)
    if (OUT/'config.json').exists():assert json.loads((OUT/'config.json').read_text(encoding='utf-8'))==config
    else:save(OUT/'config.json',config)
    sqrt2=arb(2).sqrt();normalizer=(2*arb.pi()).sqrt()
    def phi(x):return (-x*x/2).exp()/normalizer
    bins=[]
    for j in range(96):
        a,b=ball(F(j,16)),ball(F(j+1,16));w=((b/sqrt2).erf()-(a/sqrt2).erf())/2
        first=phi(a)-phi(b);second=w+a*phi(a)-b*phi(b)
        mean=first/w;variance=second-first*first/w
        assert w>0 and mean>a and mean<b and variance>0
        bins.append((w,mean,variance))
    P=2*sum((x[0] for x in bins),arb(0));D=2*sum((x[2] for x in bins),arb(0));tail=1-P*P
    assert P>0 and P<1 and D>0 and tail>0
    save(OUT/'bins.json',{'P':exact_ball(P),'D':exact_ball(D),'tail':exact_ball(tail),
        'bins':[{'weight':exact_ball(w),'mean':exact_ball(m),'variance':exact_ball(v)} for w,m,v in bins]})
    new=0
    for index,s0 in enumerate(grid):
        target=OUT/f'endpoint_{index:03d}.json'
        if target.exists():
            old=json.loads(target.read_text(encoding='utf-8'));assert old['source_sha256']==SOURCE and old['s']==str(s0)
            continue
        if new>=args.count or time.monotonic()-start>=args.seconds:break
        ss=ball(s0);c1=3*(3*ss).sqrt()/2;c2=3*ss.sqrt()/2
        cs=[((c2*m).cosh(),(2*c2*m).cosh()) for _,m,_ in bins]
        qF=arb(0);qQ=arb(0)
        for wi,mi,_ in bins:
            plus=(-9*ss/2-c1*mi).exp();minus=(-9*ss/2+c1*mi).exp()
            frow=arb(0);qrow=arb(0)
            for (wj,_,_),(ch,ch2) in zip(bins,cs):
                for exponential in (plus,minus):
                    den=1+2*exponential*ch;f=1/den
                    radial=9*(1+2*exponential*exponential*ch2)/(den*den)-3
                    frow+=2*wj*f;qrow+=2*wj*radial*radial
            qF+=wi*frow;qQ+=wi*qrow
        errF=ball(F(9,10))*ss*P*D;errQ=90*ss*P*D
        gU=qF+errF+tail-arb(1)/3
        UG_U=qQ+errQ+36*tail
        gate=ball(alpha)*(ss-gU)-ball(B)*ss*ss-UG_U
        row={'source_sha256':SOURCE,'index':index,'s':str(s0),
            'F_quadrature':exact_ball(qF),'Q_quadrature':exact_ball(qQ),
            'g_error':exact_ball(errF),'U_error':exact_ball(errQ),
            'g_upper':exact_ball(gU),'U_upper':exact_ball(UG_U),
            'gate_lower_ball':exact_ball(gate),'endpoint_positive':bool(gate>0)}
        save(target,row);new+=1
        print(json.dumps({'endpoint':index,'s':str(s0),'positive':row['endpoint_positive'],'gate':str(gate)}),flush=True)
    rows=[]
    for i,s0 in enumerate(grid):
        path=OUT/f'endpoint_{i:03d}.json'
        if path.exists():
            row=json.loads(path.read_text(encoding='utf-8'));assert row['source_sha256']==SOURCE and row['s']==str(s0)
            lo=as_fraction(row['gate_lower_ball']['lower'])
            rows.append({'index':i,'s':str(s0),'lower':str(lo),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    intervals=[]
    if len(rows)==86:
        for i in range(85):
            a,b=grid[i:i+2];margin=min(F(rows[i]['lower']),F(rows[i+1]['lower']))-curvature*(b-a)**2/8
            intervals.append({'index':i,'margin':str(margin),'positive':margin>0})
    status='PASS' if len(intervals)==85 and all(q['positive'] for q in intervals) else ('FAILED_GATE' if len(rows)==86 else 'PARTIAL')
    result={**config,'status':status,'new_this_run':new,'completed':len(rows),'endpoints':rows,'intervals':intervals,
            'scope':'Conditional on analytic derivative, quadrature and interpolation proof; no independent audit',
            'elapsed_seconds':time.monotonic()-start}
    save(OUT/'report.json',result);print(json.dumps({'status':status,'completed':len(rows),'elapsed':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
