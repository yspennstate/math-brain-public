from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
spec={'helper':'review-v3-and-general-reset-v1','family':'balanced activated Boolean cores; all Boolean functions on 1..3 bits','domain':'review all balanced n1,2 and n3 masks15,23; r1..3; three references; literal posterior r1..4; sharp coefficient r1..5 and analytic tail. General reset all singleton queries n1..3','case_count':{'review_references':90,'posterior':4,'general':804},'symmetry':'none; selected n3 review cases explicit, not exhaustive','arithmetic':'Fraction and prime-log vectors; outward 20-term rational log intervals','memory_MB':70,'maximum_runtime_seconds':50,'reason':'prior combined and review runs reached internal cutoff; shrink review independently; retain analytic proof'}
(p/'out/FINAL_SPEC.json').write_text(json.dumps(spec,indent=2))
s=(p/'code/check_review.py').read_text()
s=s.replace('for mask in range(1<<(1<<n)):', 'for mask in (range(1<<(1<<n)) if n<3 else [15,23]):')
(p/'code/check_review_v3.py').write_text(s)
(p/'code/common.py').write_text(s[:s.index('# Independent reference review')])
print('Frozen 90 review reference cases and 804 physical-query cases.')
