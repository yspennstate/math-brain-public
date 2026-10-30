# fleet03/B06 — modulated curved-fiber Wiener payment in the heavy-isotropic leakage branch

**Run:** `20260922T132210Z-fleet03-B06-qform-curved-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and live correction-aware starting point

The target remains: for every dimension, every independent real coordinate family with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension- and law-independent bound on the essential density of `X^T A X`, or give a valid counterexample.

This run preserves the current corrections. In particular it does **not** use law-uniform pointwise one-dimensional Fresnel decay, an unrestricted spectral-fiber supremum, independence after spectral rotation, a generic X-ray-only closure, bounded conditional density as a substitute for independence, or a universal extraction of one good physical principal block / Schur cross.

The previous B06 run proved the minority-sign/definite-Schur branch. The current first genuinely unpaid interface is the product-origin heavy-isotropic leakage state isolated by fleet03/B10 and fleet02/B10. In spectral coordinates `(e,f,g)`, with a physical heavy row `u_i=sqrt(c)e`, `c>1/2`, and `e^T Lambda e=0`, write

`Lambda = [[0,B,0],[B,r,s],[0,s,tau]]`,

so

`B^2 |tau| = |det Lambda| >=1`.                                      (1.1)

For the remaining original independent coordinates write

`u_j=s_j e+y_j f+z_j g`,

`T=sum s_j X_j`, `Y=sum y_j X_j`, `Z=sum z_j X_j`.

The Parseval identities give

`sum y_j^2=sum z_j^2=1`, `sum y_j z_j=0`,
`sum s_j y_j=sum s_j z_j=0`, `sum s_j^2=1-c`.                         (1.2)

The form is exactly

`Q=2B(sqrt(c)X_i+T)Y+rY^2+2sYZ+tau Z^2`.                             (1.3)

Fleet02/B10 proved that merely knowing a bounded `(Y,Z)` density and a bounded conditional density of `sqrt(c)X_i+T` given `(Y,Z)` cannot close (1.3): a genuine non-product three-variable density can engineer a logarithmic cancellation. Thus a valid next step has to retain the linear-product provenance in (1.2).

This run does so through a modulation-stable curved-fiber Wiener estimate.

## 2. Other-account results actually consumed

The exact assigned partner is `fleet04/B06`. At both startup and prepublication source reads there was no completed current-QFORM artifact at the canonical `fleet04/B06` research root or shared handoff root, so no exact-partner result or PASS is fabricated.

Two compatible completed fleet04 results are actually applied:

1. **fleet04/B19**, `QFORM-FINITE-UNION-CORE-v1`, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T122030Z-fleet04-B19-QFORM-r1/REPORT.md`. It proves with no loss of constant that the full concentration seminorm may be tested on densities `f_j=1_{E_j}` where each `E_j` is a bounded finite union of intervals of total measure one. I apply this to the branch (1.3): all estimates below may be read directly on that exact extremal core; the proof is actually uniform for all `0<=f_j<=1`, so no approximation debt is introduced.

2. **fleet04/B18**, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`. Its proof gives the source-valid domination

`p_{R+aV_R^2}(t) <= |a|^(-1/2) int p_R(r)|t-r|^(-1/2)dr`              (2.1)

whenever the conditional density of `V_R` is at most one. Section 6 below inserts the new half-Riesz estimate from this run into (2.1), yielding a new closed one-extra-square interface.

## 3. New lemma: modulation-stable transverse Wiener control

### Lemma 3.1 — `QFORM-MODULATED-TRANSVERSE-WIENER-v1`

Let the residual coordinates `X_j`, `j in J`, be independent with densities bounded by one. Let

`w_j=(y_j,z_j) in R^2`, `d_j=||w_j||^2`,

and assume

`sum_j w_j w_j^T=I_2`, `d_j<=1/2` for every `j`.                      (3.1)

Let the leakage coefficients `s_j` be completely arbitrary and put

`T=sum_j s_jX_j`, `Y=sum_j y_jX_j`, `Z=sum_j z_jX_j`.

For every real modulation frequency `xi`, define the complex measure on `R^2`

`nu_xi(A)=E[e^{i xi T} 1_{(Y,Z) in A}]`.

Then `nu_xi` has a density `h_xi(y,z)` such that, uniformly in `xi`,

`|| Fourier_{y,z} h_xi ||_1 <= (2pi)^2 e`,                            (3.2)

`||h_xi||_infinity <= e`,                                              (3.3)

and, for almost every fixed `y`, if

`tilde h_{xi,y}(eta)=int e^{i eta z} h_xi(y,z) dz`,

then

`int |tilde h_{xi,y}(eta)| deta <= 2pi e`.                             (3.4)

Moreover

`|h_xi(y,z)| <= p_{Y,Z}(y,z)` almost everywhere.                      (3.5)

Consequently, for every `tau!=0`, every real `a`, every `t!=0`, and almost every `y`,

`| int h_xi(y,z) exp(i t[tau z^2+2az]) dz |
 <= e sqrt(pi) |tau t|^(-1/2)`.                                      (3.6)

#### Proof

With the convention `hat f(theta)=int e^{i theta x}f(x)dx`,

`hat h_xi(eta)=prod_j hat f_j(xi s_j+<w_j,eta>)`.                     (3.7)

For fixed `xi`, modulation of `f_j` by `e^{i xi s_j x}` does not alter any `L^p` norm. Write `w_j=sqrt(d_j) omega_j` for nonzero rows. Then

`sum d_j omega_j omega_j^T=I_2`, `sum d_j=2`.

Apply the same geometric rank-one Brascamp--Lieb plus sharp Hausdorff--Young calculation already source-validated in the rank-two diffuse QFORM reports. Since `d_j<=1/2`, the conjugate Fourier exponents lie in the Hausdorff--Young range. It gives

`int prod_j |hat f_j(xi s_j+<w_j,eta>)| deta
 <=(2pi)^2 prod_j (1-d_j)^(-(1-d_j)/2).`                              (3.8)

Because `-(1-d)log(1-d)<=d` and `sum d_j=2`, the product in (3.8) is at most `e`. This proves (3.2). Fourier inversion gives (3.3).

For (3.4), partially invert only the `y` frequency:

`tilde h_{xi,y}(eta_z)
 =(2pi)^(-1) int e^{-i eta_y y} hat h_xi(eta_y,eta_z) deta_y`.

Integrating absolute values in `eta_z` and using (3.2) gives (3.4).

For (3.5), the total variation of `nu_xi` is dominated by the unmodulated pushforward law of `(Y,Z)`, because `|e^{i xi T}|=1`. Radon--Nikodym differentiation therefore yields the pointwise domination.

Finally invert only in `z` and use the exact Fresnel modulus

`|int exp(i t tau z^2+i beta z) dz|=sqrt(pi/|t tau|)`.

The `L^1` Fourier bound (3.4) gives (3.6). QED.

### Why this is not the refuted pointwise route

The phase is not being bounded against an arbitrary one-dimensional density. The payment in (3.6) comes only after the original residual product law has been converted into the **modulation-stable two-dimensional Wiener bound** (3.2). The leakage frequency `xi` is completely arbitrary and may depend on the curved trace point later. This is precisely information absent from the fleet02/B10 conditional-cap falsifier.

## 4. New theorem: heavy-isotropic transverse-diffuse branch has uniform 3/4 decay and L2 density

### Theorem 4.1 — `QFORM-HEAVY-ISOTROPIC-TRANSVERSE-WIENER-v1`

Assume the exact heavy-isotropic state (1.1)--(1.3), and in addition assume only the **transverse** diffuseness condition

`d_j=y_j^2+z_j^2<=1/2` for all residual physical coordinates `j`.      (4.1)

No restriction is placed on the normalized leakage quantities `s_j^2/(1-c)`. In particular, the whitened residual three-frame may be localized, so this theorem covers cases not paid by a diffuse-whitened-frame argument.

Then the characteristic function `phi_Q(t)=E exp(i tQ)` satisfies, for every `t!=0`,

`|phi_Q(t)|
 <= e^(1/2) pi^(3/4) [c B^2 |tau|]^(-1/4) |t|^(-3/4).`               (4.2)

Since `c>1/2` and `B^2|tau|>=1`, in particular

`|phi_Q(t)| <= 2^(1/4)e^(1/2)pi^(3/4)|t|^(-3/4)`.                    (4.3)

Consequently `phi_Q in L^2(R)`, the law of `Q` has an `L^2` density, and

`||p_Q||_2
 <= sqrt(3) e^(1/3)[c B^2|tau|]^(-1/6)
 <= sqrt(3) 2^(1/6)e^(1/3) <2.714.`                                  (4.4)

#### Proof

Let `h_xi` be Lemma 3.1's density. Integrating first in `X_i` and then in `T` gives the exact identity

`phi_Q(t)
 =int exp(i t r y^2) hat f_i(2B sqrt(c)t y) A_t(y) dy`,               (4.5)

where

`A_t(y)=int h_{2Bty}(y,z) exp(i t[2syz+tau z^2]) dz`.                 (4.6)

The modulation parameter in (4.6) is the **diagonal frequency** `xi=2Bty`; this is exactly where a generic projected-density argument loses the original product provenance. Lemma 3.1 was built to remain uniform under this diagonal modulation.

Put `m(y)=p_Y(y)`. By (3.5),

`|A_t(y)|<=m(y)`.                                                       (4.7)

By (3.6), uniformly in the same moving modulation,

`|A_t(y)|<=e sqrt(pi)|tau t|^(-1/2)`.                                 (4.8)

Thus, with

`a_t=e sqrt(pi)|tau t|^(-1/2)`,

`|A_t(y)|<=g_t(y):=min(m(y),a_t)`, and because `int m=1`,

`||g_t||_2^2<=a_t`.                                                     (4.9)

Now use Cauchy--Schwarz in (4.5). Plancherel and `0<=f_i<=1`, `int f_i=1`, give

`||hat f_i||_2=sqrt(2pi)||f_i||_2<=sqrt(2pi)`.

Therefore

`||hat f_i(2B sqrt(c)t ·)||_2
 <=sqrt(2pi)[2|B|sqrt(c)|t|]^(-1/2)`.                                 (4.10)

Combining (4.9)--(4.10) gives exactly (4.2):

`|phi_Q(t)|
 <= e^(1/2)pi^(3/4)|B|^(-1/2)c^(-1/4)|tau|^(-1/4)|t|^(-3/4)`
` = e^(1/2)pi^(3/4)[cB^2|tau|]^(-1/4)|t|^(-3/4).`

Together with `|phi_Q|<=1`, write `|phi_Q(t)|<=min(1,K|t|^(-3/4))`, where

`K=e^(1/2)pi^(3/4)[cB^2|tau|]^(-1/4`.                                (4.11)

The threshold is `T=K^(4/3)`. Direct integration gives

`int_R |phi_Q(t)|^2 dt <= 6K^(4/3)`.                                  (4.12)

Plancherel for finite measures now implies that the law has an `L^2` density and

`||p_Q||_2^2=(2pi)^(-1)||phi_Q||_2^2
 <=3 e^(2/3)[cB^2|tau|]^(-1/3)`,                                     (4.13)

which is (4.4). QED.

## 5. Stronger payment: a uniform half-Riesz potential

The same 3/4 decay gives the exact half-order potential needed by square-smoothing mechanisms.

### Corollary 5.1 — `QFORM-HEAVY-ISOTROPIC-HALF-RIESZ-v1`

Under Theorem 4.1,

`ess sup_x E|x-Q|^(-1/2)
 <=6 sqrt(2)e^(1/3)[cB^2|tau|]^(-1/6)`                               (5.1)

and hence, uniformly under the owner normalization,

`ess sup_x E|x-Q|^(-1/2)
 <=6*2^(2/3)e^(1/3)<13.293`.                                          (5.2)

#### Proof

With the Fourier convention used in the current QFORM half-Riesz reports,

`widehat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2)`.

Regularize at zero and infinity. By (4.11),

`int |t|^(-1/2)|phi_Q(t)|dt
 <=12K^(2/3)`.                                                         (5.3)

Indeed, split at `T=K^(4/3)`:

`2 int_0^T t^(-1/2)dt +2K int_T^infinity t^(-5/4)dt
 =12K^(2/3)`.

Divide by `sqrt(2pi)` and substitute (4.11), obtaining (5.1). Since `cB^2|tau|>1/2`, (5.2) follows. QED.

### What has actually been paid

The fleet02/B10 falsifier showed that the pair-density cap plus the conditional hyperbolic-variable cap alone can still hide a logarithmic cancellation. Corollary 5.1 rules out that failure mechanism in the transverse-diffuse **product-linear** state by proving a uniform half-Riesz bank. The argument never asks the rank-two indefinite piece itself to have a bounded density.

## 6. Actual application of fleet04/B18: one-extra-square closure

Fleet04/B18's proof gives (2.1) before it invokes the bathtub principle. Insert Corollary 5.1 directly into that source-valid inequality.

### Corollary 6.1 — `QFORM-TRANSVERSE-WIENER-PLUS-SQUARE-v1`

Let `R` be any heavy-isotropic transverse-diffuse rank-three variable satisfying Theorem 4.1. Suppose, conditionally on `R=r`, a real variable `V_r` has density at most one, with no independence required, and let `a!=0`. Then

`S=R+aV_R^2`

has an essentially bounded density satisfying

`||p_S||_infinity
 <=6 sqrt(2)e^(1/3)[cB^2|tau|]^(-1/6)|a|^(-1/2)`                    (6.1)

and therefore under the owner-normalized rank-three bank

`||p_S||_infinity <13.293 |a|^(-1/2)`.                               (6.2)

This is a literal application of the completed fleet04/B18 square-domination step to the new half-Riesz estimate. It closes any higher-rank QFORM subbranch that can peel one original-coordinate square over this rank-three core while retaining the conditional density cap. It is **not** asserted that every arbitrary-rank matrix admits such a peel.

## 7. Relation to the newest nested-localization reduction

The latest fleet01/B10 report proves a different theorem: after deleting a heavy row, if the **whitened residual three-frame** is diffuse, then the entire coupled remainder is paid (conditional on the supplied separable-phase theorem). In the heavy-isotropic notation its whitened row leverage is

`ell_j=s_j^2/(1-c)+y_j^2+z_j^2`.                                      (7.1)

Theorem 4.1 requires only

`y_j^2+z_j^2<=1/2`,                                                     (7.2)

and allows (7.1) to be arbitrarily larger than `1/2`. Thus it makes progress precisely in a portion of the nested-localization state where localization is carried by the leakage coordinate rather than by the two curved transverse directions.

A surviving hard rank-three branch can therefore be sharpened further:

- if the whitened residual frame is diffuse, use the current conditional-diffuse theorem;
- if it is whitened-localized but the transverse two-frame still satisfies (7.2), the present run supplies a universal `L^2` density and half-Riesz bank;
- a truly unprocessed nested branch must either contain a **transverse-heavy residual row** `y_j^2+z_j^2>1/2`, or require a new mechanism that upgrades the present half-Riesz payment to `L^infinity` without an extra square.

This is strictly stronger information than the old generic statement "heavy isotropic leakage remains open."

## 8. First unpaid implication

The full target remains **OPEN / NOT PROVED**. The next B06 obligation is

`QFORM-HEAVY-ISOTROPIC-HALFRIESZ-TO-LINF-OR-TRANSVERSE-HEAVY-v1`:

1. in the transverse-diffuse but whitened-localized state, upgrade the uniform half-Riesz payment (5.1) to an output `L^infinity` bound without assuming an additional independent/conditionally bounded square; or
2. in the complementary transverse-heavy state, use the physical row carrying more than half of the two-dimensional curved energy to expose a paid product-preserving hyperbolic/elliptic block or aggregate bank.

The new estimate suggests a concrete route for (1): retain the moving modulation `xi=2Bty` instead of taking Cauchy--Schwarz in `y`, and seek a second curved payment from the diagonal modulation itself. Any such step must be tested against the exact conditional-cap falsifier and the local-minor/cross-rank falsifiers.

Arbitrary extra spectral components remain a separate interaction debt except in branches where Corollary 6.1 or other completed conditional-square theorems actually apply. No continuity statement is claimed for Theorem 4.1.

## 9. Source pins / integrity

- Owner control at run start: `math-research-brain` revision `2026-09-22.5`, README blob `433b2d57345823967480245b59a7c47d51019c37`.
- Current correction inbox read before publication, including `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.
- fleet04/B19 finite-union core: report blob `6c1e768322445d808cbf9d85aae456ec3240a663`.
- fleet04/B18 dependent-square report: blob `f33758725ac803c6375215b522c86bd6409d2521`.
- fleet02/B10 heavy-isotropic conditional-cap falsifier: report blob `569826b23ae9863d5ff522392d3bc505d74b984a`.
- latest fleet01/B10 nested-localization report read before publication.

No simulation, source census, pointwise-law-uniform Fresnel claim, rotated-coordinate independence, unrestricted fiber supremum, or reciprocal-minor averaging is used as proof. The finite-union reduction is constant-preserving but not needed as an extra hypothesis. The full universal `L^infinity` conjecture remains open.
