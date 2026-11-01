from pathlib import Path
from fractions import Fraction as Q
import json, sys, time
import check as m

def test(t,transform):
    delta=Q(1,1<<t); size=1<<t
    u=[1]*(size)+[-1]*(size)
    v=[a*(-1 if i%size==0 else 1) for i,a in enumerate(u)]
    f=u+v
    check=m.check
    check(sum(u)==sum(v)==0); check(Q(sum(a*b for a,b in zip(u,v)),len(u))==1-2*delta)
    inf=m.influences(f)
    check(inf==[delta]*t+[Q(1),delta]); check(sum(inf)==1+(t+1)*delta)
    check(m.influences(u)==[Q(0)]*t+[Q(1)])
    check(m.influences(v)==[2*delta]*t+[Q(1)])
    check(Q(1)/inf[-1]==1<<t)
    check(Q(1)==2*inf[-1]+(1-2*delta))
    hf=m.H(f,transform); hu=m.H(u,transform); hv=m.H(v,transform)
    eta=lambda p:m.entropy([p])
    check(hu=={})
    check(hf==m.add(eta((1-delta)**2),{2:2*t*(2*delta-delta*delta)}))
    check(hv==m.add(eta((1-2*delta)**2),{2:(2*t-2)*(4*delta-4*delta*delta)}))
    check(sum(inf)==delta+(sum(m.influences(u))+sum(m.influences(v)))/2)
    for vals in [u,v,f]:
        spec=transform(vals); check(sum(c*c for c in spec)==1)
        check(sum(Q(i.bit_count())*c*c for i,c in enumerate(spec))==sum(m.influences(vals)))
    return {'t':t,'reserve':1,'control_influence':str(delta),'reserve_control_ratio':1<<t,'root_influence':str(sum(inf)),'root_entropy':m.dyadic(m.interval(hf)),'terminal_entropy':m.dyadic(m.interval(m.scale(hv,Q(1,2))))}

mode=sys.argv[1] if len(sys.argv)>1 else 'main'; start=time.perf_counter()
rows=[test(t,m.fwht) for t in ([1,2] if mode=='pilot' else range(1,9))]
if mode=='main':
    for t in range(1,5): test(t,m.direct)
m.check(time.perf_counter()-start<55)
result={'status':'PASS','mode':mode,'assertions':m.CHECKS,'seconds':time.perf_counter()-start,'rows':rows}
(m.ROOT/'out'/('boundary_'+mode+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
