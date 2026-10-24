SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T16:47:47Z.
attacking: derive the exact q-dependent Hausdorff--Young marginal factor in the third-volume Fourier compiler, optimize it on a regular-simplex rank-four cross block, and compare with the projection-tail gate and account02/B04 support-defect exit.

# account01/B04 — exact q-dependent marginal factors for third-volume Fourier smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T164747Z-account01-B04-QFORM-auto11-r15`  
Status: `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The new theorem proves a continuous `C_0` density in its stated original-coordinate product-Fourier scope.

## 1. Source-pinned inputs and live corrections

The current owner control read this run is revision `2026-09-22.15`, QFORM-only. The slot assignment is product Fourier rearrangement, with designated partner account02/B04.

The analytic predecessor actually used is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its q-dependent third-volume proof gives the decoupling, determinant Brascamp--Lieb datum, and sharp Hausdorff--Young row estimate. This run does not replace the exact row/column factors by the generic `e^3` relaxation.

The designated partner result actually applied below is

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

from

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

The live correction set was refreshed. In particular, no law-uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint coarea bound, positive moment of worst conditional projection-density caps, worst-fiber supremum, or uniformly good single physical minor is used.

## 2. Exact q-dependent marginal-factor theorem

Let `I,J` be disjoint ORIGINAL-coordinate banks and `M=A[I,J]`. Let `w_(S,T)` be any probability law supported on positive physical `3x3` minors, with

`d_(S,T)=det(M[S,T])^2>0`.

Define row and column inclusion marginals

`alpha_i=sum_(S contains i,T) w_(S,T)`,

`beta_j=sum_(S,T contains j) w_(S,T)`,

and determinant/entropy currency

`G(w)=exp(sum_(S,T) w_(S,T) log(d_(S,T)/w_(S,T))).`

For `1<=q<3/2`, define

`R_q(w)=prod_i (1-alpha_i/q)^(-(q-alpha_i)/2)
          *prod_j (1-beta_j)^(-(1-beta_j)/2),`                 (2.1)

with the continuous value one at zero exponents.

### Theorem `QFORM-Q-EXACT-MARGINAL-FACTOR-v1`

Assume

`alpha_i<=q/2` for every constrained-side row.                 (2.2)

Then the full ambient quadratic form, allowing arbitrary within-bank measurable phases/quadratic curvature, arbitrary outside coefficients and couplings, and induced affine terms, satisfies

`boxed: ||p_Q||_infinity
 <= [3/((3-2q)sqrt(q))] R_q(w)^(1/3) G(w)^(-1/6).`             (2.3)

Moreover

`boxed: integral_R |phi_Q(t)|dt
 <= [6pi/((3-2q)sqrt(q))] R_q(w)^(1/3) G(w)^(-1/6),`           (2.4)

so the density has a continuous representative vanishing at infinity.

### Proof

The predecessor's original-coordinate decoupling gives

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(MD)_i)|`.               (2.5)

The weighted determinant AM--GM argument, valid for arbitrary `w`, gives the Gaussian BL determinant currency `G(w)` and hence BL constant at most

`G(w)^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2).`                           (2.6)

Use Jensen at power `q` exactly as in the predecessor. Because (2.2) implies `q/alpha_i>=2`, sharp Hausdorff--Young gives for each active row

`|| |psi_i(2t .)|^q ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2).`                           (2.7)

The powers of `alpha_i` cancel between (2.6) and (2.7). Since `sum_i alpha_i=3`, the remaining powers of `q` give `q^(-3/2)`. Keeping every marginal factor instead of bounding it by `e^3` yields

`E F_t^q
 <= q^(-3/2)(pi/|t|)^3 G(w)^(-1/2) R_q(w).`              (2.8)

Therefore

`|phi_Q(t)| <= min(1,K |t|^(-b)),`                            (2.9)

where

`b=3/(2q)>1`,

`K=[q^(-3/2) pi^3 G(w)^(-1/2) R_q(w)]^(1/(2q)).`              (2.10)

The transition point is

`T=K^(1/b)=pi q^(-1/2)G(w)^(-1/6)R_q(w)^(1/3).`               (2.11)

Exact integration gives

`integral_R min(1,K|t|^-b)dt
 =2T+2K integral_T^infinity t^-b dt
 =2bT/(b-1)
 =[6pi/((3-2q)sqrt(q))]R_q(w)^(1/3)G(w)^(-1/6).`              (2.12)

This proves (2.4), and Fourier inversion gives (2.3). The integrable characteristic function gives the `C_0` representative. QED.

### Consistency checks

Using `-(1-x)log(1-x)<=x` on both products gives `R_q(w)<=e^3`, so (2.3) recovers the predecessor's generic coefficient

`3e/[(3-2q)sqrt(q)]`.

At `q=1`, (2.1)--(2.4) reduce exactly to the preceding account01/B04 theorem `QFORM-Q1-EXACT-MARGINAL-FACTOR-v1`.

## 3. A dense regular-simplex rank-four block

Let

`u_0=5^(-1/2)(1,1,1,1,1)^T`,

and let `H` be the Householder orthogonal matrix sending `e_5` to `u_0`. Let `U` be the first four columns of `H`. Explicitly, with

`c=(5+sqrt(5))/20`,

we may write

`U_ij=delta_ij-c` for `1<=i,j<=4`,

`U_5j=1/sqrt(5)` for `1<=j<=4`.                               (3.1)

Every entry of `U` is nonzero. Since the fifth column of `H` is `u_0`,

`U^T U=I_4`,

`UU^T=I_5-(1/5)J_5`.                                         (3.2)

Set

`M=2U`.                                                        (3.3)

Thus the four nonzero singular values of `M` are all exactly two, and every physical row has leverage `4/5`.

For any physical three-row set `S`, (3.2) gives

`M_S M_S^T=4(I_3-(1/5)J_3)`.

Its eigenvalues are `4,4,8/5`, hence

`det(M_S M_S^T)=128/5`.                                      (3.4)

There are ten row triples, so

`E3(M)=10*(128/5)=256`.                                      (3.5)

## 4. Canonical volume marginals and the optimal canonical exponent

Use the canonical squared-minor law

`w_(S,T)=det(M[S,T])^2/E3(M)`.

Because every nonzero singular value squared is four, its third-volume spectral inclusion multiplier is

`p_j=4*e2(4,4,4)/256=3/4`.                                   (4.1)

The row marginal matrix is therefore

`W=(3/4)UU^T`,

so every physical row marginal is

`alpha_i=(3/4)*(4/5)=3/5`.                                   (4.2)

On the four-column side the right singular frame is the physical identity and every column marginal is

`beta_j=3/4`.                                                  (4.3)

The smallest admissible `q` for this canonical weight is therefore

`q=2 alpha_*=6/5`.                                            (4.4)

This is also the optimal exponent for this fixed canonical weight. Indeed, for fixed `a=3/5`,

`f(q)=((q-a)/2)log(q/(q-a))`

has derivative

`f'(q)=(1/2)[-log(1-a/q)-a/q]>0`,

while

`d/dq log[(3-2q)^(-1)q^(-1/2)]
 =2/(3-2q)-1/(2q)>0`

for `q>1/2`. The column factor is independent of `q`. Thus the right side of (2.3) strictly increases for `q>=6/5` with the canonical weight.

At `q=6/5`, each row factor in (2.1) is `2^(3/10)` and each column factor is `2^(1/4)`. Hence

`R_(6/5)=2^(5/2)=4sqrt(2)`.                                  (4.5)

Since the canonical law has `G=E3(M)=256`, (2.3) gives the exact all-product-law certificate

`boxed: ||p_Q||_infinity <= 5sqrt(15)/6
 =3.227486121839514... .`                                    (4.6)

Also

`boxed: integral |phi_Q(t)|dt <=5pi sqrt(15)/3
 =20.27889337986806... .`                                    (4.7)

The generic `e^3` relaxation on the same canonical weight and same `q` would give

`4.923801492785458...`,

so retaining the exact marginal factors is a substantial improvement.

## 5. Fully dense rotated indefinite target matrix

Put

`C_5=J_5/100`, `C_4=J_4/100`, and

`A_*=[[C_5,M],[M^T,C_4]].`                                   (5.1)

Every physical entry of `A_*` is nonzero. The matrix is not diagonal in the independent coordinates and is indefinite.

For

`A_0=[[0,M],[M^T,0]]`,

the spectrum is

`{+2 (multiplicity 4), -2 (multiplicity 4), 0}`.               (5.2)

The perturbation `A_*-A_0=diag(C_5,C_4)` has operator norm

`max(5/100,4/100)=1/20`.                                      (5.3)

Weyl's inequality therefore leaves four positive and four negative eigenvalues of modulus at least

`2-1/20=39/20>1`.                                             (5.4)

Thus (5.1) is a genuinely dense, rotated, indefinite instance of the owner's exact spectral target. The theorem permits both self blocks without treating them as independent convolution noise. Consequently, for every admissible independent cap-one input law,

`boxed: ||p_(X^T A_* X)||_infinity <=5sqrt(15)/6`,             (5.5)

and this density has a `C_0` representative.

## 6. The newest projection-tail sufficient gate fails on the same block

The projection-tail theorem at the predecessor commit uses

`T2=sum_(j>=3) sigma_j(M)^2=8`                                (6.1)

and asks for an orthogonal projection `P` on the five-row physical space with

`max_i P_ii<=1/2`,

`epsilon=||(I-P)M||op<=sqrt(T2)/15`.                           (6.2)

But `rank P=tr P<=5/2`, hence `rank P<=2`. Since `ran U` has dimension four and `ker P` has dimension at least three,

`ran U intersect ker P != {0}`.                               (6.3)

Choose a unit `y=Uz` in this intersection. Because `U` is an isometry, `||z||=1`, and

`||(I-P)Mz||=||2(I-P)y||=2`.                                 (6.4)

Thus `epsilon>=2`; since `||M||op=2`, in fact `epsilon=2`. Therefore

`epsilon/sqrt(T2)=1/sqrt(2)>1/15`.                            (6.5)

So the current projection-tail **sufficient** certificate fails for every admissible `P` on this physical block, while the exact fractional-volume compiler succeeds at `q=6/5`. This is a complementary regime, not a contradiction to the projection-tail theorem.

## 7. Designated partner account02/B04 applied to the same ambient matrix

Condition any one original coordinate in the five-row left bank. The retained four-row cross block `B` has four physical row triples, each still having squared row volume `128/5`. Therefore

`E3(B)=4*(128/5)=512/5`.                                      (7.1)

For any probability law on three-subsets of four active rows, the four row inclusion marginals sum to three, so at least one is at least `3/4`. Hence no supported minor law can have every constrained-side row marginal strictly below `3/4`.

The completed account02/B04 theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` therefore applies to each conditional ambient form, with all induced affine terms and same-bank curvature retained, and gives

`||p_Q||_infinity
 <=6*4^(1/6)*(512/5)^(-1/6)
 =6*(5/128)^(1/6)
 =3.494979152252139... .`                                    (7.2)

The direct exact-q certificate (5.5) improves this completed partner bound on the same target-valid matrix by a factor

`3.494979152252139... / 3.227486121839514...
 =1.08287968416117... .`                                     (7.3)

This is an equation-level use of the designated partner result, not a bibliography-only citation.

## 8. What changed and what remains

The preceding B04 run retained exact marginal factors only at `q=1`. This run proves the exact factor for the entire admissible fractional window `1<=q<3/2`. That matters precisely for matrices such as the five-row regular-simplex block, where the canonical volume law has `alpha_*=3/5>1/2`: the q=1 theorem is unavailable, while the new theorem gives an explicit constant at the sharp canonical exponent `q=6/5`.

The next structural obligation remains global rather than analytic:

`QFORM-EXACT-Q-MARGINAL-VOLUME-OR-COMPOUND-HUB-ROUTING-v1`:

Starting only from the bare three-large-eigenvalue hypothesis, either force an original-coordinate cross block and minor weighting for which some `q<3/2` has a uniform marginal gap and target-scale exact `R_q`--`G` currency, or route quantitative failure into the completed fractional-support-defect, compound-hub, ridge, pair-log, aggregate-square, grouped-bank, or exact-rank exits without multiplying by an arbitrarily small extra singular direction.

That implication is **not proved** here. The full conjecture and the full-target continuity conclusion remain **OPEN**.

## 9. Integrity and status

No Gaussianity, moments, log-concavity, compact support, connected support, spectral-coordinate independence, pointwise oscillatory decay, or numerical histogram is used. All displayed decimals only evaluate exact closed forms. Scheduler/task state, email/push settings, public visibility, paid model/API use, account authentication, and permissions were not changed. Repository transport is not verified learned-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
