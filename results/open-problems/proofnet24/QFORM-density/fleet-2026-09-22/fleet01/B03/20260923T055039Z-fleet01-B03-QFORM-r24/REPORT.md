SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T05:50:39Z.
attacking: repair the localized physical 3x3 branch without the false arbitrary-joint coarea lemma, by a diagonal/off-diagonal dichotomy and the completed fleet02/B03 pair estimates.

# fleet01/B03 r24 — rigorous localized physical 3x3 theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T055039Z-fleet01-B03-QFORM-r24`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The full conjecture remains OPEN. This run repairs one important branch that had previously been justified through the now-refuted arbitrary-joint rank-three coarea lemma. The theorem below uses only original-coordinate independence and two completed product-coordinate fleet02/B03 results.


Completed fleet02/B03 dependencies actually read and applied:

1. `yspennstate/math-open-problems@33cd6fae4e8adb85cf1ee43a244f628e563f1cbf`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T161346Z-fleet02-B03-QFORM-r12/REPORT.md`:
   for an arbitrary affine perturbation of an invertible indefinite binary quadratic with determinant magnitude `Delta`,
   `sup_t E|t-R|^(-1/2) <=16 sqrt(2) Delta^(-1/4)`.

2. `yspennstate/math-open-problems@ab591d183afaaeb8c8accbc9a80c06241f433532`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T041654Z-fleet02-B03-QFORM-auto11/REPORT.md`:
   after completing an invertible indefinite original-coordinate pair `P`, if the scalar/bank residual obeys
   `sup_t P(|R-t|<=rho)<=H sqrt(rho)`, then, with `D=|det P|`, `kappa=sigma_min(P)`,
   `||p_Q||_infinity <=4 sqrt(2H)(D kappa)^(-1/4)`.

No moment, compact-support, connected-support, log-concavity, Gaussian, sign, or diagonal-basis assumption is introduced.

## 2. Main theorem

### Theorem 2.1 — `QFORM-PHYSICAL-3X3-WELL-CONDITIONED-v1`

Let `B` be a real symmetric `3x3` matrix with

`sigma_min(B)>=s>0`.

Let `X_1,X_2,X_3` be independent real variables, each with a probability density bounded by one. For arbitrary `ell in R^3` and `r in R`, define

`q(X)=X^T B X+ell^T X+r`.

Then `q(X)` is absolutely continuous and

`boxed: ||p_q||_infinity <= C_3/s`,

where

`C_3=16 sqrt(2) (1601/512)^(1/8)=26.093068347867227... .`       (2.1)

Consequently, for an arbitrary-dimensional symmetric matrix `A`, if some ORIGINAL-coordinate principal triple `I` satisfies

`sigma_min(A[I,I])>=s`,

then for every independent cap-one product input,

`boxed: ||p_(X^T A X)||_infinity <= C_3/s`.                       (2.2)

All outside quadratic coefficients and outside-to-triple couplings are allowed. They become affine terms after conditioning on the outside ORIGINAL coordinates.

### Choice of threshold

Put

`c_* = sqrt(512/1601)=0.5655087310748825...`,

`k_* = sqrt((1-c_*^2)/2)-c_* = c_*/32`

`=0.01767214784609008... .`                                      (2.3)

Note `c_*<1/sqrt(3)`.

We split according to whether a physical diagonal of `B` is at least `c_* s` in magnitude.

## 3. Case I: a large physical diagonal

Assume `|B_ii|>=c_* s` for some original coordinate `i`. Reorder so `i=1` and write

`B=[[a,r^T],[r,C]]`, `|a|>=c_* s`.

Complete the square only in the original coordinate `X_1`:

`q=a(X_1+h(Y))^2+R(Y)`,                                           (3.1)

where `Y=(X_2,X_3)` remains a pair of independent cap-one variables and the quadratic part of `R` is the Schur complement

`S=C-r r^T/a`.

Because `B` is invertible and `a!=0`, `S` is invertible and

`det B=a det S`.                                                   (3.2)

For fixed `Y`, the translated square `a(X_1+h)^2` has conditional density bounded by

`|a|^(-1/2)|u|^(-1/2)`

at displacement `u`. Therefore

`p_q(t)<=|a|^(-1/2) E|t-R|^(-1/2)`.                              (3.3)

### 3a. Indefinite Schur complement

If `S` is indefinite, apply the completed fleet02/B03 binary half-Riesz theorem with `Delta=|det S|`:

`sup_t E|t-R|^(-1/2)<=16 sqrt(2)|det S|^(-1/4)`.                  (3.4)

Combining (3.2)--(3.4),

`||p_q||_infinity`
` <=16 sqrt(2)|a|^(-1/4)|det B|^(-1/4)`
` <=16 sqrt(2)c_*^(-1/4)s^(-1)`.                                 (3.5)

Here `|det B|>=s^3` because all three singular values of `B` are at least `s`.

### 3b. Definite Schur complement

If `S` is positive or negative definite, complete its affine term by translation. Since the joint density of the two original variables is bounded by one, the pushforward under the definite quadratic has density cap

`M_S<=pi/sqrt(|det S|)`.                                          (3.6)

Indeed, after the linear map `z=|S|^(1/2)(y-y_0)`, the derivative of the area of a two-dimensional disk sublevel is exactly `pi`, while the Jacobian contributes `|det S|^(-1/2)`.

For any probability density bounded by `M`, the sharp bathtub estimate gives

`sup_t E|t-R|^(-1/2)<=2 sqrt(2M)`.                                (3.7)

Using (3.6) in (3.7), then (3.3), yields

`||p_q||_infinity<=2 sqrt(2pi)|a|^(-1/4)|det B|^(-1/4)`,          (3.8)

which is strictly smaller than the right side of (3.5). Thus in every large-diagonal case

`||p_q||_infinity<=16 sqrt(2)c_*^(-1/4)s^(-1)`.                  (3.9)

## 4. Case II: all three physical diagonals are small

Assume

`|B_11|,|B_22|,|B_33|<c_* s`.                                    (4.1)

Because `sigma_min(B)>=s`, every physical row has Euclidean norm at least `s`. Fix any row `i`. Its two off-diagonal entries therefore have squared sum at least

`(1-c_*^2)s^2`,

so one of them, call it `beta=B_ij`, satisfies

`|beta|>=s sqrt((1-c_*^2)/2)`.                                   (4.2)

Consider the corresponding original-coordinate pair

`P=[[a,beta],[beta,b]]`,

where `|a|,|b|<c_*s`. Since `c_*<1/sqrt(3)`,

`beta^2 >=(1-c_*^2)s^2/2 > c_*^2 s^2 > |ab|`,                    (4.3)

so `P` is invertible and indefinite.

Moreover, compare `P` with `[[0,beta],[beta,0]]`. Weyl's singular-value perturbation inequality gives

`kappa:=sigma_min(P)`
` >=|beta|-max(|a|,|b|)`
` >=[sqrt((1-c_*^2)/2)-c_*]s`
` =k_* s`.                                                        (4.4)

Complete this physical pair. There is one residual original coordinate `Z`, whose scalar quadratic coefficient is

`tau=det B/det P`.                                                 (4.5)

The remaining affine terms are arbitrary. For a cap-one scalar variable, uniformly in the translation and target level,

`sup_t P(|tau(Z-h)^2-t|<=rho)<=2 sqrt(2)|tau|^(-1/2) sqrt(rho)`.  (4.6)

Apply the completed fleet02/B03 physical-indefinite-pair logarithmic transducer with

`D=|det P|`, `H=2 sqrt(2)|tau|^(-1/2)`.

It yields

`||p_q||_infinity`
` <=2^(13/4)|tau|^(-1/4)D^(-1/4)kappa^(-1/4)`
` =2^(13/4)|det B|^(-1/4)kappa^(-1/4)`
` <=2^(13/4)k_*^(-1/4)s^(-1)`.                                  (4.7)

The determinant cancellation in the second line uses exactly `D|tau|=|det B|`.

## 5. Optimize the two branches

The large-diagonal constant is

`C_large(c)=16 sqrt(2)c^(-1/4)`,

while the all-small-diagonal constant is

`C_small(c)=2^(13/4)[sqrt((1-c^2)/2)-c]^(-1/4)`.                 (5.1)

For `0<c<1/sqrt(3)`, the first decreases and the second increases. They are equal exactly when

`sqrt((1-c^2)/2)-c=c/32`.                                       (5.2)

Solving gives

`c^2=512/1601`,                                                   (5.3)

hence the threshold (2.3), and both constants equal

`C_3=16 sqrt(2)(1601/512)^(1/8)`
`=26.093068347867227... .`                                       (5.4)

This proves Theorem 2.1.

## 6. Ambient conditionalization is legitimate

Let `I` be the selected original-coordinate triple in the full matrix `A`. Condition on every original coordinate outside `I`. Independence of the original variables means the three coordinates in `I` retain their cap-one product law. The outside variables contribute only affine and constant terms to the conditional polynomial on `I`; its quadratic matrix remains exactly `A[I,I]`. Theorem 2.1 therefore bounds every conditional output density by `C_3/s`. Averaging those conditional densities gives (2.2).

This step never rotates the product measure and never uses a density bound for an arbitrary dependent three-dimensional projection. It is therefore unaffected by `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`.

## 7. Genuine target family and sharper zero-diagonal example

Take

`B_0=[[0,1,1],[1,0,1],[1,1,0]]`.

Its spectrum is `{2,-1,-1}`, so `sigma_min(B_0)=1`. The small-diagonal branch can use the pair

`P=[[0,1],[1,0]]`,

for which `D=kappa=1` and the scalar Schur coefficient has magnitude `|tau|=2`. Formula (4.7) then gives the sharper explicit bound

`boxed: ||p_(X^T B_0 X+affine)||_infinity<=8`.                    (7.1)

If `B_0` occurs as a principal triple inside a larger symmetric `A`, Cauchy interlacing gives at least one eigenvalue of `A` at least `2` and at least two eigenvalues at most `-1`; hence it is itself a genuine owner-target ambient branch. Arbitrary outside couplings remain allowed by Section 6.

## 8. Independent-copy / time-integral corollary

The theorem already gives the stronger linear small-ball conclusion

`P(q in I)<=C_3 s^(-1)|I|`.                                      (8.1)

It also gives a dependence-safe total pair-collision time estimate. Let `q'` be an independent copy and `phi_q(t)=E exp(itq)`. Keeping the difference law intact,

`|phi_q(t)|^2=E exp(it(q-q'))`.                                   (8.2)

Since `p_q` is a probability density and `||p_q||_infinity<=C_3/s`,

`||p_q||_2^2<=C_3/s`.

Plancherel therefore yields

`boxed: integral_R |phi_q(t)|^2 dt <=2 pi C_3/s`.                 (8.3)

No coordinatewise sum/difference independence is asserted. Equation (8.3) is recorded as a collision integral downstream of the stronger density theorem; it is not being misused as an L-infinity sufficiency statement.

## 9. What this repairs, and what remains open

The source owner message had proposed a localized principal-3x3 branch through a rank-three coarea lemma for an arbitrary bounded joint density. The live correction later refuted that arbitrary-joint lemma. Theorem 2.1 restores the localized branch rigorously from the actual product structure, with an explicit universal constant.

It does NOT make the full conjecture automatic: the exact family `[1] direct_sum J_m/m direct_sum (-J_m/m)` has target spectrum `{1,1,-1}` while every nonsingular physical principal triple becomes badly conditioned at scale `1/m`. Thus the remaining first implication is still the aggregate-before-inversion structural compiler: derive from only three large eigenvalues either a dimension-free well-conditioned physical triple (now fully paid here), or one of the already-paid ridge/diffuse/grouped-bank/mixed-hub certificates, without selecting a tiny local minor first.

Absolute continuity and an essential density bound are proved in this localized branch. Continuity is **not proved** by this argument. Full QFORM remains **OPEN**.

## 10. Finite regression checks and integrity

The accompanying `check.py` verifies the exact threshold identity `k_*=c_*/32`, equality of the two optimized constants, the `B_0` spectrum and branch constant `8`, and 5000 deterministic random symmetric-matrix instances of the small-diagonal pair-selection inequality. These finite tests are regression evidence only; Sections 2--8 are the proof.

No scheduler mutation, task creation, notification/email change, installation, paid model/API call, remote workflow, permission expansion, public release, unrelated data, or credentials were used. Repository transport is not native learned-memory ingestion, so the run remains `WITHOUT_VERIFIED_BRAIN`.
