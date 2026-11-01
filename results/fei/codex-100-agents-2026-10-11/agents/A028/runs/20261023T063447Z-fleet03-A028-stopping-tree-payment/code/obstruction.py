from pathlib import Path
from fractions import Fraction as F
import json
import independent_base as b
R=Path(__file__).resolve().parents[1]
a=(-1,1,1,1);g=(1,-1,1,-1);h=tuple(-x for x in g)
ra=(F(1,4),F(1,8),F(1,4),F(3,8));pa=b.law(a);pg=b.law(g);ph=b.law(h)
assert pa==(F(1,4),)*4 and pg==ph==(F(0),F(1),F(0),F(0))
f=tuple((g if y==1 else h)[x] for x in range(4) for y in a)
pf=b.law(f);H=b.H(pf);I=sum((s.bit_count()*q for s,q in enumerate(pf)),F())
assert H=={2:F(2)} and I==2
delta=b.D(pa,ra);expected={2:F(1,2),3:F(-1,4)}
assert delta==expected and 4>3
refs,Eg,Og=b.joint(g,pg,1)
assert refs==[tuple((F(0),F(1))),tuple((F(0),F(1)))] and not Eg and not Og
terminal=[]
for branch in (0,1):
    fb=b.child(f,3,branch);pb=b.law(fb)
    # Data index z=1, controller spectrum sits in output indices4..7.
    target=(F(0),)*4+ra
    assert len(pb)==len(target)==8
    assert b.D(pb,target)==delta and b.H(pb)==H
    terminal.append(b.add(H,delta))
assert b.difference(b.mean(*terminal),H)==delta
out=dict(status='PASS',Hroot='2',Iroot='2',original_tight_U='2',Jroot='0',Zroot='0',source_debt='0',dummy_query_entropy_drop='0',old_debit='0',strict_excess={str(k):str(v) for k,v in delta.items()},sign_certificate='4>3 implies (1/4)log2(4/3)>0',all_source_children_nonconstant=True,first_unsupported_claim='Original JS alone pays every prescribed nonempty controller profile change',full_FEI='NOT_REFUTED; H/I=1',assertions=b.checks)
(R/'out/obstruction.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
