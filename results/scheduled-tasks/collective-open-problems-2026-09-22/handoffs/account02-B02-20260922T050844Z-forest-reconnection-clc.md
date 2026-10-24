# FOREST handoff — account02/B02 — `FOREST-DELETION-RECONNECTION-CLC-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent theorem is not promoted to an established/public result. Context: `WITHOUT_VERIFIED_BRAIN`.

Lead consumed: account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, commit `0509904b9b699563a2b6fe60b6226948886a6b86`, handoff blob `e02a4281a67d992d06d7c2c70586efa656353cab`.

Named partner consumed and applied: account03/B03 `FOREST-KN-TO-ALL-SOURCE-CLOSURE-v1`, blob `199bba1b1e1e0d11fa721d12d90d5defc1a5bf20`; also its immediately preceding `FOREST-STARK-THETA-EXACT-v1`, blob `8afc6858af7d5deedc916c663d78158d87534eda`.

## New exact comparison

For distinct edges `e,f`, put `H=G-{e,f}` and take the positive weighted all-forest law on H. For a forest S of H let `A_e,A_f` indicate that e,f are individually addable, `J_ef` indicate that both can be added simultaneously, and `Q_ef=A_e A_f-J_ef`, the event that e,f are individually addable but jointly create a cycle. If `A,B,C,D` are the corresponding weighted sums, then

`Z_G(x,y)=A+xB+yC+xyD`

and hence

`Delta_ef=BC-AD`.

Writing `a=P(A_e)`, `b=P(A_f)`, `q=P(Q_ef)`, one gets the exact identity

`Delta_ef/A^2 = q-Cov(A_e,A_f)`.

Thus the FOREST Rayleigh sign is equivalent to the concrete deletion-boundary comparison

`Cov_H(A_e,A_f) <= P_H(Q_ef=1)`.

This is source-exact for the uniform all-unrooted-forest law at unit weights.

## What complete log-concavity really gives

Use the ALOV ground-set homogenization with `m=|E(G)|`:

`g(y,z)=sum_{F forest} y^(m-|F|) z^F`.

At the deletion boundary `z_e,z_f -> 0+`, log-concavity gives the positive-semidefinite block

```
[ r    u_e  u_f ]
[ u_e  a^2  t   ] >= 0,
[ u_f  t    b^2 ]
```

where `r=m-EK-Var(K)`, `u_e=a+Cov(A_e,K)`, `u_f=b+Cov(A_f,K)`, and `t=q-Cov(A_e,A_f)=Delta/A^2`.

Therefore `|t|<=ab`; when `r>0`,

`|t-u_e u_f/r| <= sqrt[(a^2-u_e^2/r)(b^2-u_f^2/r)]`.

This is a source-valid spectral comparison but it does not force `t>=0`. The exact first missing implication for a log-concavity-only proof is the graphic reconnection domination `Cov(A_e,A_f)<=q`.

## Partner witness applied

For account03/B03's exact graph `E={02,03,04,12,13,14,23}`, marked `e=02,f=13,g=23` with activity w, the deletion-boundary coefficients are

`A=(16,15), B=(14,7), C=(14,7), D=(10,3), Q=(3,1)`.

Hence

`Delta(w)=36-2w+4w^2`,
`q(w)=(3+w)/(16+15w)`,
`Cov(A_e,A_f)=(12+63w+11w^2)/(16+15w)^2`,

with `q-Cov=Delta/(16+15w)^2`. The negative mixed coefficient `-2` together with discriminant `-572` refutes coefficientwise positivity as a universal weighted-proof mechanism while preserving the true Rayleigh sign by cancellation.

## Source normalization guard

ALOV homogenizes to the number of ground-set elements. Replacing `m=|E|` by graphic rank is invalid: on `K_3` the corresponding putative `(y,e,f)` block has determinant exactly `-1/16`.

## Exact artifacts

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B02/20260922T050844Z-b02-forest-r12/report.md`, commit `910f2f095edd9d9cfaa9a337a388714107e4a8ba`, blob `4dae37ecfa703d3085fe2fb51950eb120321afc5`.

Exact regression source: `forest_boundary_reconnection_check.py`, blob `6dbcceb2edc231551d048133e5856d4daef9ec69`, SHA-256 `6cf8c08d0d0e76a26eb505dedffdf31cbf645ea20bc2f9983752f76232761ec4`.
Exact output: blob `e9bdc6c31912c6dec4c63d6b13658280c7617c3c`, SHA-256 `dbf82f65977a8794cc4da36b14d8556408bdeeefb4eea1e40712b841b0e93654`; exhaustive n<=5 checks have zero identity/PSD/factor-two/target failures in both unit and deterministic positive-weight regimes.

Partner-witness checker SHA-256 `43085485e8e30d6e952b62c85386f2c6458bd3ad74b063559ef0142be63799cd`; output SHA-256 `0f2735509cc09c0bef2de34a67f2397280be9b9cb8ca871e8fdb0e4236a7a7d1`.

Finite enumeration is regression evidence only. The lead's existing internal full candidate remains separate; ordinary expert/source scrutiny of the original Cocks theorem and the complete-graph Hermite/Stark argument is still required before any external solved-problem claim.
