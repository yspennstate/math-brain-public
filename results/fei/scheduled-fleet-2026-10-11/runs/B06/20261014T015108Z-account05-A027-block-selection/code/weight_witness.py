import json
from pathlib import Path
import exact as x
Q=x.Q; run=Path(__file__).resolve().parents[1]
u=(-1,-1,-1,1); a=(-1,1,1,1); f=x.activate(u,a); p=Q(1,4)
leaves=[(((0,0),),Q(1,2)),(((0,1),(2,0)),Q(1,4)),(((0,1),(2,1)),Q(1,4))]
active=[]; leafI=Q(0); leafH={}
for fixed,w in leaves:
    child=x.restrict(f,fixed); leafI+=w*x.I(child); leafH=x.add((1,leafH),(w,x.H(child)))
    if all(b==0 for i,b in fixed if i>=2):
        rr=2-sum(i>=2 for i,b in fixed); core=x.restrict(u,tuple((i,b) for i,b in fixed if i<2))
        active.append((w,Q(1,1<<rr),x.neg(core)))
        assert x.I(child)==1 and x.H(child)=={2:Q(2)}
    else: assert x.I(child)==0 and x.H(child)=={}
assert [w*pp/p for w,pp,d in active]==[Q(1,2),Q(1,2)]
assert sum(w*pp/p*d for w,pp,d in active)==x.neg(u)==Q(3,4)
assert sum(w*d for w,pp,d in active)/sum(w for w,pp,d in active)==Q(5,6)
qcore=x.inf(f,0); at=x.restrict(f,((0,1),)); qctrl=x.inf(at,1)/2
assert qcore==qctrl==Q(1,8)
assert leafI==Q(3,4) and x.I(f)==qcore+qctrl+leafI==1
assert leafH=={2:Q(3,2)}
out={'status':'PASS','projected_leaf_weights':['1/2','1/2'],'raw_active_leaf_weights':['1/2','1/4'],'correct_bias':'3/4','wrong_raw_normalized_bias':'5/6','root_I':'1','queried_core_I':'1/8','queried_control_I':'1/8','terminal_I':'3/4','terminal_H_bits':'3/2','arithmetic':'exact Fraction, integer Walsh and physical edges','scope':'one fixed exact proof fixture, verified separately from20640-policy census; complete input saved in WEIGHT_WITNESS.md before verification, no search'}
(run/'out'/'WEIGHT_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
