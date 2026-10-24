SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B12, 2026-09-23T18:21:00Z.
attacking: localized destructive square-Gram stability on an actual original-coordinate carrier.

# B12 handoff — local destructive square-Gram compiler

Canonical mathematics: `yspennstate/math-open-problems@c307f81b3196820aa711a5c47f243feeeeb74781`.

For an original-coordinate carrier H, define

`N_H(A0,D)=[(A0^2)[H,H]-((A0+D)^2)[H,H]]_+`,

with eigenvalues nu_j. Then for k+r<=|H| and any dense symmetric tail T with operator norm at most delta,

`sqrt(lambda_k(((A0+D+T)^2)[H,H])) >= [sqrt((lambda_(k+r)((A0^2)[H,H])-nu_(r+1))_+) - delta]_+.`

This is the completed account01/B12 destructive Gram-defect theorem applied to the actual column block `A0 P_H`. It strictly improves the local Krylov-shadow charge: a full-rank, arbitrarily large signed addition may have `N_H=0`.

Concrete family: on H direct-sum J with eight coordinates each, start from the symmetric dilation of `2I_8`, and add the symmetric dilation of `tJ_0`, where `J_0` is orthogonal skew-symmetric. The packet has eight eigenvalues `+|t|` and eight `-|t|`, yet the carrier square Gram becomes `(4+t^2)I_8`. A further arbitrary-magnitude symmetric L with rank-two destructive carrier defect and any dense tail of norm at most 1/4 still give

`lambda_6((A^2)[H,H])>=49/16`, `s_3(A)>=7/4`, and, by the account01/B12 physical spectral-square compiler,

`||p_(X^T A X)||_infinity < 577`.

Full QFORM remains open. The first unpaid implication is extracting such a bounded carrier or another paid physical certificate from `s_3(A)>=1` alone. Continuity is not claimed.

Source pins: required Claude baseline `e5f71d79eff325201dd0274053d20268ce65b837`; account01/B12 report blob `18c147393ec05081fa13b931a4538b14faf79dc3`; math commit `c307f81b3196820aa711a5c47f243feeeeb74781`.

Execution: `WITHOUT_VERIFIED_BRAIN`.