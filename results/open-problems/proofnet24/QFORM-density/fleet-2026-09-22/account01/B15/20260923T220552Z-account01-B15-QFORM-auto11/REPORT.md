SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T22:05:52Z.
attacking: close the sign-definite rank-two physical-block endpoint by taking the partner ruled one-sheet theorem through a vanishing minority-curvature limit, then identify exactly when the resulting bounded receiver upgrades to a continuous full density.

# account01/B15 — minority-null endpoint closure for semidefinite rank-two physical blocks

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T220552Z-account01-B15-QFORM-auto11`  
Status: `SUPPORTING_LEMMA_PROVED / PARTNER_RESULT_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result in one sentence

The latest account02/B15 sign-sensitive ruled theorem can be closed all the way to a **singular physical block** when the disappearing curvature is the minority sign: a rank-two positive- or negative-semidefinite original-coordinate `3x3` principal block with two nonzero eigenvalue magnitudes `lambda1,lambda2` still gives the full quadratic output the measure bound

`P(Q in E) <= [2 pi/sqrt(lambda1 lambda2)] |E|`

provided the outside cross block lands in the range of that singular block. This is a genuine endpoint theorem: no reciprocal smallest singular value appears. In the original-coordinate block-diagonal case, any nonconstant independent quadratic remainder upgrades the same bounded receiver to a `C_0` density with **no loss in the height constant**.

The full owner conjecture remains open because the three-large-eigenvalue hypothesis alone does not force such a semidefinite rank-two range-aligned physical block.

## 2. Live premises and corrections retained

Fresh control commit at start: `yspennstate/math-research-brain@2469404e0673496b98e61fff8a240f0bcbae258a`; programme revision `2026-09-22.5`, owner control revision `2026-09-22.15`.

The designated partner source is

`yspennstate/math-open-problems@fe25e77b5832eb0af6db6d1b01b6c93041aff88b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T212432Z-account02-B15-QFORM-auto11b/REPORT.md`.

The partner theorem used below is the completed ruled majority/one-sheet estimate. If an invertible original-coordinate physical `3x3` block has signature `(2,1)`, with majority positive eigenvalue magnitudes `lambda1,lambda2>0` and minority magnitude `mu>0`, then after conditioning on all outside original coordinates the positive-majority submeasure obeys

`nu_+(E) <= C_+(lambda1,lambda2,mu)|E|`,

where

`C_+ = int_0^(2pi) [lambda2 mu sin^2(theta)+lambda1 mu cos^2(theta)+lambda1 lambda2]^(-1/2) dtheta`

and in particular

`C_+ <= 2 pi/sqrt(lambda1 lambda2)`.

The key sign-sensitive fact is that this last bound is independent of the minority curvature `mu`. The negative-majority statement follows by changing the sign of the quadratic form.

I retain the live corrections: no law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; no generic projection/X-ray shortcut for the minority/two-sheet term; no arbitrary-joint coarea height theorem; and the latest B15 affine-slope correction, which rules out using a large linear term to remove the cost of a nonzero small square curvature at a one-coordinate receiver.

## 3. New theorem: semidefinite physical-block endpoint

### Theorem A (minority-null endpoint, measure form)

Let the independent random vector be split in the **original coordinate system** as

`X=(U,W)`, `U in R^3`, `W in R^(n-3)`,

with every coordinate possessing a probability density bounded by one. Write the symmetric matrix in the same physical partition as

`A = [[B,C],[C^T,D]]`.

Assume:

1. `B` is positive semidefinite of rank two;
2. its two positive eigenvalues are `lambda1,lambda2>0`;
3. `Range(C) subset Range(B)`.

Then the complete output

`Q=X^T A X`

satisfies, for every Borel set `E subset R`,

`boxed( P(Q in E) <= [2 pi/sqrt(lambda1 lambda2)] |E|. )`                              (3.1)

Equivalently, `Q` has a density and

`boxed( ||p_Q||_infinity <= 2 pi/sqrt(lambda1 lambda2). )`                              (3.2)

The same statement holds when `B` is negative semidefinite of rank two, with `lambda1,lambda2` denoting the magnitudes of its two nonzero eigenvalues.

Thus if `lambda1,lambda2>=kappa`,

`boxed( ||p_Q||_infinity <= 2 pi/kappa. )`                                               (3.3)

This theorem permits arbitrary outside quadratic curvature `D` and arbitrary physical cross coupling `C` subject only to the exact range-alignment condition. It does not rotate the source.

### Proof

It is enough to treat the positive-semidefinite case. Let `n_0` be a unit vector spanning `ker B`. Since `B` is symmetric,

`Range(B)=(ker B)^perp=n_0^perp`.

For `eps>0`, define the invertible physical block

`B_eps = B - eps n_0 n_0^T`.                                                            (3.4)

Its eigenvalues are exactly `lambda1,lambda2,-eps`, so it has signature `(2,1)`. Keep the same cross block and outside block and put

`A_eps = [[B_eps,C],[C^T,D]]`,
`Q_eps=(U,W)^T A_eps(U,W)`.

The product input law is unchanged. In particular no independence is asserted in an eigenbasis of `B` or `B_eps`.

Condition on `W=w` and put

`d(w)=Cw`, `c_0(w)=w^T D w`.

By `Range(C) subset Range(B)`, one has `d(w) in Range(B)` for every `w`. Define

`b(w)=B^dagger d(w)`,

where `B^dagger` is the Moore-Penrose inverse. Then `b(w) in Range(B)` and hence `n_0^T b(w)=0`. Moreover

`B b(w)=d(w)`.

Because `B_eps` agrees with `B` on `Range(B)`,

`B_eps b(w)=d(w)`,

and therefore

`B_eps^(-1)d(w)=b(w)`                                                                  (3.5)

for every `eps>0`. This is the exact reason the affine center does **not** run off to infinity as the minority curvature disappears.

Set

`c_*(w)=c_0(w)-d(w)^T B^dagger d(w)`.

Using (3.5), the conditional quadratic is

`Q_eps(U,w)`
` = (U+b(w))^T B_eps (U+b(w)) + c_*(w).`                                                (3.6)

The critical level `c_*(w)` is independent of `eps`.

Apply the completed account02/B15 ruled theorem to this same original-coordinate active triple. Its positive-majority submeasure, conditionally on `W=w`, is

`nu_(eps,w)^+(E)`
` = P(Q_eps(U,w) in E, Q_eps(U,w)>=c_*(w) | W=w)`.

Since the two majority eigenvalues of `B_eps` are precisely `lambda1,lambda2`, the partner sign-sensitive estimate gives

`nu_(eps,w)^+(E)`
` <= [2 pi/sqrt(lambda1 lambda2)] |E|`                                                   (3.7)

for every Borel `E`, uniformly in `w` and uniformly in `eps>0`. Averaging in the untouched outside variable yields the global positive submeasure

`nu_eps^+(E)=P(Q_eps in E, Q_eps>=c_*(W))`

with the same domination

`nu_eps^+(E) <= C_0 |E|`,
`C_0=2 pi/sqrt(lambda1 lambda2).`                                                        (3.8)

We now pass to the singular endpoint. From (3.6),

`Q_eps-c_*(W)`
` = (U+b(W))^T B(U+b(W)) - eps [n_0^T(U+b(W))]^2`.

Because `n_0^T b(W)=0`, this is

`Q_eps-c_*(W)`
` = (U+b(W))^T B(U+b(W)) - eps (n_0^T U)^2.`                                            (3.9)

Pointwise,

`Q_eps -> Q_0:=X^TAX`.

Also

`(U+b(W))^T B(U+b(W)) >=0`.

The zero set of this nonnegative rank-two quadratic is

`{U+b(W) in ker B}`,                                                                    (3.10)

which, for every fixed `W=w`, is one affine line in `R^3`. The active product law is absolutely continuous with respect to three-dimensional Lebesgue measure, so (3.10) has conditional probability zero; Fubini gives joint probability zero. Therefore

`1_{Q_eps>=c_*(W)} -> 1` almost surely.                                                  (3.11)

For every bounded continuous test function `phi`, dominated convergence gives

`int phi(t) d nu_eps^+(t)`
` = E[phi(Q_eps) 1_{Q_eps>=c_*(W)}]`
` -> E phi(Q_0).`                                                                        (3.12)

Thus `nu_eps^+` converges weakly to the **full** law `mu_0=L(Q_0)`.

Let `G` be any bounded open interval. By Portmanteau and (3.8),

`mu_0(G) <= liminf_(eps->0) nu_eps^+(G) <= C_0 |G|.`                                    (3.13)

Outer regularity extends (3.13) to every Borel set `E`. Hence `mu_0<=C_0 dt`, proving (3.1)-(3.2).

For negative-semidefinite `B`, apply the positive-semidefinite result to `-Q`; reflection preserves density height. QED.

## 4. Exact owner-scale corollaries

### 4.1 Fixed tent

For

`T_r(y)=E[(r-|Q-y|)_+]`,

Theorem A implies

`T_r(y) <= C_0 int_(-r)^r (r-|t|)dt = C_0 r^2`,

so

`boxed( E[(r-|Q-y|)_+] <= [2 pi/sqrt(lambda1 lambda2)] r^2. )`                           (4.1)

At the fixed owner scale `r=1`, the entire output is therefore already paid by the same unit-tent functional used in the scale-homogeneous formulation of QFORM.

### 4.2 Exact three-large-eigenvalue branch

If, in addition, the two nonzero eigenvalues of the physical semidefinite block satisfy

`lambda1,lambda2>=1`,

then

`boxed( ||p_Q||_infinity <= 2 pi. )`                                                     (4.2)

If the whole matrix has a third eigenvalue of modulus at least one elsewhere, this is an exact branch of the owner's three-large-eigenvalue target. No lower bound on the zero physical-block eigenvalue is needed—there is no reciprocal-minor blow-up at this endpoint.

The important structural condition is the range alignment

`Range(A_(S,S^c)) subset Range(A_(S,S))`.                                                (4.3)

The bare three-large-eigenvalue hypothesis does not force a physical triple satisfying (4.3), so (4.2) is a completed branch rather than a full solution.

## 5. Why this endpoint is genuinely sign-sensitive

The theorem closes exactly the endpoint where the disappearing eigenvalue is the **minority sign** of a nearby invertible ruled triple. This is not a generic singular-block closure.

If a rank-two limit is indefinite, with one positive and one negative nonzero eigenvalue, then whichever sign is assigned to a small third eigenvalue, that small eigenvalue becomes one of the **majority-sign** pair in the resulting rank-three signature. The latest account02/B15 target-valid family shows that this opposite endpoint can carry a real logarithmic loss:

`Q_gamma=2XY+gamma Z^2+W^2`,

for iid `Uniform[-1/2,1/2]` variables and `0<gamma<=1`. The active triple `(X,Y,Z)` has eigenvalues `{1,-1,gamma}`. Conditioning on `W`,

`R_gamma=2XY+gamma Z^2`

has the exact peak

`p_(R_gamma)(0)=2+log(2/gamma)`,                                                        (5.1)

which diverges as the positive majority curvature `gamma` tends to zero. Yet the full target law remains uniformly bounded by routing the outside square before taking a conditional supremum.

Thus:

- semidefinite rank-two endpoint = minority-null collar = finite one-sheet constant and Theorem A closes to the full law under range alignment;
- indefinite rank-two endpoint = majority-null collar = a logarithmic selected-triple loss is real and cannot be removed by simply taking the singular limit.

This distinction is mathematical, not an artifact of the crude `1/sigma_min` bound.

## 6. Bounded density still does not mean continuous density

Theorem A is deliberately an essential-boundedness theorem. The singular receiver itself can have a bounded density with a genuine jump.

Take

`B=diag(1,1,0)`

and `X_1,X_2` iid `Uniform[-1/2,1/2]`; `X_3` may be any independent cap-one variable. Put

`U=X_1^2+X_2^2`.

For a single square,

`p_(X_i^2)(s)=s^(-1/2) 1_(0,1/4)(s)`.

Hence for `0<t<1/4`,

`p_U(t)=int_0^t [s(t-s)]^(-1/2) ds = pi,`                                               (6.1)

while `p_U(t)=0` for `t<0`. Therefore the law has a bounded density, but no continuous representative at zero. In particular, even on this very regular physical receiver,

`bounded density != continuous density.`                                                (6.2)

This is not a counterexample to the owner's full continuity question because this receiver has only two nonzero eigenvalues. It is instead a precise warning that continuity cannot be inferred from the local height certificate itself.

## 7. A no-loss continuity compiler when an independent remainder is retained

The preceding jump disappears as soon as an independent absolutely continuous remainder is convolved **after** the height is paid.

### Lemma B (independent AC convolution upgrades a paid receiver to `C_0`)

Let `Y` and `Z` be independent real random variables. Assume `Y` has a density `h` with

`h in L^1 cap L^infinity`, `||h||_infinity<=M`,

and `Z` has any density `g in L^1`. Then

`p_(Y+Z)=h*g in C_0(R)`

and

`boxed( ||p_(Y+Z)||_infinity <= M. )`                                                   (7.1)

Proof: `L^1*L^1 subset C_0`, while Young's inequality gives

`||h*g||_infinity <= ||h||_infinity ||g||_1=M`.

Thus continuity is an additional regularity conclusion obtained from a separate independent smoothing source, with zero loss in the already-established height constant.

### Lemma C (nonconstant quadratic remainder is absolutely continuous)

If a random vector has an absolutely continuous joint law and `R(v)=v^T Dv` with `D!=0`, then `R(V)` is absolutely continuous. Under the product setting this can be seen entirely in original coordinates. If some diagonal `D_ii!=0`, condition on the other coordinates; the remaining map in `V_i` is a nonconstant quadratic. If all diagonals vanish, choose `D_ij!=0`; after conditioning on all variables except `V_i`, the slope is a nonconstant affine function of the absolutely continuous variable `V_j`, hence is nonzero almost surely. The one-dimensional pushforward is then absolutely continuous, and averaging the conditional laws proves the claim.

### Corollary D (block-diagonal exact-target continuity branch)

Suppose in original coordinates

`A=B direct_sum D`,

where `B` is a `3x3` rank-two positive- or negative-semidefinite block with nonzero eigenvalue magnitudes `lambda1,lambda2`, and `D!=0`. Then

`Q=U^TBU + W^TDW`

is a sum of independent random variables. By Theorem A the first summand has a bounded density `h` with

`||h||_infinity <= 2 pi/sqrt(lambda1 lambda2)`,

and by Lemma C the second summand has a density `g in L^1`. Lemma B therefore gives

`boxed( p_Q in C_0(R),`  
`       ||p_Q||_infinity <= 2 pi/sqrt(lambda1 lambda2). )`                               (7.2)

If `lambda1,lambda2>=1` and `D` has an eigenvalue of modulus at least one, then `A` has at least three eigenvalues of modulus at least one. Consequently

`boxed( p_Q in C_0(R), ||p_Q||_infinity <= 2 pi )`                                      (7.3)

for this exact full-target branch.

This is a clean separation of roles:

- The height constant is supplied by the rank-two semidefinite physical receiver through the partner ruled theorem and its minority-null endpoint closure.
- Continuity is supplied afterward by an independent absolutely continuous remainder.
- No continuity input is used in proving the height.

## 8. Relation to the full target

The new endpoint eliminates one common artificial singularity: if a good physical triple loses only its minority curvature and its cross block remains in the range of the limiting rank-two block, one must **not** pay `1/sigma_min(B)`; the correct endpoint price is at most

`2 pi/sqrt(lambda1 lambda2)`.

Therefore a full structural compiler may safely route such minority-null triples to Theorem A. The still-unpaid configurations are those where:

1. no physical triple exposes two same-sign curvatures of target scale;
2. the limiting physical block is indefinite rank two, where the partner logarithmic example shows real majority-null loss; or
3. the null direction has non-range-aligned coupling to the outside variables, so the affine center in the `B_eps` approximation runs along the vanishing eigenvector and the simple endpoint limit above does not apply.

The latest B15 affine-slope correction says item 3 cannot be solved by pretending a large affine slope uniformly rescues a nonzero small square coefficient. A successful treatment must preserve the joint original-product geometry or route an outside smoothing resource before taking a worst conditional supremum.

## 9. Regularity ledger

For the owner's exact target the logically distinct statements remain:

- **Absolute continuity:** qualitatively much easier; a nonconstant quadratic applied to an absolutely continuous product law has an absolutely continuous output.
- **Universal essential boundedness:** the central open theorem. Theorem A pays the semidefinite rank-two range-aligned physical branch with the explicit constant `2pi/sqrt(lambda1 lambda2)`.
- **Continuous density:** stronger and separate. A paid receiver need not itself have a continuous representative, as (6.1) shows. In a block-diagonal target branch, an independent nonconstant quadratic remainder upgrades the paid receiver to `C_0` with no height loss by convolution.

Nothing here uses uniform pointwise quadratic Fourier decay, spectral-coordinate independence, or projection-only/X-ray control.

## 10. First unpaid implication after this run

The most precise next local problem is the **non-range-aligned null direction**. For a rank-two semidefinite physical block `B`, write `n_0` for its null vector and `C=A_(S,S^c)`. The new theorem closes the branch `n_0^T C=0`. The remaining endpoint has

`n_0^T C !=0`.

A useful full-target compiler would show that this failure itself creates an original-coordinate product-preserving smoothing receiver with a universal cost, or that it can be aggregated over many triples before inversion. One must not freeze the outside variable and take a supremum over the induced affine slope; the partner target-valid conditional-sup obstruction shows that worst-fiber conditioning can be arbitrarily lossy.

Full QFORM remains `OPEN_NOT_PROVED`.
