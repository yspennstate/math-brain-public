import json
from pathlib import Path
p=Path('ATTEMPT.md')
s=p.read_text(encoding='utf8')
s+='''

## 6. A hostile-referee obstruction: adaptive elliptic submartingales (proved; outside C0133)
We construct a nearest-neighbor process Y on Z with each conditional right-step probability in {1/2,3/4}, returning to 0 infinitely often almost surely, but
liminf Y_n/n=0 and limsup Y_n/n=1/2 almost surely.
This is a history-dependent process, not a supplied IID cookie environment, and therefore NOT a counterexample to the problem.

Let t_1=0. At stage k the process is at 0 at time t_k. Put N_k=(t_k+1)^2 and u_k=t_k+N_k. For N_k steps, take independent increments with probabilities P(+1)=3/4, P(−1)=1/4 using fresh independent uniforms. From u_k onward take fair independent steps until the first visit to 0, defining t_{k+1}; if Y_{u_k}=0, set t_{k+1}=u_k. The entire construction uses a single sequence of independent uniforms. Every stage start is a stopping time; its duration N_k is measurable at its start. Fair one-dimensional walk hits 0 almost surely from every finite integer, as proved by finite-interval stopping in Section 5. Induction shows each stage is finite almost surely, and countable intersection shows all stages are completed. Since N_k≥1, t_k≥k−1 and t_k→∞; thus the process returns to 0 infinitely often.

Conditioned on the history at t_k, Y_{u_k} is a sum of N_k independent ±1 variables of mean 1/2. The conditional moment bound for centered variables of range length 2 (or the weaker bound with absolute size 2) gives, for every ε>0,
P(|Y_{u_k}−N_k/2|≥εN_k | F_{t_k}) ≤ 2exp(−ε²N_k/8).
Because N_k≥k², the annealed probabilities are summable. Borel–Cantelli for each positive rational ε gives Y_{u_k}/N_k→1/2 almost surely. Also t_k/N_k=t_k/(t_k+1)^2→0, so N_k/u_k→1 and Y_{u_k}/u_k→1/2.

For all times, the predictable drift per step is either 0 or 1/2. Write Y_n=M_n+A_n. Then 0≤A_n≤n/2, and Section 1's bounded-increment argument gives M_n/n→0. Consequently liminf Y_n/n≥0 and limsup Y_n/n≤1/2. Return times give liminf≤0 and the pulse endpoints give limsup≥1/2, proving the exact values.

This rules out deducing C0133 merely from bounded steps, uniform ellipticity, nonnegative predictable drift, and recurrence. In particular, a general martingale/submartingale argument must use the spatial IID cookie structure. During this process the right-step law at a site can depend on the global stage, even at its first visit: first visiting +1 just after the initial +1 step is in the fair phase, whereas first visiting +1 in the second stage after initial −1 and then +1 steps is in a biased phase. No deterministic stack is defined by this construction; no IID stack representation has been proved or claimed.
'''
p.write_text(s,encoding='utf8')
claims=[
('The martingale part of X_n dot ell is o(n); C0133 is equivalent to D_n=o(n) on the non-transient event.','proved','ATTEMPT.md, Section 1','Need control of predictable drift on the event in question.'),
('If every cookie has zero projected drift, X_n dot ell/n tends to zero almost surely, without IID or ellipticity.','proved_special_case','ATTEMPT.md, Section 2','General signed cookie drifts are not treated.'),
('For bounded-step paths returning to a fixed finite ball with successive return-time ratio tending to one, vector speed is zero.','proved','ATTEMPT.md, Section 3','IID and EL have not been shown to imply the return-time ratio condition.'),
('Sublinear accumulated absolute cookie-drift budget on departure sites implies zero projected speed.','proved','ATTEMPT.md, Section 4','No general sublinear range or adaptive budget estimate on the returning event.'),
('Simple symmetric walk has unrestricted positive excursion tail 1/(2L), excluding a uniform exponential spatial-tail consequence of BD and UEL.','proved_special_case','ATTEMPT.md, Section 5','Does not exclude estimates with a linear time budget.'),
('A uniformly elliptic history-adapted nearest-neighbor submartingale can return infinitely often with normalized liminf 0 and limsup 1/2.','proved','ATTEMPT.md, Section 6','Outside the fixed IID cookie model; not a counterexample to C0133.')]
with Path('CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for claim,status,loc,gap in claims:f.write(json.dumps(dict(problem_id='C0133',claim=claim,status=status,proof_location=loc,remaining_gap=gap,checks=['Written proof; further algebraic and exact-computation checks pending']),ensure_ascii=False)+'\n')
Path('STATUS.md').write_text('STATE: WORKING\nNEXT: Verify the one-dimensional LLN hypotheses, check finite algebra in Lean, and audit the drift reduction.\nVERDICT: PARTIAL\n\n2026-10-12: Source confirmed; exact-hypothesis full solution not located. Proved martingale reduction, balanced-cookie special case, return-time and drift-budget criteria, and an adaptive-process obstruction outside the model.\n',encoding='utf8')
print('saved obstruction and claims')
