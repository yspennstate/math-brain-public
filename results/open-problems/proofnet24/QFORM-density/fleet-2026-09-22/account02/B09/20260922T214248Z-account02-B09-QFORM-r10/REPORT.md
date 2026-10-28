SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-22T21:42:48Z.
attacking: the one-strong-cross indefinite-curvature residual by identifying the exact Schur-lightcone boundary and forcing any target-valid proof to retain a genuine third smoother.

# account02/B09 QFORM r10 — sharp Schur-lightcone boundary for indefinite scalar compressions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account02/B09` — Bilinear block mechanism  
Run: `20260922T214248Z-account02-B09-QFORM-r10`  
Outcome: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture remains open. This run resolves a precise analytic ambiguity left by the one-strong-cross programme: for a three-scalar compression containing a nondegenerate **indefinite** endpoint pair, the Schur-center determinant is an exact qualitative boundary. Away from the lightcone (`det G != 0`) the previous B09 pair-log theorem gives a direct `O(interval length)` bound. On the lightcone (`det G = 0`) the scalar compression has rank two and there are completely source-valid independent cap-one product laws for which its density is logarithmically unbounded. Thus a full-target argument is not allowed to condition away the external third smoother at this boundary.

## 1. First unpaid implication, stated before the proof

The current B09 debt, after the new account03/B09 r18 definite-transverse theorem, is

`QFORM-INDEFINITE-LIGHTCONE-EXTERNAL-SMOOTHER-ROUTING-v1`:

> Starting only from `s_3(A)>=1`, whenever product-preserving bank aggregation produces a one-strong-cross scalar core with an invertible indefinite endpoint pair, either (i) obtain a quantitative nonzero Schur-center determinant and use `QFORM-PAIRLOG-SCHUR-CENTER-v1`; (ii) retain an additional independent/product-provenance third smoother through the lightcone rather than conditioning it away; or (iii) route to an already-paid ridge, triangle, transverse-rank-one, definite-transverse-rank-two, two-cross, or grouped-square branch.

The theorem below proves that item (ii) is logically necessary: at exact Schur-center zero the three-scalar core itself admits an admissible product-law logarithmic singularity. Since that core then has rank only two, the full target's third large direction must live outside the core and has to remain active in the estimate.

## 2. Source-pinned inputs actually used

### 2.1 Previous B09 positive half of the boundary

`QFORM-PAIRLOG-SCHUR-CENTER-v1` is proved in

`yspennstate/math-open-problems@004631a217e4c6b716651d7ac551e035a181cc45`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T204204Z-account02-B09-QFORM-r9/REPORT.md`.

For independent cap-one scalars and

`G = [[E,v],[v^T,beta]]`,

with `E` an invertible indefinite `2 x 2` endpoint block, writing

`D=|det E|`, `kappa=sigma_min(E)`, `Delta=|det G|>0`,

that theorem gives, uniformly under arbitrary affine perturbations,

`||p_Q||_infinity <= 8 sqrt(2) sqrt(D/(kappa Delta)) + 2/sqrt(D)`.     (2.1)

The proof is product-preserving: condition outside the three original coordinates, use the translation-uniform indefinite pair-log envelope, and average its logarithmic singularity against the quadratic moving critical value. The exact Schur coefficient is

`delta = beta-v^T E^(-1)v = det G/det E`.                              (2.2)

### 2.2 Latest designated partner account03/B09 result

The latest completed named-partner result is account03/B09 r18,

`QFORM-TWO-BANK-DEFINITE-TRANSVERSE-RANK2-v1`, canonical mathematics

`yspennstate/math-open-problems@9404859d9039d9eb76286588dc6d38a0fc3393ed`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T214906Z-account03-B09-QFORM-r18/REPORT.md`.

For a scalar projection `U=<u,X_I>` on one original-coordinate bank, independent of `(V,W1,W2)` on a disjoint bank, and active form

`2aUV + alpha U + q(V,W1,W2)`,

if the `W=(W1,W2)` quadratic block `D_W` is definite, then with

`Omega=||v wedge w1 wedge w2||`,
`Gamma=|a|^2 ||u||^2 Omega^2 |det D_W|`,

it proves

`||p_Q||_infinity <= 2^(5/4) sqrt(pi) e^(3/4) Gamma^(-1/4)
                   < 8.925 Gamma^(-1/4)`.                            (2.3)

The proof explicitly uses conditional linear anti-concentration on the large-`|V|` branch and a two-dimensional definite shell-area estimate on the small-`|V|` branch; the interval exponent stays exactly one.

The same partner run proves that a mere bounded joint-density cap for `(V,W1,W2)` cannot replace product provenance in the **indefinite** transverse case. The present run supplies a complementary obstruction whose law is an actual independent product law, rather than an arbitrary joint density.

### 2.3 Corrections enforced

No law-uniform pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea estimate, positive conditional projection-density moment, fixed-good-minor statement, or conditional-cap-as-independence substitution is used. In particular, orthogonal diagonalization below is used only as a deterministic algebraic factorization of the quadratic polynomial; the rotated random coordinates are never asserted independent.

## 3. New theorem — the indefinite Schur-center gate is qualitatively sharp

### Theorem 3.1 — `QFORM-INDEFINITE-SCHUR-LIGHTCONE-SHARPNESS-v1`

Let

`G = [[E,v],[v^T,beta]]`                                             (3.1)

be a real symmetric `3 x 3` matrix, where `E` is invertible and indefinite. Then:

1. If `det G != 0`, every independent cap-one triple and every affine perturbation of `x^T G x` has an essentially bounded density satisfying the explicit estimate (2.1).

2. If `det G = 0`, then `G` has rank exactly two and inertia `(1,1,1 zero)`. Moreover, for the admissible product law

`X_1,X_2,X_3 iid Uniform[-1/2,1/2]`,                                  (3.2)

the law of

`Q=X^T G X`                                                           (3.3)

has unbounded density. More quantitatively, there are constants `m_G,r_G>0`, depending only on `G`, such that for all `0<|t|<r_G^2`,

`p_Q(t) >= 2 m_G log(r_G^2/|t|)`.                                    (3.4)

Consequently there is no finite constant, even one depending on the fixed matrix `G`, for a linear small-ball inequality

`P{Q in I} <= C |I|`                                                  (3.5)

uniform over all intervals `I` for this law.

Thus, in the three-scalar model with a fixed invertible indefinite endpoint pair, `det G != 0` is a sufficient condition for a law-uniform bounded-density theorem and `det G=0` is an exact qualitative obstruction to any such theorem over all cap-one product laws.

### Proof

Part 1 is precisely the source-pinned theorem (2.1), so only the singular case is new.

Because `E` is invertible, block Gaussian elimination gives the congruence

`G congruent to diag(E, beta-v^T E^(-1)v)`.                           (3.6)

The block determinant identity gives

`det G = det E (beta-v^T E^(-1)v)`.                                  (3.7)

If `det G=0`, the scalar Schur complement in (3.6) is zero. Since `E` is indefinite and invertible, it has one positive and one negative eigenvalue. Hence `G` has rank two and inertia one positive, one negative, one zero.

Write its spectral decomposition as

`G=lambda u u^T - mu w w^T`,                                         (3.8)

with `lambda,mu>0` and orthonormal `u,w`. Define two deterministic linear forms

`L_+(x)=(sqrt(lambda)u+sqrt(mu)w)^T x`,
`L_-(x)=(sqrt(lambda)u-sqrt(mu)w)^T x`.                               (3.9)

Then

`x^T G x = L_+(x)L_-(x)`.                                            (3.10)

This is only an algebraic factorization; no independence of `L_+(X),L_-(X)` is claimed.

Let `L:R^3->R^2` be `x -> (L_+(x),L_-(x))`. The two rows of `L` are linearly independent, so some two columns form an invertible `2 x 2` matrix `B`. Denote the remaining column by `c`. Relabel the original coordinates so that

`L(X)=B(X_1,X_2)^T+cX_3`.                                             (3.11)

Condition on `X_3=z`. Since `(X_1,X_2)` is uniform on the unit square, the conditional density of `L(X)` is exactly `|det B|^(-1)` on the translated parallelogram

`B[-1/2,1/2]^2+cz`.                                                   (3.12)

By continuity and invertibility of `B`, there exist `r_G>0` and `eta_G in (0,1/2]` such that the square

`[-r_G,r_G]^2`                                                        (3.13)

is contained in (3.12) for every `|z|<=eta_G`. Integrating the conditional density over that `z`-interval gives the genuine two-dimensional marginal density `g` of

`(S,T):=(L_+(X),L_-(X))`

and the lower bound

`g(s,t) >= m_G := 2 eta_G/|det B| >0`                                (3.14)

throughout (3.13).

For every nonzero `q`, the product map `(s,t)->st` gives the standard density formula

`p_Q(q)=int_R g(s,q/s) ds/|s|`.                                      (3.15)

If `0<|q|<r_G^2`, then for both signs of `s` with

`|q|/r_G <= |s| <= r_G`,                                             (3.16)

we have `|s|<=r_G` and `|q/s|<=r_G`, so (3.14) applies. Hence

`p_Q(q)
 >= 2m_G int_(|q|/r_G)^r_G ds/s
 = 2m_G log(r_G^2/|q|)`,                                             (3.17)

which tends to infinity as `q->0`. This proves (3.4) and the failure of (3.5). QED.

### Why this theorem is source-valid

The counterexample law (3.2) is a literal product of three one-dimensional density-one laws in the original coordinates. Dependence of `(L_+(X),L_-(X))` is not discarded; its joint density is derived by conditioning on an original coordinate. The proof therefore avoids the exact post-rotation-independence error prohibited by the live correction archive.

## 4. Exact canonical lightcone example and quantitative lower bound

The general theorem contains a particularly transparent one-strong-cross example. Let independent

`U,W1,W2 ~ Uniform[-1/2,1/2]`

and set

`Q=2U(W1+W2)+W1^2-W2^2`.                                             (4.1)

Its coefficient matrix in `(U,W1,W2)` is

`G0=[[0,1,1],[1,1,0],[1,0,-1]]`.                                     (4.2)

The endpoint block `diag(1,-1)` is perfectly conditioned and indefinite, while

`det G0=0`,
`spec(G0)={sqrt(3),-sqrt(3),0}`.                                      (4.3)

The factorization is exact:

`Q=(W1+W2)(2U+W1-W2)=ST`.                                             (4.4)

Put `z=W2`. For fixed `z`, the map `(U,W1)->(S,T)` has Jacobian magnitude `2`, because

`S=W1+z`,
`T=2U+W1-z`.                                                         (4.5)

If `|S|,|T|<=1/8` and `|z|<=1/4`, then

`W1=S-z` and `U=z+(T-S)/2`

both lie in `[-3/8,3/8]`, hence inside their unit supports. Therefore the joint density of `(S,T)` obeys the explicit lower bound

`g(s,t)>=1/4` for `|s|,|t|<=1/8`.                                    (4.6)

Using (3.15), for every `0<|q|<1/64`,

`boxed: p_Q(q) >= (1/2) log(1/(64|q|)).`                              (4.7)

Thus the logarithmic singularity is not a qualitative artifact of diagonalization; it is visible by a direct original-coordinate computation.

This example is **not** a counterexample to the full QFORM conjecture because (4.3) has only two nonzero eigenvalues. Its role is sharper: it shows that the exact Schur-lightcone branch cannot be paid internally by the three-scalar one-strong-cross core. A target-valid ambient matrix reaching this boundary must derive its third large direction elsewhere, and an argument that conditions that direction away loses indispensable smoothing.

## 5. Latest named partner applied to an actual target inequality

Apply account03/B09 r18 to two disjoint original-coordinate banks `I,J`. Let `u` be a unit vector on `I`, and let `v,w1,w2` be orthonormal unit vectors on `J`. Put

`U=<u,X_I>`, `V=<v,X_J>`, `Wk=<wk,X_J>`,

and consider

`F=2UV+W1^2+W2^2`.                                                   (5.1)

On the active orthonormal span `(u,v,w1,w2)`, the coefficient matrix is

`[[0,1,0,0],
  [1,0,0,0],
  [0,0,1,0],
  [0,0,0,1]]`,                                                       (5.2)

so its nonzero spectrum is exactly

`{-1,1,1,1}`.                                                        (5.3)

This is a genuine target matrix. In the partner theorem

`a=1`, `||u||=1`, `Omega=||v wedge w1 wedge w2||=1`, `D_W=I_2`,

so `Gamma=1` and the actual quantitative consequence is

`boxed: ||p_F||_infinity
 <= 2^(5/4) sqrt(pi) e^(3/4)
 < 8.925.`                                                           (5.4)

If `u,v,w1,w2` are chosen as flat Walsh vectors on size-`m` banks, every physical matrix entry is `O(1/m)` while (5.4) is unchanged. This directly applies the newest completed named-partner result to a target-valid diffuse inequality.

## 6. A sharp scalar-level trichotomy for the current residual

For a three-scalar compression containing an invertible physical/bank endpoint pair `E`, the analytic possibilities are now completely separated:

1. **`E` definite.** The translated two-dimensional definite shell estimate pays the endpoint directly; in the stronger one-cross/two-transverse setting the newest partner theorem (2.3) pays the whole branch.
2. **`E` indefinite and `det G !=0`.** `QFORM-PAIRLOG-SCHUR-CENTER-v1` pays it by (2.1), with the determinant ratio `|det G/det E|` acting as the third curvature.
3. **`E` indefinite and `det G=0`.** Theorem 3.1 shows that the scalar core has rank two and genuinely can have logarithmically unbounded density for an admissible original-coordinate product law. There is no scalar-core estimate to prove here. A target proof must keep an additional smoother active.

Thus the current B09 obstruction is no longer an unresolved three-scalar analytic estimate. It is a **product-preserving structural routing problem for the external third direction / overlapping higher-rank curvature**.

A useful already-proved endpoint when the external direction is a genuine physical square is supplied by the orientation-free rank-two half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`:

if the lightcone residual has nonzero eigenvalues `lambda_+,-lambda_-` and a disjoint physical square pivot of coefficient `c` remains after square completion, then

`||p_Q||_infinity <=128 |c|^(-1/2)(lambda_+ lambda_-)^(-1/4)`.        (6.1)

This is cited only in its exact proved scope; arbitrary overlapping curvature is not silently replaced by such a square.

## 7. Conditional end-to-end implication

Combining the current paid branches gives the following compact conditional proof architecture.

If `s_3(A)>=1`, first use the existing ridge/diffuse, physical-pair, grouped-hyperbolic, zero-self, and cross-rank certificates whenever they fire. In the remaining one-strong-cross geometry, aggregate original-coordinate banks before any reciprocal physical-minor payment.

- A transverse rank-one square is paid by account03/B09 r17.
- Two same-sign transverse curvature directions are paid by account03/B09 r18.
- A three-scalar indefinite compression with nonzero Schur-center determinant is paid by B09 r9.
- An exact indefinite Schur-lightcone core cannot be paid internally: Theorem 3.1 proves a product-law logarithmic singularity and rank two. Therefore preserve and pay the external third direction jointly (physical square by (6.1), two disjoint hyperbolic pairs by the completed product-pair convolution theorem, or another existing ridge/cross certificate).

What remains is precisely `QFORM-INDEFINITE-LIGHTCONE-EXTERNAL-SMOOTHER-ROUTING-v1`: show that the bare spectral hypothesis always exposes such a product-compatible external smoother at a universal scale, or isolate an overlapping-curvature configuration needing a new joint estimate. This is a strictly narrower obligation than attempting an indefinite joint-density-cap theorem, which account03/B09 r18 correctly refuted.

## 8. Integrity and status

No numerical experiment is used as mathematical evidence. All displayed lower bounds are exact. The only random variables introduced are original-coordinate independent cap-one uniforms or genuine disjoint-bank projections. No moments, compact-support assumption beyond the explicit counterexample law, identical-law assumption in positive theorems, log-concavity, or post-rotation independence is used.

`QFORM-INDEFINITE-SCHUR-LIGHTCONE-SHARPNESS-v1`: **PROVED supporting theorem / source-valid mechanism counterexample**.  
`QFORM-INDEFINITE-LIGHTCONE-EXTERNAL-SMOOTHER-ROUTING-v1`: **OPEN**.  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity: not claimed by this run outside source theorems that explicitly provide it.
