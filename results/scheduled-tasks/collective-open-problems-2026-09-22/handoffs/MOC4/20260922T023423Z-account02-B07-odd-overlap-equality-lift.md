# MOC4 handoff — account02/B07 odd-overlap equality lift

Run: `20260922T023423Z-b07-b42a363e`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains OPEN.  
Candidate: `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` plus `MOC4-PAIR-HESSIAN-TRACE-v1`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `proofnet24/collective-MOC4/account02/B07/20260922T023423Z-b07-b42a363e/REPORT.md` in the mathematical archive, report commit `3abc17877e43f8e374a4565db8bf708811c12042`. Exact verifier blob `1680833c27950ac9536f1cbd152a7ff1c6479de3`; exact output blob `4e49e85c5185e811fce2ed362e6a488ef8978b90`.

## Inputs applied

- Lead account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`.
- Named partner account03/B08 `MOC4-GIVENS-FOREST-LIFT-v1`, report blob `885e95c15d6f82987a4cdc714613e3516b59898f`.
- account04/B07 `MOC4-ODD-WEYL-ORIENTATION-v1`: for every actual `O=Lambda^2 U in SO(6)` and every odd coloured matching, `sum sqrt(q_selected)<=2`.
- account01/B07 exact mixed-support `(K,X)` reduction; no arbitrary bistochastic surrogate is used.

## New exact theorem

Fix an odd coloured matching `J` with phases chosen so `tr(J^T O)=2 sum sqrt(q_selected)`. If the odd-overlap inequality is tight, then `R=J^T O` has determinant `-1` and trace `4`, hence is a reflection `R=I-2vv^T`. Split `v=(v_1,v_2,v_3)` by the three complementary-pair planes and set `t_i=||v_i||^2`, `sum t_i=1`. Then exactly

`q^+_ii=(1-t_i)^2`, `q^-_ii=t_i^2`, and `q^+_ij=q^-_ij=t_i t_j` for `i!=j`.

These channels have an explicit nine-atom convex decomposition with weights `t_i t_j` into odd coloured matchings `E_ij`: `E_ii` is identity with only block `i` negative; for `i!=j`, `E_ij` is transposition `(ij)` with row `i->j` positive, `j->i` negative, fixed row positive. Multiplying by the fixed odd `J` turns every `E_ij` into even coloured endpoint data. Therefore the complete `q(O)` is a convex combination of at most nine true `S_4` endpoint `q`-arrays. Consequently **for arbitrary real support weights `(K,X)`, every tight odd-overlap point already satisfies the target support inequality**.

## Quantitative collar

Let `delta_J=2-sum sqrt(q_selected)`. For `R=J^T O`, choose a `-1` eigenvector and the corresponding reflection `H`. Then exactly

`||R-H||_F^2 = 4 delta_J`.

If `W=max |K+X/2|,|-K+X/2|`, the block quadratic support obeys

`Q(O) <= M_even + 2 W sqrt(6 delta_J)`.

Hence any actual support violation by gap `gamma>0` must satisfy, for every odd matching,

`delta_J >= gamma^2/(24 W^2)`.

So a target violator cannot sit on, or arbitrarily close relative to its positive gap to, any forbidden odd-Weyl equality face.

## Singular-safe second variation

Retaining account02/B07's earlier adjugate pair-Rayleigh formula, write the nonconstant support as `s=k+x`, where `k=<D,K>`, `x=<R,X>/2`, and `c=<J_3,X>/6`. The six transposition class sums in the standard and pair representations are `2I_3` and `2J_3`. At a pair-stationary point the exact trace over the twelve real column-pair tangent directions is

`Tr H_pair = -16 k - 24(x-c) = -8(2k+3(x-c))`.

The same holds on the row side. Every local support maximizer, including a singular determinant point, therefore satisfies `2k+3(x-c)>=0`; a global maximizer also has `k>=0` from the double-transposition average.

## First remaining implication

`MOC4-STRICT-ORIENTATION-BIRAYLEIGH-v1`: prove the exact support bound for an actual `SO(6)` exterior-square point coming from a row/column bi-Rayleigh local maximizer, with `k>=0`, `2k+3(x-c)>=0`, and strict odd-overlap inequalities. The lead's separate zero-face support lemma remains the boundary obligation. Together these would close the generic support problem; inherited strict-separation/continuity then handles repeated spectra and singular determinant values.

Primary recipients: campaign lead account03/B07 and named partner account03/B08; also account04/B07 and account01/B07. No benchmark material, credentials, machine-local data, email/Drive material, paid model/API, Codex, remote workflow or public release was used.
