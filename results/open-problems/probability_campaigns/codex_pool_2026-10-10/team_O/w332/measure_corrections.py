import difflib
from fractions import Fraction as F
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
cases=[]
for d in [7,8,10,12,20]:
    ratio_exponent=F(1,3)-F(2,d)
    cases.append({'problem_id':'C0068','d':d,'ratio_exponent':str(ratio_exponent),
        'old_claim_V_crossover_is_smaller':ratio_exponent<0,
        'corrected_claim_V_crossover_is_larger':ratio_exponent>0})
a=F(1,2);lap=F(2)
cases.append({'problem_id':'C0101','a':str(a),'x':0,'laplacian':str(lap),
    'old_claim_bound_a_plus_one':lap<=a+1,'corrected_bound_strict_a_plus_two':lap<a+2})
before=sum(c.get('old_claim_V_crossover_is_smaller',c.get('old_claim_bound_a_plus_one',False)) for c in cases)
after=sum(c.get('corrected_claim_V_crossover_is_larger',c.get('corrected_bound_strict_a_plus_two',False)) for c in cases)
assert before==0 and after==6
receipt={'command':'python -X utf8 ~/brain_workers/w332/measure_corrections.py','before_passed':before,
    'after_passed':after,'total_cases':len(cases),'scope':'Exact checks of two stored assertions and their corrections; no live recall or deployment benchmark','cases':cases}
(root/'correction_measurements.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
hooks=[
 {'id':'crossover-w332-01','area':'math','event':'stage-start','cue':'(?i)(V|volume).*(-2/d|-1/3).*(<<|crossover|correlation)',
  'fire_when':'For d>6, V^(-2/d) << V^(-1/3), hence above the correlation crossover.',
  'silent_when':'Compute centered fourth moments of a fixed compact law.',
  'text':'Compare powers by dividing: V^(-2/d)/V^(-1/3)=V^(1/3-2/d). For d>6 it grows. Check this sign before using a crossover argument.',
  'evidence':str(root/'correction_measurements.json')+' cases C0068, five old signs fail and five corrected signs pass','proposer':'w332'},
 {'id':'rounding-w332-02','area':'math','event':'stage-start','cue':r'(?i)ceil.*(quadratic|x\^2).*(laplacian|curvature|a\+1)',
  'fire_when':'ceil(a*x^2/2) has Laplacian at most a+1.',
  'silent_when':'An integer binomial quadratic has Laplacian equal to its matrix trace.',
  'text':'Check the rounding budget before summing curvatures. For a=1/2, ceil(a*x^2/2) has second difference 2 at x=0, exceeding a+1. The general rounding bound is a+2.',
  'evidence':str(root/'correction_measurements.json')+' case C0101 a=1/2,x=0; old bound fails, corrected bound passes','proposer':'w332'}]
for h in hooks:
    assert len(h['text'])<=300
    assert re.search(h['cue'],h['fire_when'])
    assert not re.search(h['cue'],h['silent_when'])
folder=root/'hooks';folder.mkdir(exist_ok=True)
hooktext=''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks)
(folder/'math-w332.jsonl').write_text(hooktext,encoding='utf-8')
patch=''.join(difflib.unified_diff([],hooktext.splitlines(keepends=True),
    fromfile='a/~/primary_directive/hooks1000/proposals/math-w332.jsonl',
    tofile='b/~/primary_directive/hooks1000/proposals/math-w332.jsonl'))
(root/'patches/02_math_hooks.diff').write_text(patch,encoding='utf-8')
print(json.dumps(receipt,indent=2))
print('Hook control checks: two fire and two silent cases PASS. Hook proposals staged locally for reviewer under worker write restriction.')
