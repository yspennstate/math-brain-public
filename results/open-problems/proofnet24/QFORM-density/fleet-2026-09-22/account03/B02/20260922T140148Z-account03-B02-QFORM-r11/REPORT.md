# account03/B02 — integrated square Fourier budget and an overlap-free rank-three closure

**Run:** `20260922T140148Z-account03-B02-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Integrated Fourier estimate  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and live corrections

The full target remains open: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the essential supremum of the density of `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

This run uses no law-uniform pointwise scalar Fresnel decay, no independence after a spectral rotation, no moment/support/log-concavity assumptions, no fiber supremum, and no conditional-density-cap substitute for genuine independence. It also does not use the refuted single-Schur or local-cross-rank-three extraction claims.

The designated partner `account04/B02` still had no completed QFORM handoff at both the startup and prepublication checks. No result is attributed to that worker. A compatible completed same-pathway result is actually applied below: `account01/B02`, canonical report `yspennstate/math-open-problems@e58461e07b19315b290cb4b397929090ec6f48b9:proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260922T132111Z-qform-a01-b02-r12/REPORT.md`. Its rank-two diffuse residual estimate is inserted into the new Fourier inequality in Section 4.

The main mechanism change is to spend a **law-uniform integrated Fourier budget of a physical square**, rather than ask for false pointwise decay.

---

## 2. A sharp-enough law-uniform `L^3_t` budget for one physical square

### Lemma 2.1 — `QFORM-SINGLE-SQUARE-L3-FOURIER-v1`

Let `V` be any real random variable with probability density `f` satisfying `0<=f<=1`, and let `d!=0`. Put

`Y=d V^2`, `psi(t)=E exp(i t Y)`.

Then `Y` has a density `g_d` with

`||g_d||_(3/2) <= 2 |d|^(-1/3)`,                                    (2.1)

and its characteristic function obeys

`boxed( ||psi||_3 <= 2 * 3^(1/6) * pi^(1/3) * |d|^(-1/3). )`        (2.2)

The same bound holds after an arbitrary deterministic translation of `V`.

### Proof

First take `d=1`. For `y>0`, the density of `V^2` is

`g(y)=[f(sqrt(y))+f(-sqrt(y))]/[2 sqrt(y)]`.

Set `y=x^2`. Then

`int_0^infinity g(y)^(3/2) dy`
`= 2^(-1/2) int_0^infinity x^(-1/2)[f(x)+f(-x)]^(3/2) dx`.

Using `(u+v)^(3/2)<=sqrt(2)(u^(3/2)+v^(3/2))` and `f^(3/2)<=f`,

`int g^(3/2) <= int_R |x|^(-1/2) f(x) dx`.                         (2.3)

Among all `0<=f<=1` of mass one, the last integral is maximized by filling the region where `|x|^(-1/2)` is largest, namely the interval `[-1/2,1/2]`. Hence

`int_R |x|^(-1/2)f(x)dx <= 2 int_0^(1/2) x^(-1/2)dx = 2 sqrt(2)`.

Therefore

`||g||_(3/2) <= (2sqrt(2))^(2/3)=2`.                               (2.4)

Scaling by `d` gives (2.1), because an `L^(3/2)` density norm scales by `|d|^(-1/3)`.

For the unnormalised Fourier convention `hat h(t)=int exp(i t x)h(x)dx`, sharp Hausdorff--Young at input exponent `3/2` and output exponent `3` gives

`||hat h||_3 <= (2pi)^(1/3) [3^(1/6)/2^(1/3)] ||h||_(3/2)`
`= pi^(1/3)3^(1/6)||h||_(3/2)`.

This is the same Beckner constant already source-pinned and used in the completed diffuse-frame work. Insert (2.1) to obtain (2.2). Translation of `V` leaves the assumptions and the proof unchanged. QED.

### Corollary 2.2 — every nonzero physical diagonal gives a full-form `L^3_t` estimate

Let `Q=X^T A X` be any quadratic form under the exact product-density assumptions, with no rank or spectral restriction. If one physical diagonal entry `d=A_kk` is nonzero, then

`boxed( ||phi_Q||_3 <= 2*3^(1/6)pi^(1/3)|d|^(-1/3). )`              (2.5)

Indeed, condition on all variables except `X_k` and complete the physical square:

`Q=d(X_k+H)^2+R`,                                                    (2.6)

where `H,R` are functions of the other original coordinates. For each fixed conditioning value, Lemma 2.1 applies with the same constant. If `psi_h(t)` is the conditional characteristic function of the square term, then

`phi_Q(t)=E[e^(itR) psi_H(t)]`.

Minkowski in `L^3(dt)` yields

`||phi_Q||_3 <= E ||psi_H||_3`,

and (2.5) follows. No conditional density of a transformed light variable is asserted. Only the original physical `X_k`, genuinely independent of the conditioning sigma-field, is used.

This is a global integrated Fourier estimate for an arbitrary coupled matrix whenever a physical diagonal is nonzero. It is **not** by itself an `L^1_t` estimate, so it does not prove the target density bound.

---

## 3. The diagonal target actually satisfies a uniform `L^1_t` criterion

The phase-aligned-support correction refutes law-uniform pointwise decay, but it does not refute a uniform integrated Fourier estimate even on the adversarial input class.

### Corollary 3.1 — `QFORM-DIAGONAL-L1-FOURIER-v1`

Suppose `A` is diagonal and has three diagonal coefficients `d_1,d_2,d_3` with `|d_j|>=1`. All other diagonal coefficients may be arbitrary. Then

`boxed( ||phi_Q||_1 <= 8 sqrt(3) pi (|d_1d_2d_3|)^(-1/3) <= 8sqrt(3)pi. )`  (3.1)

Consequently `Q` has a bounded **continuous** density and

`boxed( ||p_Q||_infinity <= 4sqrt(3) < 6.929. )`                    (3.2)

### Proof

For a diagonal form the three selected square terms are independent, and the characteristic function of every remaining independent term has modulus at most one. Thus

`|phi_Q(t)| <= product_(j=1)^3 |psi_j(t)|`.

Hölder with exponents `(3,3,3)` and Lemma 2.1 gives

`||phi_Q||_1 <= product_j ||psi_j||_3`
`<= [2*3^(1/6)pi^(1/3)]^3 (|d_1d_2d_3|)^(-1/3)`
`=8sqrt(3)pi (|d_1d_2d_3|)^(-1/3)`.

Fourier inversion gives (3.2) and a continuous representative. QED.

The already-known direct physical-space diagonal estimate `||p_Q||_infinity<=pi` is numerically sharper for essential boundedness. The new point is different: it proves that the **integrated Fourier criterion itself survives arbitrary fragmented cap-one input laws** on the full diagonal target, and it supplies continuity directly.

---

## 4. New closure when the square shift and rank-two residual use independent product resources

The previous compatible `account01/B02` result gives, in a rank-exactly-three unique-heavy decomposition, a rank-two residual with a law-uniform `L^(3/2)_t` budget. Combining it with Lemma 2.1 pays the small-diagonal branch completely whenever the square shift and residual are genuinely independent. Importantly, the small physical pivot cancels from the final constant.

### Theorem 4.1 — `QFORM-INDEPENDENT-SHIFT-RESIDUAL-L1-v1`

Let `X` have a density bounded by one and be independent of a pair `(H,R)`. Assume additionally that `H` and `R` are independent. Let `d!=0`, and set

`Q=d(X+H)^2+R`.                                                      (4.1)

If `phi_R in L^(3/2)` with norm `M`, then

`boxed( ||phi_Q||_1 <= 2*3^(1/6)pi^(1/3)|d|^(-1/3) M. )`            (4.2)

Hence `Q` has a bounded continuous density with

`||p_Q||_infinity <= 3^(1/6)pi^(-2/3)|d|^(-1/3)M`.                 (4.3)

### Proof

Because `X` is independent of `H`, the convolution `V=X+H` has a density bounded by one. Because `H` is independent of `R` and `X` is independent of `(H,R)`, `V` is independent of `R`. Therefore

`phi_Q(t)=phi_(dV^2)(t) phi_R(t)`.

Apply Hölder with exponents `3` and `3/2`, then Lemma 2.1. This gives (4.2). Fourier inversion yields (4.3) and continuity. QED.

### Application to the compatible account01/B02 unique-heavy residual

Use exactly the notation of the completed account01/B02 report. For a rank-exactly-three form

`A=U Lambda U^T`, `U^TU=I_3`,

choose its unique leverage-heavy physical row `k`, with `c=||u_k||^2>1/2`. In spectral coordinates with `u_k=sqrt(c)e_1`, write

`Lambda=[[a,b^T],[b,C]]`, `d=A_kk=ca`,

and complete the physical square as

`Q=d(X_k+H)^2+R`,                                                    (4.4)

where the rank-two residual is `R=Z^T S Z`, `S=C-bb^T/a`, and

`|det S|=|det Lambda|/|a|=c|det Lambda|/|d|`.                       (4.5)

For the unique-heavy geometry the transverse frame is diffuse. The completed account01/B02 estimate gives

`|phi_R(t)| <= min(1, pi e |det S|^(-1/2)/|t|)`

and therefore

`||phi_R||_(3/2) <= (6pi e)^(2/3)|det S|^(-1/3).`                  (4.6)

This is the named compatible peer result applied to an actual inequality.

If, in addition, the completed-square shift `H` is genuinely independent of `R` (for example because a product-preserving structural reduction places the shift and rank-two residual on disjoint independent coordinate banks), insert (4.6) into Theorem 4.1. The exact factors simplify as

`|d|^(-1/3)|det S|^(-1/3)=c^(-1/3)|det Lambda|^(-1/3)`.             (4.7)

Thus

`boxed( ||phi_Q||_1 <= 2^(5/3)3^(5/6) pi e^(2/3)
                     c^(-1/3)|det Lambda|^(-1/3). )`               (4.8)

and

`boxed( ||p_Q||_infinity <= 2^(2/3)3^(5/6)e^(2/3)
                           c^(-1/3)|det Lambda|^(-1/3). )`          (4.9)

Under the target rank-three normalization `|det Lambda|>=1` and `c>1/2`,

`||p_Q||_infinity <= 2*3^(5/6)e^(2/3) < 9.732.`                    (4.10)

This bound is independent of how small `d` is, as long as `d!=0`. The cancellation in (4.7) is the key new quantitative point: on an overlap-free product decomposition, the cross-dominant/small-diagonal regime is not singular at all.

The theorem does **not** replace independence by a conditional density cap. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` is therefore respected exactly.

---

## 5. Why the remaining overlap problem cannot be closed by abstract norm interpolation

In the general unique-heavy decomposition, `H` and `R` are functions of the same light physical coordinates, so Theorem 4.1 does not apply. Two valid estimates are then available:

1. the new global pivot budget `phi_Q in L^3`, equation (2.5);
2. in the cross-dominant small-diagonal branch, the compatible account02/B02/account01-B02 route supplies a pointwise `O(|t|^(-1/2))` envelope.

These two statements alone cannot imply `L^1`. As an abstract analytic sanity check, on `[1,T]` the functions

`F_T(t)=t^(-1/2) 1_[1,T](t)`

have uniformly bounded `L^3` norm but `||F_T||_1=2(sqrt(T)-1)` diverges. This is **not** a characteristic-function counterexample and is not a counterexample to QFORM; it only proves that the current two inequalities, if used solely as black-box norm/envelope statements, are insufficient.

Therefore the next step has to preserve the actual dependence/cancellation of the light product coordinates.

---

## 6. Exact first unpaid implication after this run

The first unpaid implication for B02 is now narrower than the previous generic Schur-or-aggregate statement:

### `QFORM-OVERLAPPED-SHIFT-RESIDUAL-FOURIER-v1` — OPEN

In the rank-three unique-heavy decomposition

`Q=d(X_k+H(Y))^2+R(Y)`

with a diffuse rank-two residual and arbitrary cap-one product law for the original light coordinates `Y`, prove a dimension-free `L^1_t` characteristic-function or direct linear small-ball estimate **without assuming `H(Y)` independent of `R(Y)`**.

The new theorem shows that all reciprocal small-pivot loss disappears once the overlap is removed. Hence the actual debt is now precisely the shared-coordinate correlation between the shift and the rank-two saddle, not the size of `d`.

A useful exact representation explains what must be controlled. If `H=l.Y` is linear and `R=(V^T Y)^T S(V^T Y)`, first Fourier-transform the shifted-square kernel in `H` and use the two-dimensional Fresnel representation for `R`. Before absolute values this gives a three-frequency oscillatory integral whose product factors are

`hat f_k(-s) * product_j hat f_j(<v_j,xi>-s l_j)`,                  (6.1)

with a total Fresnel prefactor proportional to

`|t|^(-3/2)|d det S|^(-1/2)`.                                      (6.2)

Taking the **entire** `(s,xi)` integral in absolute value is too strong: the live phase-Wiener correction already shows that such absolute spectral obligations can diverge even for bounded-density QFORM examples. The required next mechanism must therefore retain at least one Fresnel/time cancellation while spending the high-power Fourier budgets of the original product factors. A mixed-norm or phase-retaining Brascamp--Lieb estimate is the concrete next derivation.

After rank-exactly-three overlap is closed, arbitrary additional nonseparable spectral directions remain a separate full-target debt. The interactive regularized-determinant theorem closes the full-spectrum diffuse-range branch but does not remove this heavy-coordinate overlap obstruction.

---

## 7. Constants and status discipline

Exact constants checked algebraically:

- single square: `2*3^(1/6)*pi^(1/3) = 3.517765...` in `L^3_t` per `|d|^(-1/3)`;
- diffuse rank-two residual factor: `(6*pi*e)^(2/3) = 13.795276...` per `|det S|^(-1/3)`;
- product `L^1_t` prefactor before the spectral cancellation: `48.52854...`;
- density prefactor in (4.9): `2^(2/3)3^(5/6)e^(2/3)=7.723557...` before `c^(-1/3)|det Lambda|^(-1/3)`;
- unique-heavy target branch `c>1/2`, `|det Lambda|>=1`: `<9.731073`.

**Proved this run:** Lemma 2.1, Corollary 2.2, Corollary 3.1, Theorem 4.1, and the overlap-free unique-heavy application (4.8)--(4.10).

**Not proved:** independence of the square shift and residual in the general unique-heavy geometry; the overlapped mixed-norm estimate; the at-least-two-heavy geometry; arbitrary extra spectral directions; the full conjecture.

The full target remains `OPEN`. No counterexample to the owner conjecture is claimed. Essential boundedness versus continuity is stated separately: Sections 3 and 4 obtain continuity because `phi in L^1`; the global estimate (2.5) alone gives neither an `L^infinity` density nor continuity.

## 8. Source pins actually used

- Fresh owner/control state: `yspennstate/math-research-brain`, programme revision `2026-09-22.5`; initial source head `7262469c70ff2e86837f6751eee8006ff0a64681`, refreshed during the run with unchanged owner order.
- Compatible completed same-pathway peer: account01/B02, `yspennstate/math-open-problems@e58461e07b19315b290cb4b397929090ec6f48b9:proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260922T132111Z-qform-a01-b02-r12/REPORT.md`.
- Diffuse Fourier/Beckner source chain: account03/B08, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T114830Z-account03-B08-qform-diffuse-v1/REPORT.md`, which source-pins W. Beckner, *Inequalities in Fourier Analysis*, PNAS 72 (1975), 638--641.
- Current phase-Wiener correction: `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`, canonical correction commit `2a6981ee2518d8b92f734b5763e89d5bf26a8048`.
- Interactive regularized-determinant handoff: canonical math commit `a302aab3477c64757b511e80d3907f982e04873a`.

No paid model/API call, no installation work, no public release, and no native learned-memory ingestion occurred.