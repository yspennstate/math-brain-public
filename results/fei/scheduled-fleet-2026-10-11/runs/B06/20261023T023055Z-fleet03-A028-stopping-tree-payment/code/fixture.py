"""Exact receipt on the predeclared nonconstant seven-variable fixture."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import check as m
e=m.e;ROOT=Path(__file__).resolve().parents[1];START=time.monotonic()
a=tuple(-1 if x<3 else 1 for x in range(8))
g=tuple((-1 if x&7==0 else 1)*(-1 if x&8 else 1) for x in range(16))
h=tuple((-1 if (x&7).bit_count()>=2 else 1)*(-1 if x&8 else 1) for x in range(16))
r=tuple(F(1,16) for _ in g)
S=m.profile(a,g,h,r,r)
J=e.add(e.entropy(tuple((1-S['p'])*x+S['p']*y for x,y in zip(m.spectrum(g),m.spectrum(h)))),e.scale(e.entropy(m.spectrum(g)),-(1-S['p'])),e.scale(e.entropy(m.spectrum(h)),-S['p']))
m.eq(S['Z'],J,'root slack is SAME J')
If=e.stats(m.mux(a,g,h))[3];U=4*If;b=F(1,8)
original=e.add(S['H'],S['W'])
reserve=e.add({2:U-b},m.neg(original));m.nn(reserve,'old-debit admission')

def walk(a,g,h,rg,rh,labels,order):
    s=m.profile(a,g,h,rg,rh)
    if not order:
        return dict(sig={},A={},zl=s['Z'],path={},ce=e.add(s['H'],s['D']),leaves=1,terminals=[dict(H=m.encoded(s['H']),D=m.encoded(s['D']),Z=m.encoded(s['Z']))])
    label=order[0];i=labels.index(label);na=len(a).bit_length()-1
    inh,Ef,Of,rho=m.physical(m.mux(a,g,h),s['rf'],i)
    if i<na: args=[(m.restrict(a,i,t),g,h,rg,rh) for t in (0,1)]
    else:
        j=i-na;rgg,_,_,_=m.physical(g,rg,j);rhh,_,_,_=m.physical(h,rh,j)
        args=[(a,m.restrict(g,j,t),m.restrict(h,j,t),rgg[t],rhh[t]) for t in (0,1)]
    kids=[m.profile(*ar) for ar in args]
    A=e.add(s['W'],m.neg(m.avg(*(v['W'] for v in kids))))
    sigma=e.add(m.avg(*(v['D'] for v in kids)),m.neg(s['D']))
    kappa=e.add(sigma,Ef,Of)
    charge=dict(query=label,sigma=m.encoded(sigma),kappa=m.encoded(kappa),Ef=m.encoded(Ef),Of=m.encoded(Of),rho=[str(x) for x in rho],child_D=[m.encoded(v['D']) for v in kids])
    remaining=labels[:i]+labels[i+1:]
    ret=[walk(*args[t],remaining,order[1:]) for t in (0,1)]
    out={k:m.avg(*(v[k] for v in ret)) for k in ('sig','A','zl','path','ce')}
    out['sig']=e.add(sigma,out['sig']);out['A']=e.add(A,out['A'])
    out['path']=e.add(s['H'],m.neg(m.avg(*(v['H'] for v in kids))),out['path'])
    out['leaves']=sum(v['leaves'] for v in ret)
    out['terminals']=ret[0]['terminals']+ret[1]['terminals']
    out['queries']=[charge]+sum((v.get('queries',[]) for v in ret),[])
    m.eq(e.add(out['sig'],out['A'],out['zl']),s['Z'])
    m.eq(e.add(out['path'],out['ce'],out['A'],out['zl']),e.add(s['H'],s['W']))
    return out

labels=('C0','C1','C2','D0','D1','D2','D3')
rows=[]
for order in [('D0','C0','D1','C1'),('C0','C1','C2')]:
    ans=walk(a,g,h,r,r,labels,order)
    paid=e.add(ans['path'],ans['ce'])
    remaining=e.add({2:U-b},m.neg(paid));m.nn(remaining)
    if len(order)==3:
        m.eq(ans['sig'],J);m.eq(ans['A'],{});m.eq(ans['zl'],{})
    rows.append(dict(order=order,leaves=ans['leaves'],ledger={k:m.encoded(ans[k]) for k in ('sig','A','zl','path','ce')},remaining=m.encoded(remaining),remaining_interval=m.interval(remaining),queries=ans['queries'],terminals=ans['terminals']))
out=dict(status='PASS',a=a,g=g,h=h,I_f=str(If),original_U=str(U),old_debit=str(b),original_required=m.encoded(original),root_Z_equals_J=m.encoded(J),root_Z_interval=m.interval(J),original_reserve=m.encoded(reserve),original_reserve_interval=m.interval(reserve),policies=rows,assertions=m.checks,seconds=time.monotonic()-START)
(ROOT/'out/fixture.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('policies','a','g','h')}))
