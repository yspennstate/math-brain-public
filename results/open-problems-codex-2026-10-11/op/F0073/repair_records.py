from pathlib import Path
import json

root = Path(__file__).resolve().parent
p = root / 'ATTEMPT.md'
old = p.read_text(encoding='utf8')
(root / 'ATTEMPT.precontinuation.txt').write_text(old, encoding='utf8')
header = '''# F0073 - research record (2026-10-12)

## Exact target and normalization
Velenik, *Localization and delocalization of random interfaces*, Probability Surveys 3 (2006), 112-169, DOI 10.1214/154957806000000050, arXiv:math/0509695v3, PDF p.23 (printed p.134), asks: "Open Problem 6. Extend (21) (when d = 2) to the case of uniformly strictly convex interactions V." The preceding paragraph includes existence of the positive infinite-volume field pinned at 0 and a mean comparable to log |i|.

Section 1.1, PDF p.5, assumes V even, convex, V(0)=0, V in C^2, and 0<c_- <= V'' <= c_+ < infinity. We study the real-valued nearest-neighbor field with edges counted once and H=sum_e V(phi_x-phi_y). Fixed positive inverse temperature and the uniform nearest-neighbor normalization can be incorporated into V and its curvature constants. More general edge weights are not part of the unit-edge normalization; the weighted modification of the local inequality is described below. Heights are real, not integer-valued. Logarithmic comparisons concern large |i|; log(2+|i|) avoids zero at neighbors.

For Lambda_N=[-N,N]^2 intersect Z^2 set phi_0=0, phi=0 outside Lambda_N, and impose phi_x>=0 at every free vertex. Let mu_N^+ be the density proportional to exp(-H) on this orthant. The source paragraph does not spell out the infinite-volume construction. Here the precise construction is the increasing zero-boundary finite-volume exhaustion, consistent with its domain notation. No uniqueness assertion for every possible pinned positive DLR measure is made. The target includes a proper limit and constants 0<c<C<infinity such that c log|i| <= E phi_i <= C log|i| for large |i|.

## Prior attempt audit
The intake F0073-A001 (2026-09-08) claims an upper bound by domination by a wall field without the pin in Lambda_(2|i|), followed by a monotone limit. This does not prove the upper bound. Domain enlargement with nonnegative boundary values increases the wall field. A bound in a single small box cannot upper-bound the increasing infinite-volume limit. Comparison in Lambda_N instead gives C log N, which diverges as N tends to infinity at fixed i. The local comparison supplies a lower bound.

'''
s = header + old[old.index('## Components developed below'):]
start = s.index('Here is a direct edge check:')
end = s.index(' The orthant is closed', start)
s = s[:start] + '''Here is a direct edge check: for a<=b and c<=d,
    V(a-d)+V(b-c)-V(a-c)-V(b-d)
      = integral_a^b [V'(t-c)-V'(t-d)] dt >= 0,
since V' is increasing. On each edge, taking coordinatewise minimum and maximum either preserves the two original endpoint pairs or replaces crossed pairs by ordered pairs. The displayed inequality decreases the total edge energy. Single-coordinate boundary terms preserve their sum exactly. Hence H(a meet b)+H(a join b)<=H(a)+H(b), which proves the lattice condition, including the boundary by continuity.''' + s[end:]
start = s.index('## Diagnostic proposition 6:')
end = s.index('Execution audit:', start)
diagnostic = '''## Diagnostic proposition 6: the moment and order bounds do not force tightness

This is not a counterexample to the Gibbs model. It checks an invalid possible inference from necessary bounds.

For N>=1, put deterministic height h_N=sqrt(N/2) at every vertex of Lambda_N except 0, with height zero at 0 and outside. Let nu_N be its Dirac law. There are n_N=(2N+1)^2-1=4N(N+1) free sites. The outer boundary has 4(2N+1)=8N+4 free-ground edges, and the origin contributes four more: B_N=8(N+1) nonzero-gradient edges. Free-free gradients vanish. Therefore
    Q(h_N)=B_N h_N^2=8(N+1)(N/2)=4N(N+1)=n_N.
For V(t)=t^2/2, this is exactly the Euler energy identity and both curvature energy bounds in Proposition 3. The resistance inequality holds deterministically. All variances vanish, so the centered variance upper bound holds. Every free vertex has at most four positive neighbors, so
    h_N >= (1/4) sum_(w~v) h_N(w).
This is the averaged lower inequality of Proposition 4. Domain enlargement increases nu_N stochastically, since h_N increases and newly free coordinates are positive. These configurations also satisfy a logarithmic lower bound at large distances, uniformly for N>=2||i||_infinity: h_N>=sqrt(||i||_infinity), which exceeds c log||i||_infinity for sufficiently large distances. Yet the neighboring height tends to infinity.

The nu_N are not Gibbs measures: their single-site conditionals are point masses, whereas the Gibbs conditional is a positive continuous density proportional to exp(-sum_j V(s-b_j)). Thus this example does not contradict the Gaussian result. It shows that the necessary energy, order, centered variance, and averaged local lower bounds alone cannot prove tightness. More Gibbs structure is needed.

'''
s = s[:start] + diagnostic + s[end:]
s = s.replace('a detour around the unit square boundary', 'a detour along the eight-vertex perimeter of [-1,1]^2 intersect Z^2, which avoids 0')
p.write_text(s, encoding='utf8')
assert '?' not in s, 'An unrepaired question-mark substitution remains'

status = root / 'STATUS.md'
status.write_text('STATE: WORKING\nNEXT: Finish one fresh shared-slot Lean check on the repaired ASCII source; save the result and final referee audit, then set DONE with PARTIAL verdict.\nVERDICT: PARTIAL\n\n2026-10-12: Resumed the completed mathematical attempt. Prior tool session 91345 is unavailable, and no matching shared-verifier completion record was found.\n2026-10-12: Found and repaired PowerShell encoding substitutions in the Lean file and three mathematical text blocks. Preserved their original bytes in this folder. No prior Lean success is claimed.\n2026-10-12: Mathematical results remain partial: finite-volume lower bound from the known box theorem, energy identity and resistance bound, local mean comparison, and a one-neighbor existence criterion. Missing uniform first-moment and logarithmic spatial upper estimates remain explicit in ATTEMPT.md.\n', encoding='utf8')
with (root / 'LITERATURE.md').open('a', encoding='utf8') as f:
    f.write('\n2026-10-12 continuation: brain.py recall query `F0073 pinned positive convex field proof mistakes`; no memory containing F0073 and no on-target theorem found. No new literature resolution is asserted.\n')
print('Restored exact mathematical text; prior versions preserved; STATUS updated.')
