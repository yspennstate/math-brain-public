SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T16:30:50Z.
attacking: near-singular but nonzero physical-pair determinant; quantify the scalar-completed leakage branch by a dependence-safe random-slope estimate and then reattach the outer scalar square inside the signed Fejer kernel.

# account03/B01 — near-null leakage: residual square-root smoothing and a full-Q signed-Fejer logarithmic bound

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T163050Z-auto11`  
Assignment: `Oscillatory replacement` / FOURIER  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING AVERAGED-FREQUENCY / DISTRIBUTION-FUNCTION ESTIMATE; FULL QFORM OPEN; CONTINUITY NOT PROVED HERE**.

The full target remains open: for independent original-coordinate real inputs with probability densities bounded by one and any real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal density bound for `Q=X^TAX`, or give a valid target counterexample. No moments, bounded support, connected support, Gaussianity, log-concavity, identical laws, or independence after a rotation is used below.

The phase-aligned fragmented-support obstruction is retained. For every prescribed frequency `s>0` and every small `eta>0`, one may choose a finite union of intervals of total length one contained in

`{x: dist(s x^2,2 pi Z)<=eta}`

and take its indicator as a probability density. Then

`Re E exp(i s X^2) >= cos eta`.

Thus no law-uniform positive-power pointwise Fresnel decay is available. The estimates below gain only after a genuinely random original-coordinate slope is averaged, and the final full-form statement is a signed Fejer estimate rather than a false pointwise scalar estimate.

## 1. Exact source boundary and results applied

### 1.1 Designated partner: scalar-pivot overlap-two routing

The main partner input is account04/B01,

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

For an original-coordinate physical pair `S={i,j}` with

`B=[[a,b],[b,c]]`, `a!=0`,

scalar-complete coordinate `i` and put

`delta=det(B)/a`,
`ell_k=A_jk-(b/a)A_ik`,
`M_kl=A_kl-a^(-1)A_ik A_il`.

For distinct `k,l` outside `S`, the partner proves the exact identity

`det A[S union {k}, S union {l}] = a(delta M_kl-ell_k ell_l)`.

With

`W2(S)=sum_(k!=l) det A[S union {k},S union {l}]^2`,

one of two alternatives holds. The branch used in this report is the **leakage alternative**

`sum_(k!=l) ell_k^2 ell_l^2 >= W2(S)/(4a^2)`.                    (1.1)

This is applied below at an actual inequality; it is not merely cited.

### 1.2 Random-slope theorem already proved in this slot

The completed account03/B01 source is

`yspennstate/math-open-problems@bb42aaf0dbcd702ece4a23fdc3d24f3e18363d6e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T235524Z-r21/REPORT.md`.

It proves the following dependence-safe statement. If `Y` is one independent original coordinate with density at most one, `L=L(Z)` has marginal density bounded by `K`, and `S=S(Z)` may be arbitrarily dependent on `L`, then for every real `delta`

`R=delta Y^2+2LY+S`

satisfies

`|phi_R(t)| <= min(1, K^(1/2)(pi/|t|)^(1/2))`,                  (1.2)

and

`P(|R-u|<=rho) <= min(1,4 sqrt(K rho))`.                         (1.3)

The same report records the source-valid product projection cap supplied by account04/B01's grouped-square/Fejer work,

`||p_(ell dot Z)||_infinity <= sqrt(2)/||ell||_2`.               (1.4)

### 1.3 Signed Fejer interface from account04/B01

Account04/B01's completed Fejer theorem is source-pinned at

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law `mu`, define

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T) Re[e^(-ity) phi_mu(t)] dt`.

This is convolution with the nonnegative Fejer density

`K_T(x)=(1-cos(Tx))/(pi T x^2)`,                                (1.5)

with the continuous value `K_T(0)=T/(2pi)`. The partner proves

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                       (1.6)

whenever the left side is interpreted through the exact bounded-density equivalence. It also gives the interval majorant: if `I` has length `q` and center `y`, and `s0=4 sin(1/2)^2`, then

`mu(I) <= (pi q/s0) D_(2/q) mu(y)`.                              (1.7)

### 1.4 Required newest-Claude volume/tail exit, applied before the near-null branch

The required current package is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For an original-coordinate cross block `C`, let `P` be the top-two left singular projection and `T2=sum_(j>=3)s_j(C)^2`. If

`max_i P_ii<=1/2`,
`||(I-P)C||_op <= sqrt(T2)/15`,                                  (1.8)

then the full ambient form, retaining all self blocks, outside couplings and affine terms, has a continuous density with

`||p_Q||_infinity <= (9 sqrt(3)e/2)[s1(C)^2 s2(C)^2 T2]^(-1/6)`. (1.9)

This is an actual proof-map reduction used in this run: every candidate satisfying (1.8) exits immediately through (1.9). The analysis below concerns a surviving low-tail/high-leverage near-null state; it does not rename the already-paid collective-tail branch.

## 2. Leakage currency gives a dimension-free random-slope cap

After scalar completion of coordinate `i`, the active residual has the form

`R = delta Y^2 + 2Y(ell dot Z + beta) + H(Z)`,                   (2.1)

where `Y=X_j` is one original coordinate, `Z=X_(S^c)` is its independent original-coordinate complement, and `H` may contain arbitrary dense, high-rank, indefinite quadratic and affine curvature.

From (1.1),

`||ell||_2^4 >= sum_(k!=l)ell_k^2ell_l^2 >= W2/(4a^2)`,

so

`||ell||_2 >= W2^(1/4)/(sqrt(2)|a|^(1/2)).`                      (2.2)

By (1.4), the slope `L=ell dot Z+beta` has density cap

`K <= sqrt(2)/||ell||_2`.                                        (2.3)

Substituting (2.2) into (2.3) and then into (1.2) gives the first new explicit inequality:

`boxed:`
`|phi_R(t)| <= min(1, sqrt(2pi)|a|^(1/4) W2^(-1/8)|t|^(-1/2))`. (2.4)

This holds for every `delta`, including arbitrarily small nonzero `delta`, and for arbitrary `H(Z)`. No reciprocal power of `delta` appears.

Likewise (1.3) gives, with

`H0 = 4 sqrt(2)|a|^(1/4)W2^(-1/8)`,                              (2.5)

`boxed:`
`P(|R-u|<=rho) <= min(1,H0 sqrt(rho))`.                           (2.6)

For an interval `J` of length `q`, take `rho=q/2` to obtain

`boxed:`
`P(R in J) <= min(1,4 |a|^(1/4)W2^(-1/8) sqrt(q))`.              (2.7)

Equation (2.7) is a dimension-free distribution-function replacement for pointwise scalar Fresnel decay on the actual near-null leakage residual. The square-root exponent is borderline and, with arbitrary `H`, is genuinely the natural exponent; it is not yet a bounded-density statement.

The Fejer average of the residual itself follows immediately from (2.4). Put

`A0=sqrt(2pi)|a|^(1/4)W2^(-1/8)`.

Using the triangular Fourier weight,

`D_T law(R)(y)`
` <= (1/(2pi)) int_(-T)^T (1-|t|/T) A0 |t|^(-1/2) dt`
` = (4A0/(3pi)) sqrt(T)`.

Thus

`boxed:`
`D_T law(R)(y) <= [4 sqrt(2)/(3 sqrt(pi))] |a|^(1/4)W2^(-1/8) sqrt(T)`.  (2.8)

This is signed-Fejer compatible but intentionally does not claim a uniform-in-`T` bound.

## 3. A Fejer convolution lemma for one translated scalar square

The original scalar completion reconstructs the full form as

`Q = a (X+h(V))^2 + R(V)`,                                       (3.1)

where `X=X_i` is one genuine original coordinate independent of `V=(Y,Z)`, while `h(V)` may be arbitrary and correlated with `R(V)`.

Conditional on `V=v`, the density of `a(X+h(v))^2` is bounded by

`|a|^(-1/2)|u|^(-1/2) 1_(sign(a)u>0)`.                           (3.2)

The following elementary estimate is the useful signed-frequency replacement.

### Lemma 3.1 — square against the Fejer kernel

For every `T>0` and `s in R`,

`int_0^infinity u^(-1/2) K_T(s-u) du`
` <= 5 min(sqrt(T),|s|^(-1/2)).`                                 (3.3)

The same bound holds with `s+u` in place of `s-u`.

#### Proof

The scaling `K_T(x)=T K_1(Tx)` reduces (3.3) to

`J(z):=int_0^infinity u^(-1/2)K_1(z-u)du <=5 min(1,|z|^(-1/2))`. (3.4)

Use

`K_1(x) <= min(1/(2pi),2/(pi x^2))`.                             (3.5)

If `|z|<=2`, split at `u=4`. The first part is at most

`(1/(2pi)) int_0^4 u^(-1/2)du =2/pi`,

and the tail is at most

`(8/pi) int_4^infinity u^(-5/2)du =2/(3pi)`.

Thus `J(z)<=8/(3pi)<0.85`, which is stronger than (3.4) on `|z|<=1` and still below `5|z|^(-1/2)` on `1<|z|<=2`.

If `z>=2`, split into `u<z/2`, `z/2<=u<=3z/2`, and `u>3z/2`. The three pieces are respectively bounded by

`(8sqrt(2)/pi)z^(-3/2)`,
`sqrt(2)z^(-1/2)`,
`(12/pi)(3/2)^(-3/2)z^(-3/2)`.

Since `z>=2`, their sum is less than `4.26 z^(-1/2) <5z^(-1/2)`.

If `z<=-2`, then `|z-u|=|z|+u` and the beta integral gives

`J(z) <= (2/pi) int_0^infinity u^(-1/2)(|z|+u)^(-2)du`
`     = |z|^(-3/2)`
`     <= |z|^(-1/2)`.

This proves (3.4), hence (3.3). Reflection gives the opposite half-line. QED.

## 4. Main new theorem: a full-Q logarithmic signed-Fejer bound in the near-null leakage branch

### Theorem 4.1 — `QFORM-NEARNULL-LEAKAGE-FEJER-LOG-v1`

Assume the scalar-completed leakage branch (1.1). Define `H0` by (2.5), and for `S>=0` define

`F_H(S)=S`, if `S<=H`,
`F_H(S)=H[1+log(S/H)]`, if `S>H`.                                (4.1)

Then for every `T>0` and `y in R`, the **full original quadratic form** satisfies

`boxed:`
`D_T law(Q)(y) <= 5 |a|^(-1/2) F_(H0)(sqrt(T)).`                 (4.2)

In particular,

`boxed:`
`D_T law(Q)(y)`
` <=20 sqrt(2)|a|^(-1/4)W2^(-1/8)`
`   *[1+log_+( sqrt(T)/H0 )]`.                                   (4.3)

#### Proof

Using (1.5), condition only on `V`. Equations (3.1)-(3.3) give

`D_T law(Q)(y)`
` <=5 |a|^(-1/2) E min(sqrt(T),|R-y|^(-1/2)).`                  (4.4)

Layer cake and (2.6) yield

`E min(sqrt(T),|R-y|^(-1/2))`
` = int_0^(sqrt(T)) P(|R-y|<s^(-2)) ds`
` <= int_0^(sqrt(T)) min(1,H0/s) ds`
` =F_(H0)(sqrt(T)).`                                             (4.5)

This proves (4.2). Since `F_H(S)<=H[1+log_+(S/H)]`, substitution of (2.5) gives (4.3). QED.

The dimensional scaling is correct. Under `A -> lambda A`, `a->lambda a`, `W2->lambda^6 W2`, and `T->T/lambda` in the Fourier variable; the prefactor `|a|^(-1/4)W2^(-1/8)` scales as `|lambda|^(-1)`, while the logarithm is dimensionless.

### Corollary 4.2 — almost-linear interval concentration for the full form

Combining (4.2) with account04/B01's interval majorant (1.7), every interval `I` of length `q` and center `y` satisfies

`boxed:`
`P(Q in I)`
` <= (5pi q/s0)|a|^(-1/2) F_(H0)(sqrt(2/q)),`                    (4.6)

where `s0=4 sin(1/2)^2`. In particular,

`P(Q in I)`
` <= (20 sqrt(2)pi/s0)|a|^(-1/4)W2^(-1/8) q`
`    *[1+log_+( sqrt(2/q)/H0 )].`                                (4.7)

This is a true full-coupled distribution-function estimate with only a logarithmic defect from the desired linear small-ball bound. It is uniform over arbitrary dense complementary curvature and over arbitrarily small nonzero pair determinant.

## 5. What this proves, and the exact remaining implication

The theorem does **not** prove bounded density in this branch: (4.3) grows logarithmically with `T`, so account04/B01's exact equivalence (1.6) does not close. This is a useful localization of the missing implication rather than a renamed solution.

The exact-null endpoint `delta=0` is already paid more strongly by preceding worker results. The collective-tail/diffuse cross regime satisfying (1.8) is also already paid continuously by the required newest-Claude theorem (1.9). Therefore the remaining B01 debt after this run is sharply restricted to the punctured near-null leakage state in which:

1. `delta!=0` is small enough that reciprocal pair estimates are poor;
2. the newest collective-tail gate (1.8) fails;
3. the partner's leakage alternative (1.1) carries the overlap-two currency; and
4. one must remove the single logarithm in (4.3), or route the same state to an already-paid mixed-Fresnel/ridge/grouped-coordinate/volume branch.

The logarithm cannot be removed merely by pretending the self coefficient `delta` is a perturbation: arbitrary unbounded input supports make a small matrix coefficient an uncontrolled random quadratic perturbation. The next mechanism must use the genuine additional target curvature/spectrum jointly with the random slope before the final square-root endpoint is taken.

This also explains why the pointwise phase-alignment correction and the present theorem are compatible. The law-uniform scalar Fresnel transform may be arbitrarily large at a prescribed frequency, but the actual product-form leakage produces a dimension-free residual square-root concentration estimate, and after the outer square this becomes an explicit signed-Fejer `O(log T)` rather than a false pointwise `O(T^-alpha)` claim.

## 6. Regularity and review status

- Residual `R`: (2.4) and (2.6) are proved; no `L^1` characteristic-function bound is obtained at `k=1`.
- Full `Q`: (4.2)-(4.7) are proved. They do not imply a bounded density because of the logarithmic growth.
- Continuous density: **not proved in this new branch**.
- Full QFORM: **OPEN**.
- Independent end-to-end review of Theorem 4.1: **pending**.
- Native learned-memory receiver use: **not verified**; repository retrieval/writeback is separate, so execution remains `WITHOUT_VERIFIED_BRAIN`.
