from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s+='''

## 10. Nonnegative-drift refinement: a ballistic outward leg forces a much later return (proved)
Assume all b(x,i)≥0 in the chosen direction ℓ. Thus D_n is nondecreasing. Work on the full-probability event M_n/n→0 of Section 1. Fix R<∞ and ε>0, and suppose n_j→∞ with X_{n_j}·ℓ≥εn_j. Let t_j≥n_j be any subsequent time with ||X_{t_j}||≤R, if such times exist. For large j,
D_{n_j}=X_{n_j}·ℓ−M_{n_j}≥εn_j/2,
while D_{t_j}≥D_{n_j} and |X_{t_j}·ℓ|≤R||ℓ||. Hence
εn_j/2 ≤ R||ℓ|| + |M_{t_j}|.
Divide by t_j. Since t_j≥n_j→∞, the right side tends to 0, proving n_j/t_j→0, equivalently t_j/n_j→∞. If the first return is used, this says a nonzero subsequential positive speed on the returning event requires excursions whose future return time grows faster than the time at their high point.

There is also a direct time-constrained return estimate, but its drift-sign assumption is essential. Given deterministic n with X_n·ℓ≥εn, let j≤Kn with ||X_{n+j}||≤R. For n≥2R||ℓ||/ε, monotonicity of D implies
M_{n+j}−M_n = X_{n+j}·ℓ−X_n·ℓ−(D_{n+j}−D_n) ≤−εn/2.
Conditionally on F_n, the shifted martingale has increments bounded by 2c. Section 1's one-sided bound gives, for fixed j,
P(M_{n+j}−M_n≤−εn/2 | F_n) ≤ exp(−ε²n²/(32c²j)).
For integer K≥1 and a union over 1≤j≤Kn,
P(∃ j≤Kn: ||X_{n+j}||≤R | F_n) ≤ Kn exp(−ε²n/(32c²K))
on {X_n·ℓ≥εn}. Summing over deterministic n and applying Borel–Cantelli establishes that such fast returns occur only finitely often. This is a valid timed return estimate under nonnegative cookie drift; it is not the unrestricted excursion estimate from the earlier attempt and does not imply zero speed by itself. The adaptive example in Section 6 obeys this slowdown requirement.
''';p.write_text(s,encoding='utf8')
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'problem_id':'C0133','claim':'For nonnegative projected cookie drift, any sequence of ballistic projected heights with subsequent bounded-ball returns has return-time/height-time ratio tending to infinity; a fixed linear-time return window has a summable exponential bound.','status':'proved','proof_location':'ATTEMPT.md Section 10','remaining_gap':'Does not exclude very long returning excursions, and does not treat arbitrary signed projected drift.','checks':['Monotonicity of predictable drift plus proved martingale strong law; conditional Azuma constant and finite union written explicitly.']})+'\n')
Path('CHECK_HISTORY.md').write_text('''# Check history

2026-10-12. First exact linear-system check failed: integer coefficient assignments introduced float division. Corrected all coefficients to Fraction; exact checks then passed for L=2,3,5,10,20,40 and all 4096 twelve-step paths.

First Lean run failed because PowerShell piped Unicode mathematical characters to Python as question marks. No formal check was claimed. Recreated the Lean file in ASCII.

Second Lean run failed because Windows PowerShell Set-Content added a UTF8 BOM, which this Lean invocation did not accept at the first import. Removed the BOM with Python utf-8-sig input and utf8 output, and replaced ASCII Boolean inequality by Not of equality. Final run result is recorded in lean_result.json and lean_check.log; only return code zero will count as checked.
''',encoding='utf8')
print('saved stronger sign-restricted return bound')
