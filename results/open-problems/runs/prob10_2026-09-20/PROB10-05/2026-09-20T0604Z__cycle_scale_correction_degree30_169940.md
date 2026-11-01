Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. PROB10-05 correction + source metric movement: the current `0.16798` repository candidate depended on an invalid softened-cycle trace normalization; the last unaffected certified endpoint is `1647/10000=0.1647`. This run repairs the route and proves the stronger candidate `8497/50000=0.16994 < theta_{2,1/4} <= 1/4`, so the rigorously supported repository gap moves `0.0853 -> 0.08006`.**

# PROB10-05 bounded research iteration — softened-cycle scale correction and degree-30 spectral certificate

**Status: PARTIAL / source target OPEN / self-check complete / independent validation still required.** The exact value of `theta_{2,1/4}` is not determined. The external source bracket remains `1/8 <= theta_{2,1/4} <= 1/4`; the stronger lower bound below is repository research progress, not a literature claim.

The corrected candidate is

\[
\boxed{\frac{8497}{50000}=0.16994<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}<\frac{4003}{50000}=0.08006}.
\tag{0.1}
\]

The important point of this run is both corrective and positive: it finds an exact scale error in the softened four-cycle trace refinement used by the recent `0.16798` chain, gives an independent finite-dimensional contradiction to that trace cap, rolls the rigorous baseline back to the last unaffected `0.1647` result, and then exceeds the withdrawn candidate using a new degree-30 quasimode together with the older, scale-safe hard-edge trace bound.

## 1. Frozen source model, exponent existence, and current literature

Freeze centered standard fractional Brownian motion at `H=1/4`,

\[
\mathbb E B_H(t)B_H(s)=\frac12\bigl(t^{2H}+s^{2H}-|t-s|^{2H}\bigr),
\]

and

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\tag{1.1}
\]

The source event is the continuous one-sided fixed-barrier event

\[
p(T)=\Pr\left\{\sup_{0\le t\le T}I(t)\le1\right\}
=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.2}
\]

No two-sided interval, Riemann--Liouville substitute, or discretely sampled definition is substituted for (1.2).

The controlling source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11, repository-recorded revision 4 July 2026. The full relevant result was already recovered in the immediately preceding PROB10-05 continuity chain: Statement 1.2(a) gives existence of the persistence exponent and equality with the Lamperti-dual exponent throughout

\[
\Omega=\{(\alpha,H):\alpha+H>1,\ 0<H<1\}.
\]

Thus `(alpha,H)=(2,1/4)` is inside the proved existence regime. The same current source explicitly reports the old general proposal `theta_{2,H}=H(1-H)` as false; that refutation is Molchan's result, not ours, and it is not used as a target here. The one-sided `alpha=2`, `H!=1/2` values remain the source's unresolved regime.

A fresh bounded primary-source search on 20 September 2026 rechecked arXiv:2509.10265 and later nearby work. It recovered Molchan arXiv:2608.26680 (multivariate-time fBM), Aurzada--Müller arXiv:2603.14934 (random Hurst exponent), Aurzada--Helmer arXiv:2608.17463 (fractional Levy fields on Riemannian index sets), and the previously archived Aurzada--Kilian endpoint-asymptotic work. None of the retrieved statements determines the continuous one-sided integrated-fBM exponent at `H=1/4`. This is bounded negative evidence only, not a worldwide novelty certificate.

The source-displayed special-point bracket retained by this track is

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\tag{1.3}
\]

## 2. Consumed repository state and ownership

This run consumed current `master` versions of:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md` (no integrated-fBM/Molchan posting exclusion);
- `operations/claims/MOLCHAN-2025-THETA2H.md`, whose canonical owner remains `HARD7-05`;
- newest substantive PROB10-05 report `runs/prob10_2026-09-20/PROB10-05/2026-09-20T0512Z__degree22_ritz_167980.md`;
- the pre-refocus HARD7-05 chain, especially `2026-09-19T2100Z__soft_edge_164000.md`, `2026-09-19T2148Z__softening_frontier_164700.md`, and `2026-09-19T2250Z__triple_orthant_trace_164800.md`;
- exact predecessor checkers `2026-09-19T2058Z__soft_edge_exact_check.py`, `2026-09-19T2140Z__softening_frontier_exact_check.py`, and `2026-09-19T2244Z__triple_orthant_trace_exact_check.py`;
- complementary non-owning T05 report `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0443Z__u16-mills-composition-1654871.md`.

No ownership transfer is made. The PROB10 refocus is still a continuation of the canonical HARD7-05 problem. This report does not overwrite the complementary T05 files; it records that the common softened-cycle trace input used there requires correction.

The mathematical idea and all three attacks were written before the new checker in

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0544Z__cycle_scale_audit_degree30_idea.md`

at commit `9d8930a170036c330a754f5254335f06aee66d2a`.

## 3. Frozen valid Lamperti comparison

For `H=1/4`, keep the already proved unit-variance Lamperti dual

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau),
\]

and the frozen softened AR-edge comparator parameters

\[
r=\frac78,
\qquad s=\frac{24861}{25000},
\qquad c=s\frac{1+r}{2}=\frac{74583}{80000}.
\tag{3.1}
\]

The earlier exact covariance calculation proves for every integer `k>=1`

\[
R(r^k)<cr^{k-1},
\tag{3.2}
\]

where `R` is the Lamperti covariance. This part does not use the four-cycle trace refinement corrected below.

Let

\[
(Kf)(x)=\int p_r(x,dy)\,
\Phi\!\left(-\sqrt{\frac{s}{1-s}}
\frac{x+y}{\sqrt{2(1+r)}}\right)f(y).
\tag{3.3}
\]

Detailed balance and symmetry of the killing weight make `K` compact self-adjoint on `L^2(phi)`. Its kernel is strictly positive, so its spectral radius `lambda_1` is its simple positive Perron eigenvalue.

With `Delta=4 log(8/7)`, the continuous event is deterministically contained in the grid event,

\[
\{X(t)<0\ \forall 0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=1,\dots,n\}.
\tag{3.4}
\]

Slepian and (3.2) therefore give the source-valid continuous lower-bound implication

\[
\boxed{\theta_{2,1/4}\ge
\frac{-\log\lambda_1}{4\log(8/7)}.}
\tag{3.5}
\]

There is exactly zero interpolation loss in this direction. Nothing below uses the invalid reverse implication from sampled survival to continuous survival.

## 4. Attack A — exact audit of the softened four-cycle scale: the recent trace cap is invalid

This attack deliberately tried to falsify the inherited spectral input before sharpening it.

### 4.1 Where the scale was lost

In the four-step trace expansion for the AR kernel, after normalizing the cyclic Gaussian measure, the actual loop-vertex covariance at cyclic distance `d` is

\[
G_d=\frac{r^d+r^{4-d}}{1-r^4},
\qquad d=0,1,2,3.
\tag{4.1}
\]

In particular

\[
G_0=\frac{1+r^4}{1-r^4}>1.
\tag{4.2}
\]

The convenient quantities

\[
a=\frac{r+r^3}{1+r^4},
\qquad b=\frac{2r^2}{1+r^4}
\tag{4.3}
\]

are **correlations**, obtained after dividing all loop vertices by `sqrt(G_0)`.

For the hard-edge sign event (`s=1`), this common positive rescaling is harmless. It is not harmless after adding fixed unit-variance independent edge noise. Under the loop measure put

\[
S_i=\frac{X_i+X_{i+1}}{\sqrt{2(1+r)}},
\qquad
V_i=\sqrt{s}\,S_i+\sqrt{1-s}\,E_i,
\tag{4.4}
\]

with iid standard `E_i`. If `v_u,g_u,h_u` are the variance/adjacent/opposite covariance computed from the unit-variance rescaled loop, then the actual signal values before adding noise are

\[
v=G_0v_u,\qquad g=G_0g_u,\qquad h=G_0h_u.
\tag{4.5}
\]

Therefore the true softened correlations are

\[
\rho_{\rm adj}=\frac{sG_0g_u}{sG_0v_u+1-s},
\qquad
\rho_{\rm opp}=\frac{sG_0h_u}{sG_0v_u+1-s},
\tag{4.6}
\]

not the formulas with `G_0` omitted.

At the frozen exact parameters the checker proves

\[
\rho_{\rm adj}^{\rm old}
=\frac{168557580}{170952323}
=0.9859917492\ldots,
\]

but

\[
\boxed{\rho_{\rm adj}^{\rm true}
=\frac{11237172}{11352323}
=0.9898566134\ldots},
\tag{4.7}
\]

and similarly

\[
\rho_{\rm opp}^{\rm old}
=\frac{167065920}{170952323}
=0.9772661585\ldots,
\]

whereas

\[
\boxed{\rho_{\rm opp}^{\rm true}
=\frac{11137728}{11352323}
=0.9810968204\ldots}.\tag{4.8}
\]

Both true correlations are strictly larger. Hence the old softened-loop orthant estimate cannot be retained as an upper bound by monotonicity.

### 4.2 Independent finite-dimensional contradiction to the old trace cap

To make the correction independent of merely inspecting the derivation, let `P_11` be the orthogonal projection in `L^2(phi)` onto the first twelve probabilists' Hermite polynomials `He_0,...,He_11`. Since `K` is self-adjoint Hilbert--Schmidt,

\[
\operatorname{tr}((P_{11}KP_{11})^4)
=\|P_{11}KP_{11}\|_{S_4}^4
\le \|K\|_{S_4}^4
=\operatorname{tr}(K^4).
\tag{4.9}
\]

The new exact checker evaluates every matrix entry `\langle He_i,KHe_j\rangle` by the same outward-rational truncated-Gaussian moment recurrences used in the previous Ritz certificates. In the Hermite coordinate matrix it then multiplies four times with interval arithmetic and certifies

\[
\operatorname{tr}((P_{11}KP_{11})^4)
>1.08546756149.
\tag{4.10}
\]

But the recent chain used

\[
\operatorname{tr}(K^4)<1.081798,
\tag{4.11}
\]

and the complementary route later sharpened this to `1.08178606`. Equation (4.10) is an exact contradiction to (4.11), so those softened-cycle trace caps are withdrawn as certified inputs.

Consequently, the recent `0.16798` endpoint is not retained on the basis of its published checker. The last unaffected lower endpoint in the repository chain is the `2026-09-19T2148Z` result

\[
\boxed{\theta_{2,1/4}>\frac{1647}{10000}=0.1647},
\tag{4.12}
\]

whose checker uses only the older hard-edge cap and the valid soft-vs-hard monotonicity theorem.

### 4.3 Why the older soft-vs-hard trace comparison remains valid

The `2026-09-19T2100Z` proof did not normalize away `G_0`. Under the actual cyclic loop law, every covariance `Cov(S_i,S_j)` is positive. For

\[
V_i(s)=\sqrt{s}S_i+\sqrt{1-s}E_i,
\]

with common signal variance `v` and signal covariance `g_{ij}>0`,

\[
\operatorname{Corr}(V_i(s),V_j(s))
=\frac{s g_{ij}}{1+s(v-1)}.
\tag{4.13}
\]

Differentiation gives

\[
\frac{d}{ds}\operatorname{Corr}(V_i(s),V_j(s))
=\frac{g_{ij}}{(1+s(v-1))^2}>0.
\tag{4.14}
\]

Slepian therefore implies the four-negative orthant probability, and hence the normalized fourth trace, increases with `s`. Thus the still-valid bound is

\[
\operatorname{tr}(K_{r,s}^4)
\le \operatorname{tr}(K_{r,1}^4)
<\frac{553151}{500000}=1.106302.
\tag{4.15}
\]

This is weaker than the invalid refined cap but scale-correct.

## 5. Attack B — new degree-30 quasimode with the safe trace cap: success

Instead of trying to rescue the bad cycle normalization, this attack spends the available slack on the quasimode residual. Exploratory Hermite--Galerkin diagonalization was used only to select a polynomial. The final degree-30 polynomial is frozen to exact integer monomial coefficients in the checker; every promoted moment, Rayleigh quotient, residual, and spectral inequality is recomputed by exact/outward-rational arithmetic.

Let `f` be the normalized frozen polynomial. Define

\[
\mu=\langle f,Kf\rangle,
\qquad
\varepsilon^2=\|(K-\mu)f\|_2^2.
\tag{5.1}
\]

The exact checker proves

\[
\frac{91208413}{10^8}<\mu<\frac{45604207}{5\cdot10^7},
\qquad
\varepsilon^2<\frac{126929}{10^9}.
\tag{5.2}
\]

Numerically only for readability,

\[
\mu=0.9120841320878648\ldots,
\qquad
\varepsilon^2=0.00012692860442193034\ldots.
\tag{5.3}
\]

This reduces the previous degree-22 residual `~2.85492e-4` by more than a factor two, and unlike that previous endpoint the proof below uses only the scale-safe trace cap (4.15).

Set

\[
\theta_*:=\frac{8497}{50000}=0.16994,
\quad
x:=\frac{913227}{10^6}=0.913227,
\quad
\beta:=\frac{320229}{400000}=0.8005725.
\tag{5.4}
\]

The exact power comparison

\[
x^{12500}<r^{8497}
\tag{5.5}
\]

is exactly `x<r^{4\theta_*}`.

Suppose for contradiction that `lambda_1>=r^{4 theta_*}`. Then `lambda_1>x`. From the fourth-trace cap and the spectral decomposition,

\[
\sum_{j\ge2}\lambda_j^4
\le \operatorname{tr}(K^4)-\lambda_1^4
<\frac{553151}{500000}-x^4.
\tag{5.6}
\]

The checker proves

\[
\beta^4>\frac{553151}{500000}-x^4,
\tag{5.7}
\]

so every non-Perron spectral point obeys `|lambda_j|<beta`; in particular `lambda_j<beta<mu` for `j>=2`.

For completeness, the Temple/spectral-measure step used here is elementary. Let `w_j` be the spectral mass of the unit vector `f`. With one spectral point at least `x>mu` and all remaining points at most `beta<mu`, the mean identity `mu=sum_j w_j lambda_j` implies

\[
\varepsilon^2
=\sum_j w_j(\lambda_j-\mu)^2
\ge (x-\mu)(\mu-\beta).
\tag{5.8}
\]

Using the outward-safe endpoints from (5.2), the checker obtains

\[
(x-\mu_{\rm hi})(\mu_{\rm lo}-\beta)
=\frac{637210907309}{5\cdot10^{15}}
=0.0001274421814618\ldots,
\tag{5.9}
\]

which exceeds the certified residual cap by

\[
\frac{2565907309}{5\cdot10^{15}}
=5.131814618\times10^{-7}>0.
\tag{5.10}
\]

This contradiction proves

\[
\lambda_1<r^{4\theta_*}.
\tag{5.11}
\]

Substitution in the continuous source implication (3.5) yields the new source-valid candidate lower bound

\[
\boxed{\theta_{2,1/4}>\frac{8497}{50000}=0.16994}.\tag{5.12}
\]

Together with the retained source upper bound `1/4`, this proves (0.1) subject to the repository's independent-validation requirement.

## 6. Attack C — intrinsic spectral contraction / reverse interpolation: obstruction isolated

A materially different attempt was to remove dependence on fourth traces by controlling the non-Perron spectrum directly through a Doob transform or Poincare inequality for the killed AR-edge kernel. The natural transformed invariant measure depends on the unknown positive Perron eigenfunction; no explicit log-concavity or curvature bound strong enough to beat the present trace separation emerged. The bare OU contraction scale is too weak after killing.

Separately, a source upper-bound improvement would need the reverse continuous-time direction: grid survival must imply continuous survival at only subexponential cost. The current conditioned process can approach the barrier arbitrarily closely at many mesh points, so a cellwise Gaussian modulus union bound is exponentially expensive unless one first proves a long-survival barrier-repulsion estimate. This run does not prove that estimate. Therefore the upper endpoint remains `1/4`, and no discretely sampled exponent is promoted to a continuous upper bound.

## 7. Before/after metrics and affected dependencies

There are three distinct numbers that must not be conflated:

1. **Published/source literature bracket:** unchanged,
   \[
   1/8\le\theta_{2,1/4}\le1/4.
   \]
2. **Incoming repository candidate:** `theta>0.16798`, but its proof used the now-refuted softened-cycle trace cap and is therefore withdrawn pending a different proof.
3. **Last unaffected repository bound before this run:**
   \[
   0.1647<\theta_{2,1/4}\le0.25,
   \quad W=0.0853.
   \]
   The new corrected proof gives
   \[
   0.16994<\theta_{2,1/4}\le0.25,
   \quad W=0.08006.
   \]

Thus the rigorously supported candidate gap improves by

\[
0.0853-0.08006=0.00524=\frac{131}{25000}.
\tag{7.1}
\]

The correction affects every later candidate whose non-Perron separation imports the softened cyclic trace cap derived from the omitted `G_0` scale, including the `1.081798` / `1.08178606` branch. This report does **not** assert that their other scalar inequalities are false; only that the common trace transfer is not valid as written.

## 8. Exact test actually run and archived

The new exact checker is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0550Z__corrected_cycle_degree30_exact_check.py`

and its executed output is archived as

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0550Z__corrected_cycle_degree30_exact_check.out`.

The executed output certifies:

- exact wrong-vs-correct softened-cycle correlations (4.7)--(4.8);
- the degree-11 compression lower bound `tr((P_11 K P_11)^4)>1.08546756`, contradicting the old `1.081798` cap;
- the degree-30 Rayleigh/residual intervals (5.2)--(5.3);
- the safe hard-edge fourth-trace cap `1.106302`;
- exact power, spectral-tail, and Temple margins for `theta_*=0.16994`;
- final line `ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit. No closure status is claimed.

## 9. Remaining full-scope gap

The exact `theta_{2,1/4}` remains unknown. The present certified-candidate interval still has width `0.08006`, and the full source problem asks for the family away from `H=1/2`, not only this special point. The largest immediate mathematical obligations are:

- independently audit the corrected cycle-scale derivation and degree-30 certificate;
- improve `lambda_1` without reusing the invalid normalized-noise trace geometry, preferably via a scale-correct direct four-cycle integral or an intrinsic spectral-gap/Doob-transform bound;
- obtain a genuine reverse continuous-time interpolation/barrier-repulsion theorem if the upper endpoint is to move.

**Final label: PARTIAL / OPEN.**
