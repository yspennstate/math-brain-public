SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-23T22:01:20Z.
attacking: QFORM-FINITECORE-EXTRA-SPECTRUM-INDUCTIVE-DESCENT-v1 — remove arbitrary additional-spectrum duplication from the rank-six retained-error debt by exact original-bank conditioning and strong induction, then isolate the base-subcritical carrier.

# account03/B19 r43 — principal-minimal descent and removal of arbitrary extra-spectrum debt

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **NEW TARGET-LEVEL REDUCTION / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **OPEN for the full target.** The descent below proves the essential-density reduction only; it does not claim a new continuity theorem.

## 1. Exact target and source boundary

The target remains exactly the owner statement. The original coordinates are independent real random variables with one-dimensional probability densities bounded by one. The coefficient matrix `A=A^T` is arbitrary and has at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, iid, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced.


The immediate finite-core input is account03/B20 r39,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T214857Z-account03-B20-QFORM-r39/REPORT.md`.

It proves that every still-unpaid state in that finite-core branch has an ORIGINAL-coordinate partition `H disjoint_union L`, with `|H|<=124`, and

`A[H,H]=L_H+E_H`, `rank(L_H)<=2`, `||E_H||_op<0.000370786548`,

`A[H,L]=C_2+R_C`, `rank(C_2)<=2`, `||R_C||_op<1/64`,

while `A[L,L]` is retained exactly. Equivalently

`A=diag(0_H,A[L,L])+K+E`, `rank(K)<=6`, `||E||_op<0.015995786548`.

No probabilistic argument is allowed to discard `E`. The first debt left there was to pay the rank-six carrier over an arbitrary `L`-bank base and arbitrary additional spectrum.

This run proves that the phrase **arbitrary additional spectrum above the target threshold** can be removed exactly from that local debt. The mechanism is not a perturbation estimate: it is original-coordinate conditioning plus strong induction at exactly the same threshold `1`.

## 2. Affine principal-minimal class

For a real symmetric matrix `M`, define

`N_M(1)=#{eigenvalues lambda of M : |lambda|>=1}`,

counting multiplicity.

Call an `n x n` target matrix `A` **principal-minimal at threshold 1** if

1. `N_A(1)>=3`, and
2. every proper ORIGINAL-coordinate principal submatrix `A[I,I]`, `I proper subset {1,...,n}`, satisfies `N_{A[I,I]}(1)<=2`.

Because conditioning original coordinates creates affine terms, the correct inductive class is the affine strengthening

`Q_{A,b,c}(X)=X^T A X+b^T X+c`.

The inputs remain independent cap-one originals. This is a stronger statement than the homogeneous owner target, but it is exactly the strength required by source-preserving conditioning. All signs and all eigenvalue degeneracies are allowed.

## 3. Main theorem: same-constant descent to principal-minimal matrices

### Theorem 3.1 — `QFORM-PRINCIPAL-MINIMAL-INDUCTIVE-REDUCTION-v1`

Assume there is one finite constant `C_*` with the following property:

> For every dimension `n>=3`, every principal-minimal real symmetric `A`, every deterministic affine vector `b` and constant `c`, and every independent cap-one product input, the law of `Q_{A,b,c}` satisfies the interval bound
>
> `P(Q_{A,b,c} in I) <= C_* |I|`
>
> for every bounded interval `I`.

Then **the same constant `C_*`** satisfies the identical interval bound for every real symmetric `A` with `N_A(1)>=3`, in every dimension, with arbitrary affine terms. Consequently the homogeneous owner target has an essentially bounded density with `||p_Q||_infinity<=C_*`.

There is no multiplicative induction loss.

### Proof

Use strong induction on `n`.

For `n=3`, every target matrix is principal-minimal because no proper principal submatrix can have three eigenvalues. Hence the hypothesis gives the conclusion.

Now let `n>3`, and suppose the conclusion is known in every lower dimension. If `A` is principal-minimal, apply the assumed bound directly.

Otherwise there is a proper original-coordinate set `L` such that

`D:=A[L,L]`

has `N_D(1)>=3`. Let `H=L^c`, so `H` is nonempty. Write the exact block decomposition

`A=[[B,C],[C^T,D]]`,
`b=(b_H,b_L)`.

Condition on the ORIGINAL variables `X_H=h`. No rotation or conditional-density estimate is used. The remaining coordinates `X_L` are still independent with exactly their original one-dimensional density caps. The conditional output is

`Q | (X_H=h)
 =X_L^T D X_L
  +(2 C^T h+b_L)^T X_L
  +[h^T B h+b_H^T h+c]`.

Thus its quadratic matrix is the exact principal submatrix `D`, while every coefficient involving the conditioned bank appears only in the deterministic affine/constant part. Since `|L|<n` and `N_D(1)>=3`, the strong induction hypothesis gives, uniformly for every value of `h`,

`P(Q in I | X_H=h) <= C_* |I|`.

Average over `h`:

`P(Q in I)=E[P(Q in I | X_H)] <=C_* |I|`.

The interval domination implies absolute continuity and an essential density bound `C_*` by the Radon-Nikodym theorem. This completes the induction. QED.

### Important scope point

The proof retains **every** coefficient of the actual matrix. In particular it is valid when `B` and `C` contain the nonzero r39 error terms `E_H` and `R_C`; after conditioning `H`, they simply enter the constant and affine vector. No claim that a small coefficient gives a small random variable is made.

## 4. Spectral consequence: an irreducible target has only three or four large eigenvalues

The reduction has a useful exact consequence that removes a large amount of duplicate casework.

Let the eigenvalues of `A` be ordered decreasingly, and put

`p=#{lambda_j(A)>=1}`, `q=#{lambda_j(A)<=-1}`.

For any one-coordinate deletion `A^(i)`, Cauchy interlacing gives

`p_i>=max(p-1,0)`,
`q_i>=max(q-1,0)`.

Therefore:

### Corollary 4.1 — `QFORM-PRINCIPAL-MINIMAL-SPECTRAL-COUNT-v1`

If `A` is principal-minimal, then

`3 <= N_A(1)=p+q <=4`.

Moreover, if `N_A(1)=4`, the four threshold-large eigenvalues must have mixed signs. Equivalently the only possible sign counts are

`(p,q)=(3,0),(2,1),(1,2),(0,3)` when `N=3`,

and

`(3,1),(2,2),(1,3)` when `N=4`.

#### Proof

If `p+q>=5` and both signs occur, then every one-coordinate deletion has

`N_{A^(i)}(1)>= (p-1)+(q-1)=p+q-2>=3`,

contradicting principal minimality. If all threshold-large eigenvalues have one sign, then every deletion has at least `p-1` or `q-1`; for total count at least five this is at least four and again contradicts minimality.

If `p+q=4` and all four have one sign, interlacing gives at least three threshold-large eigenvalues in every deletion, again a contradiction. Hence count four is necessarily mixed. QED.

This handles repeated eigenvalues and eigenvalues exactly equal to `+1` or `-1`: interlacing is non-strict and the recursive threshold is also non-strict.

A particularly useful formulation is:

* every matrix with at least five eigenvalues of modulus at least one is dimension-reducible immediately;
* every matrix with four such eigenvalues of one sign is dimension-reducible immediately;
* a genuinely irreducible analytic proof only needs `N_A(1)=3` or a mixed-sign `N_A(1)=4` state.

## 5. Actual splice into the r39 rank-six retained-error state

Return to the current finite-core state from account03/B20 r39. The partition `H disjoint_union L` is physical and `H` is nonempty. Put

`D=A[L,L]`.

If

`N_D(1)>=3`,

Theorem 3.1 says there is **no new rank-six carrier analysis to do at this dimension**: condition the actual `H` variables and descend to the lower-dimensional affine QFORM problem with matrix `D`. This keeps the exact cross block `C_2+R_C`, the exact self block `L_H+E_H`, every sign, and every rough input law.

Therefore any inductively minimal unpaid r39 carrier automatically satisfies the exact base-subcritical condition

`boxed: N_{A[L,L]}(1)<=2.`

At the same time Corollary 4.1 allows the full matrix to be assumed to have only three threshold-large eigenvalues, or four with mixed signs.

This is the main assembly gain of the run. The previous first missing implication

`QFORM-FINITECORE-RANK6-CARRIER-WITH-RETAINED-ERROR-PAYMENT-v1`

can be sharpened to

`QFORM-PRINCIPALMINIMAL-RANK6-CARRIER-BASESUBCRITICAL-PAYMENT-v1`:

> Pay only the retained-error r39 carrier states for which the untouched physical base `A[L,L]` has at most two eigenvalues of modulus at least one, and the full matrix has exactly three threshold-large eigenvalues or four of mixed sign. Any state with three target-scale modes already living in `L` is removed by exact same-constant dimension descent.

This does **not** delete arbitrary subthreshold spectrum of `A[L,L]`; eigenvalues may accumulate arbitrarily close to `+1` or `-1`. That near-threshold regime remains part of the analytic debt, and no reciprocal spectral gap may be inserted silently.

## 6. Designated partner account04/B19 applied at an actual inequality

The designated partner source is account04/B19 r2,

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

Its proved exact-null-coloop / residual-diffuse theorem states, in its stated scope,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`, `0<D_res<=1`,

with a continuous density.

Apply it at the actual threshold

`2^(-40) <= D_res <=1`.

Then

`||p_Q||_infinity
 <34 sqrt(log(e 2^40))
 =182.228224... <183.`

This is only a paid branch in the exact partner scope. It is not extended to a near-null coloop, arbitrary joint density, or the general r39 carrier.

## 7. Finite checks

A deterministic regression script accompanies this report. It generated random orthogonal conjugates in dimensions `5` through `12`, with either at least five threshold-large eigenvalues or four same-sign threshold-large eigenvalues, deleted every physical coordinate, and checked the interlacing consequence numerically. Across `20,400` deletions there were zero violations; the minimum observed threshold-large count after deletion was `3`.

The same checker evaluates the partner threshold as

`34 sqrt(log(e 2^40)) =182.228224018926`.

These computations are only checks. The proof of Theorem 3.1 and Corollary 4.1 is exact and does not depend on random testing.

## 8. Conditional end-to-end position after this run

The current assembly is now compact:

1. All already-paid physical-pair, physical-triple, grouped-crossing, diagonal, ridge, common-plane and null-coloop branches retain their exact scopes.
2. Account03/B20 r39 closes the pairwise-weak finite `H` self bank into an actual rank-at-most-six carrier plus a retained coefficient error `<0.015996`, or pays the law explicitly.
3. This run removes any carrier state whose untouched `L` principal block already contains three target-scale modes, with **no constant loss** and without touching the retained error.
4. Hence the first local analytic debt is the principal-minimal, base-subcritical rank-six carrier: `N_{A[L,L]}(1)<=2`, full `N_A(1)=3` or mixed-sign `4`, arbitrary subthreshold extra spectrum, arbitrary fragmented/unbounded product laws, and the genuine nonzero collar retained.

The unrestricted conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is still **OPEN**. The new result proves a target-level reduction for essential boundedness; it does not by itself produce the final universal constant.

## 9. Next mathematical attack

The next mechanism should use the strict structural fact `N_{A[L,L]}(1)<=2` rather than treating the `L` bank as an arbitrary additional-spectrum adversary. In particular, a valid receiver may spend the third (or fourth mixed-sign) threshold crossing created by the `H` self/cross carrier against the two-mode-or-less base, but must remain uniform as subthreshold eigenvalues of `A[L,L]` approach `+1` or `-1`. A proof that divides by the distance of `s_3(A[L,L])` from one is not sufficient.

Repository transport and native learned-memory ingestion remain distinct. No authenticated native brain retrieval/receiver use occurred, so execution remains `WITHOUT_VERIFIED_BRAIN`.
