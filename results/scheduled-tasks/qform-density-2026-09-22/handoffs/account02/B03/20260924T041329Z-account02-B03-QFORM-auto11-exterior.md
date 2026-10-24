SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T04:13:29Z.
attacking: global exterior-minor overlap decomposition — convert disjoint spectral exterior mass into a literal physical E3 crossing, then isolate the overlap-heavy residue.

# Handoff — account02/B03

Status: **NEW STRUCTURAL/ANALYTIC EXIT / LINEAR SMALL-BALL BRANCH / FULL QFORM OPEN**.

Canonical mathematics: `yspennstate/math-open-problems@5e5366b98337d13ba24bf666f4e42155553de7c2`, report in this run's account02/B03 deliverable directory. Early calculation commit: `43eab33dc9cd6063c84089b5fc3692abceeadb21`.

New theorem `QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`. For symmetric `A` define

`E_r(A)=sum_{|S|=|T|=3, |S∩T|=r} det(A[S,T])^2`, `r=0,1,2,3`.

Cauchy–Binet gives the exact identity

`sum_r E_r(A)=e_3(A^2)=sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2`.

Thus the owner spectral hypothesis implies `sum_r E_r>=1`. A random physical bipartition satisfies

`E_{I|J} e_3(A[I,J]^T A[I,J])=E_0(A)/64`,

so some literal cut has physical crossing `E3>=E_0/64`.

Applying the newest account03/B03 r48 marginal-free physical-E3 receiver (`C_E3=8.4530212255281768747...`) gives

`||p_Q||inf <= 2 C_E3 E_0(A)^(-1/6)
             =16.9060424511... E_0(A)^(-1/6)`,

and therefore linear one-copy small-ball scaling on this branch. The same branch gives, using only the whole-output independent-copy identity,

`int |t|^-1/2 |phi_Q(t)|^2 dt
 <=4 sqrt(2 pi C_E3) E_0(A)^(-1/12)
 =29.1511643035... E_0(A)^(-1/12)`

and

`E|Q-Q'|^-1/2 <=4 sqrt(C_E3) E_0(A)^(-1/12)`.

Clean universal fork: if `E_0>=1/4`, then `||p_Q||inf <21.301`; otherwise one of `E_1,E_2,E_3` exceeds `1/4`. So the structural debt has been narrowed to overlap-heavy one-anchor, two-anchor, or principal-triple exterior energy. This does not claim those overlap-heavy branches are already closed.

Required pinned source application: for the exact target-valid signed-frame family `A_q=R diag(1,1,-1)R^T`, where `R` repeats the four tetrahedral sign rows equally, an even balanced physical cut has three cross singular values exactly `1/2`, hence `Z_3=1/64`. Its Theorem-D row marginals are `3/(2q)<=1/2` for even `q>=4`. The pinned `e5f71d79eff325201dd0274053d20268ce65b837` Theorem D therefore gives

`||p_Q||inf <=12 sqrt(e)=19.7846552484...`,

`int |t|^-1/2 |phi_Q(t)|^2 dt <=(48/5)sqrt(pi)e^(1/4)=21.8484076269...`,

`E|Q-Q'|^-1/2 <=(24 sqrt(2)/5)e^(1/4)=8.7162535618...`.

The same family is a source-valid localization obstruction: every physical principal triple determinant is at most `1/(4q^3)`, while total third exterior energy is exactly one and

`E_0(q)=(1/4)(1-1/q)^3+(3/4)(1-1/q)^2 ->1`.

Thus aggregate disjoint exterior mass can remain order one while every individual principal triple degenerates.

First unpaid implication: for each `r=1,2,3`, convert `E_r(A)>=c` product-preservingly into an already-paid finite-hub / nested-rank-two / localized-principal / aggregate-frame receiver, or isolate a sharper exact obstruction. Do not demand one large individual minor, do not delete nonzero coefficient tails, and preserve the whole-copy dependence structure.

Latest designated partner actually applied: account03/B03 r48, source report `math-open-problems@3638467084deb8af24d1b01aa01cc300ee85ea8a`.

Full QFORM remains OPEN. Unrestricted continuity remains OPEN. Repository retrieval/writeback occurred, but authenticated native learned-memory receiver use was not verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.
