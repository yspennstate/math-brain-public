from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; agent=ROOT.parents[1]
p=ROOT/'REPORT.md'; s=p.read_text(encoding='utf-8')
s=s.replace('was interrupted after stalling in trial factorization; it did NOT PASS.','was interrupted after stalling; trial factorization is the code-path diagnosis, without a captured stack profile. It did NOT PASS.')
s=s.replace('What I stopped: only my stalled targeted check to enforce its frozen runtime cap; no other live work.','What I stopped: only my stalled targeted check after the outer-loop deadline failed to bound a single step; no other live work.')
s=s.replace('Total1080243 exact author assertions.','All EIGHT raw reset charges are strictly positive before their actual refunds; out/FIXTURE.json certifies the signed combined payment rather than assuming free resets. Total1080243 exact author assertions.')
p.write_text(s,encoding='utf-8',newline='')
p=ROOT/'VALIDATION_REVISION.json'; obj=json.loads(p.read_text(encoding='utf-8')); obj['diagnosis_limit']='No stack sample or exact interrupted elapsed-time measurement was captured. Trial factorization is inferred from code and the successful GCD-log replacement, not asserted as a profiled stack fact.'; p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='')
p=agent/'LEARNED.md'; s=p.read_text(encoding='utf-8-sig'); marker='20261023T040353Z-GCD'
if marker not in s:
    p.write_text(s+'\n2026-10-23 ['+marker+'] Exact log identities need no prime factorization: split integer bases at pairwise GCDs, combining rational coefficients. The product of distinct bases decreases at each split; pairwise coprime final bases imply zero iff all coefficients vanish by unique factorization after clearing denominators. Composite-base atanh bounds still certify signs. This avoids large physical-reference normalizer factorization stalls. Also the delta1/2 overhead-release failure is an actual family a_r=-1 only at0 for EVERY r>=5, by strict convexity on means[7/8,1]. All8 saved raw resets are positive, so actual phase refunds are essential to the demonstrated transaction.\n',encoding='utf-8',newline='')
parts=s if False else (ROOT/'REPORT.md').read_text(encoding='utf-8')
print(parts[:2200]); print('\nVALIDATION/BOUNDARY EXCERPT\n'+parts[parts.index('The initial t=3'):parts.index('## proof dependencies')]); print('\n'+parts[parts.rindex('Universal bridge:'):])
