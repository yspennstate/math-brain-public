# fleet03/B05 — universal rank-two half-Riesz closure for product quadratic forms

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `fleet03-B05-20260922T133738Z-qform-r12`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and live corrections

The owner target remains the full arbitrary-product-law statement: for every dimension, every independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a dimension-, law-, sign-, and matrix-independent bound on the essential density of `X^T A X`, or give a valid counterexample. Continuity is a separate stronger request.

This report uses no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no unrestricted fiber supremum, no fixed-minor structural dichotomy, and no conditional sum/difference density cap. It also respects the fresh correction that product aggregation must occur before or jointly with an indefinite curved trace.

The assigned partner is `fleet04/B05`. At startup and again immediately before publication, the current QFORM archive and shared-handoff roots contained no completed `fleet04/B05` QFORM artifact, so no assigned-partner theorem is fabricated. The proof instead applies three completed compatible results line-by-line:

1. `fleet03/B19`, `QFORM-DIFFUSE-RANK2-L3-v1`: if a rank-two Parseval spectral frame has every squared row leverage `<=1/2`, then for an invertible `2x2` coefficient matrix `Gamma`,

   `||p_R||_3 <= (3e)^(2/3) |det Gamma|^(-1/3)`.

2. `fleet02/B04`, `QFORM-LINEAR-FORM-L2-CAP-v1`: for independent density-cap-one coordinates,

   `M(sum c_j X_j) <= sqrt(2)/||c||_2`.

3. `fleet02/B05`, scalar-square coarea: if

   `Q=a(X+m(Y))^2+R(Y)`, `a!=0`,

   with `X` an original independent coordinate of density cap one, then

   `p_Q(t) <= |a|^(-1/2) E|t-R(Y)|^(-1/2)`.

The new theorem below closes the complementary **localized** rank-two half-Riesz problem with no loss in the second scalar pivot. Combined with item 1, it yields a universal determinant-scale half-Riesz bound for every rank-two product quadratic form.

## 2. Two elementary kernel lemmas

### Lemma 2.1 — one shifted square into a quarter-Riesz kernel

Let `X` have a probability density bounded by one. For every `b!=0`, every real shift `m`, and every `v!=0`,

`E |v-b(X+m)^2|^(-1/2) <= 4 sqrt(2) |b|^(-1/4)|v|^(-1/4)`.    (2.1)

#### Proof

After translation and scaling it suffices to bound

`int f(x)|w-x^2|^(-1/2) dx`, `f<=1`, `int f=1`.

If `w=-r^2<0`, then `x^2+r^2>=2r|x|`, so

`|w-x^2|^(-1/2) <= (2r)^(-1/2)|x|^(-1/2)`.

The bathtub principle gives

`sup_{f<=1, int f=1} int f(x)|x|^(-1/2)dx = 2sqrt(2)`,

hence this case is at most `2 r^(-1/2)`.

If `w=r^2>0`, put `a=|x-r|`, `c=|x+r|`. Since `max(a,c)>=r`,

`1/sqrt(ac) <= r^(-1/2)(a^(-1/2)+c^(-1/2))`.

Each translated `|.|^(-1/2)` integral is at most `2sqrt(2)`, so the total is at most `4sqrt(2) r^(-1/2)`. Restoring `w=v/b` proves (2.1). QED.

### Lemma 2.2 — quarter-Riesz bound for one square

Let `Z` have probability density bounded by `M`. Then, for every `kappa!=0`,

`sup_t E|t-kappa Z^2|^(-1/4)
 <= 2^(7/4) M^(1/2)|kappa|^(-1/4)`.                       (2.2)

In particular, if `M<=sqrt(2)`, the right side is at most

`4 |kappa|^(-1/4)`.                                        (2.3)

#### Proof

For every `s in R` and `eps>0`,

`Leb{z: |s-z^2|<eps} <= 2sqrt(2 eps)`.

Indeed, when `s>=eps` the set is two intervals of total length

`2(sqrt(s+eps)-sqrt(s-eps)) <=2sqrt(2eps)`;

when `0<=s<eps` it lies in `[-sqrt(s+eps),sqrt(s+eps)]`; and `s<0` is easier. Therefore

`P(|s-Z^2|<eps) <= min(1, C sqrt(eps))`, `C=2sqrt(2)M`.

Layer cake gives

`E|s-Z^2|^(-1/4)
 =(1/4) int_0^infinity eps^(-5/4) P(|s-Z^2|<eps) d eps`.

Split at `eps_0=C^(-2)`. The two pieces are both `sqrt(C)`, yielding `2sqrt(C)=2^(7/4)M^(1/2)`. Scaling by `kappa` proves (2.2). QED.

## 3. New localized rank-two theorem

Let `S` be an `m x 2` real matrix with orthonormal columns. Write its rows as `s_j`. Let `Gamma` be a real symmetric invertible `2x2` matrix and

`R=(S^T X)^T Gamma(S^T X)`,

where the original coordinates `X_1,...,X_m` are independent and have densities bounded by one.

### Theorem 3.1 — `QFORM-RANK2-LOCALIZED-HALF-RIESZ-v1`

For every row `j` of squared leverage

`d=||s_j||_2^2>0`,

one has the following bound whenever this row is used as the localizing row:

`sup_t E|t-R|^(-1/2)
 <= 16 sqrt(2) d^(-1/4)|det Gamma|^(-1/4)`.               (3.1)

If `d>1/2`, this becomes

`sup_t E|t-R|^(-1/2)
 <= 16*2^(3/4)|det Gamma|^(-1/4)
 <26.909 |det Gamma|^(-1/4)`.                             (3.2)

The exact isotropic-row subcase has the sharper constant `8` in (3.2).

#### Proof

Let `e=s_j/sqrt(d)` and choose a unit `g perpendicular e` in the two-dimensional spectral plane. Write every other row as

`s_k=alpha_k e+beta_k g`.

Because `S^T S=I_2` and the `j`th row is `sqrt(d)e`,

`sum_{k!=j} beta_k^2=1`,
`sum_{k!=j} alpha_k beta_k=0`,
`sum_{k!=j} alpha_k^2=1-d`.                              (3.3)

Define original-coordinate linear aggregates

`T=sum_{k!=j} alpha_k X_k`,
`Z=sum_{k!=j} beta_k X_k`.

The variable `X_j` is independent of `(T,Z)`. By the completed `fleet02/B04` linear-form theorem and (3.3),

`M(Z)<=sqrt(2)`.                                           (3.4)

In the basis `(e,g)`, write

`Gamma=[[r,s],[s,tau]]`.

Then

`R=r(sqrt(d)X_j+T)^2+2s(sqrt(d)X_j+T)Z+tau Z^2`.          (3.5)

**Case 1: `r!=0`.** Complete only the original coordinate `X_j`:

`R=b(X_j+M_0)^2+kappa Z^2`,                               (3.6)

where

`b=dr`,
`M_0=(T+(s/r)Z)/sqrt(d)`,
`kappa=det(Gamma)/r`.

Crucially,

`|b kappa|=d |det Gamma|`.                                (3.7)

Condition on all coordinates except `X_j`. Lemma 2.1 is uniform in the random shift `M_0`, so for almost every residual configuration,

`E_{X_j}|t-R|^(-1/2)
 <=4sqrt(2)|b|^(-1/4)|t-kappa Z^2|^(-1/4)`.

The exceptional event `t=kappa Z^2` has probability zero because `Z` is absolutely continuous. Average and use Lemma 2.2 with (3.4):

`E|t-R|^(-1/2)
 <=16sqrt(2)|b kappa|^(-1/4)
 =16sqrt(2)d^(-1/4)|det Gamma|^(-1/4)`.                   (3.8)

**Case 2: `r=0`.** Since `Gamma` is invertible, `s!=0` and `|det Gamma|=s^2`. Now

`R=2s sqrt(d) X_j Z + 2sTZ+tau Z^2`.

Conditioning on the other coordinates makes `R` affine in `X_j` with slope `2s sqrt(d)Z`. A probability density capped by `M` has half-Riesz potential at most `2sqrt(2M)`, so

`E_{X_j}|t-R|^(-1/2)
 <=2 |s|^(-1/2)d^(-1/4)|Z|^(-1/2)`.

For a variable with density cap `sqrt(2)`, the bathtub bound gives

`E|Z|^(-1/2)<=2^(7/4)`.

Thus

`sup_t E|t-R|^(-1/2)
 <=2^(11/4)d^(-1/4)|det Gamma|^(-1/4)`,                   (3.9)

which is stronger than (3.1), and if `d>1/2` is at most `8|det Gamma|^(-1/4)`. QED.

### Why this is the missing coarea mechanism

The potentially dangerous second scalar pivot `r` disappears from (3.8): the product `b kappa` is exactly `d det Gamma`. Thus neither a tiny nonzero second pivot nor the exact null-cone boundary costs a reciprocal pivot factor. The proof retains original-coordinate independence at the only place it is used (`X_j` versus the remaining coordinates), and spends the distributed remainder through the normalized linear form `Z` before taking the singular kernel.

## 4. Universal rank-two half-Riesz theorem

### Theorem 4.1 — `QFORM-RANK2-HALF-RIESZ-UNIVERSAL-v1`

Let `R=X^T A_2 X` be any real rank-two quadratic form in independent density-cap-one coordinates, with nonzero eigenvalues `mu_1,mu_2`. Then

`sup_t E|t-R|^(-1/2)
 <= C_2 |mu_1 mu_2|^(-1/4)`,                            (4.1)

where one may take

`C_2=16*2^(3/4)<26.909`.                                  (4.2)

No sign condition is imposed. In particular this theorem includes the opposite-sign logarithmic-density case; it does not claim the rank-two density itself is bounded.

#### Proof

Choose a Parseval two-frame `S` and coefficient matrix `Gamma` with eigenvalues `mu_1,mu_2`.

If every squared row leverage is at most `1/2`, apply the completed `fleet03/B19` theorem

`||p_R||_3 <=(3e)^(2/3)|det Gamma|^(-1/3)`.               (4.3)

For any probability density `p in L^3`, split its half-Riesz potential at radius `L`:

`int |t-u|^(-1/2)p(u)du
 <=4||p||_3 L^(1/6)+L^(-1/2)`.

Optimizing at `L=(3/(4||p||_3))^(3/2)` gives

`sup_t int |t-u|^(-1/2)p(u)du
 <= [8sqrt(2)/3^(3/4)] ||p||_3^(3/4)`.                   (4.4)

Using (4.3), the diffuse constant is

`8sqrt(2e)/3^(1/4)<14.174`,                               (4.5)

strictly below `C_2`.

Otherwise some row has squared leverage `d>1/2`; apply Theorem 3.1 and (3.2). Since `|det Gamma|=|mu_1mu_2|`, (4.1) follows. QED.

This theorem removes the entire second-level diffuse/localized dichotomy from rank-two coarea.

## 5. Consequence for the exact rank-three spectral-Schur branch

Let

`A=U Lambda U^T`, `U^T U=I_3`,

be rank exactly three, with `Lambda` invertible. Let `u_i` be a physical spectral row,

`c_i=||u_i||^2`, `a_i=u_i^T Lambda u_i=A_ii`.

If `a_i!=0`, completing the original coordinate `X_i` gives

`Q=a_i(X_i+m)^2+R_i`,

where `R_i` has rank two. The completed Schur identity gives

`|pdet(R_i)|=c_i |det Lambda|/|a_i|`.                    (5.1)

Apply the `fleet02/B05` scalar-square coarea inequality and Theorem 4.1:

`||p_Q||_infinity
 <= C_2 |a_i|^(-1/2)|pdet(R_i)|^(-1/4)`
` = C_2 (|a_i| c_i |det Lambda|)^(-1/4)`.                 (5.2)

Hence **after any nonzero first physical pivot, no second-level localization or near-isotropic second pivot remains unpaid**. This strengthens the current `QFORM-TWOLEVEL-LOCALIZED-SQUARE-CASCADE-v1`, whose bound still paid powers of two nonzero scalar pivots.

The exact-rank-three obstruction is therefore narrowed to the **first-level** heavy near-isotropic regime: when the three-frame is not globally diffuse, a heavy row may have `a_i` zero or arbitrarily small. The exact leverage-one isotropic boundary is already closed by `fleet03/B10`; for leverage `c_i in (1/2,1)` the product-preserving isotropic-leakage/bank extraction remains open.

## 6. Scope, status, and next implication

**Proved here:**

- `QFORM-RANK2-LOCALIZED-HALF-RIESZ-v1`;
- `QFORM-RANK2-HALF-RIESZ-UNIVERSAL-v1`, with `C_2=16*2^(3/4)<26.909`;
- elimination of the second-level residual-localization and second-pivot-smallness debt in the exact rank-three coarea branch via (5.2).

**Not proved:**

- a uniform lower bound on `|a_i|c_i` for a usable first pivot;
- the heavy first-level isotropic-leakage / aggregate-bank theorem;
- arbitrary additional nonseparable spectral directions in full generality;
- the full QFORM conjecture;
- continuity in the new coarea branch.

**First unpaid implication after this run:** `QFORM-FIRST-PIVOT-ISOTROPIC-BANK-COAREA-v1`: for an indefinite rank-three form with a leverage-heavy physical row `c>1/2` and tiny or zero Rayleigh quotient, exploit the aggregate off-diagonal bank energy before any reciprocal first-pivot factor is paid, producing either a direct small-ball/coarea bound or a disjoint aggregate hyperbolic-square certificate. The current exact-rank-three source identities show the necessary cross energy is present; the missing step is a product-preserving conversion of that energy into linear-in-interval small-ball scaling.

The full conjecture remains `OPEN / NOT PROVED`.

## 7. Source pins

Fresh controls immediately before publication: `yspennstate/math-research-brain@026692a030fc864d59bccb110245e7f5491482c3`, owner revision `2026-09-22.5`; live correction inbox blob `b9bf5f3faf9e9725becf7fbbdad56ee5ba9c0d50`.

Mathematical dependencies were retrieved from `yspennstate/math-open-problems` on `master` at commit `e58461e07b19315b290cb4b397929090ec6f48b9`:

- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/fleet03-B19-20260922T123215Z-186f53a8/REPORT.md` (`QFORM-DIFFUSE-RANK2-L3-v1`);
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T125623Z-r11-product-fourier/REPORT.md` (`QFORM-LINEAR-FORM-L2-CAP-v1`);
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md` (scalar-square coarea and binary half-Riesz context);
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T131539Z-fleet03-B20-qform-r11/REPORT.md` (current two-level cascade comparison).

No completed current-QFORM artifact existed for the assigned `fleet04/B05` partner at the final source check; the absence is recorded rather than replaced by an unrelated historical result.
