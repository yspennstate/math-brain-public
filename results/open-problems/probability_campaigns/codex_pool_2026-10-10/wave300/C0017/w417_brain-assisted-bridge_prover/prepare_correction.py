"""Build a reversible review-only ledger patch and measure a source canary."""
import difflib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
live=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl')
match=None
with live.open(encoding='utf-8') as stream:
    for lineno,line in enumerate(stream,1):
        if '"attempt_id": "C0017-A001"' in line:
            match=(lineno,line)
            break
assert match is not None
lineno,oldline=match
old=json.loads(oldline)
new=dict(old)
bad='for the q=1 FK model the parafermionic observable has spin sigma = 2/3'
good='for the q=1 FK model the parafermionic observable has spin sigma = 1/3'
assert old['result'].count(bad)==1
new['result']=old['result'].replace(bad,good)
new['correction_note']='DRAFT source correction by w417, 2026-10-10; independent review pending. In the convention F(e)=E[exp(i sigma W(e,e_b)) 1_{e in gamma}], Duminil-Copin, Divergence of the correlation length for critical planar FK percolation, Conjecture 1 Eq.(3.3), PDF page index 9, gives sigma=1-(2/pi)arccos(sqrt(q)/2). Thus q=1 has sigma=1/3, while sigma=2/3 has q=3. https://www.ihes.fr/~duminil/publi/divergenceFK.pdf . The historical failed-route assessment is retained; this correction does not prove conformal invariance.'
new['correction_status']='draft_pending_w419'
newline=json.dumps(new,ensure_ascii=False)+'\n'
relative='06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl'
patch=''.join(difflib.unified_diff([oldline],[newline],fromfile='a/'+relative,tofile='b/'+relative,n=0)).replace('@@ -1 +1 @@',f'@@ -{lineno} +{lineno} @@')
(ROOT/'patches').mkdir(exist_ok=True)
(ROOT/'patches/01_c0017_spin_source_correction.diff').write_text(patch,encoding='utf-8')
(ROOT/'CORRECTED_ATTEMPT_DRAFT.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
cards=json.loads((ROOT/'MATH_BRAIN_RETRIEVAL.json').read_text(encoding='utf-8'))['cards']
card=next(c for c in cards if c['metadata'].get('logical_id','').endswith(':attempt-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic'))
assert bad in card['body']
before=abs(4*math.sin(math.pi*(2/3)/2)**2-1)
after=abs(4*math.sin(math.pi*(1/3)/2)**2-1)
assert before>1.9 and after<1e-14
result={'canary':'Source parameter equation applied to the exact returned C0017 attempt card','node_id':card['id'],'logical_id':card['metadata']['logical_id'],'returned_card_truth_status':card['metadata']['truth_status'],'assumed_q':1,'before_sigma':'2/3','after_sigma':'1/3','before_equation_residual_in_q':before,'after_equation_residual_in_q':after,'source_url':'https://www.ihes.fr/~duminil/publi/divergenceFK.pdf','source_locator':'Conjecture 1 Eq.(3.3), PDF page index 9 (10th PDF page)','ledger_line':lineno,'patch_applied_to_live':False,'scope':'One exact legacy record and a concept correction; not a global recall benchmark or a proof of C0017.'}
(ROOT/'REPAIR_MEASUREMENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
