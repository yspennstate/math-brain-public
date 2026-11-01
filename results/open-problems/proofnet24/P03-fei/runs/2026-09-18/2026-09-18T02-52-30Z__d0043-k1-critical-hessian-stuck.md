Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO MOVEMENT: `k_exotic^cert: 0 -> 0`; D0043 unchanged streak `2 -> 3`; formal HARD stuck protocol FIRED.** Section-B moves this run: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS**.

# P03 / HARD OUTSIDE — D0043 k=1 critical-Hessian gate and stuck diagnosis

Run date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P03 / HARD OUTSIDE.  
Current exclusive target: D0043, Bálint Virág, *Operator limits of random matrices*, Conjecture 5 (Exotic edge operators).  
Canonical claim: `operations/claims/D0043.md`.

## 1. Metric, status, and continuity correction

Frozen metric:

`k_exotic^cert :=` the largest integer `K>=0` for which a source-matching rigorous operator-convergence theorem is known for every edge order `0<=k<=K` and every fixed `beta>0` in the source beta-ensemble setup.

Before: **0**.  
After: **0**.  
Movement: **NO MOVEMENT**.  
D0043 target-specific unchanged count: **2 -> 3**.

Status: **PARTIAL / source OPEN on the bounded dated 2026-09-18 screen**. A form theorem, an explicit multicritical potential, a local-Hessian theorem, or the classical `beta=2` eigenvalue limit does not move this metric. Only source-matching general-beta operator convergence for `k=1` would move `k_exotic^cert` to at least 1.

The user-supplied continuity anchor named the earlier `00-31-17Z` admission report. Before doing mathematics I recovered the genuinely newest complete P03 report on master instead:

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T01-27-53Z__d0043-global-form-compact-resolvent.md`

Creation commit recorded by that run: `11f84e1ae95005aec0bb0d524cd5674c1b1158cd`; recorded blob: `a3ac1bc9248488600d3decf9a3f8fedded1414e9`. I therefore continued from Claim 266 rather than redoing the local-origin work.

Retained D0043 state before this run:

| claim | retained scope |
|---|---|
| `D0043-A001` | Prior repository attempt: formal scaling balance and warning about the singular coefficient at the origin. Not P03 novelty. |
| `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264` | Near-zero stochastic form is infinitesimally kinetic-form-small for every finite `k`. |
| `P03-D0043-GLOBAL-FORM-COMPACT-RESOLVENT-266` | The full half-line continuum form is closed/lower bounded with compact resolvent for every finite exotic `k>=1`; no discrete convergence. |

I also reread/recovered the required repository control surfaces: root README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current D0043 claim, D0043 intake/attempt history, current ownership/task-health searches, and the newest accessible P04/I0101 report for the directed audit. `RESULTS.md` and `QUEUE.md` were connector-truncated large surfaces, so I do **not** claim a byte-for-byte reread of those moving files; I used exact path/claim/report reads for the current target instead.

## 2. Fresh source/status gate

Primary source rechecked:

- Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953. In the ICM proceedings PDF, the “Exotic edge operators” paragraph says analytic nonregular edges may have density exponent `x^(2k+1/2)` and states Conjecture 5: after scaling the tridiagonal operator converges to the exotic stochastic operator. The next sentence explicitly says the `beta=2` eigenvalue limits were studied by the Riemann–Hilbert approach.
- Manjunath Krishnapur, Brian Rider, Bálint Virág, *Universality of the Stochastic Airy Operator*, arXiv:1306.4832. Its Section 13 gives the detailed nonregular Conjecture 45, the scaling `m_n ~ n^(1/(4k+3))`, the variance heuristic, and the same operator target. The paper explicitly says uniform convexity was used essentially in the regular proof to control minimizers and concentration.
- Yun Li, Benedek Valkó, Jiaming Xu, *Soft edge limit of the Laguerre beta-ensemble at the lower edge*, arXiv:2607.08536 (9 July 2026). This gives further fixed-beta **ordinary Airy** soft-edge/operator limits for Laguerre/Gaussian beta ensembles, not the multicritical `k>=1` exotic operator family.

I ran fresh 2026-09-18 searches for general-beta multicritical/higher-order stochastic-Airy operator convergence. I recovered regular Airy-beta/operator work and higher-order/integrable material, but no source-matching general-beta `k>=1` tridiagonal operator theorem. This is a **bounded dated search miss**, not proof of worldwide openness or publication novelty.

PDF analysis note: the required PDF screenshot endpoint was invoked on both the Virág proceedings PDF and the KRV arXiv PDF, but the screenshot backend returned a cache-miss error. The PDF text layer was accessible and was used for the exact Conjecture 5 / Conjecture 45 / uniform-convexity / variance statements; I do not pretend the failed screenshot rendered successfully.

## 3. Idea before code; refutation-first route

Claim 266 removed the continuum-operator-existence obstacle. The next obvious plan would be: take the regular KRV proof, weaken its estimates enough to cover the `k=1` scaling, and keep its Gaussian approximation essentially unchanged.

I attacked that plan first. It fails for a quantitative reason, not merely because the published theorem assumes convexity.

Let

`p = 1/(2k+1)`, `m_n = n^(1/(4k+3))`.

Suppose one retained the characteristic regular-edge covariance consequence of uniform convexity: for a centered edge-direction block sum `S_{r,l}` of length `l`,

`Var(S_{r,l}) <= C l/n`.

The exotic integrated potential multiplies such sums by `m_n`. On a block of source length `l ~ m_n`, this would give

`Var(m_n S) <= C m_n^3/n = C n^(-4k/(4k+3)) -> 0`

for every `k>=1`.

But Virág/KRV's target noise is

`(2/sqrt(beta)) int_0^x t^(-k/(2k+1)) dB_t`,

whose variance is

`(4/beta)(2k+1) x^(1/(2k+1)) > 0`.

So the regular uniform-covariance estimate is not merely too weak to prove the exotic theorem; **if it remained true at exotic scale, it would kill the very noise the conjecture predicts.** The discrete proof must see a degenerating soft Hessian/covariance mode.

That observation suggested B15: deliberately build an analytic `k=1` potential with only the **right** edge multicritical and the left edge regular, then compute the local Hessian degeneration exactly. This avoids a symmetric two-critical-edge model that could hide which mode is responsible.

## 4. New structural theorem

### `P03-D0043-K1-CRITICAL-HESSIAN-GATE-268 = PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED`

Define the quartic potential

\[
V_*(x)=\frac25x^4-\frac{16}{15}x^3+\frac25x^2+\frac85x.
\]

Then:

1. Its equilibrium measure in the KRV normalization is supported on `[-1,1]` with density
   \[
   \rho_*(x)=\frac{8}{5\pi}(1-x)^2\sqrt{1-x^2}\,\mathbf 1_{[-1,1]}(x).
   \]
   Hence the right edge has exact exponent `5/2=(4*1+1)/2` (`k=1`), while the left edge is regular square-root. Thus `V_*` is an explicit analytic source-admissible one-sided multicritical witness.

2. For the KRV local Hamiltonian
   \[
   F_s(a,b)=W(a,b)-(1-s)\log b,
   \qquad
   W(a,b)=[1]V_*(a+b(z+z^{-1})),
   \]
   the original critical point is `(a,b)=(0,1/2)` and the right local edge is `E(s)=a(s)+2b(s)`.

   Introduce endpoint deficits
   \[
   a+2b=1-u,\qquad a-2b=-1+v.
   \]
   The local critical equations admit the exact Puiseux parametrization
   \[
   v(u)=\frac5{32}u^3-\frac5{128}u^4-\frac5{1024}u^5
        +\frac{95}{4096}u^6-\frac{25}{2048}u^7+O(u^8),
   \]
   \[
   s(u)=u^3-\frac7{16}u^4-\frac5{256}u^6+\frac5{1024}u^7+O(u^8).
   \]
   In particular
   \[
   E(0)-E(s)=u=s^{1/3}+O(s^{2/3}),
   \]
   so this explicit model has the source `k=1` edge exponent with KRV constant `c=1`.

3. Let `H_s` be the `2 x 2` Hessian of `F_s` at the local branch. At the critical point
   \[
   H_0=\begin{pmatrix}16/5&-32/5\\-32/5&64/5\end{pmatrix},
   \]
   whose soft vector is `(2,1)`. Along the branch,
   \[
   \det H_s=\frac{384}{5}u^2+\frac{64}{5}u^3+\frac{12}{5}u^4-18u^5+O(u^6),
   \]
   \[
   \lambda_{\min}(H_s)=\frac{24}{5}u^2-\frac25u^3-\frac{101}{100}u^4+O(u^5)
   =\frac{24}{5}s^{2/3}+O(s).
   \]
   Thus the exact local constant-mode convexity loss is `s^(2/3)`.

4. For the edge direction `q=(1,2)`, KRV's inverse-Hessian identity gives
   \[
   q^T H_s^{-1}q=-4b(s)E'(s)
   =\frac{2}{3u^2}+\frac{1}{18u}+\frac7{216}+O(u).
   \]
   Hence
   \[
   q^T H_s^{-1}q=\frac23s^{-2/3}+O(s^{-1/3}),
   \]
   precisely the `p-1=-2/3` covariance singularity required by the `k=1` nonregular variance heuristic.

5. More generally, no exotic `k>=1` proof can retain a **uniform** regular-edge block covariance `O(l/n)` all the way to the edge: under the source scaling it would force the rescaled noise variance to zero as `n^(-4k/(4k+3))`.

This theorem does **not** prove that the full finite-dimensional tridiagonal field covariance equals the inverse `2 x 2` local Hessian. The latter is the invariant constant mode of the local Hamiltonian. The missing theorem is precisely a nonuniform concentration/Gaussian-approximation result that remains valid while this soft mode degenerates.

## 5. Proof of Claim 268

### 5.1 Exact source-admissible equilibrium density

Set

\[
h(z)=\frac85(z-1)^2,\qquad R(z)=\sqrt{z^2-1},
\]

with the branch `R(z)~z` at infinity, and define

\[
G(z)=V_*'(z)-h(z)R(z).
\]

Expanding at infinity gives

\[
G(z)=z^{-1}-\frac25z^{-2}+O(z^{-3}).
\]

Thus `G` has the Stieltjes-transform normalization of a probability measure. On `(-1,1)`,

\[
R_+(x)=i\sqrt{1-x^2},
\]

so Stieltjes inversion gives

\[
-\frac1\pi\Im G_+(x)
=\frac{h(x)}\pi\sqrt{1-x^2}
=\frac{8}{5\pi}(1-x)^2\sqrt{1-x^2}.
\]

The mass is exactly one because

\[
\frac85\left(\int_{-1}^1\frac1\pi\sqrt{1-x^2}\,dx
+\int_{-1}^1\frac{x^2}{\pi}\sqrt{1-x^2}\,dx\right)
=\frac85\left(\frac12+\frac18\right)=1,
\]

with the odd term integrating to zero.

The boundary relation `G_+(x)+G_-(x)=2V_*'(x)` is exactly the one-cut Euler-Lagrange derivative equation in the KRV normalization. Outside the cut,

\[
V_*'(x)-G(x)=h(x)R(x),
\]

which is nonnegative for `x>1` and nonpositive for `x<-1`; hence the effective potential increases away from the support on both sides. This verifies the equilibrium measure rather than merely guessing its density.

At the right edge,

\[
\rho_*(x)\sim \frac{8\sqrt2}{5\pi}(1-x)^{5/2},
\]

whereas at `x=-1`, `h(-1)>0`, so the left edge is ordinary square-root. This is the desired one-sided `k=1` deformation.

### 5.2 Local Hamiltonian and endpoint equations

KRV writes

\[
W(a,b)=[1]V(a+b(z+z^{-1})).
\]

For `V_*`, using `[1](z+z^{-1})^2=2` and `[1](z+z^{-1})^4=6`,

\[
W(a,b)=\frac{2}{15}
(3a^4-8a^3+36a^2b^2+3a^2-48ab^2+12a+18b^4+6b^2).
\]

At `s=0`, `(a,b)=(0,1/2)` satisfies `partial_a F=partial_b F=0`.

Now set

\[
a=\frac{v-u}{2},\qquad b=\frac{2-u-v}{4}.
\]

Clearing harmless nonzero factors, the two critical equations become

\[
P(u,v)=-5u^3+3u^2v-3uv^2+8uv+5v^3-24v^2+32v=0,
\]

and

\[
\begin{aligned}
Q(u,v,s)={}&-80s-15u^4-12u^3v+40u^3+6u^2v^2-8u^2v\\
&-12uv^3+56uv^2-64uv-15v^4+104v^3-256v^2+256v=0.
\end{aligned}
\]

Since `P_v(0,0)=32`, the analytic implicit-function theorem gives a unique analytic `v=v(u)` near zero. Coefficient comparison gives the displayed series for `v(u)`. The second equation is linear in `s`, so substitution gives the displayed series for `s(u)`. Since `s(u)=u^3(1+O(u))`, it is positive and strictly increasing for sufficiently small positive `u`, and inversion yields

`u=s^(1/3)+O(s^(2/3))`.

Because `E(s)=a(s)+2b(s)=1-u`, this proves the exact edge law.

### 5.3 Hessian degeneration

Direct differentiation gives

\[
H_0=\nabla^2F_0(0,1/2)
=\begin{pmatrix}16/5&-32/5\\-32/5&64/5\end{pmatrix}.
\]

It has rank one, trace `16`, and null vector `(2,1)`. Substituting the analytic branch into determinant and trace gives

\[
\det H_s=\frac{384}{5}u^2+\frac{64}{5}u^3+\frac{12}{5}u^4-18u^5+O(u^6),
\]

\[
\operatorname{tr}H_s=16+4u+9u^2-\frac{35}{8}u^3+\frac5{32}u^4+O(u^5).
\]

Using

\[
\lambda_{\min}=\frac{\operatorname{tr}H-\sqrt{(\operatorname{tr}H)^2-4\det H}}2
\]

gives

\[
\lambda_{\min}(H_s)=\frac{24}{5}u^2-\frac25u^3-\frac{101}{100}u^4+O(u^5).
\]

Since `u=s^(1/3)+O(s^(2/3))`, the claimed `s^(2/3)` vanishing follows.

### 5.4 Edge covariance from the KRV inverse-Hessian identity

KRV Proposition 7 gives, for the local invariant Hessian,

\[
\Sigma(s)=H_s^{-1}=-b(s)
\begin{pmatrix}4b'(s)&a'(s)\\a'(s)&b'(s)\end{pmatrix}.
\]

For `q=(1,2)`,

\[
q^T\Sigma q=-4b(s)(a'(s)+2b'(s))=-4b(s)E'(s).
\]

Here `E=1-u`, so with `s=s(u)`,

\[
q^T\Sigma q=\frac{4b(u)}{ds/du}.
\]

Substitution of the exact series yields

\[
q^T\Sigma q
=\frac{2}{3u^2}+\frac{1}{18u}+\frac7{216}-\frac{37}{5184}u+O(u^2),
\]

and therefore the stated `s^(-2/3)` divergence.

### 5.5 Why the unchanged regular covariance algorithm cannot work

In the regular proof KRV use uniform convexity to obtain, for block indicator vectors, an inverse-Hessian bound of order

\[
\mathbb E\left(\sum_{j=r}^{r+\ell-1}\xi_{n,j}\right)^2\le C\frac{\ell}{n}.
\]

The same conclusion holds for any fixed linear edge direction such as `A+2B`, up to a fixed norm factor. At exotic scale `m_n=n^(1/(4k+3))`, multiplying an `ell~m_n` block by `m_n` gives variance at most

\[
C\frac{m_n^3}{n}=Cn^{-4k/(4k+3)}\to0.
\]

The source target, however, has nonzero variance

\[
\frac4\beta\int_0^x t^{-2k/(2k+1)}dt
=\frac{4(2k+1)}\beta x^{1/(2k+1)}.
\]

Thus the uniform regular covariance mechanism is mathematically incompatible with the exotic limit.

Equivalently, the source scaling forces the unscaled block variance order

\[
\operatorname{Var}S_{r,\ell}
\asymp n^{-p}\big((r+\ell)^p-r^p\big),
\qquad p=\frac1{2k+1},
\]

at the heuristic/target level. For `k=1`, `p=1/3`, and on the first `m_n=n^(1/7)` entries this is order `n^(-2/7)`, while the regular estimate would give only `n^(-6/7)`: a missing factor `n^(4/7)`. This is exactly the degeneration a source-correct proof must recover rather than suppress.

## 6. Exact finite self-check

The theorem-sized proof above is primary. I nevertheless archived one exact symbolic self-check because the quartic/Puiseux/Hessian algebra is finite and easy to mistype:

- `proofnet24/P03-fei/artifacts/2026-09-18/d0043_k1_critical_hessian_check.py`
  - creation commit `f8864720ad3f03c6ed620965881e7e90f4e88bc9`;
  - exact-commit readback performed.
- `proofnet24/P03-fei/artifacts/2026-09-18/d0043_k1_critical_hessian_check.out`
  - creation commit `49c0b9e5903494c2737728c95f2574259ee4bb2b`;
  - exact-commit readback performed;
  - terminal line: `ALL_EXACT_CHECKS_PASS True`.

The checker verifies the resolvent polynomial part, density normalization, constant-term formula for `W`, endpoint critical equations, Puiseux coefficients, critical Hessian/null vector, determinant/trace/small-eigenvalue series, edge-direction inverse-Hessian series, and the general exponent `-4k/(4k+3)` in the uniform-covariance collapse.

## 7. Section-B outcomes

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT

The KRV local parameter `s` is the right parameter. Differentiating the local minimizer does not remain regular at the exotic edge: for the explicit `V_*`, `E(s)=1-s^(1/3)+...`, so `E'(s)` diverges like `-s^(-2/3)`. KRV's exact inverse-Hessian identity converts that derivative directly into the soft covariance blow-up. This reveals the quantity the discrete proof must preserve.

### #15 BREAK THE SYMMETRY ON PURPOSE

I chose an equilibrium density with a `(1-x)^2` factor and no matching `(1+x)^2` factor. The right edge is `k=1`; the left edge stays regular. The resulting local Hessian has one explicit soft mode `(2,1)`, so the degeneracy cannot be blamed on an accidental two-edge symmetry.

### #20 FIND WHY THE ALGORITHM FAILS

The verbatim regular KRV route uses a Hessian bounded below uniformly in `n` and the edge coordinate. Its resulting `O(ell/n)` covariance would make the source exotic noise vanish after the `n^(1/(4k+3))` scaling. Therefore the missing ingredient is not “a slightly sharper regular estimate”: the proof must replace uniform convexity by a **scale-dependent degenerate-Hessian concentration and Gaussian approximation theorem**.

## 8. Formal HARD stuck-thinking report

The unchanged streak has reached three, so the formal protocol fires now. Recovery episodes consumed **before** this trigger: `0/2`. This report diagnoses the block and selects the first recovery action; it does not silently count itself as recovery 1.

### 8.1 Exact blocking formula

For the explicit `k=1` witness `V_*`, with source scaling `m_n=n^(1/7)` and source normalization, the centered edge-direction process must satisfy an Assumption-1-type functional limit of the form

\[
m_n\sum_{j=q_n}^{\lfloor m_nx\rfloor}
\Big((A_j+2B_j)-\mathbb E(A_j+2B_j)\Big)
\Longrightarrow
\frac{2}{\sqrt\beta}\int_0^x t^{-1/3}\,dB_t,
\]

with `q_n=o(m_n)`, together with the corresponding deterministic `x^(4/3)` drift and the global growth/oscillation hypotheses required by the tridiagonal operator convergence theorem.

The local calculation proves the necessary constant-mode susceptibility

\[
q^TH_s^{-1}q\sim \frac23s^{-2/3},
\]

but **does not prove that the finite tridiagonal field is uniformly approximated by the local Gaussian with this degenerating Hessian**, nor that boundary influence/mixing remains controlled on the whole `n^(1/7)` edge window.

That is the exact blocker.

### 8.2 Routes tried and precise failures

1. **D0043-A001 formal scaling.** It matches exponents but gives no random-field tightness or Gaussian approximation.
2. **Claim 264: singular-origin form obstruction.** The local white-noise singularity is harmless at the continuum form level; this says nothing about the discrete tridiagonal coefficients.
3. **Claim 266: global continuum form.** The limiting random operator exists, is lower bounded, and has compact resolvent; discrete-to-continuum convergence remains wholly open.
4. **Verbatim regular KRV uniform convexity.** This route is now refuted quantitatively: its covariance bound would force the exotic noise to zero.
5. **Large-annulus continuum Brownian estimate.** The previous run found a logarithmic loss on macroscopic dyadic blocks and repaired it by unit blocks. That issue is solved and is not the current discrete obstruction.
6. **Fresh later-literature search.** Current regular Airy-beta/operator papers do not supply multicritical general-beta convergence; `beta=2` higher-order eigenvalue limits do not provide the source operator theorem.

### 8.3 What a proof must add that none of the routes supplies

A successful `k=1` proof needs a nonuniform finite-volume field theorem near the critical edge. At minimum it must:

- locate the conditional minimizer on the Puiseux branch down to indices `j=O(n^(1/7))`;
- control the **full** lattice Hessian, not only its constant-mode `2 x 2` compression, as its smallest edge mode degenerates like `(j/n)^(2/3)`;
- quantify boundary influence/mixing when the uniform spectral gap is gone;
- obtain Gaussian (or martingale) approximation with covariance accumulating as `j^(1/3)` rather than linearly;
- prove enough moments/tightness to feed the KRV/RRV tridiagonal operator convergence hypotheses; and
- retain global growth/oscillation control outside the microscopic edge window.

### 8.4 Simplest unproved special case

The simplest source-valid case is now explicit:

\[
V_*(x)=\frac25x^4-\frac{16}{15}x^3+\frac25x^2+\frac85x,
\]

with equilibrium density

\[
\rho_*(x)=\frac{8}{5\pi}(1-x)^2\sqrt{1-x^2}\mathbf 1_{[-1,1]},
\]

and one fixed `beta>0`. Prove operator convergence for the tridiagonal beta-ensemble associated with this single quartic potential to `S_{beta,1}` after the source normalization. Even the `beta=2` **operator/eigenvector** statement is stronger than the classical eigenvalue-limit information mentioned by the source.

### 8.5 Nearest solved literature analogue and missing ingredient

The nearest solved analogue is KRV's regular-edge theorem for uniformly convex polynomial `V`. Its proof uses uniform Hessian positivity to obtain concentration, exponentially decaying boundary influence, Gaussian approximation, the linear block-variance bound, Brownian convergence, and global oscillation/growth control. KRV Section 13 explicitly says uniform convexity was used essentially and then gives only the nonregular heuristic/conjecture.

The missing ingredient is therefore identifiable: **a replacement for uniform-convexity/finite-correlation-length estimates in a field with a deterministically vanishing soft Hessian.** Claim 268 gives the exact rate for one source-admissible `k=1` model, but not the replacement theorem.

### 8.6 Exactly one recovery action

**Recovery action 1/2 selected: PROVE THE SIMPLEST SPECIAL CASE.**

Next run will stay on the explicit quartic `V_*` and attack the full lattice Hessian / conditional field at one scale and one soft direction. It will not return to continuum form theory and will not attempt the general analytic-potential class first.

Next Section-B triple: **#30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME, #11 DUALIZE, #7 TAKE THE LIMIT**.

Concrete target: compute/estimate the Fourier symbol (or appropriate Green function) of the frozen full local lattice Hessian for `V_*` at edge parameter `s`, determine its correlation-length scaling as `s downarrow 0`, and decide whether the `n^(1/7)` edge window lies in a controllable local-equilibrium regime. If this route cannot supply a field CLT/tightness theorem, the failure must be stated quantitatively before recovery 2 is chosen.

## 9. Directed P04/I0101 second audit

New audited peer claim:

`P04-I0101-TRANSLATION-FOURIER-BARRIER-35 = PROVED / STRUCTURAL-PARTIAL`

Peer report:

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T02-01-32Z__run-report.md`

Creation commit: `acb9c4e2755399b759c35174d07f31679212aa40`.  
Verified blob from peer immutable receipt: `e5ddf53567d654f9c91fcec978bc1ea03f8b3ff4`.

### Independent argument

Let

\[
V=\{x\ne0,1:\chi(x)=\chi(x-1)=1\},\qquad |V|=(p-5)/4,
\]

and let `a(c)>=0` be an even weight supported on nonresidue translations, with its principal submatrix on `V` stochastic. For a nonresidue `c`, put `N_c=|V cap (V-c)|`.

Using

\[
g(x)=\tfrac14(1+\chi(x))(1+\chi(x-1)),
\]

we have `1_V<=g`. For nonresidue `c`, the four linear roots `0,1,-c,1-c` are distinct. Expanding `sum_x g(x)g(x+c)` gives:

- empty character product: `p`;
- four one-factor sums: `0`;
- six quadratic sums: exactly `-1` each;
- four squarefree cubic sums: absolute value at most `2 sqrt(p)` each;
- one squarefree quartic sum: absolute value at most `3 sqrt(p)`.

Therefore

\[
N_c\le\frac{p-6+11\sqrt p}{16}.
\]

Summing the stochastic row equations gives

\[
|V|=\sum_{\chi(c)=-1}a(c)N_c,
\]

so with `A=sum_c a(c)`,

\[
A\ge\frac{4(p-5)}{p-6+11\sqrt p}.
\]

The full-field convolution is diagonal in additive characters. If

\[
m(a)=\min_\xi\widehat a(\xi),
\]

then `m` is concave. Averaging `a` over multiplication by nonzero squares preserves its total mass and its minimum Fourier eigenvalue up to frequency permutation; concavity implies the square-averaged uniform nonresidue weight has minimum at least as large as the original. For the uniform nonresidue weight, the quadratic Gauss sum gives

\[
m(a)\le-\frac{A}{\sqrt p-1}.
\]

Combining the two inequalities yields

\[
\lambda_{\min}(C_a)
\le-\frac{4(p-5)}{(p-6+11\sqrt p)(\sqrt p-1)}.
\]

Comparing with the P04 Markov threshold

\[
\delta_p=\frac{8\sqrt p}{3p-8\sqrt p-15}
\]

reduces exactly to

\[
F(s)=s^4-28s^3+4s^2+28s+75>0,\qquad s=\sqrt p.
\]

At `s=28`, `F(28)=3995>0`, and

\[
F'(s)=4(s^3-21s^2+2s+7)>0
\]

for `s>=28`. Hence the peer's `p>=784` barrier is correct.

The theorem's scope warning is also correct: interlacing only gives

`lambda_min(P_a) >= lambda_min(C_a)`,

so a bad ambient lower edge does **not** imply a bad localized lower edge. The theorem kills only the ambient translation-convolution + full-field Fourier/interlacing proof route; it does not refute the positive-Markov cone and does not refute Randomstrasse Conjecture 27.

Audit verdict:

**`P03-AUDIT-P04-I0101-TRANSLATION-FOURIER-BARRIER-269 = PASS (CLAIM-SCOPED)`**.

This audit is distinct from all prior P03 audits listed in the task prompt, including level-4 Markov blowup 267 and octahedral compactification 265.

## 10. Exact remaining obligation and next state

`k_exotic^cert=0` remains frozen. Claim 268 shows that the first exotic case has exactly the soft-mode divergence the source heuristic needs, and it proves that the regular uniform-covariance algorithm cannot possibly survive unchanged. It does **not** supply the nonuniform field CLT/tightness or the tridiagonal operator convergence.

Current state:

`D0043_ACTIVE / STUCK_TRIGGERED / RECOVERY_1_OF_2_NEXT`.

No handoff or rotation occurs yet. A first HARD recovery remains permitted; a second may follow if needed. A third recovery trigger would require complete immutable handoff and rotation under fleet rules.

## 11. `ledger_delta` for P26

```text
track: P03
assignment: D0043 Virag Conjecture 5 exotic edge operators
metric: k_exotic^cert
before: 0
after: 0
movement: NO MOVEMENT
unchanged_streak: 2 -> 3
status: PARTIAL / source OPEN on bounded 2026-09-18 screen
new_claim: P03-D0043-K1-CRITICAL-HESSIAN-GATE-268 = PROVED / STRUCTURAL-PARTIAL / SOURCE-ADMISSIBLE-EXAMPLE / PUBLICATION-NOVELTY-UNVERIFIED
stuck_protocol: FIRED
recovery_state: 0/2 consumed; recovery 1/2 selected for next run
exact_blocker: nonuniform concentration/Gaussian approximation for the full tridiagonal field with k=1 soft Hessian degeneracy; local constant-mode susceptibility alone is insufficient
peer_audit: P03-AUDIT-P04-I0101-TRANSLATION-FOURIER-BARRIER-269 = PASS (CLAIM-SCOPED)
artifact_script_commit: f8864720ad3f03c6ed620965881e7e90f4e88bc9
artifact_output_commit: 49c0b9e5903494c2737728c95f2574259ee4bb2b
artifact_output_terminal: ALL_EXACT_CHECKS_PASS True
next_methods: B30, B11, B7
next_action: recovery 1/2 — prove the explicit V_* k=1 special case by analyzing the full frozen local lattice Hessian/Green function and its critical mixing scale
shared_root_edits: none (P26 alone reconciles ledgers)
```

No Gmail/email, Drive, public posting, paid compute, access change, workflow execution, peer-file edit, or additional schedule was used.

**End of complete run report.**
