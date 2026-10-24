# QFORM account02/B01 r27 — unnormalized overlap shears and a corrected weighted trace

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T200159Z-account02-B01-qform-r27`  
Assignment: `Oscillatory replacement`  
Status: `ESSENTIAL_STEP_APPLIED / CORRECTION_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Full target and fresh source boundary

The target remains the full arbitrary-matrix conjecture: for every dimension, independent real inputs with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `Q=X^T A X`, or produce a valid target counterexample.

Fresh control at the beginning of this run was brain main `8efb061f07e415755e0fd571d9c085629f585a9c`, OWNER CONTROL revision `2026-09-22.15`. A later source refresh observed main `6ea81e119e39a8c97e2480cccc3a5c057afbd123`; QFORM remained the sole target and no B01 stop appeared. The latest correction state is retained: no uniform pointwise scalar quadratic-phase decay, no post-rotation independence, no unrestricted arbitrary-joint rank-three coarea bound, no positive conditional-projection-density moment shortcut, and no worst-level scalar-remainder conditional-density supremum.

This run directly consumes the completed named-partner result account03/B01 r17, canonical report `yspennstate/math-open-problems@b6c3fd34d5c608023be5149189c1e88e66f3baeb:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T192922Z-r17/REPORT.md` and its decoupling addendum `yspennstate/math-open-problems@e3ea72181ebd1934c889703821a7a9396c5fb853:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T192922Z-r17/DECOUPLING_CRITICAL_LOSS.md`.

The partner proves the translation-uniform scalar Fresnel `L^p`, `p>2`, theorem and identifies the unnormalized overlap kernel

`K_f(u,s)=int f(x)f(x-u) exp(i s(2x-u)) dx`

as the object that must replace the divergent normalized conditional-`L^3` implementation. It records the global mixed identity `int int |K_f|^2 <= pi` and exhibits the valid family `f_R=1_[1,R]/(x log R)` on which the normalized critical factor grows like `(log R)^(1/3)`.

The new theorem below upgrades that single `L^2` identity to a full translation/shear-uniform mixed-norm family and, importantly, remains valid for complex `t`-dependent amplitudes produced by arbitrary within-bank phases. This is an exact source-valid step toward the current residual-leakage gap.

## 2. Mandatory pointwise counterexample remains in force

The phase-aligned construction is unchanged. For any fixed nonzero frequency `s` and arbitrarily small `delta>0`, the set

`{x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure. A measurable subset of measure one, used as a cap-one probability density, makes `Re E exp(i s X^2)>=cos(delta)`. Thus no law-uniform pointwise decay `|E exp(i t X^2)|<=C|t|^-alpha`, `alpha>0`, is available. Everything below is averaged/distributional and does not revive that false route.

## 3. New theorem: unnormalized overlap shear mixed norms

### Theorem 3.1 — `QFORM-OVERLAP-SHEAR-MIXED-NORM-v1`

Let `f` be a probability density on `R` with `0<=f<=L`, where `L>=1`. Let `a(x)` be any complex measurable function satisfying `|a(x)|<=f(x)`. Define

`g(u)=int f(x)f(x-u) dx`,

`K_a(u,s)=int a(x) conj(a(x-u)) exp(i s(2x-u)) dx`.

Then:

1. `0<=g<=L`, `int g=1`, and `|K_a(u,s)|<=g(u)`.
2. For every fixed `u`,

   `int_R |K_a(u,s)|^2 ds <= pi L^2 g(u)`.                    (3.1)

   In particular

   `int_R int_R |K_a(u,s)|^2 du ds <= pi L^2`.                (3.2)

3. For every `p>=2`, put `q=p/(p-1)`. Then

   `int_R [ int_R |K_a(u,s)|^q du ]^(p/q) ds <= pi L^2`.       (3.3)

4. The same estimate is uniform under every affine shear in phase space: for every real `alpha`,

   `int_R [ int_R |K_a(u,alpha u+beta)|^q du ]^(p/q) dbeta
      <= pi L^2`.                                               (3.4)

5. Consequently, for `t b!=0` and arbitrary real `a0,r`,

   `int_R [ int_R |K_a(u,t(a0 u+bv+r))|^q du ]^(p/q) dv
      <= pi L^2/(|t b|)`.                                      (3.5)

At the critical cubic value `p=3`, `q=3/2`, this becomes

`int_R [int_R |K_a(u,t(a0 u+bv+r))|^(3/2)du]^2 dv
 <= pi L^2/(|t b|)`.                                          (3.6)

The estimate contains no reciprocal difference density `g(u)^-1` and is uniform over fragmented supports.

### Proof

The pointwise assertions follow immediately from `|a|<=f`. Also

`int g(u)du=(int f)^2=1`.

For fixed `u`, set `h_u(x)=a(x)conj(a(x-u))`. With Fourier convention `hat h(xi)=int exp(i xi x)h(x)dx`,

`K_a(u,s)=exp(-isu) hat h_u(2s)`.

Plancherel and the change `xi=2s` give

`int |K_a(u,s)|^2 ds
 = pi int |a(x)|^2 |a(x-u)|^2 dx`.

Since `|a|^2<=f^2<=L f` twice, this is at most `pi L^2 g(u)`, proving (3.1)-(3.2).

For every fixed `s`, pointwise domination by `g` gives

`||K_a(.,s)||_1<=1`.

Interpolate only in the `u` variable between `L^1` and `L^2`. If `q=p/(p-1)` then the interpolation parameter is `theta=2/p`, hence

`||K_a(.,s)||_q^p
 <= ||K_a(.,s)||_1^(p-2) ||K_a(.,s)||_2^2
 <= ||K_a(.,s)||_2^2`.

Integrating in `s` and using (3.2) proves (3.3).

For the shear define `H(u,beta)=K_a(u,alpha u+beta)`. For every `beta`, `||H(.,beta)||_1<=1`, while the unit-Jacobian change `(u,beta)->(u,s=alpha u+beta)` preserves the global `L^2` norm. Repeating the preceding interpolation proves (3.4). Finally set `beta=t(bv+r)` and use `d beta=|tb|dv` to obtain (3.5). QED.

### Why this pays the partner's critical loss

For the partner's exact family `f_R=1_[1,R]/(x log R)`, the normalized conditional route creates

`I(f_R)=int g_R(u)^(2/3)|u|^(-1/3)du ~ const*(log R)^(1/3)`.

Theorem 3.1 instead gives, for every `R`, every shear, and `p=3`, the uniform right side `pi/(|tb|)` because `L=1`. Thus the logarithm is absent *before* the critical displacement integration: the divergence is caused by dividing by `g_R(u)` and then taking absolute coordinatewise conditional norms, not by the unnormalized overlap itself. This is a direct application of the named partner's completed construction, not a citation-only mention.

## 4. Leakage-preserving bank version

The theorem survives arbitrary internal phases in a disjoint original-coordinate bank.

Let a bank random vector `W` have the original product law, let `U=e.W` be a scalar aggregate with a density `p_U` satisfying `||p_U||_infinity<=L`, and let `R(W)` be an arbitrary real measurable function, finite almost surely. For every frequency `t`, disintegrate over `U` and define the complex scalar amplitude

`a_t(u)=p_U(u) E[exp(i t R(W)) | U=u]`.

Then

`|a_t(u)|<=p_U(u)`, `int |a_t(u)|du<=1`.

Therefore the overlap kernel constructed from `a_t` obeys every estimate in Theorem 3.1 with the same `L`, uniformly in `t` and uniformly in the internal phase `R`.

More concretely, suppose three disjoint banks produce scalar aggregates `U_1,U_2,U_3` and the full bank-level phase has the exact form

`Q = U^T M U + R_1(W_1)+R_2(W_2)+R_3(W_3)`,                  (4.1)

where the `R_i` may be arbitrary within their own banks. Then

`phi_Q(t)=int_R3 exp(i t u^T M u) prod_i a_(i,t)(u_i) du`,    (4.2)

and symmetrization gives the exact unnormalized identity

`|phi_Q(t)|^2
 = int_R3 prod_i K_(i,t)(delta_i, t(M delta)_i) d delta`.    (4.3)

Each `K_(i,t)` has the shear/mixed-norm budget (3.3)-(3.6), with no conditional density normalization and no post-rotation independence.

This is a useful precise interface for the latest three-bank programme. It does **not** by itself prove that a nonsingular compressed `M` remains a valid certificate under arbitrary `R_i`: a phase `R_i` containing a term `-M_ii U_i^2` can cancel diagonal curvature. Thus the remaining synthesis must use cross-bank credit from the *actual total quadratic form* or otherwise prevent such cancellation. The theorem pays the analytic one-bank overlap budget, not the still-unproved global structural/noncancellation step.

## 5. Full-matrix cross-edge corollary

The overlap identity also gives a simple leakage-safe estimate directly for the full original matrix.

### Corollary 5.1 — `QFORM-CROSS-EDGE-POINTWISE-v1`

For any two distinct original coordinates `i,k` with `b=A_ik!=0`, the full characteristic function satisfies

`|phi_Q(t)| <= min(1, sqrt(pi/(|t b|)))`.                      (5.1)

All diagonal terms, every other coupling, every other eigenvalue, and every input law remain arbitrary subject only to the original product density caps.

Proof. Use the exact coordinatewise decoupling identity

`|phi_Q(t)|^2 = int prod_j K_j(u_j,t(Au)_j) du`.

Take absolute values and dominate every factor except `i,k` by `g_j(u_j)`. Fix the remaining displacements. For the selected pair, Cauchy-Schwarz gives

`I <= [int |K_i(u_i,t(A_ii u_i+b u_k+r_i))|^2 du_i du_k]^(1/2)
      [int |K_k(u_k,t(b u_i+A_kk u_k+r_k))|^2 du_i du_k]^(1/2)`.

The changes `(u_i,u_k)->(u_i,s_i)` and `(u_i,u_k)->(u_k,s_k)` have Jacobian magnitude `|tb|`. By (3.2) with `L=1`, each square bracket is at most `(pi/(|tb|))^(1/2)`. Hence `I<=pi/(|tb|)`. The other `g_j` integrate to one, proving `|phi_Q(t)|^2<=pi/(|tb|)`. QED.

This is not enough for the full theorem—the exponent `1/2` is nonintegrable and is sharp as a one-cross-direction currency—but it is robust to exactly the residual leakage that invalidates treating a compressed scalar core in isolation.

## 6. Correction to account02/B01 r26 and exact salvage of its example

The previous B01 r26 report correctly refuted the worst-level scalar conditioning supremum, but its Section 6 attempted to justify a global weighted conditional-cap bound through a `K ||rho||_infinity^(2/3)` rank-three arbitrary-joint coarea estimate. Revision `.15` now source-validly refutes that arbitrary-joint lemma. Therefore **r26 equations (6.2)-(6.6) are not a valid general proof route and must not be used as a premise.**

The specific four-dimensional Hadamard example from r26 nevertheless has a valid weighted bound, by a different elementary argument.

Let `X_i` be iid `Unif[0,1]`, let the orthogonal Hadamard coordinates be `Y_1,...,Y_4`, and put

`Q_3=Y_1^2+Y_2^2-Y_3^2`.

The joint density of `Y=(Y_1,...,Y_4)` is exactly the indicator of the rotated unit cube. If `h(y)` is the marginal density of `Y_4`, then for almost every `y` with `h(y)>0`, the conditional density of `(Y_1,Y_2,Y_3)` is

`rho_y(z)=1_(slice_y)(z)/h(y)`.

Every selected coordinate `Y_1,Y_2,Y_3` lies in `[-1,1]`, so `rho_y` is dominated by `h(y)^(-1)` times Lebesgue measure on `[-1,1]^3`.

Under one-dimensional Lebesgue measure on `[-1,1]`, the pushforward by `x->x^2` has density `u^(-1/2) 1_(0,1)(u)`. The convolution of two such measures has density at most

`int_0^s du/sqrt(u(s-u)) <= pi`,

and convolving with the reflected third square measure, whose total mass is two, gives a density bound `2 pi` for the pushforward of three-dimensional cube Lebesgue measure under

`q(z)=z_1^2+z_2^2-z_3^2`.

Therefore

`||p_(Q_3 | Y_4=y)||_infinity <= 2 pi/h(y)`                  (6.1)

for almost every relevant `y`, and hence

`h(y) ||p_(Q_3 | Y_4=y)||_infinity <=2 pi`.                  (6.2)

The support of `Y_4=(X_1+X_2+X_3+X_4)/2` has length two, so

`E ||p_(Q_3 | Y_4)||_infinity <=4 pi`.                       (6.3)

For the r26 residual `Q'=Y_4^2/128`, the map `Y_4->Q'` is one-to-one on `[0,2]`, hence

`E ||p_(Q_3 | Q')||_infinity <=4 pi`.                        (6.4)

Thus the **specific weighted-trace conclusion for the Hadamard example is salvaged with an explicit constant `4 pi`**, but the false arbitrary-joint coarea premise is removed. This distinction is essential: (6.4) uses the actual bounded cube section geometry and does not extend to arbitrary joint cap-one sources.

## 7. Exact weighted-trace Fourier interface

For any decomposition `Q=Q_3+Q'`, let `mu_t(db)` be the complex measure

`mu_t(E)=E[ exp(i t Q_3) 1_{Q' in E} ]`.

Whenever it has a Lebesgue density `m_t(b)`, Fourier inversion in the first coordinate gives the source-valid sufficient interface

`int ||p_(Q_3,Q')(.,b)||_infinity db
 <= (1/(2 pi)) int_R ||m_t||_(L^1(db)) dt`.                  (7.1)

The left side is exactly

`E_(Q') ||p_(Q_3 | Q')||_infinity`

when regular conditional densities exist. Crucially, (7.1) contains the **unnormalized** scalar-level Fourier measure `m_t`; it never divides by `p_(Q')(b)`. This is the correct Fourier counterpart of the correction to worst-level conditioning.

There is also a vector-valued one-pivot estimate. If `X` is independent of an outside variable `W`, `f_X<=1`, `a!=0`, and

`Q_3=aX^2+B(W)X+C(W)`, `Q'=R(W)`,

then, with `nu_t` the analogous complex measure in the `Q'` coordinate,

`|| ||nu_t||_(TV) ||_(L^p(dt))
 <= C_p |a|^(-1/p), p>2`,                                    (7.2)

where `C_p` is the named partner's translated-Fresnel constant. Indeed, condition on `W`: `nu_t` is the pushforward of the complex weights `F_W(t)`, so `||nu_t||_(TV)<=E_W |F_W(t)|`; Minkowski followed by the partner theorem gives (7.2). This is a genuine distributional replacement for a false pointwise conditional bound, but one pivot alone does not make the right side of (7.1) integrable.

## 8. Relation to the newest three-bank result

During this run account02/B05 published `QFORM-THREE-BANK-GENERAL-CORE-v1` at `yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`. It proves `<36/s` once three **independent scalar aggregates** with density-normalized compressed `3x3` core have `sigma_min>=s`; the old arrowhead zero pattern is unnecessary. Its explicit first unpaid step is preservation/extraction of that three-scalar interface in the presence of within-bank quadratic residual dependence.

Equations (4.2)-(4.3) above give an exact analytic representation of precisely that leakage: every bank residual is retained inside a complex amplitude, while its unnormalized overlap keeps the full shear budget (3.3)-(3.6). What remains unpaid is a multi-bank Brascamp-Lieb / signed-Fejer synthesis that converts these individual overlap budgets plus the **total** three-large-eigenvalue geometry into `L^1_t`, without assuming the compressed core survives a canceling internal phase.

## 9. First unpaid implication

`QFORM-LEAKAGE-SAFE-THREE-BANK-OVERLAP-SYNTHESIS-v1`:

Starting from the exact bank identity (4.3), prove a dimension-free `L^1_t` / signed-Fejer bound whenever the full target matrix has three large spectral directions and the three-bank extraction supplies enough cross-bank credit, while allowing the bank amplitudes `a_(i,t)` to be arbitrary complex functions dominated by their certified scalar aggregate marginals. Equivalently, find the correct noncancellation currency of the **total** quadratic form that can be paired with the shear mixed norms (3.3)-(3.6). A theorem depending only on a compressed diagonal curvature that can be canceled by `R_i` is invalid.

This is strictly downstream of the named partner's mixed-overlap identity and the new B05 general scalar-core theorem. It does not assume the false conditional normalization, arbitrary-joint coarea, or pointwise Fresnel decay.

Full QFORM remains OPEN. This is not a full-proof candidate and has not received two end-to-end independent reviews.

## 10. Provenance / computation

No numerical computation is used as mathematical evidence in this report. Every displayed constant follows symbolically from Plancherel, interpolation, Jacobian changes, convolution, and the cited completed source theorems. Operational timestamps are recorded separately in the run metadata and are not mathematical premises.
