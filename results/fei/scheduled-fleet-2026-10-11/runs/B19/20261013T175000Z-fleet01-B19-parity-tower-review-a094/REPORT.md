# Independent A094 review: parity-balanced activation towers

## Verdict

**ACCEPTED at the exact formal scope of
`B05_A023_PARITY_BALANCED_TOWER_RETAINED_U_v1`.**

For every Boolean base (P), every (d\ge1), and the tower obtained by
alternating a fresh character balancer with a fair half-activation,
[
U(T_d(P))=2+2^{-d}(U(P)-2),qquad
I(T_d(P))=2+2^{-d}(I(P)-2).
]
Consequently (U(P)\le2I(P)) implies (U(T_d(P))\le2I(T_d(P))).
For every adaptive/pruned restriction tree querying the (n+2d) tower
variables, and every common disjoint Boolean factor (h),
[
U(T_d(P)h)-\sum_ell\lambda_ell U((T_d(P)|_ell)h)
\le2I(T_d(P)).
]
The proof has no hidden dependence on dimension, depth, the terminal
activation probability (2^{-d}), tree order, pruning, or (h).

## Independent reconstruction

For a fresh character (w), Fourier support is shifted by adjoining (w),
so (U(wf)=U(f)) and (I(wf)=I(f)+1).  If (q) is balanced, the
half-activation (A_z(q)) has masses (1/4) at
(\varnothing,{z}) and, for every nonempty (S), two masses
(p_q(S)/4) at (S,S\cup{z}).  Their caps are
[
1,quad rac12,quad rac12pi_q(S),quadrac14pi_q(S),
]
which gives
[
U(A_z(q))=1+rac12U(q),qquad
I(A_z(q))=rac12+rac12I(q).
]
Solving the alternating affine recurrences yields the displayed identities
and counts exactly (d) selectors plus (d) balancers.

The tree conclusion is valid but elementary once the root inequality is
known:
[
U(T_d)-\mathbb E_ell U(T_d|_ell)\le U(T_d)\le2I(T_d),
]
because (U\ge0).  Disjoint tensor additivity cancels (U(h)) exactly.
Thus no nodewise sign or influence-ownership claim is required.

## Required scope correction

The formal claim is correct, but two interpretive phrases in the author
report are too strong:

1. The positive-depth tower family is **not restriction-closed** under
   arbitrary physical restrictions.  Take (P=1,d=1).  Then
   (T_1(P)=A_z(w)); restricting (w=-1) leaves the dictator (z), whose
   (U) is zero.  Every positive-depth tower has
   [
   U(T_d(P))=2+2^{-d}(U(P)-2)\ge1,
   ]
   so this dictator is not another positive-depth tower.
2. The proof does not establish a single-use pivotal-event ownership or a
   local/global refund mechanism.  The retained-tree estimate follows from
   the root endpoint and leaf nonnegativity.  Fresh characters make the
   root recurrence exact, but no per-node credit is identified.

These corrections do not alter the theorem in `CLAIMS.json`.  They do
mean the result should be described as an expanding all-depth family with
an endpoint telescope, not as a restriction-closed solution of the
changing-core amortization problem.

## Dense-nullity-two instantiation

The corollary over rank-((m-2)) physical shields is valid.  Its only
external mathematical input, the base bound (U(P)\le2I(P)), was
independently accepted in B19 commit
`b10d0889f9a326b40fe1028af9d8ebf936967367`.  The tower transfer itself
is self-contained.

## Verification

Command:

`python3 INDEPENDENT_CHECK.py`

The independent implementation enumerated all 278 Boolean truth tables
through three variables, checked 1,112 tower identities at depths 1--4,
202 coordinate restrictions, and nine disjoint tensor products.  Maximum
formula error was (2.220\times10^{-16}).  It also reconstructs the exact
restriction-closure falsifier above.

## Source record and remaining gap

Reviewed source: canonical commit
`b1afa5899bf3729e5c44d029fee9cf4a6ea656b8`, author proof blob
`bd46b14b8c0c52109a22430913ec6f66011d26a0`, claim blob
`7095e99b8e1926a2b587f671ecad79adb1f8cb1d`.

The result does not cover biased selectors, imperfect or absent balancing,
reused/shared variables, leaf-dependent terminal cores, or arbitrary
changing coherent cores.  The next unpaid step is a quantitative
mean/correlation-defect recurrence whose errors admit a proved nonreusing
payment.  Full FEI remains **OPEN**.

## Delivery

The complete review bundle was delivered to the canonical repository at
commit `f442d13919b7361e830b1afb0fec8ff4208d25e7` and mirrored to the
Brain handoff route at commit
`af2aeabbda33d78934035ae2da8e6851d56bb807`.  Native adoption is not
claimed.

