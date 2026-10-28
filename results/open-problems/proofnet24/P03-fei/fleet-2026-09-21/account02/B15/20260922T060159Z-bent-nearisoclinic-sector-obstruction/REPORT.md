# account02/B15 — bent-carrier one-point suspension: no high-posterior KL sector, exact child-slack compensation

**Classification:** `BOOLEAN_OBSTRUCTION / BRIDGE_CHANGED / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Control, target, and movement


The owner target is the all-gate inequality `(G)` from `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`. Its balanced-uniform specialization is the support-deficit currency

\[
D_C(f):=C\,(I(f)-1)-H(f)
\]

for balanced Boolean functions. The live numerical center used only for the finite table below is

\[
C^\dagger=6.521851214.
\]

No statement below promotes that numerical candidate to a theorem.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** the previous three substantive B15 reports (balanced stopping/mixing KL; high-posterior sector KL for a character cofactor; packet-plus-original-coordinate price KL on the Numaro source) all tried to make a negative relative-entropy credit pay a Shannon loss locally. This run attacks the first missing Booleanity implication behind the sector route and constructs a genuine Boolean family in which *every* posterior sector stays rare and the whole vertical KL is only quadratic in the disagreement. It then keeps, rather than discards, the exact child defects and proves that they pay the same family with large dimension-free margin.

The fleet-method moves used are #2 (attack the negation of the hoped-for sector lemma), #11 (work in exact relative entropy), and #30 (isolate one physical defect scale).

## 1. Other-account result consumed

The named completed other-account input is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T043923Z-balanced-pivot-joint-credit/REPORT.md`

including its later dyadic-Boolean-rigidity addendum committed as `989bdee7c3e16b3c667c8d27a4e43e857a2bd682`.

At a balanced physical pivot, that work writes the exact joint credit in terms of the angular variables

\[
T_S={a_S^2+b_S^2\over2},\qquad
c_S={2a_Sb_S\over a_S^2+b_S^2},
\]

and proves that after forgetting Boolean realizability the scalar relaxation can be sharp. Its addendum proves strict Boolean rigidity for sparse dyadic disagreement but leaves the quantitative size of the rigidity credit open. A same-account compatible handoff (`account02/B17/.../LATE_HANDOFF_ADDENDUM.md`) identifies the remaining threat as a Boolean near-isoclinic/sign-coherent family whose local rigidity gap tends to zero sufficiently fast.

This report constructs exactly such a genuine Boolean near-isoclinic/sign-coherent family. It is therefore a direct use of the account01/B16 state variables and a resolution of that existence question, but not a counterexample to FEI.

There is important prior negative context: account03/B13's completed `20260922T040037Z-bent-swap-local-margin` report already proves that a pointwise scalar local-margin bound fails, with unbounded requested correction. The result below does **not** re-claim that broad obstruction. Its sharper contribution is specific to the Shannon/KL bridge: it proves that on a realizable Boolean family there is no hidden high-posterior spectral sector at all, the entire vertical KL is `O(delta^2)`, and the account01/B16 angular state is simultaneously near-isoclinic and sign coherent. It then exhibits the exact child-slack compensation.

## 2. Exact balanced restriction cocycle and the missing Shannon implication

For an unbiased pivot with balanced restrictions `f_0,f_1`, let

\[
a_S=\widehat f_0(S),\qquad b_S=\widehat f_1(S),
\]

\[
T_S={a_S^2+b_S^2\over2},\qquad
z_S={1\over4}(b_S-a_S)^2,\qquad
\theta_S={z_S\over T_S},
\]

and let

\[
d=\Pr[f_0\ne f_1]=\sum_S z_S.
\]

The exact information credit has the decomposition already used in the preceding B15 sector report

\[
\mathcal C=H(B\mid S)+I(S;J),
\]

where

\[
I(S;J)=\sum_S T_S
D_{\rm KL,2}\!\left(\operatorname{Bern}(\theta_S)\middle\|\operatorname{Bern}(d)\right).
\tag{2.1}
\]

At a balanced-uniform node the exact support-deficit cocycle is

\[
D_C(f)=\frac{D_C(f_0)+D_C(f_1)}2+\mathcal L_C,
\tag{2.2}
\]

with

\[
\boxed{\mathcal L_C
=Cd-1-h_2(d)+H(B\mid S)+I(S;J).}
\tag{2.3}
\]

The previous character-cofactor theorem succeeds because a source-defined nonshared sector has posterior `theta=1/2`, so data processing of (2.1) keeps the rare `d log(1/d)` payment.

The first missing Shannon implication was therefore the hoped-for Boolean statement:

> whenever (2.3) is dangerous at fixed finite `C`, Boolean realizability forces some source-defined sector with posterior bounded away from the global rare value `d`, or at least forces `I(S;J)` to carry the missing `d log(1/d)` scale.

The construction below refutes this implication in the strongest possible posterior form.

## 3. Genuine Boolean bent-carrier one-point suspension

Let `m=2r` be even. On

\[
x=(u,v)\in\mathbb F_2^r\times\mathbb F_2^r
\]

define the standard quadratic bent sign

\[
b(u,v)=(-1)^{u\cdot v}.
\tag{3.1}
\]

Its normalized Walsh coefficients are

\[
\widehat b(A,B)=2^{-r}(-1)^{A\cdot B}.
\tag{3.2}
\]

Put

\[
d=2^{-m},\qquad s=2^{-r}=\sqrt d,
\qquad \sigma_R=(-1)^{A\cdot B}.
\tag{3.3}
\]

Add one fresh unbiased physical bit `y` and define two actual Boolean restrictions

\[
f_0(y,x)=\chi_y b(x),
\tag{3.4}
\]

\[
h(x)=1-2\mathbf 1_{\{x=0\}},\qquad
f_1(y,x)=f_0(y,x)h(x).
\tag{3.5}
\]

Both restrictions are balanced because every Fourier mode contains the fresh character `chi_y`. They disagree exactly when `x=0`, hence

\[
\Pr[f_0\ne f_1]=d=2^{-m}.
\tag{3.6}
\]

For the residual frequency `R=(A,B)`, (3.2) and the single physical point flip give

\[
\boxed{a_R=\sigma_R s,\qquad b_R=\sigma_Rs-2d.}
\tag{3.7}
\]

No projection-integrality assumption is used.

## 4. Every posterior is rare; total vertical KL is `O(d^2)`

From (3.7),

\[
T_R=dA_{\sigma_R},\qquad
A_\sigma:=1-2\sigma s+2d,
\tag{4.1}
\]

while the within-pair odd-layer mass is independent of `R`:

\[
z_R=d^2.
\tag{4.2}
\]

Therefore

\[
\boxed{\theta_R={d\over A_{\sigma_R}}.}
\tag{4.3}
\]

For `m>=4`, `s<=1/4`, so

\[
{5\over8}\le A_\sigma\le {13\over8}.
\tag{4.4}
\]

Consequently every Fourier mode satisfies the uniform posterior collar

\[
\boxed{{8\over13}d\le\theta_R\le {8\over5}d.}
\tag{4.5}
\]

Thus there is literally no high-posterior spectral sector: every atom has posterior comparable to the tiny global disagreement.

More quantitatively,

\[
|1-A_\sigma|\le2s+2s^2\le{5\over2}s,
\]

and (4.4) gives

\[
\boxed{|\theta_R-d|\le4ds.}
\tag{4.6}
\]

For Bernoulli laws, base-two KL is bounded by chi-squared divergence:

\[
D_{\rm KL,2}(\operatorname{Bern}(p)\|\operatorname{Bern}(q))
\le { (p-q)^2\over q(1-q)\ln2}.
\tag{4.7}
\]

Using `s^2=d`, `d<=1/16`, and (4.6), every summand in (2.1) is at most `40 d^2`. Since the `T_R` sum to one,

\[
\boxed{I(S;J)\le40d^2\qquad(m\ge4).}
\tag{4.8}
\]

In particular every sector/data-processed KL lower bound is also at most `40d^2`. No partition of the Fourier modes can recover a `d log(1/d)` payment from the vertical KL on this family.

This is the rigorous obstruction that changes the B15 sector bridge.

## 5. Exact near-isoclinic and sign-coherent angular state

The account01/B16 angular variable is

\[
c_R={2a_Rb_R\over a_R^2+b_R^2}
={1-2\sigma_Rs\over1-2\sigma_Rs+2d}
=1-2\theta_R.
\tag{5.1}
\]

For `m>=4`, every numerator is positive. Thus all `c_R>0`: the family is exactly sign coherent.

Moreover

\[
E_T\theta_R=d,
\]

so

\[
E_Tc_R=1-2d=:\rho.
\tag{5.2}
\]

Hence the account01/B16 absolute-coherence defect

\[
A:=E_T|c_R|-|\rho|
\]

vanishes **exactly**:

\[
\boxed{A=0.}
\tag{5.3}
\]

Finally, by (4.6),

\[
\operatorname{Var}_T(c_R)
=4\operatorname{Var}_T(\theta_R)
\le64d^3.
\tag{5.4}
\]

Therefore the completed account01/B16 Boolean-rigidity addendum is compatible with this family—equality is not attained—but its quantitative rigidity gap can be arbitrarily small. A genuine Boolean near-isoclinic/coherent corridor does exist.

## 6. Full exact local Shannon credit still cannot pay without child slack

The branch posterior at a mode of sign `sigma` is

\[
\Pr[B=1\mid S,R]
={1-4\sigma s+4d\over2A_\sigma}.
\tag{6.1}
\]

We do not need to discard its exact value. The elementary upper bound `H(B|S)<=1`, together with (4.8), gives from (2.3)

\[
\mathcal L_C
\le Cd-h_2(d)+40d^2.
\tag{6.2}
\]

Since

\[
h_2(d)\ge d\log_2(1/d)=md,
\]

we obtain the decisive estimate

\[
\boxed{\mathcal L_C\le d\,[C-m+40d].}
\tag{6.3}
\]

For every fixed finite `C`, the right side is negative for all sufficiently large even `m`. Thus:

\[
\boxed{
\text{No universal zero-child-subsidy local Shannon payment can hold at every balanced Boolean pivot,}
}
\]

even when the *entire* branch entropy and the *entire* exact vertical relative-entropy credit are retained.

At the live numerical center `C^dagger=6.521851214`, (6.3) is already negative for every even `m>=8`.

This is not a counterexample to the all-gate inequality or to FEI. It is a counterexample to the first missing local Shannon implication described in section 2.

## 7. The same family is paid strongly by the child defects

The obstruction disappears once the exact child slack demanded by the owner is retained.

For `f_0`, the spectral law is uniform on the `2^m` frequencies containing `y`. Hence

\[
H(f_0)=m=2r,
\qquad I(f_0)-1=r,
\]

and therefore

\[
\boxed{D_C(f_0)=r(C-2).}
\tag{7.1}
\]

For `f_1`, (3.7) gives spectral masses

\[
p_R=(\sigma_Rs-2d)^2
=d-4\sigma_Rd^{3/2}+4d^2.
\tag{7.2}
\]

The bent sign satisfies the exact first-moment cancellation

\[
\sum_R |R|\sigma_R=0.
\tag{7.3}
\]

Indeed each coordinate indicator forces one nonzero half of `A` or `B`, and summing the character `(-1)^{A\cdot B}` over the opposite block gives zero. Since

\[
\sum_R|R|=2^m r,
\]

(7.2)-(7.3) yield

\[
\boxed{I(f_1)-1=r(1+4d).}
\tag{7.4}
\]

The spectrum of `f_1` has at most `2^m` atoms, so

\[
H(f_1)\le m=2r.
\]

Consequently

\[
\boxed{D_C(f_1)\ge r(C-2).}
\tag{7.5}
\]

Finally, from (2.3) and nonnegativity of both exact information credits,

\[
\mathcal L_C\ge Cd-1-h_2(d)\ge-2.
\tag{7.6}
\]

Combining (2.2), (7.1), (7.5), and (7.6),

\[
\boxed{
D_C(f)
\ge r(C-2)-2.
}
\tag{7.7}
\]

Thus for every `C>=4` and every even `m>=2`, this whole near-isoclinic family is globally safe under the exact two-child cocycle. The same source that makes the local Shannon payment fail carries a large positive child support-deficit reserve.

This is a concrete, source-exact instance of the owner's warning that blind arity/restriction induction fails only when child slack is discarded.

## 8. Exact replacement obligation

The high-posterior-sector route is now exhausted as a universal local mechanism. Any next proof must preserve a child-slack or stopped-block reserve.

At a balanced pivot, the source-exact next implication has the form

\[
\boxed{
{D_{\Gamma^\dagger}(f_0)+D_{\Gamma^\dagger}(f_1)\over2}
+H(B\mid S)+I(S;J)
\ge
[-\mathcal R_{\Gamma^\dagger,j}]_+,
}
\tag{8.1}
\]

or an aggregate/stopped-tree variant whose right side is the same exact local deficit. Proving (8.1) pointwise may still be stronger than necessary; account03/B13 already warns that a whole-tree weighted payment can be the correct object. What is no longer viable is replacing the left side by the information credits alone.

For the present extremal family, sections 4-7 prove exactly why: the information part is too small at the rare scale, while the children have order-`r` positive slack.

The universal all-gate inequality `(G)` and unrestricted FEI remain open.

## 9. Essential checks and finite scope

`check_bent_nearisoclinic.py` performs two types of checks.

First, for `r=1,2,3,4` it reconstructs the bent truth table and integer Walsh transform and verifies exactly (using Python `Fraction` where needed): flat Walsh magnitude, the physical one-point update `W_1=W_0-2`, the sign counts, spectral normalization, and (7.4).

Second, for even `m=2,...,20` it evaluates the closed formulas numerically. At `C^dagger` the first analytic-certified negative local upper bound occurs at `m=8`:

\[
\mathcal L_{C^\dagger}=-0.0226107151382\ldots,
\qquad
d(C^\dagger-m+40d)=-0.00516366713281\ldots.
\]

At `m=20`, the exact-formula evaluation has

\[
I(S;J)=2.62424\times10^{-12},
\qquad
\mathcal L_{C^\dagger}=-1.69813\times10^{-5}.
\]

These finite computations are implementation sanity checks only. The posterior collar (4.5), KL bound (4.8), local obstruction (6.3), and child payment (7.7) are analytic for the whole stated family.

## 10. Literature and priority

No novelty or priority claim is made from this repository search. The current FEI README continues to mark unrestricted FEI open and separately warns that dyadic Fourier coefficients do not imply integral physical magnitude projections. Recent work visible to this run gives structured-class or partial progress rather than a general proof. The present report is therefore an internal proof/obstruction handoff only.

## 11. Status

- `FULL-PROBLEM CHANGE`: `OPEN -> OPEN`.
- `MECHANISM CHANGE`: `local high-posterior sector-KL rescue -> genuine Boolean near-isoclinic/coherent obstruction + exact child-slack compensation`.
- `OTHER-ACCOUNT RESULT CONSUMED`: account01/B16 balanced-pivot joint-credit plus dyadic-rigidity addendum; account03/B13 is explicitly respected as prior broader pointwise-local obstruction.
- `FIRST MISSING SHANNON IMPLICATION`: local Booleanity forcing a `d log(1/d)` vertical-KL payment is false.
- `NEW EXACT OBLIGATION`: retain child defects and prove a two-generation/aggregate information-plus-slack payment such as (8.1), or the all-gate equivalent, with no loss of the negative credits.
- `FULL FEI`: **OPEN / NOT PROVED**.
